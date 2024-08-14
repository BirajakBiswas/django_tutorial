# def index():
    #return "hello"
#note that this will return error


from django.http import HttpResponse
from django.shortcuts import render#important command

def template(request):#template is the path/object/function name and templates is the folder
    return render(request, 'index.html')#here we have created a seperate html file and the path to this page is given as /template, here we can see the website as per the changes made in the templates file

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
                        #here we used the link of the home page to direct the user back to the home button instead we can use <a href='/'>Back</a> , this will work the same way, we will use this process in the other cases    
def analyze(request):
    djtext=request.GET.get('text','default')#here this is used to just display the text in the terminal,basically we can say it is identifying the text,if no text is there it returns "default"
    removepunc=request.GET.get('removepunc','off')
    print(removepunc)
    print(djtext)
    if removepunc=="on":#checking whether removepunc is on or not
        punctuations='''. , ? ! : ; ' " ` ~ - _ ( ) [ ] { } < > / \ | @ # $ % ^ & * + = … • ¬ ° © ® ™ ‽ ¿ ¡ ¶ § † ‡ « » “ ” '''#here we are listing a few punctuations
        analyzed=""
        for char in djtext:
            if char not in punctuations:#this is nothing we are just adding those characters to analyzed which here is the main output which does not contain characters present in punctuations
                analyzed=analyzed + char#this way we are able to get our putput withput punctuations
        params={'purpose':'Remove Punctuations','analyzed_text':analyzed}#note 'purpose' and 'analyzed_text' are both part of analyze.html created by us,we are simply alloting them as parameters here
        # Analyze the r
        return render(request,'analyze.html',params)
    else:
        return HttpResponse("Error")#error is returned when the Remove Punctuations is not checked i.e removepunc is off hence will return error

#def removepunc(request):
    return HttpResponse("Remove punc <a href='/'> Back </a>")

def capfirst(request):
    return HttpResponse("Capitalize first letter <a href='/'> Back </a>")

def newlineremove(request):
    return HttpResponse("New line remover")

def spaceremover(request):
    return HttpResponse("Space remove first")

def charcount(request):
    return HttpResponse("char count")