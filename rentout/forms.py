from django import forms
from django.utils import timezone

from .models import Wish

__author__ = 'king'


class WishCreationForm(forms.ModelForm):

    class Meta:
        model = Wish
        fields = ("price", "description", "rating", "start_date", "end_date")

    # def clean_password2(self):
    #     password1 = self.cleaned_data.get("password1")
    #     password2 = self.cleaned_data.get("password2")
    #     if password1 and password2 and password1 != password2:
    #         raise forms.ValidationError(
    #             self.error_messages['password_mismatch'],
    #             code='password_mismatch',
    #             )
    #     return password2

    def save(self, outorder, user, commit=True):
        wish = super(WishCreationForm, self).save(commit=False)
        wish.outorder = outorder
        wish.creator = user
        wish.pub_date = timezone.now()
        if commit:
            wish.save()
        return wish

