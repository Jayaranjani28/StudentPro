from .models import StudentInfo,StudentAcademics

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import StudentInfo

class LoginRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1','password2']
        labels = {
                'username':'Name',
        }
    def __init__(self, *args, **kwargs):
        super(LoginRegisterForm, self).__init__(*args, **kwargs)
         
        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'form-control'})

class ProfileForm(forms.ModelForm):
    class Meta:
        model = StudentInfo
        fields = ['name','classes','school','mobile','address']
       
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
         
        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'form-control'})

class AcademicForm(forms.ModelForm):
    class Meta:
        model = StudentAcademics
        fields = ['rollno','maths','physics','chemistry','biology','english']
       
    def __init__(self, *args, **kwargs):
        super(AcademicForm, self).__init__(*args, **kwargs)
         
        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'form-control'})