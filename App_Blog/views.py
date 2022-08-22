
from django.shortcuts import render
from django.views.generic import CreateView,UpdateView,ListView,DetailView,DeleteView,View,TemplateView
from App_Blog.models import Blog,Comment,Likes
from django.urls import reverse_lazy,reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import uuid
from django.shortcuts import HttpResponseRedirect
from App_Blog.forms import CommentForm
# Create your views here.

class MyBlogs(LoginRequiredMixin,TemplateView):
    template_name = 'App_Blog/my_blogs.html'


def Home(request):
    return HttpResponseRedirect(reverse('App_Blog:blog_list'))

class CreateBlog(LoginRequiredMixin,CreateView):
    model = Blog
    template_name = 'App_Blog/create_blog.html'
    fields = ('title','blog_content','blog_image')

    def form_valid(self,form):
        blog_obj = form.save(commit=False)
        blog_obj.author = self.request.user
        blog_obj.save()
        return HttpResponseRedirect(reverse('App_Blog:home'))
        

class BlogList(ListView):
    context_object_name = 'blogs'
    model = Blog
    template_name = 'App_Blog/blog_list.html'


@login_required
def Blog_details(request,pk):
    blog = Blog.objects.get(pk=pk)
    form = CommentForm()
    already_liked = Likes.objects.filter(blog=blog,user=request.user)
    if already_liked:
        like = True
    else:
        like = False
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.blog = blog
            comment.save()
            return HttpResponseRedirect(reverse('App_Blog:blog_details',kwargs={'pk':pk}))
    return render(request,'App_Blog/blog_details.html',context={'blog':blog,'form':form,'like':like})

@login_required
def Like_Blog(request,pk):
    blog = Blog.objects.get(pk=pk)
    already_like = Likes.objects.filter(blog=blog,user=request.user)
    if not already_like:
        like = Likes(blog=blog,user=request.user)
        like.save()
        return HttpResponseRedirect(reverse('App_Blog:blog_details',kwargs={'pk':blog.pk}))

@login_required
def Unlike(request,pk):
    blog = Blog.objects.get(pk=pk)
    user = request.user
    already_liked = Likes.objects.filter(blog=blog,user=user)
    already_liked.delete()
    return HttpResponseRedirect(reverse('App_Blog:blog_details',kwargs={'pk':blog.pk}))

class UpdateBlog(LoginRequiredMixin,UpdateView):
    model = Blog
    template_name = 'App_Blog/edit_blog.html'
    fields = ('title','blog_content','blog_image')

    def get_success_url(self,**kwargs):
        return reverse_lazy('App_Blog:blog_details',kwargs={'pk':self.object.pk})

