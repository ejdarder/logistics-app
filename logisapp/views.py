from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404

from .models import Part#, PO

def index(request):
    recently_added_parts = Part.objects.order_by('-part_number')[:10]
    # template = loader.get_template('logisapp/index.html')
    context = {
    	'recently_added_parts': recently_added_parts,
    }
    # output=', '.join([p.part_number for p in recently_added_parts])
    # return HttpResponse(template.render(context, request))
    return render(request, 'logisapp/index.html', context)

def detail(request, pk):
	part = get_object_or_404(Part, pk=pk)
	return render(request, 'logisapp/detail.html', {'part': part})

def add_part(request, part_number):
	return HttpResponse("New functionality to Add Parts soon")

