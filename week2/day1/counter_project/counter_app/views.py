from django.shortcuts import redirect, render

# import random 	                # import the random module

# Create your views here.


def index(request):
    # random.randint(1, 100) 		# random number between 1-100

    if 'counter' in request.session:
        print('key exists!')
        request.session['counter'] += 1
    else:
        print("key 'counter' does NOT exist")
        request.session['counter'] = 1

    return render(request, 'index.html')


def clear_session(request):
    del request.session['counter']
    return redirect('/')


def something(request):
    print(request.POST)
    return redirect('/')
