from django.views import generic

class IndexView(generic.TemplateView):
    template_name="index.html"
    
class IntroduceView(generic.TemplateView):
    template_name="introduce.html"
    
# class ProposingView(generic.TemplateView):
#     template_name="proposing.html"
class MembershipView(generic.TemplateView):
    template_name="membership.html"

from django.shortcuts import render
import openai
from .forms import ChatGPTForm
from django.shortcuts import render
openai.api_key="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"

def ans_chatGPT(request):
    if request.method == 'POST':
        form = ChatGPTForm(request.POST)
        if form.is_valid():
            userans = form.cleaned_data['question']
        completion=openai.ChatCompletion.create(
            model="gpt-3.5-turbo",

            messages=[{"role":"system","content":
                       '''
                       あなたはダンスのジャンル選択を悩んでいる人間の相談役です。
                       相談者はストリートダンスの中でどのジャンルを選択しようか悩んでいます。
                       相談者は、自分に関する特徴を話すので、その特徴から相談者に適したダンスのジャンルを判断してください。
                       以下の制約条件を厳密に守って、ジャンルを提案してください。
                       制約条件:
                       *ダンスのジャンルは、「Hiphop」、「Break」、「Pop」、「Girlshiphop」、「Jazz」、「House」、「Lock」「Punking」の8ジャンルの中から提案してください。
                       *提案の一文目は必ず、「あなたに適しているジャンルは、～と～です。」と２つのジャンルを答えてください。
                       *提案には、提案するジャンルの詳細な説明を含めてください。
                       *提案には、なぜ提案したジャンルが相談者に適しているか、提案するジャンルの特徴と絡めて説明してください。
                       *相談者を示す二人称は「あなた」です。
                       
                       '''
                       },{
                "role":"user",
                "content":userans,
            }]
        )

        response=completion.choices[0].message.content

        a= {'userans':response}

        return render(request, "anschatgpt.html", a)

    else:
        form = ChatGPTForm()
    return render(request, 'proposing.html', {'form': form})