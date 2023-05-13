from django.views import generic

import csv
from django.views import View
from django.shortcuts import render
from django.views.generic import TemplateView

class IndexView(generic.TemplateView):
    template_name="index.html"
    
class IntroduceView(generic.TemplateView):
    template_name="introduce.html"
    
class ProposingView(generic.TemplateView):
    template_name="proposing.html"
class MembershipView(generic.TemplateView):
    template_name="membership.html"


class MembershipView(TemplateView):
    template_name = "membership.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            # CSVファイルがアップロードされたときの処理
            csv_file = request.FILES['csv_file']
            data = {}
            reader = csv.DictReader(csv_file.read().decode('utf-8').splitlines())
            for row in reader:
                genre = row['ジャンル']
                if genre not in data:
                    data[genre] = []
                data[genre].append({'age': row['年齢'], 'name': row['名前']})
            for genre in data:
                data[genre] = sorted(data[genre], key=lambda x: x['age'])
            sorted_data = sorted(data.items(), key=lambda x: x[0])
            return render(request, self.template_name, {'sorted_data': sorted_data})
        else:
            return render(request, self.template_name)