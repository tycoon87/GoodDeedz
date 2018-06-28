from __future__ import unicode_literals
from django.db import models
import re, bcrypt 

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
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