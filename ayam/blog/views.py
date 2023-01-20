from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import logout, authenticate, login
import json
from django.views.decorators.csrf import csrf_exempt
from . import forms

# Create your views here.
def home(request):
    return render(request,'index.html')

from . models import Karyawan
def about(request):
    postingan=Karyawan.objects.all()
    context ={
        'TampungKaryawan':postingan,
    }
    return render(request,'about.html',context)

def review(request):
    return render(request,'review.html')

def login_request(request):
    if request.method == 'POST':
        form = forms.Login(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username') 
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)

                return redirect('https://example.com/')
        else:
            return render(request = request,
                    template_name = "login.html",
                    context={"form":form,"error":"Incorrect Username or Password"})
    form = forms.Login()
    return render(request = request,
                    template_name = "login.html",
                    context={"form":form})

def register(request):
    if request.method == "POST":
        form = forms.Registrasi(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            login(request, user)
            return redirect("home")

        return render(request = request,
                          template_name = "register.html",
                          context={"form":form})
    form = forms.Registrasi()
    return render(request = request,
                  template_name = "register.html",
                  context={"form":form})

from . models import DaftarMenu
def menu(request):
    postingan=DaftarMenu.objects.all()
    context ={
        'TampungPostingan':postingan,
    } 
    return render (request, 'menu.html',context)

def cart(request):
    if request.user.is_authenticated:
        return render(request, "cart.html")
    else:
        return redirect("login")

def logout_request(request):
    logout(request)
    return redirect("home")



def checkout(request):
    if request.method == 'POST':
        cart = json.loads(request.POST.get('cart'))
        price = request.POST.get('price_of_cart')
        username = request.user.username
        response_data = {}
        list_of_items = [item["item_description"] for item in cart]

        order = UserOrder(username=username, order=list_of_items, price=float(price), delivered=False) #create the row entry
        order.save() #save row entry in database

        response_data['result'] = 'Order Recieved!'

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )

def view_orders(request):
    if request.user.is_superuser:
        #make a request for all the orders in the database
        rows = UserOrder.objects.all().order_by('-time_of_order')
        #orders.append(row.order[1:-1].split(","))

        return render(request, "orders.html", context = {"rows":rows})
    else:
        rows = UserOrder.objects.all().filter(username = request.user.username).order_by('-time_of_order')
        return render(request, "orders.html", context = {"rows":rows})

def mark_order_as_delivered(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        UserOrder.objects.filter(pk=id).update(delivered=True)
        return HttpResponse(
            json.dumps({"good":"boy"}),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )
from . models import SavedCarts,UserOrder
def save_cart(request):
    if request.method == 'POST':
        cart = request.POST.get('cart')
        saved_cart = SavedCarts(username=request.user.username, cart=cart) #create the row entry
        saved_cart.save() #save row entry in database
        return HttpResponse(
            json.dumps({"good":"boy"}),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )

def retrieve_saved_cart(request):
    try:
        saved_cart = SavedCarts.objects.get(username = request.user.username)
        return HttpResponse(saved_cart.cart)
    except:
        return HttpResponse('')

def check_superuser(request):
    print(f"User super??? {request.user.is_superuser}")
    return HttpResponse(request.user.is_superuser)
