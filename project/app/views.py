from django.shortcuts import render, redirect
from .models import Hotels

def index(request):
    hotels = Hotels.objects.all()
    context = {"hotels":hotels}
    return render(request, 'index.html', context)

def add_hotel(request):
    if request.method == 'POST':
        hotels = request.POST
        if hotels['name'] != '' and hotels['description'] != '' and hotels['date_openning'] != '': # this is to be sure that no inputs are empty
            name = hotels['name']
            description = hotels['description']
            date_openning = hotels['date_openning']
            add = Hotels()
            add.name = name
            add.description = description
            add.date_openning = date_openning
            add.clean_fields() # to check if validators work
            add.save()
            return redirect('index')
        else:
            return render(request, 'add_hotel.html')    
    else:
        return render(request, 'add_hotel.html')
    
def update_hotel(request, id):
    hotels = Hotels.objects.get(id=id)
    if request.method == 'POST':
        hotels.name = request.POST['name']
        hotels.description = request.POST['description']
        hotels.date_openning = request.POST['date_openning']
        hotels.clean_fields()
        hotels.save()
        return redirect('index')
    else:
        return render(request, 'update_hotel.html')

def full_info(request, name):
    hotels = Hotels.objects.get(name = name)
    context = {"hotels":hotels}    
    return render(request, 'full_info.html', context)
    