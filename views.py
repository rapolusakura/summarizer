from __future__ import unicode_literals
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib import messages
from summarize import summarize_text
from summarize import common
from summarize import commonppl

class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'main.html', context=None)

def About(request):
    return render(request, 'about.html', context=None)

def Done(request):
    result = []
    chars = []
    others = []
    if request.method == 'POST':
        text = request.POST.get('subject', '')
        numb = request.POST.get('number', '')
        if not numb:
            numb = 1
        if (text != '' and numb != ''):
            test = common(text)
            test2 = commonppl(text)
            summary = summarize_text(text, numb)
            others.append(test)
            chars.append(test2)
            result.append(str(summary))
        elif numb == '' or text == '':
            result.append("You didn't enter a number or You didn't enter any text")
        return render(request, 'results.html', {'result': result[0],'chars': chars[0],'others': others[0]})
#edge case: letter in number
