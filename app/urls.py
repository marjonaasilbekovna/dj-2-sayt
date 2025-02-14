from django .urls import path
from .views import blog_index, blog_about, blog_contact, blog_coffees, blog_bl

urlpatterns = [
path('',blog_index , name='home-page'),
path('about/',blog_about , name='about-page'),
path('contact/',blog_contact , name='contact-page'),
path('coffees/',blog_coffees , name='coffees-page'),
path('blog/',blog_bl , name='blog-page')

]
