# from .forms import NewUserForm
from  django.contrib.auth import login, authenticate
from django. contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect

from django.contrib.auth import login
from django.contrib import messages

def register_request(request):

    return render(request,'login.html')

def login_request(request):
    if request.method=="POST":
        form=AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user =authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                messages.info(request,f"You are now loggged in as {username}.")
                return redirect()


# def register_request(request):
#     if request.method == "POST":
#         form = NewuserForm(request.POST)
#         if form. is_valid():
#             user =form.save()
#             login(request, user)
#             messages.success(request, "Registration complete")
#             return redirect("main:homepage")
#         messages.error(request, "Registration cant be completed due to invalid information.")
#         form = NewuserForm()
#         return render(request=request,template_name="main/register.html", context={"register_form":form})
