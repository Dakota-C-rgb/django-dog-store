from django.shortcuts import render, redirect
from app.models import DogProduct, Purchase, DogTag
from django.contrib import messages
from datetime import datetime
from app.forms import NewDogTagForm
# Create your views here.

def home(request):
    dog_products = DogProduct.objects.all()
    return render(request, "home.html", {"dog_products": dog_products})


def dog_product_detail(request, id):
    dog_product = DogProduct.objects.get(id=id)
    return render(request, "dog_product_detail.html", {"dog_product": dog_product})


def purchase_dog_product(request, id):
    dog_product = DogProduct.objects.get(id=id)
    if dog_product.quantity != 0:
        messages.success(request, f"Purchased {dog_product.name}")
        dog_product.quantity -= 1
        dog_product.save()
        purchase = Purchase.objects.create(dog_product=dog_product, purchased_at=datetime.now())
        return redirect("purchase_detail", purchase.id)
    else:
        messages.error(request, f"{dog_product.name} is out of stock")
        return redirect("dog_product_detail", dog_product.id)


def purchase_detail(request, id):
    purchase = Purchase.objects.get(id=id)
    return render(request, "purchase_detail.html", {"purchase":purchase})


def new_dog_tag(request):
    if request.method == "GET":
        return render(request, "new_dog_tag.html")
    elif request.method == "POST":
        form = NewDogTagForm(request.POST)
        if form.is_valid():
            owner_name = form.cleaned_data["owner_name"]
            dog_name = form.cleaned_data["dog_name"]
            dog_birthday = form.cleaned_data["dog_birthday"]
            owner_address = form.cleaned_data["owner_address"]
            dog_color = form.cleaned_data["dog_color"]
            new_dog_tag = DogTag.objects.create(owner_name=owner_name, dog_name=dog_name, dog_birthday=dog_birthday,
            dog_color=dog_color, owner_address=owner_address)
            return redirect("dog_tag_list")
        if not form.is_valid():
            return render(request, "new_dog_tag.html", {"form":form})


def dog_tag_list(request):
    dog_tags = DogTag.objects.all()
    return render(request, "dog_tag_list.html", {"dog_tags":dog_tags})