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
    if removepunc=="on":#checking whether removepunc is on or not
        punctuations='''. , ? ! : ; ' " ` ~ - _ ( ) [ ] { } < > / \ | @ # $ % ^ & * + = … • ¬ ° © ® ™ ‽ ¿ ¡ ¶ § † ‡ « » “ ” '''#here we are listing a few punctuations
        analyzed=""
        
        for char in djtext:
        
            if char not in punctuations:#this is nothing we are just adding those characters to analyzed which here is the main output which does not contain characters present in punctuations
                analyzed=analyzed + char#this way we are able to get our putput withput punctuations
        
        params={'purpose':'Remove Punctuations','analyzed_text':analyzed}#note 'purpose' and 'analyzed_text' are both part of analyze.html created by us,we are simply alloting them as parameters here
        # Analyze the r
        
        return render(request,'analyze.html',params)
    
    elif(fullcaps=="on"):
        analyzed=""
        
        for char in djtext:#djtext is the input text we will be putting in the website
            analyzed=analyzed+char.upper()#.upper() is a built in function to make uppercase

        params={'purpose':'Change to uppercase','analyzed_text':analyzed}#note 'purpose' and 'analyzed_text' are both part of analyze.html created by us,we are simply alloting them as parameters here
        return render(request,'analyze.html',params)
    
    elif(newlineremover=="on"):
        analyzed=""
        
        for char in djtext:
            if char !="\n" and char!="\r":
                analyzed=analyzed+char

        
         
        params={'purpose':'Remove New line','analyzed_text':analyzed}#note 'purpose' and 'analyzed_text' are both part of analyze.html created by us,we are simply alloting them as parameters here
        # Analyze the r
        
        return render(request,'analyze.html',params)#
    
#code to use removepunc ,UPPERCASE and new line remover all 3 at the same time
    
    #if removepunc == "on" and fullcaps == "on" or newlineremover == "on":
        for char in djtext:
            if char not in punctuations and  char !='\n':
                analyzed = analyzed + char.upper()

        params = {'purpose':'removepunctuations','analyzed_text':analyzed}
        return render(request,'analyze.html',params)


    
    elif(extraspaceremover=="on"):
        analyzed=""
        
        for index,char in enumerate(djtext):#enumerate is a built in function which counts the ginti of for loop
            if djtext[index]==" " and djtext[index+1]==" ":#basically here we are specifying that if there exists a space or two spaces in djtext then we will pass/we will not account that entry
                pass
            else:
                analyzed=analyzed+char

        
         
        params={'purpose':'Remove Extra Space','analyzed_text':analyzed}#note 'purpose' and 'analyzed_text' are both part of analyze.html created by us,we are simply alloting them as parameters here
        # Analyze the r
        
        return render(request,'analyze.html',params)
    
    
    else:
    
        return HttpResponse("Error")#error is returned when the Remove Punctuations is not checked i.e removepunc is off hence will return error

