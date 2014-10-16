from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

from gifai.models import Gif

def index(request):
	gif_list = Gif.objects.all()
	context = {'gif_list': gif_list}
	return render(request, 'gifai/index.html', context)
def detail(request, gif_id):
	try:
		gif = Gif.objects.get(pk=gif_id)
		context = {'gif': gif}
	except Gif.DoesNotExist:
		raise Http404
	return render(request, 'gifai/detail.html', context)

#return HttpResponse("looking at %s" % pk)
def vote(request, gif_id):
	g = get_object_or_404(Gif, pk=gif_id)
	g.score += 1
	g.save()
	#return HttpResponse('at id G.ID %s' % g.id)
	return HttpResponseRedirect(reverse('gifai:detail', args=(g.id,)))
# Create your views here.
