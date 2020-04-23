from social import models
from datetime import date, datetime

def populate():
    # Creating Users (UserInfo objects) 
    u1 = models.UserInfo.objects.create_user_info(username="Hashem", password="123456") 
    u1.save()
    u2 = models.UserInfo.objects.create_user_info(username="Anthony", password="123456")
    u2.save()
    u3 = models.UserInfo.objects.create_user_info(username="Jimmy", password="123456")
    u3.save()
    u4 = models.UserInfo.objects.create_user_info(username="John", password="123456")
    u4.save()
    u5 = models.UserInfo.objects.create_user_info(username="Craig", password="123456")
    u5.save() 
    u6 = models.UserInfo.objects.create_user_info(username="Omar", password="123456")
    u6.save()
    u7 = models.UserInfo.objects.create_user_info(username="Ahme", password="123456")
    u7.save()

    # Updating Employment for users,
    u1.employment = "McMaster University"
    u1.save()
    u2.employment = "IBM"
    u2.save()
    u3.employment = "Google"
    u3.save()
    u4.employment = "Apple"
    u4.save()
    u5.employment = "Food Basics"
    u5.save()
    u6.employment = "Fortinos"
    u6.save()
    u7.employment = "Toyota"
    u7.save()

    # Updating Location for users
    u1.location = "Hamilton, ON"
    u1.save()
    u2.location = "Waterloo, ON"
    u2.save()
    u3.location = "Montreal, QC"
    u3.save()
    u4.location = "Madrid, Spain"
    u4.save()
    u5.location = "Amman, Jordan"
    u5.save()
    u6.location = "Dubai, UAE"
    u6.save()
    u7.location = "Cairo, Egypt"
    u7.save()

    # Updating Birthday for Users
    u1.birthday = date(2001, 7, 3)
    u1.save()
    u2.birthday = date(1983, 10, 4)
    u2.save()
    u3.birthday = date(1965, 2, 27)
    u3.save()
    u4.birthday = date(1990, 4, 30)
    u4.save()
    u5.birthday = date(2003, 5, 12)
    u5.save()
    u6.birthday = date(1979, 8, 6)
    u6.save()
    u7.birthday = date(1999, 1, 16)
    u7.save()

    # Updating Interests for Users
    u1.interests.create(label="Cooking")
    u1.interests.create(label="Football")
    u1.save()
    u2.interests.create(label="Basketball")
    u2.interests.create(label="Going to Gym")
    u2.save()
    u3.interests.create(label="Reading")
    u3.interests.create(label="Watching Movies")
    u3.save()
    u4.interests.create(label="Jogging")
    u4.interests.create(label="Traveling")
    u4.interests.create(label="Shopping")
    u4.save()
    u5.interests.create(label="Fishing")
    u5.interests.create(label="Video Games")
    u5.save()
    u6.interests.create(label="Listening to Music")
    u6.interests.create(label="Podcasts")
    u6.save()
    u7.interests.create(label="Board Games")
    u7.interests.create(label="Card Games")
    u7.interests.create(label="Watching the Sunset")
    u7.save()

    # Updating Friends List for Every User
    u1.friends.add(u2)
    u1.friends.add(u3)
    u1.save()
    u2.friends.add(u4)
    u2.save()
    u3.friends.add(u6)
    u3.friends.add(u4)
    u3.save()
    u6.friends.add(u7)
    u6.save()

    # Creating Friend Requests
    models.FriendRequest.objects.create(from_user=u4, from_user_id=u4.user_id, to_user=u5, to_user_id=u5.user_id)
    models.FriendRequest.objects.create(from_user=u4, from_user_id=u4.user_id, to_user=u6, to_user_id=u6.user_id)
    models.FriendRequest.objects.create(from_user=u7, from_user_id=u7.user_id, to_user=u1, to_user_id=u1.user_id)
    models.FriendRequest.objects.create(from_user=u3, from_user_id=u3.user_id, to_user=u2, to_user_id=u2.user_id)
    models.FriendRequest.objects.create(from_user=u6, from_user_id=u6.user_id, to_user=u1, to_user_id=u1.user_id)

    # Creating Posts
    current_time = datetime.now()
    p1 = models.Post.objects.create(owner=u1, timestamp=current_time, content="The new iPhone SE 2 is a great and affordable new phone! Just got it today! #apple")
    p2 = models.Post.objects.create(owner=u3, timestamp=current_time, content="Hello World! This is my first post")
    p3 = models.Post.objects.create(owner=u4, timestamp=current_time, content="I did a 8.5 km hike in the Cootes Paradise Trail in Hamilton this morning. Amazing!")
    p4 = models.Post.objects.create(owner=u7, timestamp=current_time, content="Canada has gone past the 40,000 cases mark for COVID-19, while the world reaches 2.6 million recorded cases.")
    p5 = models.Post.objects.create(owner=u2, timestamp=current_time, content="Call of Duty: Modern Warfare has reached over 30 million players worldwide!")

    # Adding Likes to Posts
    p1.likes.add(u3)
    p1.likes.add(u2)
    p1.save()
    p2.likes.add(u5)
    p2.likes.add(u7)
    p2.likes.add(u2)
    p2.likes.add(u1)
    p2.likes.add(u4)
    p2.save()
    p3.likes.add(u5)
    p3.likes.add(u3)
    p3.likes.add(u6)
    p3.save()
    p4.likes.add(u1)
    p4.likes.add(u7)
    p4.likes.add(u2)
    p4.save()
    p5.likes.add(u3)
    p5.save()

    
    
