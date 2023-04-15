import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product, FeatProduct, contactus
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def index(request):
    products = Product.objects.all()
    Fiction_category = FeatProduct.objects.filter(IsFiction="True")
    nonFiction_category = FeatProduct.objects.filter(IsFiction="False")

    # logic for new_arrivals start from here
    all_dates = FeatProduct.objects.values_list("publish_date")
    from_date = datetime.date.today() - datetime.timedelta(days=7)
    # newArrivals() function
    new_arrivals = newArrivals(all_dates, from_date)
    # logic for new_arrivals ends here

    all_prods = [[Fiction_category], [nonFiction_category]]
    params = {'products': products, 'all_prods': all_prods, 'new_arrivals1': new_arrivals[:int(len(new_arrivals) / 2)],
              'new_arrivals2': new_arrivals[int(len(new_arrivals) / 2):]}
    return render(request, 'shop/index.html', params)


def signup(request):
    if request.method == "POST":
        user_name = request.POST.get('user_name')
        user_email = request.POST.get('user_email')
        user_password = request.POST.get('user_password')
        user_password_repeat = request.POST.get('user_password_repeat')

        try:
            if len(user_password) >= 8:
                if user_password_repeat == user_password:
                    if len(user_name) >= 3:
                        user = User.objects.create(
                            username=user_name,
                            email=user_email,
                            password=user_password,
                        )
                        user.last_login = datetime.datetime.now()
                        user.save()
                        return redirect("shop/login")

                    else:
                        error_msg = "User name is too short, try resolving mistakes"
                        return render(request, "shop/signup.html", {"error_msg": error_msg})
                else:
                    error_msg = "Password didn't match, try resolving mistakes"
                    return render(request, "shop/signup.html", {"error_msg": error_msg})
            else:
                error_msg = "Password should contain at least 8 characters, try resolving mistakes"
                return render(request, "shop/signup.html", {"error_msg": error_msg})

        except:
            error_msg = "username already exists, Try with the different one!!"
            return render(request, "shop/signup.html", {"error_msg": error_msg})

    return render(request, 'shop/signup.html')


def login(request):
    return render(request, 'shop/login.html')


def create(request):
    p = FeatProduct.objects.create(
        IsFiction=True,
        category="Fiction",
        sub_category="Hard-Science",
        product_name="Weaponized",
        product_price=279,
        product_desc="Ursula has lived twice the normal human lifespan, courtesy of the latest technology. But now she’s struggling to find excitement and purpose, so signs up to the Polity’s military. But after botching a powerful new ammunition test, she’s dismissed from service. Hunting for a simpler, more meaningful existence, she heads for the stars. And after founding a colony on the hostile planet of Threpsis, Ursula finally feels alive. Then deadly raptors attack and the colonists are forced to adapt in unprecedented ways. The raptors also raise a deeply troubling question: how could the Polity miss these apex predators? And alien ruins?",
        publish_date=datetime.datetime(2023, 4, 9),
        image="shop/images/weaponized.jpg"
    )


def cart(request):
    return render(request, 'shop/cart.html')


def wishlist(request):
    return render(request, 'shop/wishlist.html')


def about(request):
    return render(request, 'shop/about.html')


def contact(request):
    if request.method == "POST":
        user_name = request.POST.get('user_name', "")
        user_tel = request.POST.get('user_tel', "")
        user_email = request.POST.get('user_email', "")
        user_feedback = request.POST.get('feedback', "")
        if user_name == "":
            pass
        else:
            # this is also a way to add data to the data base by taking input from the user

            # contactus.objects.create(
            #     name=user_name,
            #     email=user_email,
            #     tel=user_tel,
            #     desc=user_feedback
            # )

            contact = contactus(name=user_name, email=user_email, tel=user_tel, desc=user_feedback)
            contact.save()

    return render(request, 'shop/contact.html')


def search(request):
    return HttpResponse("We are in search end point")


def productview(request):
    product = Product.objects.all()
    params = {'product': product}
    return render(request, 'shop/product_view.html', params)


def viewing(request, id):
    product = FeatProduct.objects.filter(id=id)
    params = {'product': product[0]}
    return render(request, 'shop/viewing.html', params)


def viewing2(request, id):
    product = Product.objects.filter(id=id)
    params = {'product': product[0]}
    return render(request, 'shop/viewing.html', params)


def checkout(request):
    return render(request, 'shop/check_out.html')


def tracker(request):
    return render(request, 'shop/tracker.html')


def newArrivals(all_dates, from_date):
    """
    this 'newArrivals' function is used to filter last 7 days books that've listed
    all_dates: gives all the date with in the database
    from_date: gives the date from which the books should be showing till present date
    """
    new_arrivals = []
    sorted_dates = []
    for date in all_dates:
        if date not in sorted_dates:
            sorted_dates.append(date)

    for dates in sorted_dates:
        for date in dates:
            if date > from_date:
                book = FeatProduct.objects.filter(publish_date=date)
                new_arrivals.append(book)
    return new_arrivals
