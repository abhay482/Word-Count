from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request, 'home.html', {'xyz':'most used text'} )

def count(request):
    fulltext=request.GET['fulltext']
    Wd={}
    wordlist = fulltext.split()
    for x in wordlist:
        if x in Wd:
            Wd[x]+=1
        else:
            Wd[x]=1
    sortedwords = sorted(Wd.items(), key=operator.itemgetter(1), reverse=True)
    return render(request, 'count.html',{'fulltext':fulltext, 'count':len(wordlist),'Wd':sortedwords})

def about(request):
     return render(request, 'about.html')
