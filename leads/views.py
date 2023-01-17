from django.shortcuts import render
from django.http import HttpResponse
from .models import Lead


def index(request):
    # return HttpResponse('Hello world')
    # context = {'name': 'Gilbert', 'age': 35}

    leads = Lead.objects.all()
    context = {'leads': leads}

    return render(request, 'leads/lead_list.html', context)


def lead_detail(request, pk):
    lead = Lead.objects.get(pk=pk)

    context = {'lead': lead}

    return render(request, 'leads/lead_detail.html', context)
