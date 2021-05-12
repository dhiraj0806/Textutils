"""This file is made by me."""
from django.http import HttpResponse
from django.shortcuts import render

#Code 6:
# def index(request):
#     # return HttpResponse("<h1>Hello DJ</h1>")
#     f= open("1.txt")
#     contents = f.read()
#     return HttpResponse(contents)
#
# def about(request):
#     return HttpResponse("About DJ")
#
# Ex.1 solution
# def navigate(request):
#     return HttpResponse('''<h1>My Sites!</h1> <a href="https://codewithharry.com/videos/python-tutorials-for-absolute-beginners-26">
#     Source Code with Harry</a><br>
#     <a href="https://www.typingclub.com/sportal/"> Touch Typing</a><br>
#     <a href="https://www.hackerrank.com/dashboard"> HackerRank</a>''')

# Lec 7:
def index(request):
    # params = {'name': 'Dhiraj', 'place': 'India'}
    return render(request, 'index.html')
    # return HttpResponse('''<h1>Home</h1>
    # <br>
    # <a href="/removepunc"> <button>Removepunc</button></a>
    # <br>
    # <a href="/capfirst"> <button>Capitalize First</button></a>''')
#
# def removepunc(request):
#     # Get the text
#     djtext = request.GET.get('text', 'default')
#     print(djtext)
#     # Analyze the text
#     return HttpResponse('''<h1>remove punc</h1>
#     <br>
#     <a href = "/">
#         <button>Back to Home</button>
#         </a> ''')
#
# def capfirst(request):
#     return HttpResponse('''<h1>Capitalize First</h1>
#     <br>
#     <a href = "/">
#         <button>Back to Home</button>
#         </a> ''')

# Lec 10:
def analyze(request):

    # Get the text
    djtext = request.POST.get('text', 'default')
    # Initialize checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')

    #Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if fullcaps == 'on':
        analyzed =""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Text Capitalized', 'analyzed_text': analyzed}
        djtext = analyzed
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

    if(newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        print("pre", analyzed)
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        djtext = analyzed
        # Analyze the text
        # return render(request, 'analyze.html', params)

    if(charcount == "on"):
        #Method 1
        # analyzed = len(djtext)
        # params = {'purpose': 'Counting Characters', 'analyzed_text': analyzed}
        # # Analyze the text
        # return render(request, 'analyze.html', params)

        #Method 2
        analyzed = ""
        for index, char in enumerate(djtext):
            analyzed = analyzed + char
            if char != "  ":
                index += 1

        params = {'purpose': 'Counting Characters', 'analyzed_text': {analyzed: index}}
        djtext = analyzed
        # Analyze the text
        # return render(request, 'analyze.html', params)
    if(removepunc == "on" or fullcaps == "on" or extraspaceremover == "on" or newlineremover == "on" or charcount == "on"):
        return render(request, 'analyze.html', params)

    else:
        return HttpResponse("please select any operation and try again")
