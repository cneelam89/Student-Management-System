from django import forms
from .models import Student

class StudentRegistration(forms.ModelForm):
    class Meta:
        model=Student
        fields="__all__"
        labels={'fname':"First Name",'lname':"Last Name", "email":"Email id"}
        widgets={'fname':forms.TextInput(attrs={"class":"form-control"}),'lname':forms.TextInput(attrs={"class":"form-control"}),'email':forms.EmailInput(attrs={"class":"form-control"})}


    def clean_email(self):
        ealname = self.cleaned_data['email']
        print(self.cleaned_data)
        if not "@gmail.com" in ealname :
            raise forms.ValidationError('Enter email with gmail id only')
        return ealname
    