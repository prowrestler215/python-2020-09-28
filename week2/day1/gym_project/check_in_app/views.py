from django.shortcuts import redirect, render


# will render a template
def index(request):
    return render(request, 'index.html')


def success(request):
    # protect page from users that aren't logged in
    if 'user' not in request.session:
        print('user is not logged in')
        return redirect('/')

    request.session['counter'] += 1

    context = {
        'name': request.session['user']
    }
    return render(request, 'success.html', context)


# will NOT render a template
def login(request):
    print(request.POST)
    print(request.POST['usernamee'])
    if request.POST['something_secret'] == "secret sauce":
        print('we saw the secret sauce!🦕💯')
    else:
        print('secret incorrect😭🔥😞')
    # login a user
    # check the db
    # add the user to session
    # name = request.POST['usernamee']
    # request.session['user'] = name

    request.session['user'] = request.POST['usernamee']
    request.session['counter'] = 100
    # then redirect them to the next page
    return redirect('/success')


def logout(request):
    # del request.session['user']
    # del request.session['counter']
    request.session.flush()
    print('deleting session key')
    return redirect('/')
