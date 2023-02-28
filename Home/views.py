from django.shortcuts import render
from .models import Product
from .form import ProductForm

# Create your views here.
def index(request):
    items = Product.objects.all()
    
    context = {
        "items":items
    }
    
   
   
    return render(request,"home/index.html",context)

def add_product(request):
  
    form = ProductForm()
    if request.method == "POST":
        form = ProductForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    
    
    
    context = {
        "form":form
    }
   
    return render(request,"home/create.html",context)