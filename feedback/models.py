from django.db import models

# Create your models here.

class User(models.Model):
    userid = models.ForeignKey(max_length=200)
    username = models.CharField(max_length = 40)
    email = models.CharField(max_length=50)
    role = models.CharField(max_length= 10)
class Categor(models.Model):
    categoryid = models.CharField(max_length = 200)
    title = models.CharField(max_length = 20)
    description = models.CharField(max_length = 200)

class Complaint(models.Model):
    complaintid = models.CharField(max_length = 200)
    text = models.CharField(max_length = 200)
class AdminResponse(models.Model):
    adminresponseid = models.CharField(max_length = 200)
class Feedback(models.Model):
    feedbackid = models.CharField(max_length = 200)
