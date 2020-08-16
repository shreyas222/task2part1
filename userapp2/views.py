from django.shortcuts import render, redirect

# Create your views here.
from userapp2.models import UserProfile


def intro(request):
    if request.method == 'POST':
        f_name = request.POST.get('fname')
        l_name = request.POST['lname']
        ph_no = request.POST['phno']
        email = request.POST['email']
        gender = request.POST.get('gender')

        profile = UserProfile(f_name=f_name, l_name=l_name, ph_no=ph_no, email=email, gender=gender)
        profile.save()

        return redirect('intro')
    else:
        return render(request, 'intro.html')


def call(request):
    if request.method == 'POST':
        email = request.POST['email']
        try:
            profile = UserProfile.objects.get(email=email)
            return render(request, 'check.html', {'profile': profile, 'message': 'Found user!'})
        except UserProfile.DoesNotExist:
            return render(request, 'check.html', {'message': 'Sorry no user with the entered email found'})

    else:
        return render(request, 'call.html')