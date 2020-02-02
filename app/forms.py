from django import forms
from app.models import Post, Person


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'message')


class LoginForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Nom d\'utilisateur '}))
    pwd = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Mot de passe'}))

    class Meta:
        model = Person
        fields = ('username', 'pwd')

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(LoginForm, self).__init__(*args, **kwargs)


class RegisterForm(forms.ModelForm):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Nom d\'utilisateur'}))
    mail = forms.EmailField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Mail@mail.com'}))
    pwd = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Mot de passe'}))
    pwd_confirm = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirmez'}))

    class Meta:
        model = Person
        fields = ('username', 'mail', 'pwd', 'pwd_confirm')

    def clean_username(self):
        username = self.cleaned_data['username']
        if not username.isalnum():
            self.add_error('username', 'Invalid characters detected')
            return None
        return username

    def clean(self):
        p1 = self.cleaned_data['pwd']
        p2 = self.cleaned_data['pwd_confirm']
        if p1 != p2:
            self.add_error('pwd', 'Passwords not corresponding')
            return None
        return super().clean()
