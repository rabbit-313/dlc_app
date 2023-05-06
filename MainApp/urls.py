from django.urls import path

from.import views

app_name='MainApp'
urlpatterns=[
    path('',views.IndexView.as_view(), name="index"),
    path('introduce/',views.IndexView.as_view(), name="introduce"),
    path('propose/',views.IndexView.as_view(), name="propose"),
    path('membership/',views.IndexView.as_view(), name="membership"),
]