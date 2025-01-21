from django.shortcuts import render, get_object_or_404, redirect
from .models import Item

def index(request):
    Items = Item.objects.all()
    user_id = request.user.id

    context = {
        'Items': Items,
        'User_id': user_id,
    }
    return render(request, 'manage/index.html', context)

def detail(request, id):
    item = get_object_or_404(Item, id=id)
    context = {
        'item': item,
    }
    return render(request, 'manage/detail.html', context)