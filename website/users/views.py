# users/views.py

from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.urls import reverse
from users.forms import CustomUserCreationForm
import requests
import subprocess
import os
from .forms import CountryForm
<<<<<<< HEAD
=======
import pandas as pd
from django.template.response import TemplateResponse

>>>>>>> e468c19 (finish milestone2)


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


<<<<<<< HEAD
def run_model(request):
=======
def run_model(request, template_name='run_model.html'):
>>>>>>> e468c19 (finish milestone2)
    # this should be POST request
    if request.method == 'POST':
        args = {'country': None}
        form = CountryForm(request.POST)
        # first check if it is valid
        if form.is_valid():
            # process the form
            country = form['country'].value()
            # First, we need to make sure that this input is valid or contained in the original dataset
<<<<<<< HEAD
            url = 'https://github.com/CSSEGISandData/COVID-19/blob/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'
            resp = requests.get(url)
            countryWithComa = ',' + country + ','
            if countryWithComa in resp.text:
                bashCmd = ['/Users/shujie/Documents/CPT_HU/Semester5/CISC695/project/app4/venv/bin/jupyter', 'nbconvert',
                           '--allow-errors', '--to', 'html',
=======
            url1 = 'https://github.com/CSSEGISandData/COVID-19/blob/master/csse_covid_19_data/'
            url2 = 'csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'
            url = url1 + url2
            url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'
            # resp = requests.get(url)
            # countryWithComa = ',' + country + ','
            data = pd.read_csv(url,sep=",")
            countries = data['Country/Region'].unique()

            if country in countries:
                bashCmd = ['/Users/shujie/opt/anaconda3/bin/jupyter',
                           'nbconvert', '--allow-errors', '--to', 'html',
>>>>>>> e468c19 (finish milestone2)
                           'da/analysis_world.ipynb', '--execute']

                process = subprocess.Popen(
                    bashCmd, stdout=subprocess.PIPE, env={'NB_ARGS': country})
                _, err = process.communicate()

<<<<<<< HEAD
                if err is not None:
                    print('Error is', err)
=======
>>>>>>> e468c19 (finish milestone2)
                print("Done processing")
                # When the operation is done, redirect to other page
                return redirect('/redirect_report')
            else:
                print(f'country {country} is not in')
                args['country'] = country
<<<<<<< HEAD
                render(request, 'run_model.html', {'form': form})
=======
                # render(request, 'run_model.html', {'form': form})
                return TemplateResponse(request, template_name, args)
>>>>>>> e468c19 (finish milestone2)

        else:
            print("form is not valid")

    else:
        form = CountryForm()
    return render(request, 'run_model.html', {'form': form})


def redirect_report(request):
<<<<<<< HEAD
    # return render('http://www.google.com')
=======
>>>>>>> e468c19 (finish milestone2)
    return render(request, 'analysis_world.html')
