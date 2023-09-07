
from django.contrib.auth import authenticate, login
from django.views import View
from users.forms import UserCreationForm
from django.shortcuts import redirect, render, get_object_or_404
from .models import Category, Product
from django.shortcuts import render
from .forms import TagForm
from .models import Product

class Register(View):
    template_name = 'registration/register.html'

    def get(self, request):
        context = {
            'form': UserCreationForm()
        }
        return render(request, self.template_name, context)
    
    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username = username, password = password)
            login(request, user)
            return redirect('home')
        context={
            'form': form
        }
        return render(request, self.template_name, context)
    

class Catalog(View):
    template_name = 'home.html'

    def product_list(request, category_slug=None):
        category = None
        categories = Category.objects.all()
        products = Product.objects.filter(available=True)
        if category_slug:
            category = get_object_or_404(Category, slug=category_slug)
            products = products.filter(category=category)
        return render(request, 'home.html',{'category': category,'categories': categories,'products': products})
    
    def product_detail( request, id, slug):
        product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
        return render(request,
                  'product/details.html',
                  {'product': product})
    


class configurate(View):
    template_name = 'my_builds.html'

    def product_list(request):
        return render(request, 'my_builds.html')


    def get_products_by_tag(request):
        if request.method == 'POST':
            form = TagForm(request.GET)
            if form.is_valid():
                tag = form.cleaned_data['tag']
                products = Product.objects.filter(tag=tag)
                return render(request, 'tag_form.html', {'products': products})
        else:
            form = TagForm()
        return render(request, 'configurate.html', {'form': form})




def configurate(request):
    return render(request, 'configurate.html')

from django.shortcuts import render
from users.models import Product

def my_builds(request):
    if request.method == 'GET':
        tag1 = request.GET.get('tag1')
        tag2 = request.GET.get('tag2')
        tag3 = request.GET.get('tag3')
        tag4 = request.GET.get('tag4')
        tag5 = request.GET.get('tag5')
        tag6 = request.GET.get('tag6')
        tag7 = request.GET.get('tag7')
        
        if tag1:
            products1 = Product.objects.filter(tag=tag1)
        if tag2:
            products2 = Product.objects.filter(tag=tag2)
        if tag3:
            products3 = Product.objects.filter(tag=tag3)
        if tag4:
            products4 = Product.objects.filter(tag=tag4)
        if tag5:
            products5 = Product.objects.filter(tag=tag5)
        if tag6:
            products6 = Product.objects.filter(tag=tag6)
        if tag7:
            products7 = Product.objects.filter(tag=tag7)
        else:
            products1 = Product.objects.none()
            products2 = Product.objects.none()
            products3 = Product.objects.none()
            products4 = Product.objects.none()
            products5 = Product.objects.none()
            products6 = Product.objects.none()
            products7 = Product.objects.none()
        context = {'products1': products1, 'products2': products2, 'products3': products3, 'products4': products4, 'products5': products5, 'products6': products6, 'products7': products7}
        return render(request, 'my_builds.html',context)

    return render(request, 'my_builds.html')

def my_builds2(request):
    if request.method == 'GET':
        tag4 = request.GET.get('tag4')
        tag5 = request.GET.get('tag5')
        tag6 = request.GET.get('tag6')
        if tag4:
            products = Product.objects.filter(tag=tag4)
        elif tag5:
            products = Product.objects.filter(tag=tag5)
        elif tag6:
            products = Product.objects.filter(tag=tag6)
        else:
            products = Product.objects.all()
        context = {'products': products}
        return render(request, 'my_builds.html', context)

    return render(request, 'my_builds.html')


    



