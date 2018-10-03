from __future__ import unicode_literals
from django.db import models
import re, bcrypt 

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NUMBER_REGEX = re.compile(r'^[1-9]/W+$')
class ValidateInfo(models.Manager):
    def basic_validator(self, postData):
        
        message = {}
        if not len(postData['Phonenumber']) >= 10:
            message["mustphone"] = "Please enter a valid Phone number 1234567890 !"
        if not EMAIL_REGEX.match(postData['Email']):
            message["mustemail"] = "Please enter a valid email!"
        if len(postData['Firstname']) < 2:
            message["lenFirstname"] = "First name should be more than 5 characters"
        if len(postData['Lastname']) < 2:
            message["lengLastname"] = "Last name should be more than 5 characters"
        if not len(postData['Firstname']):
            message["reqfirstname"] = " firstname is required!"
        if not len(postData['Lastname']):
            message["reqLastname"] = "Lastname is required!"
        if not len(postData['Email']):
            message["Email"] = "Email is required!"
        user = User.objects.filter(Email = postData['Email'])
        if user:
            message["emailexsis"] = "Sorry email already exist!"
        if len(postData['Password']) < 8:
            message["Password"] = "Blog desc should be more than 10 characters"
        if not postData['Password'] == postData['ConfirmPassword']:
            message["Password"] = "Passwors must match!"
        if message:
            return message
        else:
            newPassword = bcrypt.hashpw(postData['Password'].encode(),bcrypt.gensalt())
            user = self.create(Firstname = postData['Firstname'] , Lastname = postData['Lastname'],Email = postData['Email'], Dateofbirth = postData['Dateofbirth'], Phonenumber = postData['Phonenumber'], Password = newPassword)
            return message

    def Organizer_validation(self, postData):
        message = {}
        Open_spots = int(postData['Open_spots'])
        print Open_spots
        if len(postData['Title']) < 2:
            message['mustTitle'] = "Please add a Title"
        if len(postData['Cause']) < 5: 
            message['mustcause'] = "Please add what cause you support"
        if not len(postData['Open_spots']):
            message['mustspots'] = "Must have amount of availability"
        if len(postData['Types_of_work']) < 5:
            message['mustype_work'] = " Must discribe type of work needed"
        if len(postData['Description_header']) < 10:
            message ['mustheader'] = "Please give a header"
        if len(postData['Description_main']) < 50:
            message ['mustdescribe'] = "Please explain what your organization will do."
        if len(postData['Goles']) < 10: 
            message ['mustgoles'] = "please discribe the goles of your organization."
        if message:
            return message
        else:
            organization = self.create(Title = postData['Title'],Cause = postData['Cause'], Open_spots = Open_spots, Types_of_work = postData['Types_of_work'], Start_date = postData['Start_date'], Finish_date = postData['Finish_date'], Description_header = postData['Description_header'], Description_main = postData['Description_main'], Goles = postData['Goles'])
            return message
        
    def Login_validation(self, postData):
        print  postData['Email']
        message = {}
        user = User.objects.filter(Email = postData['Email'])
        if user:
            db_hashed = user[0].Password
            if db_hashed == bcrypt.hashpw(postData['Password'].encode(), db_hashed.encode()):
                message['status'] = "True"
                message['user'] = user[0]
                return message
            else:
                return message

class User(models.Model):
    objects = ValidateInfo()
    Firstname = models.CharField(max_length=255)
    Lastname = models.CharField(max_length=255)
    Dateofbirth = models.CharField(max_length=20)
    Phonenumber = models.CharField(max_length=10)
    Isorganizer = models.BooleanField(default=False)
    Email = models.CharField(max_length=255)
    Password = models.CharField(max_length=255)
    Datejoined = models.DateTimeField(auto_now_add = True)
    Friendships = models.ManyToManyField('self',related_name="Friend")

class User_adress(models.Model):
    objects = ValidateInfo()
    Street_number = models.IntegerField()
    Street_name = models.CharField(max_length = 255)
    City = models.CharField(max_length = 255)
    State_province = models.CharField(max_length = 255)
    Postcode = models.IntegerField()
    County = models.CharField(max_length = 30)

class Organizer(models.Model):
    objects = ValidateInfo()
    Organizer_id = models.ForeignKey(User, related_name='organizer')
    # Contributer_id = models.ForeignKey(User, related_name='Contributer_id')
    Associated_users = models.ManyToManyField('User',related_name="associated_user")
    Title = models.CharField(max_length=255)
    Cause = models.CharField(max_length=255)
    Open_spots = models.IntegerField()
    Types_of_work = models.CharField(max_length = 500)
    Start_date = models.DateTimeField(auto_now = False)
    Finish_date = models.DateTimeField(auto_now = False)
    Description_header = models.CharField(max_length = 500)
    Description_main = models.CharField(max_length = 500)
    Goles = models.CharField(max_length = 500)

class Organizer_address(models.Model):
    objects = ValidateInfo()
    Organizer_address = models.ForeignKey(Organizer, related_name='Organizer_address')
    Street_number = models.IntegerField()
    Street_name = models.CharField(max_length = 255)
    City = models.CharField(max_length = 255)
    State_province = models.CharField(max_length = 255)
    Postcode = models.IntegerField()
    County = models.CharField(max_length = 30)
