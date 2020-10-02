from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'index.html')

# This function handles the post request


def show_record(request):
    print('request.POST: ', request.POST)
    # print('request.GET: ', request.GET)
    print('song_title', request.POST['song_title'])
    print('album_url', request.POST['album_url'])
    # create a track in the DB
    context = {
        'title': request.POST['song_title'],
        'image': request.POST['album_url']
        # 'title': request.GET['song_title'],
        # 'image': request.GET['album_url']
    }
    return render(request, 'record.html', context)


# http: // localhost: 8000/records
# ?
# csrfmiddlewaretoken = mUrmje0NJhHpniAgvOTHTJTw4marQPTZz3ThrmTBRVWszZ0o65A1Ux4nHfkXFeyp
# &
# song_title = The+pot
# &
# album_url = https % 3A % 2F % 2Fexternal-content.duckduckgo.com % 2Fiu % 2F % 3Fu % 3Dhttps % 253A % 252F % 252Ftse1.mm.bing.net % 252Fth % 253Fid % 253DOIP.rcH4p5TAuZ9KptrvGqYGIwHaEK % 2526pid % 253DApi % 26f % 3D1

# <QueryDict:
# {'csrfmiddlewaretoken': ['KLHDkNEQLZqROvoIlHlBSRLzJohHPvZbXU9ysVxETDFU0cOQWY2VTFWqmhrdEUEB'],
#   'song_title': ['Scuttle Button'],
#   'album_url': ['https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.QEpdAEcIt4-Q_wLFiZ7PwwHaEK%26pid%3DApi&f=1']
# }>
