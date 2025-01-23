from django.shortcuts import render
from manage.models import Item
from django.contrib.auth.decorators import login_required

@login_required
def search(request):
    # 全てのメーカー名を取得（重複なし）
    manufacturers = Item.objects.values_list('Manufacturer', flat=True).distinct()

    context = {
        'manufacturers': manufacturers,
    }
    return render(request, 'search/search.html', context)

@login_required
def results(request):
    query = request.GET.get('q', '').strip()  # 検索クエリを取得
    selected_manufacturer = request.GET.get('manufacturer', '').strip()  # メーカー選択を取得

    # 初期値を設定
    results = Item.objects.all()

    # 複数キーワードでのテキスト検索
    if query:
        keywords = query.split()  # スペースでキーワードを分割
        for keyword in keywords:
            results = results.filter(name__icontains=keyword)

    # メーカーでの絞り込み
    if selected_manufacturer:
        results = results.filter(Manufacturer=selected_manufacturer)

    # メーカー一覧を取得（重複を除いて取得）
    manufacturers = Item.objects.values_list('Manufacturer', flat=True).distinct()

    context = {
        'q': query,
        'results': results,
        'manufacturers': manufacturers,
        'selected_manufacturer': selected_manufacturer,
    }
    return render(request, 'search/search.html', context)
