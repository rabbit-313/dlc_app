from django import forms

class ChatGPTForm(forms.Form):
    question = forms.CharField(label='質問', widget=forms.Textarea)
    submit = forms.CharField(label='送信', widget=forms.TextInput(attrs={'type': 'submit'}))