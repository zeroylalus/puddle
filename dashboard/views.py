from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from item import models

@login_required
def index(request):
    items = models.Item.objects.filter(created_by=request.user)
    return render(request, 'dashboard/index.html', {
        'items': items
    })