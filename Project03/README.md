# CS 1XA3 Project 03 - nabera

## Usage
In order to use this project, Conda must be installed on your machine. The Anaconda Distribution is one of the recommended packages to install, where it includes Conda, and is able to run python packages including Django, which is key for this project.
To install Conda, download the latest version from the following website:
https://docs.anaconda.com/anaconda/install/

After it has been installed, you need to create a Conda environment called "djangoenv", through running this code:
`conda create -n djangoenv python=3.7`
Then, activate the environment by:
`conda activate djangoenv`
Make sure you also install Django by running this command:
`conda install -c anaconda django`

When you have finished installation, you can run the project either locally or on mac1xa3.ca:
To run locally:
`python manage.py runserver localhost:8000`
To run on mac1xa3.ca:
`python manage.py runserver localhost:10071`

In order to use the database for storing information, you need to run these two commands:
`python manage.py makemigrations`
`python manage.py migrate`

If you are running the project on the mac1xa3.ca server, you need to run:
`python manage.py collectstatic` as well as change 'macid' to 'nabera' in Project03/settings.py and Project03/urls.py

To populate the database using a test database that contains many users, posts, friend requests, and more, scroll down to Objective 11.

Login with user "TestUser" and password "1234".


## Objective 1: Signup View

**Description:**
- This feature is displayed in signup.djhtml, which is rendered by the signup_view.
- It uses the built-in User Creation Form from Django, in order to create a user, and a reason for this is better security, where this signup form has username and password restrictions.
- When the username and password credentials entered are valid, then a POST request is made and a UserInfo object will be created containing the credentials of the user.

**Exceptions**:
- If you enter any invalid user credentials, then it redirects back to signup.djhtml, where it explains why the error occurred.
 
## Objective 2: Adding User Profile and Interests
**Description**:
- This feature is represented by social_base.djhtml, where it represents the left column of all of the pages used in the website. The left column shows the user's information such as employment, birthday, and interests.
- In views.py, a variable is defined holding the currently logged in user, which is a UserInfo object with attributes. These attributes were used to extract each value and place it in the template.

## Objective 3: Account Settings Page
**Description:**
- This page in the website has two different features, where it is displayed by account.djhtml, and it is rendered by account_view.
- The first feature is a Password Change Form, where the built-in Django form was used in this case, due to its security to maintain a secure password is being used. When valid credentials are entered in the Password Change form, a POST request is made, where the data in the new password is used to update the UserInfo object of the user. For security reasons, after a password change, the user is logged out and redirected to login.djhtml.
- The second feature is a feature for updating the user information such as employment and birthday.
- A custom form was used containing text fields for employment, location, and interests, and a date field was used for the birthday. If employment, location, or interests were left empty, then nothing would be updated for the user's information. However, if the birthday field is left empty, then that sets the user's birthday to None. Otherwise, if each would be filled, then all would be updated, and the new interest would be added.

**Exceptions:**
- If wrong password credentials were entered in the Password Change form, then the user would be redirected to the account.djhtml page again, with an error message depending on what the user has entered.

## Objective 4: Displaying People List
**Description:**
- This feature is being displayed by people.djhtml, where it displays a list of all users registered which are not friends with the user, along with their information, and a Friend Request button. The page starts off by displaying one user only, and then when the More button is clicked, it displays more users.
- The users are stored in a list, and list slicing is used to limit the number of users displayed at a current time with a session counter variable. The More button is linked to send an AJAX post using JavaScript (people.js) to more_ppl_view, which increments the counter variable by 1 as long as it is less than the number of users available, in order to display one more user.
 
**Exceptions:**
- When the user clicks More after all of the users have been displayed, then the More button wil be disabled, indicating for the user that there are no more users that they can add as a friend.

## Objective 5: Sending Friend Requests
**Description:** This feature makes the "Friend Request" button under each user in the people.djhtml page able to send a Friend Request to that user if it is valid to do so. Each "Friend Request" button has its id assigned to the user displayed with it. The id of that button is sent using JavaScript located in "people.js" to friend_request_view, where if the user has not yet sent a friend request to the user, then it will create a FriendRequest object from the currently logged in user, to the user clicked on. If the user that recieved the friend request logs in, he can see the friend request in the right column of the people.djhtml page.

**Exceptions:** When a user that has already sent a friend request to a certain user, and tries to send the same friend request again, although the user does not get an alert that he has already sent a friend request earlier, there will not be another FriendRequest object created, and only one friend request will reach the user.

## Objective 6: Accepting/Declining Friend Requests
**Description:** 
- As stated earlier, the user can check the friend requests they recieved from the right column in the people.djhtml page; precisely (e/macid/social/people).
- Each friend request will have two buttons, for Accepting or Declining the friend request. JavaScript was used in people.js, where the id of the button represented the user who sent the friend request, and the title of the button represented the decision (Accept or Decline) that the user took. They are sent to the function accept_decline_view.
- If the user accepts, then each user will be added in the friends list of the other. No matter what the decision was, the FriendRequest object will be deleted.

## Objective 7: Displaying Friends
**Description:**
- This feature is displayed by the right column of the messages.djhtml page; precisely (e/macid/social/messages).
- It is achieved by looping over the list containing the user's friends and displaying them under each other.

## Objective 8: Submitting Posts
**Description:** 
- This feature is being displayed by the middle column of the messages.djhtml page, where it is used for submitting posts, and is being rendered by messages_view and post_submit_view.
- JavaScript was used to get the id of the post button, as well as the text inside the post-text field, and they were sent via an AJAX post to post_submit_view. 
- Then, if the input entered was valid, then a new Post object would be created, with the currently logged in user as the owner, a timestamp of the current time, and the content, which was in the post-text field.

**Exceptions:**
- If the post-text field was left empty, and the post button was clicked, then no new Post object will be created, and it will just redirect back to the same page (messages.djhtml).

## Objective 9: Displaying Posts List
**Description:**
- Displaying the posts made by different users is represented in the middle column of the messages.djhtml page, under the field for submitting a post, where it is rendered by messages_view, and more_post_view.
- This feature works similarily to displaying the users who are not friends with the currently logged in user, in the sense that by default when logging in, only one post will be available, and clicking the More button will cause one more post to appear.
- The More button is linked via an AJAX post to send data to more_post_view, which will increment a certain session counter variable, used to display more posts. It increments by 1 as long as the counter is less than the number of posts avaiable.

**Exceptions:**
- When the user clicks More after all of the posts have been displayed, the user would be redirected back to the same page with the More button being disabled, indicating that there are no more posts to display.

## Objective 10: Liking Posts & Displaying Like Count
**Description:**
- This feature enables users to like posts that are displayed using the previous objective, presented in messages.djhtml. Every post object displayed has a like button, where if the user has not liked the post before, it will be clickable.
- The Like button is linked via an AJAX post to send the id of the Post object to like_view, where if the user has not liked the post, then it adds the user to the list of likes of the post.
- When a user likes a post, and it is valid, then the number of likes for that post will increase by 1.

**Exceptions:**
- When a user likes a Post object, then they will be redirected back to the messages.djhtml page, where the like button for that specific post will be disabled, as this prevents users from double liking the post.
 
## Objective 11: Test Database for Running the Django Project
**Description:**
- The test database will be a file called 'populate_db.py', where it will be located in the Project03 directory, and it contains python code that will insert many users, user information, posts, friend requests, and more aspects needed to experiment every feature of the Django Project.
- In order to run this file and populate the database, follow these steps:
        1- Run the python shell `python manage.py shell`
        2- Type `from populate_db import *`
        3- Type `populate()`
        4- Exit the python shell through typing `exit()`






 

