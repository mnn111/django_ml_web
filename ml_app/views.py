from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import TitanicDb
from .forms import TitanicForm
from django.contrib import messages
from . import ml_models


def home(request):
    return render(request, 'home.html')

@login_required
def mainframe(request):
    return render(request, 'mainframe.html')

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def titanic(request):
    # if request.method == 'POST':
    #     form = TitanicForm(request.POST or None)
    #     print('\n\n\n\nform--------', form)
    #     if form.is_valid():
    #         form.save()
    #         all_items = TitanicDb.objects.all()
    #         messages.success(request, ('new request added..'))
    #         print('message value', messages.success(request, ('new request added..')))
    #         return render(request, 'titanic.html', {'all_items': all_items})
    # else:
        all_items = TitanicDb.objects.all()
        return render(request, 'titanic.html', {'records': all_items})

@login_required
def titanic_pred(request):
    return ml_models.titanic(request)





#
#
#
#     if request.method == 'POST':
#         form = TaskForm(request.POST or None)
#         if form.is_valid():
#             form.save()
#             all_items = TaskDb.objects.all()
#             messages.success(request, ('new request added..'))
#             print('message value', messages.success(request, ('new request added..')))
#             return render(request, 'index.html', {'all_items': all_items})
#
#     else:
#         all_items = TaskDb.objects.all()
#         return render(request, 'index.html', {'all_items': all_items})
#
# def DeleteEntry(request, list_id):
#     item = TaskDb.objects.get(pk=list_id)
#     item.delete()
#     messages.success(request, ('Item deleted.....'))
#     return redirect('home')








