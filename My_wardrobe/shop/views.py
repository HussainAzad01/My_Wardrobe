import datetime
from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, FeatProduct, contactus


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


def create(request):
    p = FeatProduct.objects.create(
        IsFiction=False,
        category="Non-Fiction",
        sub_category="Educational",
        product_name="The Reluctant Carer",
        product_price=199,
        product_desc=" ",
        publish_date=datetime.datetime(2023, 3, 24),
        image="shop/images/The snakehead.jpg"
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
            #this is also a way to add data to the data base by taking input from the user

            # contactus.objects.create(
            #     name=user_name,
            #     email=user_email,
            #     tel=user_tel,
            #     desc=user_feedback
            # )

            contact = contactus(name=user_name, email=user_email,tel=user_tel, desc=user_feedback)
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
