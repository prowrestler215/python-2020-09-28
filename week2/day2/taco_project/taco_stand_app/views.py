from django.shortcuts import redirect, render

from .models import Taco


# Create your views here.
def index(request):
    context = {
        "all_tacos": Taco.objects.all()
    }
    return render(request, 'index.html', context)


def add_a_taco(request):
    print(request.POST)
    created_taco = Taco.objects.create(
        name=request.POST['name_of_item'],
        description=request.POST['description'],
        price=request.POST['price'],
        image_url=request.POST['picture']
    )
    print('We created a taco!')
    print(created_taco)
    return redirect('/')
