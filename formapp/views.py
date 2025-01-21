from django.shortcuts import render, redirect
from .forms import ApplicationForm

# Create your views here.


def home(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ApplicationForm()
    return render(request, 'home.html', {'form': form})

def success(request):
    return render(request, 'success.html')
