from django.conf.urls import url, include
from django.urls import path
from users.views import dashboard, register, run_model, redirect_report

urlpatterns = [
    url(r"^accounts/", include("django.contrib.auth.urls")),
    url(r"^dashboard/", dashboard, name="dashboard"),
    url(r"^generate-report", run_model, name="run_model"),
    url(r"^register/", register, name="register"),
    path('', dashboard, name='home'),
    path('redirect_report/', redirect_report, name='analysis_world')
]
