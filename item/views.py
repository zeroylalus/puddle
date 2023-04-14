from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
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
    if request.method == 'POST':
        form = forms.NewItemForm(request.POST,request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()
            return redirect('item:detail',pk=item.id)
    else:
        form = forms.NewItemForm()
        return render(request, 'item/form.html',{
            'form': form,
            'title': 'New item',
        })

@login_required
def edit(request,pk):
    item = get_object_or_404(models.Item,pk=pk, created_by=request.user)
    if request.method == 'POST':
        form = forms.EditItemForm(request.POST,request.FILES,instance=item)
        if form.is_valid():
            form.save()
            return redirect('item:detail',pk=item.id)
    else:
        form = forms.EditItemForm(instance=item)
        return render(request, 'item/form.html',{
            'form': form,
            'title': 'Edit item',
        })

@login_required
def delete(request,pk):
    item = get_object_or_404(models.Item,pk=pk, created_by=request.user)
    item.delete()
    return redirect('dashboard:index')