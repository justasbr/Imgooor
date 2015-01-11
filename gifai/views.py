import urllib2
import re

from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

from gifai.models import Gif
from gifai.forms import GifForm


def index(request):
    gif_list = Gif.objects.all().order_by('-pub_date')
    context = {'gif_list': gif_list, 'sort': 'new'}
    return render(request, 'gifai/index.html', context)


def index_by_score(request):
    gif_list = Gif.objects.all().order_by('-score')
    context = {'gif_list': gif_list, 'sort': 'top'}
    return render(request, 'gifai/index.html', context)


def image_exists(url):
    re_image = re.compile("([^\\s]+(\\.(?i)(/bmp|jpg|jpeg|gif|png))$)")
    try:
        f = urllib2.urlopen(urllib2.Request(url))
        if re_image.match(url):
            return True
    except:
        return False
    return False


def submit(request):
    if request.method == "POST":
        form = GifForm(request.POST)
        if form.is_valid():
            form_obj = form.save(commit=False)
            if image_exists(form_obj.source):
                form_obj.save()
                return HttpResponseRedirect(reverse('gifai:detail', args=(form_obj.id,)))
            return render(request, "gifai/submit.html", {'form': form, 'error': 'URL was not an image'})
            # return render(request, 'gifai/submit.html')
    form = GifForm()
    return render(request, "gifai/submit.html", {'form': form})


def detail(request, gif_id):
    try:
        gif = Gif.objects.get(pk=gif_id)
        context = {'gif': gif}
    except Gif.DoesNotExist:
        raise Http404
    return render(request, 'gifai/detail.html', context)


# return HttpResponse("looking at %s" % pk)
def vote(request, gif_id):
    g = get_object_or_404(Gif, pk=gif_id)
    if request.POST.get('vote') == 'upvote':
        g.score += 1
    elif request.POST.get('vote') == 'downvote':
        g.score -= 1
    g.save()
    return HttpResponseRedirect(reverse('gifai:detail', args=(g.id,)))

#return HttpResponse('at id G.ID %s' % g.id)

