from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request,'trans/index.html')

def trans(request):
    text = request.GET['text']
    words = text.split(' ')
    from googletrans import Translator,LANGUAGES
    lang = Translator().detect(text).lang
    lang = LANGUAGES[lang]
    sen_trans = Translator().translate(text).text
    word_trans = []
    for x in words:
        temp = Translator().translate(x).text
        word_trans.append((x,temp))
    return render(request,'trans/result.html',{'sen':sen_trans,'words':word_trans,'lang':lang,'speech':speak})
