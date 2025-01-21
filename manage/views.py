from django.shortcuts import render, get_object_or_404, redirect
from .models import Item
from django.contrib.auth.decorators import login_required
from .forms import RegForm

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

@login_required
def new(request):
    regForm = RegForm()
    context = {
        'regForm':regForm,
    }
    return render(request, 'manage/add.html', context)

@login_required
def create(request):
    if request.method == 'POST':
        regForm = RegForm(request.POST)
        if regForm.is_valid():
            reg = regForm.save(commit=False)
            reg.user = request.user  # ログインしているユーザーをセット
            reg.save()
            return redirect('manage:detail', id=reg.id)
        else:
            # フォームが無効な場合、エラーメッセージを含めてフォームを再表示
            return render(request, 'manage/add.html', {'regForm': regForm})
    else:
        regForm = RegForm()
    return render(request, 'manage/add.html', {'regForm': regForm})