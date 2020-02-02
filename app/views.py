from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from app.forms import PostForm, LoginForm, RegisterForm
from django.views.generic import TemplateView, DetailView, ListView, FormView
from django.urls import reverse
from app.models import Post, Person


# Create your views here.

class FirstView(TemplateView):
    template_name = 'first.html'


class LogView(LoginView):
    template_name = 'login.html'
    form_class = LoginForm

    def get_success_url(self):
        return reverse('index')

    def form_valid(self, form):
        username = form.cleaned_data['username']
        pwd = form.cleaned_data['pwd']
        user = authenticate(self.request, username=username, password=pwd)
        if user is not None:
            login(self.request, user)
            return HttpResponseRedirect(self.get_success_url())
        return render(self.request, self.template_name)


class RegisterView(FormView):
    template_name = 'register.html'
    form_class = RegisterForm

    def get_success_url(self):
        return reverse('index')

    def form_valid(self, form):
        user = User.objects.create_user(username=form.cleaned_data['username'],
                                        password=form.cleaned_data['pwd'],
                                        email=form.cleaned_data['mail'])

        user.save()
        person = Person(user=user)
        person.save()
        return HttpResponseRedirect(self.get_success_url())


class BoardView(ListView):
    template_name = 'allposts.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        user = self.request.user
        query = Person.objects.filter(user=user)
        return Post.objects.filter(author__in=query)


class PostDetailView(DetailView):
    model = Post
    template_name = 'viewpost.html'


def postcreate(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('index')
    form = PostForm()
    return render(request, 'create.html', {'form': form})


def postedit(request, pk, template_name='edit.html'):
    post = get_object_or_404(Post, pk=pk)
    form = PostForm(request.POST or None, instance=post)

    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, template_name, {'form': form})


def postdelete(request, pk, template_name='delete.html'):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('index')
    return render(request, template_name, {'object': post})
