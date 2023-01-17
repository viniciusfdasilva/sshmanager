from django import forms

class StudentForm(forms.ModelForm):
    class Meta:
        model = Server
        widgets = {
           'password': forms.PasswordInput(),
        }