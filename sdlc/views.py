from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
import pandas as pd
import pathlib


def index(request):
    try:
        return render(request, 'index.html')
    except:
        return render(request, 'index.html')