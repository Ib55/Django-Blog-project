from django.urls import path
from . import  views


app_name = "App_Blog"

urlpatterns = [
    path('',views.Home,name='home'),
    path('write/',views.CreateBlog.as_view(),name='create_blog'),
    path('blog_list/',views.BlogList.as_view(),name='blog_list'),
    path(r'^blog_details/<pk>/$',views.Blog_details,name='blog_details'),
    path('like/<pk>/',views.Like_Blog,name='like'),
    path('unlike/<pk>/',views.Unlike,name='unlike'),
    path('update/<pk>/',views.UpdateBlog.as_view(),name='update'),
    path('my_blogs/',views.MyBlogs.as_view(),name='my_blogs')
]

