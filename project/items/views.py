from django.shortcuts import render, get_object_or_404, redirect
from .models import Item
from .forms import ItemForm

def read_items(request):
    items = Item.objects.all()
    return render(request, 'items/read.html', {'items': items})

def create_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('read_items')
    else:
        form = ItemForm()
    return render(request, 'items/create.html', {'form': form})

def update_item(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('read_items')
    else:
        form = ItemForm(instance=item)
    return render(request, 'items/update.html', {'form': form})

def delete_item(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('read_items')
    return render(request, 'items/delete.html', {'item': item})
