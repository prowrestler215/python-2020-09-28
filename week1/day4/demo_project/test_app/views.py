from django.shortcuts import HttpResponse, redirect, render


# These functions render templates
def index(request):
    print(request)
    print('We hit the index function!')
    # do some magic!

    # return HttpResponse('<h1>hello</h1>')
    return render(request, 'index.html')

def show_thursday(request):
    print('Thursday function!')
    return render(request, 'thursday.html')

def display_day(request, some_day):
    print('Display Day function!')
    print(some_day)
    context = {
      "the_day": some_day,
      "name": "Zach",
      "favorite_color": "turquoise",
      "pets": ["Bruce", "Fitz", "Georgie", "Bud", "Bruce", "Fitz", "Georgie", "Bud","Bruce", "Fitz", "Georgie", "Bud","Bruce", "Fitz", "Georgie", "Bud","Bruce", "Fitz", "Georgie", "Bud","Bruce", "Fitz", "Georgie", "Bud","Bruce", "Fitz", "Georgie", "Bud","Bruce", "Fitz", "Georgie", "Bud","Bruce", "Fitz", "Georgie", "Bud","Bruce", "Fitz", "Georgie", "Bud","Bruce", "Fitz", "Georgie", "Bud","Bruce", "Fitz", "Georgie", "Bud","Bruce", "Fitz", "Georgie", "Bud","Bruce", "Fitz", "Georgie", "Bud","Bruce", "Fitz", "Georgie", "Bud","Bruce", "Fitz", "Georgie", "Bud","Bruce", "Fitz", "Georgie", "Bud","Bruce", "Fitz", "Georgie", "Bud","Bruce", "Fitz", "Georgie", "Bud","Bruce", "Fitz", "Georgie", "Bud", "Bruce", "Fitz", "Georgie", "Bud","Bruce", "Fitz", "Georgie", "Bud","Bruce", "Fitz", "Georgie", "Bud","Bruce", "Fitz", "Georgie", "Bud","Bruce", "Fitz", "Georgie", "Bud","Bruce", "Fitz", "Georgie", "Bud","Bruce", "Fitz", "Georgie", "Bud","Bruce", "Fitz", "Georgie", "Bud","Bruce", "Fitz", "Georgie", "Bud","Bruce", "Fitz", "Georgie", "Bud","Bruce", "Fitz", "Georgie", "Bud","Bruce", "Fitz", "Georgie", "Bud","Bruce", "Fitz", "Georgie", "Bud"]
    }
    return render(request, 'day.html', context)

# These functions processes requests then redirect
def demo_redirect(request):
    # some processing of the request
    # CRUD
    return redirect('/thursday')
