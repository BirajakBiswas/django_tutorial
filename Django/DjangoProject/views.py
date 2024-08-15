
from django.http import HttpResponse


def index(request):
    return HttpResponse('''<h1>Home</h1> <a href="https://humble-guacamole-x55r5jvxww73p5qg-8000.app.github.dev/links">Links</a><br>
                        <a href="https://humble-guacamole-x55r5jvxww73p5qg-8000.app.github.dev/removepunc">Punctuation Remover</a><br>
                        <a href="https://humble-guacamole-x55r5jvxww73p5qg-8000.app.github.dev/capfirst">Capitalize first letter</a><br>
                        <a href="https://humble-guacamole-x55r5jvxww73p5qg-8000.app.github.dev/newlineremove">New line remover</a><br>
                        <a href="https://humble-guacamole-x55r5jvxww73p5qg-8000.app.github.dev/spaceremover">Space Remover</a><br>
                        <a href="https://humble-guacamole-x55r5jvxww73p5qg-8000.app.github.dev/charcount">Character Counter</a>''')#makes a page with hello written on it,HTML has been used to write hello as a header
#how django works
#django looks at paths,it first comes to urls.py and since we added import views in urls.py it will check the path and come to views.py & return whatever is specifeied in the views.py file

def about(request):
    return HttpResponse("about this website")#now when we go to /about part of the website this text will get displayed

def links(request):
    return HttpResponse('''<h1>Here is a list of urls lolz</h1> <a href="https://github.com/BirajakBiswas/django_tutorial/tree/main/Django"> My Github Profile</a> 
                        <a href="https://www.instagram.com/bir.aj.ak69/"> My Insta Profile</a>
                        <a href="https://humble-guacamole-x55r5jvxww73p5qg-8000.app.github.dev/">Back</a>''')#makes a page with hello written on it,HTML has been used to write hello as a header
                        #here we u




def removepunc(request):
    return HttpResponse("Remove punc <a href='/'> Back </a>")

def capfirst(request):
    return HttpResponse("Capitalize first letter <a href='/'> Back </a>")

def newlineremove(request):
    return HttpResponse("New line remover")

def spaceremover(request):
    return HttpResponse("Space remove first")

def charcount(request):
    return HttpResponse("char count")