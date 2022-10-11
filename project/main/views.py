from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.core.paginator import Paginator
from .forms import *


# Create your views here.

def home(request):

    categories = Category.objects.all()

    context = {
        'categories':categories
    }
    return render(request, 'home.html', context)


def category_detail(request, id):
    category = get_object_or_404(Category, id=id)
    categories = Category.objects.all()
    products = category.productcategory.all()
    print(products)
    paginator = Paginator(products, 1)
    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)

    test_form = TestForm(request.POST)
    if request.method == "POST":
        test_form = TestForm(request.POST)
        if test_form.is_valid():
            test_form.save()
            print(test_form)
            return redirect('home')
            



    context = {
        'products': products,
        'categories': categories,
        'test_form':test_form

    }

    return render(request, 'test_detail.html', context)