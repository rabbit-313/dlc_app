from django.urls import path

from.import views

app_name='MainApp'
urlpatterns=[
    path('',views.IndexView.as_view(), name="index"),
    path('introduce/',views.IntroduceView.as_view(), name="introduce"),
    path('propose/',views.ProposingView.as_view(), name="proposing"),
    path('membership/',views.MembershipView.as_view(), name="membership"),
]
