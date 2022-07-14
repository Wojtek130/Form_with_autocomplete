from pyexpat import model
from django import forms
from . import models

class MovieForm(forms.ModelForm):
    class Meta:
        model = models.Movie
        fields = ("title",)


class DataLoginForm(forms.ModelForm):
    class Meta:
        model = models.LoginData
        fields = ("login", "password", "password_conf", "birth_date")

    def clean_login(self):
        data = self.cleaned_data.get("login")
        if data == "aa":
            raise forms.ValidationError("Enter valid login")
        return data

    def clean(self):
        p1 = self.cleaned_data.get("password")
        p2 = self.cleaned_data.get("password_conf")
        if p1 != p2:
            raise forms.ValidationError("Password and Password conf must be equal")

    # def clean_birth_date(self):
    #     data = self.cleaned_data.get("birth_date")
    #     print("validation", data, type(data))
    #     print(data, "!!!!!!!!!!")
    #     if data == "aa":
    #         raise forms.ValidationError("wrong birth_date")
    #     return data

