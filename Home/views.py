<<<<<<< HEAD
from django.shortcuts import render,redirect
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

def update(request,pk):
    listing = Product.objects.get(id=pk)
    form = ProductForm(instance=listing)
    if request.method == "POST":
        form = ProductForm(request.POST,instance=listing , files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/")
    
    
    
    context = {
        "form":form
    }
   
    return render(request,"home/update.html",context)

def delete(request,pk):
    listing = Product.objects.get(id=pk)
    delete()
    return redirect("/")
=======
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"home/index.html")
>>>>>>> origin/main
