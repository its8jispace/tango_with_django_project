from django.shortcuts import render
from rango.models import Category
from rango.models import Page

# Create your views here.
from django.http import HttpResponse

def index(request):
    category_list = Category.objects.order_by('-likes')[:5]
    page_list = Page.objects.order_by('-views')[:5]

    context_dict = {}
    context_dict['boldmessage'] = 'Crunchy, creamy, cookie, candy, cupcake!'
    context_dict['categories'] = category_list
    context_dict['pages'] = page_list
    

    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    #Return a rendered response to send to the client.
    #We make use of the shortcut function to make our lives easier.
    #Note that the first parameter is the template we wish to use.
    context = {'newmessage': 'This tutorial has been put together by Saksham Thukral' }
    return render(request, 'rango/about.html', context=context)

def show_category(request, category_name_slug):
    context_dict = {}


    try:
        category = Category.objects.get(slug=category_name_slug)
        pages = Page.objects.filter(category=category)
        context_dict['pages'] = pages
        context_dict['category'] = category

    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['pages'] = None
    
    return render(request, 'rango/category.html', context=context_dict)
