from django.http import HttpResponse,HttpResponseNotFound
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from datetime import datetime

from . import models

def messages_view(request):
    """Private Page Only an Authorized User Can View, renders messages page
       Displays all posts and friends, also allows user to make new posts and like posts
    Parameters
    ---------
      request: (HttpRequest) - should contain an authorized user
    Returns
    --------
      out: (HttpResponse) - if user is authenticated, will render private.djhtml
    """
    if request.user.is_authenticated:
        user_info = models.UserInfo.objects.get(user=request.user)

        friend_list1 = []

        for i in user_info.friends.all():
            friend_list1.append(i)

        #print(friend_list1)


        friends_list = friend_list1
        

        posts_list = []
        for i in models.Post.objects.all().order_by('-id'):
            posts_list.append(i)

        request.session['length_of_post_list'] = len(posts_list)

        # TODO Objective 9: query for posts (HINT only return posts needed to be displayed)
        posts = posts_list[:request.session['post_counter']]
        

        # TODO Objective 10: check if user has like post, attach as a new attribute to each post
        #for i in models.Post.objects.all():
            #id_list = []
            #for j in i.likes.all():
                #id_list.append(j)
            
            #if j.user_id in id_list:
               #i.liked = "True"
            #else:
               #i.liked = "False"



        context = { 'user_info' : user_info
                  , 'posts' : posts
                  , 'friends_list' : friends_list
                  , 'post_counter' : request.session['post_counter']
                  , 'length_of_post_list' : request.session['length_of_post_list'] }
        return render(request,'messages.djhtml',context)

    request.session['failed'] = True
    return redirect('login:login_view')

def account_view(request):
    """Private Page Only an Authorized User Can View, allows user to update
       their account information (i.e UserInfo fields), including changing
       their password
    Parameters
    ---------
      request: (HttpRequest) should be either a GET or POST
    Returns
    --------
      out: (HttpResponse)
                 GET - if user is authenticated, will render account.djhtml
                 POST - handle form submissions for changing password, or User Info
                        (if handled in this view)
    """

    user_info = models.UserInfo.objects.get(user=request.user)


    if not request.user.is_authenticated:
       return redirect('login:login_view')

    if request.method == "POST":
       if "password_submit" in request.POST:
          password_form = PasswordChangeForm(request.user, request.POST)
          if password_form.is_valid():
             new_password = password_form.cleaned_data.get('new_password1')
             user_info.user.set_password(new_password)
             user = password_form.save()
             update_session_auth_hash(request, user)
             return redirect('login:login_view')
              

        # TODO Objective 3: Create Forms and Handle POST to Update UserInfo / Password
       elif "info_submit" in request.POST:
          password_form = PasswordChangeForm(request.user)
          employment1 = request.POST['employment']
          location1 = request.POST['location']
          birthday1 = request.POST['birthday']
          interest1 = request.POST['interests']
          if employment1 != "" :
             user_info.employment = employment1
          if location1 != "" :
             user_info.location = location1
          if birthday1 != "" :
             user_info.birthday = birthday1
          else:
             user_info.birthday = None

          if interest1 != "":
             user_info.interests.create(label=interest1)
          else:
             pass
          user_info.save()   
    else:
       password_form = PasswordChangeForm(request.user)
    
    context = { 'user_info' : user_info,
                    'password_form' : password_form}  
    return render(request,'account.djhtml',context)

    

def people_view(request):
    """Private Page Only an Authorized User Can View, renders people page
       Displays all users who are not friends of the current user and friend requests
    Parameters
    ---------
      request: (HttpRequest) - should contain an authorized user
    Returns
    --------
      out: (HttpResponse) - if user is authenticated, will render people.djhtml
    """

    #request.session['counter'] = 1
    
    if request.user.is_authenticated:
        user_info = models.UserInfo.objects.get(user=request.user)
        # TODO Objective 4: create a list of all users who aren't friends to the current user (and limit size)
        
        users_list = []
        for u in models.UserInfo.objects.all():
            users_list.append(u)
        
        users_list.remove(user_info)
        f_list = []

        friends_list = user_info.friends.all()
        for j in users_list:
            if j not in friends_list:
               f_list.append(j)
          
        request.session['length_of_list'] = len(f_list)
       
        all_people = f_list[:request.session['counter']]


        # TODO Objective 5: create a list of all friend requests to current user

        friend_req_list1 = []

        for i in models.FriendRequest.objects.all():
            if i.to_user_id == user_info.user_id:
               if i.from_user_id != user_info.user_id:
                  friend_req_list1.append(i)

        friend_requests = friend_req_list1

        context = { 'user_info' : user_info,
                    'all_people' : all_people,
                    'friend_requests' : friend_requests
                    , 'counter' : request.session['counter']
                    , 'length_of_list' : request.session['length_of_list'] }

        return render(request,'people.djhtml',context)

    request.session['failed'] = True
    return redirect('login:login_view')

def like_view(request):
    '''Handles POST Request recieved from clicking Like button in messages.djhtml,
       sent by messages.js, by updating the corrresponding entry in the Post Model
       by adding user to its likes field
    Parameters
	----------
	  request : (HttpRequest) - should contain json data with attribute postID,
                                a string of format post-n where n is an id in the
                                Post model

	Returns
	-------
   	  out : (HttpResponse) - queries the Post model for the corresponding postID, and
                             adds the current user to the likes attribute, then returns
                             an empty HttpResponse, 404 if any error occurs
    '''
    postIDReq = request.POST.get('postID')
    if postIDReq is not None:
        # remove 'post-' from postID and convert to int
        # TODO Objective 10: parse post id from postIDReq
        postID = 0
        #print(postIDReq)

        if request.user.is_authenticated:
            # TODO Objective 10: update Post model entry to add user to likes field
            user_info = models.UserInfo.objects.get(user=request.user)
            d = models.Post.objects.get(id=postIDReq)
            print(d)
            print(user_info)
            d.likes.add(user_info)
            d.save()
            

            # return status='success'
            return HttpResponse()
        else:
            return redirect('login:login_view')

    return HttpResponseNotFound('like_view called without postID in POST')

def post_submit_view(request):
    '''Handles POST Request recieved from submitting a post in messages.djhtml by adding an entry
       to the Post Model
    Parameters
	----------
	  request : (HttpRequest) - should contain json data with attribute postContent, a string of content

	Returns
	-------
   	  out : (HttpResponse) - after adding a new entry to the POST model, returns an empty HttpResponse,
                             or 404 if any error occurs
    '''
    postContent = request.POST.get('postContent')
    if postContent is not None:
        if request.user.is_authenticated:
            #print(postContent)
            user_info = models.UserInfo.objects.get(user=request.user)
            now = datetime.now()
            current_time = now.strftime("%Y-%m-%d %H:%M:%S")
            if postContent != "":
                models.Post.objects.create(owner=user_info, content=postContent, timestamp=current_time)
            

            # TODO Objective 8: Add a new entry to the Post model

            # return status='success'
            return HttpResponse()
        else:
            return redirect('login:login_view')

    return HttpResponseNotFound('post_submit_view called without postContent in POST')

def more_post_view(request):
    '''Handles POST Request requesting to increase the amount of Post's displayed in messages.djhtml
    Parameters
	----------
	  request : (HttpRequest) - should be an empty POST

	Returns
	-------
   	  out : (HttpResponse) - should return an empty HttpResponse after updating hte num_posts sessions variable
    '''
    if request.user.is_authenticated:
        # update the # of posts dispalyed

        # TODO Objective 9: update how many posts are displayed/returned by messages_view
        if request.session['post_counter'] <= request.session['length_of_post_list']:
            request.session['post_counter'] += 1
        else:
            pass
        # return status='success'
        return HttpResponse()

    return redirect('login:login_view')

def more_ppl_view(request):
    '''Handles POST Request requesting to increase the amount of People displayed in people.djhtml
    Parameters
	----------
	  request : (HttpRequest) - should be an empty POST

	Returns
	-------
   	  out : (HttpResponse) - should return an empty HttpResponse after updating the num ppl sessions variable
    '''
    if request.user.is_authenticated:
        # update the # of people dispalyed

        # TODO Objective 4: increment session variable for keeping track of num ppl displayed

        if request.session['counter'] <= request.session['length_of_list']:
            request.session['counter'] += 1
        else:
            pass

        # return status='success'
        return HttpResponse()

    return redirect('login:login_view')

def friend_request_view(request):
    '''Handles POST Request recieved from clicking Friend Request button in people.djhtml,
       sent by people.js, by adding an entry to the FriendRequest Model
    Parameters
	----------
	  request : (HttpRequest) - should contain json data with attribute frID,
                                a string of format fr-name where name is a valid username

	Returns
	-------
   	  out : (HttpResponse) - adds an etnry to the FriendRequest Model, then returns
                             an empty HttpResponse, 404 if POST data doesn't contain frID
    '''
    frID = request.POST.get('frID')
    if frID is not None:
        # remove 'fr-' from frID
        username = frID[3:]

        if request.user.is_authenticated:
            # TODO Objective 5: add new entry to FriendRequest

            user_info = models.UserInfo.objects.get(user=request.user)
            friend1 = models.UserInfo.objects.get(user=frID)
            found = False
            for j in models.FriendRequest.objects.all():
                if (j.from_user_id == user_info.user_id) and (j.to_user_id == friend1.user_id):
                   found = True

            if found == False:
                friend_req = models.FriendRequest(from_user=user_info, from_user_id=user_info.user_id, to_user=friend1, to_user_id=friend1.user_id)
                friend_req.save()

            # return status='success'
            return HttpResponse()
        else:
            return redirect('login:login_view')

    return HttpResponseNotFound('friend_request_view called without frID in POST')

def accept_decline_view(request):
    '''Handles POST Request recieved from accepting or declining a friend request in people.djhtml,
       sent by people.js, deletes corresponding FriendRequest entry and adds to users friends relation
       if accepted
    Parameters
	----------
	  request : (HttpRequest) - should contain json data with attribute decision,
                                a string of format A-name or D-name where name is
                                a valid username (the user who sent the request)

	Returns
	-------
   	  out : (HttpResponse) - deletes entry to FriendRequest table, appends friends in UserInfo Models,
                             then returns an empty HttpResponse, 404 if POST data doesn't contain decision
    '''
    data = request.POST.get('decision')
    accept_decline_decision = request.POST.get('decision1')
    if data is not None and accept_decline_decision is not None:
        # TODO Objective 6: parse decision from data
        print(data)
        print(accept_decline_decision)

        if request.user.is_authenticated:
            user_info = models.UserInfo.objects.get(user=request.user)
            from_user_f = models.UserInfo.objects.get(user=data)
            
            if accept_decline_decision == "Accept":
                user_info.friends.add(from_user_f)
                from_user_f.friends.add(user_info)
                for entry in models.FriendRequest.objects.all():
                    if entry.from_user_id == from_user_f.user_id and entry.to_user_id == user_info.user_id:
                       entry.delete()

            else:
                for entry in models.FriendRequest.objects.all():
                    if entry.from_user_id == from_user_f.user_id and entry.to_user_id == user_info.user_id:
                       entry.delete()
            
            

            # TODO Objective 6: delete FriendRequest entry and update friends in both Users

            # return status='success'
            return HttpResponse()
        else:
            return redirect('login:login_view')

    return HttpResponseNotFound('accept-decline-view called without decision in POST')
