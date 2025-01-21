from django.shortcuts import render, get_object_or_404, redirect
from .models import Item
from django.contrib.auth.decorators import login_required

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

@login_required
def delete(request, id):
    item = get_object_or_404(Item, pk=id)
    item.delete()
    items = Item.objects.all()
    context = {
        'message': 'ページID:'+ str(id) + 'を削除しました',
        'items': items,
    }
    return render(request, 'manage/index.html', context)