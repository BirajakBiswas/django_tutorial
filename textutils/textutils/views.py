# def index():
    #return "hello"
#note that this will return error


from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Hello</h1>")#makes a page with hello written on it,HTML has been used to write hello as a header
#how django works
#django looks at paths,it first comes to urls.py and since we added import views in urls.py it will check the path and come to views.py & return whatever is specifeied in the views.py file

def about(request):
    return HttpResponse("about this website")#now when we go to /about part of the website this text will get displayed