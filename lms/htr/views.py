from django.shortcuts import render

def index(request):
    return render(request, 'htr/index.html')

def login(request):
    return render(request, 'htr/login.html')

def signup(request):
    return render(request, 'htr/signup.html')

def dashboard(request):
    return render(request, 'htr/dashboard.html')

def learn(request):
    return render(request, 'htr/learn.html')

def compete(request):
    return render(request, 'htr/compete.html')

def practice(request):
    return render(request, 'htr/practice.html')

def subscribe(request):
    return render(request, 'htr/subscribe.html')

def rank(request):
    return render(request, 'htr/rank.html')

def ISO_27001(request):
    return render(request, 'htr/ISO_27001.html')

def explore(request):
    return render(request, 'htr/explore.html')
