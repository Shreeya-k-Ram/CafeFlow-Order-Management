from django.shortcuts import render, redirect
from .models import MenuItem, Order, Category
from .forms import OrderForm
from django.contrib import messages
from django.db.models import Sum

# Create your views here.
def home(request) :
    return render(
        request, 
        'cafe/home.html'
    )

def menu_list(request):
    menu_items = MenuItem.objects.all()

    search_query = request.GET.get('search')

    if search_query:
        menu_items = menu_items.filter(
            name__icontains=search_query
        )

    category_id = request.GET.get('category')

    if category_id:
        menu_items = menu_items.filter(
            category_id=category_id
        )

    categories = Category.objects.all()

    return render(
        request,
        'cafe/menu_list.html',
        {
            'menu_items': menu_items,
            'categories': categories
        }
    )

def order_view(request):

    if request.method == 'POST':
        form = OrderForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request , 'Order placed successfully')
            return redirect('/order/')

    else:
        form = OrderForm()

    return render(
        request,
        'cafe/order_form.html',
        {'form': form}
    )

def order_list(request) :
    orders = Order.objects.order_by('created_at')

    return render(
        request, 
        'cafe/order_list.html',
        {'orders' : orders}
    )

def dashboard(request):
    total_orders = Order.objects.count()
    pending_orders = Order.objects.filter(status='Pending').count()
    preparing_orders = Order.objects.filter(status='Preparing').count()
    ready_orders = Order.objects.filter(status='Ready').count()
    delivered_orders = Order.objects.filter(status='Delivered').count()

    top_item = None
    items = {}

    for order in Order.objects.all():

        item_name = order.menu_item.name

        if item_name not in items:
            items[item_name] = 0

        items[item_name] += order.quantity

        if items:
            top_item = max(items, key=items.get)

    return render(
        request,
        'cafe/dashboard.html',
        {
            'total_orders': total_orders,
            'pending_orders': pending_orders,
            'preparing_orders': preparing_orders,
            'ready_orders': ready_orders,
            'delivered_orders': delivered_orders,
            'top_item': top_item
        }
    )

