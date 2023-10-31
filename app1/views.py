from django.shortcuts import render, redirect
from.models import Register, Login
from django.http import HttpResponse
# Create your views here.

def view(request):
    return render(request, 'register.html')

def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        balance = request.POST['balance']
        accno = request.POST['accno']
        username = request.POST['username']
        password = request.POST['password']
        data = Register.objects.create(name=name, phone=phone, balance=balance, accno=accno, username=username)
        data.save()
        data1 = Login.objects.create(username=username, password=password)
        data1.save()
        return HttpResponse("Account Open Successful")


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            data = Login.objects.get(username=username)
            if data.password == password:
                request.session['id'] = username    #seasion created to continue
                return redirect(accountdetails)
            else:
                return HttpResponse("PASSWORD ERROR")
        except Exception:
            return HttpResponse("USERNAME ERROR")
    else:
        return render(request, 'login.html')


def accountdetails(request):
    if 'id' in request.session:
        username = request.session['id']
        if request.method == 'GET':
            data = Register.objects.filter(username=username).all()
            return render(request, 'accountdetails.html', {'data': data})

def logout(request):
    if 'id' in request.session:
        request.session.flush()
        return redirect(login)
def regtolog(request):
    return redirect(login)

def logtoreg(request):
    return redirect(view)

def deptoacc(request):
    return redirect(accountdetails)

def wittoacc(request):
    return redirect(accountdetails)



def deposit(request):
    return render(request, 'deposit.html')

def withdraw(request):
    return render(request, 'withdraw.html')

def addmoney(request):
    if request.method == 'POST':
        accno = request.POST['accno']
        deposit = int(request.POST['deposit'])
        data = Register.objects.get(accno=accno)
        data.balance += deposit
        data.save()
        context = {
            'message': "The amount is deposit to your account"
        }
        return render(request,'deposit.html', context)


def takemoney(request):
    if request.method == 'POST':
        accno = request.POST['accno']
        withdraw = int(request.POST['withdraw'])
        if withdraw % 100 == 0 or withdraw % 200 == 0 or withdraw % 500 == 0:

            data = Register.objects.get(accno=accno)
            data.balance -= withdraw
            if data.balance< 1000:
                return render(request,'withdraw.html', {'note': 'there would be no minimum balance'})
            data.save()
            context = {
                'message': "The amount is withdrawn from your account"
            }
            return render(request, 'withdraw.html', context)
        else:
            return render(request, 'withdraw.html', {'withdrawerror': "Please enter amount multiple of 100,200 or 500"})

# Create your views here.
