from django import forms
from .models import Profile


class ProfileModelForm(forms.ModelForm):
    class Meta:
        model =Profile
        #fields =( '__all__')
        fields = ('first_name','last_name','bio','avatar')