from django.urls import path

from.import views

app_name='intro'
urlpatterns=[
    path('',views.IndexView.as_view(), name="index"),
    path('INTRODUCING/',views.IndexView.as_view(), name="INTRODUCING"),
    path('PROPOSING GENRE/',views.IndexView.as_view(), name="PROPOSING GENRE"),
    path('MEMBERSHIP SYSTEM/',views.IndexView.as_view(), name="MEMBERSHIP SYSTEM"),
]