from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout 
from django.contrib.auth import authenticate, login as auth_login
from .models import Product,CartItem
from django.contrib.auth.decorators import login_required
# from django.contrib.auth import logout
# from django.shortcuts import redirect

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']

        user = User.objects.create_user(username=username, password=password, email=email)
        print(type(user))
        user.save()

        messages.success(request, 'Registration successful. Please login.')
        return redirect('login')

    return render(request, 'register.html')

def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user = authenticate(username=username, password=password)

        # print(user)
        if user is not None:
            request.session['user_id']=user.id
            return redirect('home')
        else:
            return render (request,'login.html',{"context":"check the credentials"})
    return render (request,'login.html')


# @login_required()
def logout_view(request):
    logout(request)
    return redirect('login')


# @login_required(login_url='/login/')
def home(request):
    
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})

# @login_required()
def add_to_cart(request, product_id):

    
    existing_item = CartItem.objects.filter(product=Product.objects.get(product_id=product_id),user_id=User.objects.get(id=request.session.get('user_id'))).first()
    print(existing_item)
    if existing_item is not None:
        
        existing_item.quantity += 1
        existing_item.save()
    else:
   
        new_item =  CartItem.objects.create(product=Product.objects.get(product_id=product_id), user_id=User.objects.get(id=request.session.get('user_id')))
        print(new_item)
        new_item.save()

    messages.success(request, 'Product has been added to the cart.')
    return redirect('home')

# @login_required()
def view_cart(request):
    user_id = request.session.get('user_id')
    cart_items = CartItem.objects.filter(user_id=user_id)

    # total_price =[sum(item.price)  for item in cart_items]

    return render(request, 'cart.html', {'cart_items': cart_items})