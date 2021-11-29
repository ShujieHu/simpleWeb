# users/views.py

from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.urls import reverse
from users.forms import CustomUserCreationForm
import requests
import subprocess
import os
from .forms import CountryForm


def dashboard(request):
    return render(request, "dashboard.html")


def register(request):
    if request.method == "GET":
        return render(
            request, "registration/register.html",
            {"form": CustomUserCreationForm}
        )
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse("dashboard"))


def run_model(request):
    # this should be POST request
    if request.method == 'POST':
        args = {'country': None}
        form = CountryForm(request.POST)
        # first check if it is valid
        if form.is_valid():
            # process the form
            country = form['country'].value()
            # First, we need to make sure that this input is valid or contained in the original dataset
            url = 'https://github.com/CSSEGISandData/COVID-19/blob/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'
            resp = requests.get(url)
            countryWithComa = ',' + country + ','
            if countryWithComa in resp.text:
                bashCmd = ['/Users/shujie/Documents/CPT_HU/Semester5/CISC695/project/app4/venv/bin/jupyter', 'nbconvert',
                           '--allow-errors', '--to', 'html',
                           'da/analysis_world.ipynb', '--execute']

                process = subprocess.Popen(
                    bashCmd, stdout=subprocess.PIPE, env={'NB_ARGS': country})
                _, err = process.communicate()

                if err is not None:
                    print('Error is', err)
                print("Done processing")
                # When the operation is done, redirect to other page
                return redirect('/redirect_report')
            else:
                print(f'country {country} is not in')
                args['country'] = country
                render(request, 'run_model.html', {'form': form})

        else:
            print("form is not valid")

    else:
        form = CountryForm()
    return render(request, 'run_model.html', {'form': form})


def redirect_report(request):
    # return render('http://www.google.com')
    return render(request, 'analysis_world.html')
