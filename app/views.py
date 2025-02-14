from django.shortcuts import render

# Create your views here.

def blog_index(request):
    return render(request,'index.html')

def blog_about(request):
    return render(request,'about.html')

def blog_coffees(request):
    return render(request,'coffees.html')

def blog_contact(request):
    return render(request,'contact.html')

def blog_bl(request):
    return render(request,'blog.html')


