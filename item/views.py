from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from . import models
from . import forms

def detail(request,pk):
    item = get_object_or_404(models.Item,pk=pk)
    related_items = models.Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[0:3]
    return render(request,'item/detail.html',{
        'item': item,
        'related_items': related_items
    })

@login_required
def new(request):
    form = forms.NewItemForm()

    return render(request, 'item/form.html',{
        'form': form,
        'title': 'New item',
    })