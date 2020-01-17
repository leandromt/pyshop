from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse('Hello lead!')


def new(request):
    return HttpResponse('New lead')

def reposicoes(request):
    return HttpResponse('Repõeeeee poha!')
