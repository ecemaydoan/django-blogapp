
from django.contrib import admin
from django.urls import path
from . import views

#http://127.0.0.1:8000/ -->Index
#http://127.0.0.1:8000/index -->Index
#http://127.0.0.1:8000/blogs/ -->blogs
#http://127.0.0.1:8000/blogs/3 -->blog-details


urlpatterns = [
    #path('admin/', admin.site.urls),
    path(" ",views.index),
    path("index",views.index),
    path("blogs",views.blogs),
    path("blogs/<int:id>",views.blog_detail),
]
