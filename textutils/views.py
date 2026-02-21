# This File Created by Shubham

from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect

def index(request):
    return render(request,'index.html')

def analyze(request):
    djtext = request.GET.get('text','default')
    removepunc = request.GET.get('removepunc','off')
    fullcapse = request.GET.get('fullcapse','off')
    lowercapse = request.GET.get('lowercapse','off')
    newlineremover = request.GET.get('newlineremover','off')
    spaceremover = request.GET.get('spaceremover','off')
    charcount = request.GET.get('charcount','off')

    punctuations = '''!"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~'''
    analyzed = ''
    
    if removepunc == 'on' :
        for i in djtext:
            if i not in punctuations:
                analyzed = analyzed + i

        params = { 'purpose' : 'Removed Punctions', 'analyzed_text' : analyzed }
        return render(request, 'analyze.html',params)
    
    elif fullcapse == 'on':
        for i in djtext:
            analyzed = analyzed + i.upper()

        params = { 'purpose' : 'Cpitalize Letters', 'analyzed_text' : analyzed }
        return render(request, 'analyze.html',params)
    
    elif lowercapse == 'on':
        for i in djtext:
            analyzed = analyzed + i.lower()

        params = { 'purpose' : 'Lower Letters', 'analyzed_text' : analyzed }
        return render(request, 'analyze.html',params)
    
    elif charcount == 'on':
        count = 0
        for char in djtext:
            count = count + 1

        params = { 'purpose': 'Character Count', 'analyzed_text': count }
        return render(request, 'analyze.html', params)

    
    elif newlineremover == 'on':
        for i in djtext:
            if i !='\n':
                analyzed = analyzed + i

        params = { 'purpose' : 'New line Remove', 'analyzed_text' : analyzed }
        return render(request, 'analyze.html',params)
    
    elif spaceremover == 'on':
        for i,ch in enumerate(djtext) :
            if djtext[i]== '' and djtext[i+1]=='':
                pass
            else :
                analyzed = analyzed + ch

        params = { 'purpose' : 'New line Remove', 'analyzed_text' : analyzed }
        return render(request, 'analyze.html',params)
    else:
        messages.error(request, "Please select an Operation")
        return redirect('home')  
   
def about(request):
    
    return render(request,'about.html')
   
def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        print(name, email, subject, message)

        return render(request, "contact.html", {
            "success": "Thank you for contacting us!"
        })

    return render(request, "contact.html")



 