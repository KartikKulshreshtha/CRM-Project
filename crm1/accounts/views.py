from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import *
from .forms import *
from django.forms import inlineformset_factory
from .filters import OrderFilter
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        print('Aa rhi hai')
        form = CreateUserForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, f"{user}, you  registered your account successfully!!")
            return redirect('login')
    context = {
        'form': form
    }
    return render(request, 'accounts/register.html', context)

def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.info(request, "Username or Password is incorrect")
    return render(request, 'accounts/login.html')

def home(request):
    customers = Customer.objects.all()
    orders = Order.objects.all()
    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()
    
    context = {
        'customers': customers,
        'orders': orders,
        # 'total_customers': total_customers,
        'total_orders': total_orders,
        'delivered': delivered,
        'pending': pending,
    }
    return render(request, 'accounts/dashboard.html', context)

def products(request):
    products = Products.objects.all()
    context = {
        'data': products
    }
    return render(request, 'accounts/products.html', context)

def customer(request, pk):
    customer = Customer.objects.get(id=pk)
    
    orders = customer.order_set.all()
    order_count = orders.count()
    myfilters = OrderFilter(request.GET, queryset=orders)
    orders = myfilters.qs
    context = {
        'customer': customer,
        'orders': orders,
        'count': order_count,
        'myfilters': myfilters
    }
    return render(request, 'accounts/customer.html', context)

def createOrder(request, id):
    OrderFormSet = inlineformset_factory(Customer, Order, fields=('product', 'status'), extra=10)
    customer = Customer.objects.get(id=id)
    formset = OrderFormSet(queryset=Order.objects.none(), instance=customer)
    if request.method == "POST":
        formset = OrderFormSet(request.POST, instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('home')
    context = {'forms': formset, 'customer': customer}
    return render(request, 'accounts/order_form.html', context)

def updateOrder(request, id):
    order = Order.objects.get(id=id)
    forms = OrderForm(instance=order)
    if request.method == "POST":
        forms = OrderForm(request.POST, instance=order)
        if forms.is_valid():
            forms.save()
            return redirect('home')
    context = {'forms': forms}
    return render(request, 'accounts/order_form.html', context)


def deleteOrder(request, id):
    order = Order.objects.get(id=id)
    if request.method == "POST":
        order.delete()
        return redirect('/')
    context = {
        'order': order
    }
    return render(request, 'accounts/delete.html', context)


def createCustomer(request):
    forms = CustomerForm()
    if request.method == "POST":
        forms = CustomerForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('/')
        
    context = {
        'forms': forms
    }
    return render(request, 'accounts/customer_form.html', context)