from django import forms
from django.contrib.auth.models import User

class PasswordForm(forms.Form):
    password = forms.CharField(max_length=30)
    vpassword = forms.CharField(max_length=30)

    def passwordchecker(self, password):
        #string = cd.get('password')
        uval = 0
        dval = 0
        for c in password:
            if c.isupper():
                print c
                uval += 1
            if c.isdigit():
                print c
                dval += 1

        if uval > 0:
            if dval > 0:
                return 1
        else:
            return 0

    def clean(self):
        cd = self.cleaned_data
        password = str(cd.get('password'))
        if cd.get('password') != cd.get('vpassword'):
            print cd.get('password')
            print password
            self.add_error('vpassword', "Passwords do not match.")
        if len(cd.get('password')) < 8:
            self.add_error('password', 'Password must be 8 characters or more.')
        if self.passwordchecker(password) < 1:
            self.add_error('password', "Password must contain uppercase letter AND digit.")
        return cd

class UsernameForm(forms.Form):
    username = forms.CharField(max_length=30)
    vusername = forms.CharField(max_length=30)

    def clean(self):
        cd = self.cleaned_data
        username = str(cd.get('username'))
        if User.objects.filter(username=username).exists():
            self.add_error('username', "Username is taken.")
        if cd.get('username') != cd.get('vusername'):
            self.add_error('username', "Usernames do not match.")
