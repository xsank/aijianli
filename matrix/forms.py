__author__ = 'xsank'

from django import forms


class ResumeForm(forms.Form):
    title = forms.CharField(label='title', max_length=40)
    style = forms.IntegerField(label='style')
    language = forms.CharField(label='language', max_length=10)
    is_open = forms.BooleanField(
        label='is_open', widget=forms.CheckboxInput, required=False)
    content = forms.CharField(label='content', widget=forms.Textarea)

    def clean(self):
        self.cleaned_data['is_open'] = True if self.data.get(
            'is_open', None) else False


class UserForm(forms.Form):
    name = forms.CharField(label='name', max_length=20)
    photo = forms.ImageField(label='photo')
