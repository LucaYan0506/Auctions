from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django import forms
from datetime import datetime
import auctions

from .models import User, Auction,Bids,Comments,categories

class Auctions(forms.ModelForm):
    class Meta:
        model = Auction
        fields = ['author','title','categorie','image','bid','description']
        widgets = {
            'author': forms.HiddenInput(attrs={'value':'1'}),
            'title' : forms.TextInput( attrs={'class':'form-input'}),
            'categorie' : forms.Select( attrs={'class' : 'form-input'}),
            'image' : forms.TextInput( attrs={'placeholder':'Insert Url','class' : 'form-input'}),
            'bid' : forms.NumberInput(attrs={'class':'form-input','min':1,'max': 999999999}),
            'description' : forms.Textarea( attrs={'class':'form-input'}),
        }

def index(request):
    image = None
    if request.method == "POST":
         form = Auctions(request.POST)
         form.save()
         temp = Auction.objects.all().last()
         temp.author = User.objects.get(pk = request.user.pk)
         temp.save()
    
    #check it the current item is in the watchlist of the current user
    stuff_in_watchlist = []
    for stuff in Auction.objects.filter(isActive = True):
        stuff_in_watchlist.append(stuff.watchlist.filter(pk = request.user.pk).exists())

    #merge stuff_in_watchlist and Auction.objects.first(isActive = True)
    stuffs = zip(Auction.objects.filter(isActive = True),stuff_in_watchlist)

    return render(request, "auctions/index.html",{
        'title' : "Active Listings",
        'auction': stuffs,
        'path':'index',
    })

def login_view(request):
    if request.method == "GET" and request.GET.get('next'):
        return render(request, "auctions/login.html",{
            'next' : request.GET.get('next')
        })

    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            if request.POST['next'] != None and request.POST['next'] != '':
                return redirect(request.POST['next'])
            
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

def create_list(request):
    return render(request,"auctions/create_list.html",{
        "form":Auctions,
    })

def listing_page(request,id):
    stuff = Auction.objects.get(pk=id)
    message = None

    if stuff.isActive == False:
        bidder = Bids.objects.filter(stuff= stuff)
        if (Bids.objects.filter(stuff= stuff).count() > 0):
            if bidder.last().bidder == request.user:
                message = 'Congratulations, you won the auction'

    return render(request,'auctions/listing_page.html',{
        'auction':Auction.objects.get(pk=id),
        'message':message,
        'comments':Comments.objects.filter(stuff = id),
        'in_watchlist':Auction.objects.get(pk=id).watchlist.filter(pk = request.user.pk).exists(),
        'path':f'listing_page/{id}',
    })

def add_to_watchlist(request,id):
    stuff = Auction.objects.get(pk = id)
    stuff.watchlist.add(request.user)
    if (request.GET['next'] == 'index'):
        return HttpResponseRedirect("/")
    return  HttpResponseRedirect(f"/{request.GET['next']}/")

def remove_from_watchlist(request,id):
    Auction.objects.get(pk = id).watchlist.remove(request.user)
    if (request.GET['next'] == 'index'):
        return HttpResponseRedirect("/")
    return  HttpResponseRedirect(f"/{request.GET['next']}/")

def watchlist_view(request):
    auction = []
    stuff_in_watchlist = []
    for stuff in Auction.objects.all():
        if (stuff.watchlist.filter(pk = request.user.pk).exists()):
            auction.append(stuff)
            stuff_in_watchlist.append(True)

    stuffs =  zip(auction,stuff_in_watchlist)

    return render(request, "auctions/index.html",{
        'title' : "Watchlist",
        'auction': stuffs,
        'path':'watchlist'
    })

def add_bid(request):
    current_stuff = Auction.objects.get(pk = request.POST['pk'])
    if (int(request.POST['amount']) <= current_stuff.bid):
        return render(request,'auctions/listing_page.html',{
            'auction':Auction.objects.get(pk=request.POST['pk']),
            'error' : "You have to bid more than £" + str(current_stuff.bid) + ".00"
        })

    newbid = Bids(stuff = current_stuff,bidder=request.user,time=datetime.now(),val = request.POST['amount'])
    newbid.save()

    current_stuff.bid = request.POST['amount']
    current_stuff.save()

    return render(request,'auctions/listing_page.html',{
        'auction':Auction.objects.get(pk=request.POST['pk']),
        'success' : "Your bid was successful"
    })

def bid_history(request,id):
    stuff = Auction.objects.get(pk = id)
    bids = Bids.objects.filter(stuff = stuff)
    return render(request,"auctions/bid_history.html",{
        'bid':bids
    })

def close_auction(request,id):
    stuff = Auction.objects.get(pk=id)
    stuff.isActive = False
    stuff.save()
    return  HttpResponseRedirect(f"/listing_page/{id}/")

def add_comment(request,id):
    if request.method == "POST":
        Stuff = Auction.objects.get(pk = request.POST['stuff'])
        comments = Comments(stuff = Stuff,author = request.user, text = request.POST['comment-input'],time=datetime.now())
        comments.save()
    return  listing_page(request,id)

def  categories_view(request,category):
    if category == 'All':
        stuffs =  Auction.objects.all()
    else:
        temp = categories.objects.get(categorie = category)
        stuffs = Auction.objects.filter(categorie = temp, isActive = True)

     #check it the current item is in the watchlist of the current user
    stuff_in_watchlist = []
    for stuff in stuffs:
        stuff_in_watchlist.append(stuff.watchlist.filter(pk = request.user.pk).exists())

    #merge stuff_in_watchlist and Auction.objects.first(isActive = True)
    stuffs = zip(stuffs,stuff_in_watchlist)

    return render(request,'auctions/categories.html',{
        'title' : f"{category} Listings",
        'auction': stuffs,
        'path':f'categories/{category}',
    })

def my_listing_view(request):
    #check it the current item is in the watchlist of the current user
    stuff_in_watchlist = []
    for stuff in Auction.objects.filter(author = request.user):
        stuff_in_watchlist.append(stuff.watchlist.filter(pk = request.user.pk).exists())

    #merge stuff_in_watchlist and Auction.objects.filter(author = request.user)
    stuffs = zip(Auction.objects.filter(author = request.user),stuff_in_watchlist)

    return render(request, "auctions/index.html",{
            'title' : "My Listings",
            'auction': stuffs,
            'path':'index',
    })