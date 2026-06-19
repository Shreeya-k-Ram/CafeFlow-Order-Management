from django.shortcuts import render, redirect
from .models import MenuItem
from .forms import OrderForm

# Create your views here.
def menu_list(request):
    menu_items = MenuItem.objects.all()

    return render(
        request,
        'cafe/menu_list.html',
        {'menu_items': menu_items}
    )

def order_view(request):

    if request.method == 'POST':
        form = OrderForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/order/')

    else:
        form = OrderForm()

    return render(
        request,
        'cafe/order_form.html',
        {'form': form}
    )

