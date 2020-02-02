from django.shortcuts import render, redirect, get_object_or_404
from app.forms import PostForm
from django.views.generic import TemplateView, DetailView, ListView

from app.models import Post
# Create your views here.


# class IndexView(TemplateView):
#     template_name = 'allposts.html'


class BoardView(ListView):
    template_name = 'allposts.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        return Post.objects.all


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
