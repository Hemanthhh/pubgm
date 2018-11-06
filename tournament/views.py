from django.shortcuts import render
from django.http import HttpResponseRedirect
from . import forms
# Create your views here.



def tournament(request):
    form = forms.Enroll()
    if request.method == "POST":
        form = forms.Enroll(request.POST)
        if form.is_valid():
            form.save(commit=True)
    return render(request, 'home.html',{'Form':form})

def paytm(request):
        return HttpResponseRedirect('http://m.p-y.tm/requestPayment?recipient=7075755633&amount=200&comment=squardtournament')