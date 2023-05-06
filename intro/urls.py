from django.urls import path

from.import views

app_name='intro'
urlpatterns=[
    path('',views.IndexView.as_view(), name="index"),
    path('introducing/',views.INTRODUCINGView.as_view(), name="introducing"),
    path('proposing/',views.PROPOSINGGENREView.as_view(), name="proposing"),
    path('membership/',views.MEMBERSHIPSYSTEMView.as_view(), name="membership"),
]