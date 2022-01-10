from django.db import models

from django.contrib.auth.models import User
import uuid
from django.db.models.signals import post_delete, post_save


# Create your models here.
class StudentInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=200,null=True,blank=True)
    username = models.CharField(max_length=200,null=True,blank=True)
    classes = models.CharField(max_length=200,null=True,blank=True)
    school = models.CharField(max_length=200,null=True,blank=True)
    mobile = models.IntegerField(null=True,blank=True)
    address = models.TextField(null=True,blank=True)
    rollno = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.user)

def createProfile(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = StudentInfo.objects.create(
            user = user,
            username = user.username,
        )
def updateUser(sender, instance, created, **kwargs):
    profile = instance
    user = profile.user
    if created == False:
        user.username = profile.username
        user.save()

post_save.connect(createProfile,sender=User)
post_save.connect(updateUser,sender=StudentInfo)

class StudentAcademics(models.Model):
    rollno =models.ForeignKey(StudentInfo,on_delete=models.CASCADE,null=True,blank=True)
    maths = models.IntegerField(null=True,blank=True)
    physics = models.IntegerField(null=True,blank=True)
    english = models.IntegerField(null=True,blank=True)
    chemistry = models.IntegerField(null=True,blank=True)
    biology = models.IntegerField(null=True,blank=True)

    def __str__(self):
        return str(self.rollno)