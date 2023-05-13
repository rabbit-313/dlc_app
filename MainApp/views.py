from django.shortcuts import render
from django.views import generic
from django.http import HttpResponseRedirect
from django.urls import reverse
import csv
import re
import pandas as pd
from .forms import CSVUploadForm


# Create your views here.
def index(request):
   context = {'sample':'HelloWorld'}
   return render(request, 'index.html', context)

def membership(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            genre = {'hiphop':0, 'break':0, 'girls':0, 'house':0, 'pop':0, 'lock':0, 'punking':0, 'jazz':0}
            file = request.FILES['file']
            file = file.read().decode('utf-8').replace('\r\n', ',').split(",")
            n = 4  # 区切りの数
            file = [file[i:i+n] for i in range(0, len(file), n)]
            matrix = [row[1:] for row in file[1:]]
            for i in range(len(matrix)):
                genre = matrix[i][2]
                if genre == 'hiphop':
                    genre['hiphop']+=1
                elif genre == 'break':
                    genre['break']+=1
                elif genre == 'girls':
                    genre['girls']+=1
                elif genre == 'house':
                    genre['house']+=1
                elif genre == 'pop':
                    genre['pop']+=1
                elif genre == 'lock':
                    genre['lock']+=1
                elif genre == 'punking':
                    genre['punking']+=1
                elif genre == 'jazz':
                    genre['jazz']+=1
            
            
                
                    
            
     
            # CSVファイルを処理するためのコードをここに書く
            return render(request, 'div_result.html')
    else:
        form = CSVUploadForm()
    return render(request, 'membership.html', {'form': form})
class IndexView(generic.TemplateView):
    template_name="introduce.html"

