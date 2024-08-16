# def index():
    #return "hello"
#note that this will return error


from django.http import HttpResponse
from django.shortcuts import render#important command

def index(request):#template is the path/object/function name and templates is the folder
    return render(request, 'index.html')#here we have created a seperate html file and the path to this page is given as /template, here we can see the website as per the changes made in the templates file



def analyze(request):
    #get the text djtext is our inout text that i s to be analyzed
    djtext=request.POST.get('text','default')#here this is used to just display the text in the terminal,basically we can say it is identifying the text,if no text is there it returns "default"
    
    #check checkbox values
    removepunc=request.POST.get('removepunc','off')#POST request is used in place of GET request for a cleaner url and also it supports larger chunk of data I guess
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover=request.POST.get('newlineremover','off')
    extraspaceremover=request.POST.get('extraspaceremover','off')
   

   #check which checxkbox is on
  
    
    
#code to use removepunc ,UPPERCASE and new line remover all 3 at the same time
    
    
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if(fullcaps=="on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed
        # Analyze the text
        # return render(request, 'analyze.html', params)

    if(extraspaceremover=="on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        djtext = analyzed
        # Analyze the text
        # return render(request, 'analyze.html', params)

    if (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char!="\r":
                analyzed = analyzed + char
            else:
                print("no")
        
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}

    if(removepunc != "on" and newlineremover!="on" and extraspaceremover!="on" and fullcaps!="on"):
        return HttpResponse("Please select any operation and try again")

    return render(request, 'analyze.html', params)
