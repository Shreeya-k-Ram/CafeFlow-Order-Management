from django.shortcuts import render
from .models import MenuItem

# Create your views here.
def menu_list(request):
    menu_items = MenuItem.objects.all()

    return render(
        request,
        'cafe/menu_list.html',
        {'menu_items': menu_items}
    )

