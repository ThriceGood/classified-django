from django.core.context_processors import csrf
from django.http import HttpResponseRedirect, HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Category, Advert, Comment
from .forms import AdvertForm


def list_adverts(request, cat_id):
    c = {}
    cat_id = int(cat_id)
    if cat_id == 0:
        ads = Advert.objects.all().order_by('-pub_date')
    else:
        ads = Advert.objects.filter(category=cat_id).order_by('-pub_date')

    paginator = Paginator(ads, 5, allow_empty_first_page=True)
    page = request.GET.get('page')

    try:
        c['ads'] = paginator.page(page)
    except PageNotAnInteger:
        c['ads'] = paginator.page(1)
    except EmptyPage:
        c['ads'] = paginator.page(paginator.num_pages)

    return render(request, 'list_adverts.html', c)


@login_required()
def create_advert(request):
    if request.POST:
        form = AdvertForm(request.POST, request.FILES)
        if form.is_valid():
            ad = form.save(commit=False)
            ad.user = request.user
            ad.save()
            return HttpResponseRedirect('/adverts/list_adverts/0/')

    else:
        form = AdvertForm()

    return render(request, 'create_advert.html', {'form': form})


def display_advert(request, advert_id):
    c = {}
    c['ad'] = get_object_or_404(Advert, pk=advert_id)
    return render(request, 'display_advert.html', c)


@login_required()
def edit_advert(request, advert_id):
    c = {}
    c['ad_id'] = advert_id
    if Advert.objects.filter(pk=advert_id).exists():
        ad = Advert.objects.get(pk=advert_id)
        c['image'] = ad.image
        c['ad'] = AdvertForm(instance=ad)
    else:
        c['ad'] = AdvertForm()

    if request.POST:
        adform = AdvertForm(request.POST, instance=ad)
        if adform.is_valid():
            ad = adform.save(False)
            ad.user = request.user
            ad.save(force_update=True)

        return HttpResponseRedirect('/adverts/display_advert/%s' % (advert_id))
    else:

        return render(request, 'edit_advert.html', c)


@login_required()
def delete_advert(request, advert_id):
    if Advert.objects.filter(pk=advert_id).exists():
        ad = Advert.objects.get(pk=advert_id)
        ad.delete()

    return HttpResponseRedirect('/adverts/list_adverts/0/')


def view_user_adverts(request, user_id):
    c = {}
    if Advert.objects.filter(user=user_id).exists():
        ads = Advert.objects.filter(user=user_id)

        paginator = Paginator(ads, 5, allow_empty_first_page=True)
        page = request.GET.get('page')

        try:
            c['ads'] = paginator.page(page)
        except PageNotAnInteger:
            c['ads'] = paginator.page(1)
        except EmptyPage:
            c['ads'] = paginator.page(paginator.num_pages)


    return render(request, 'user_adverts.html', c)


@login_required()
def save_comment(request):
    if request.POST:
        ad_id = request.POST['ad_id']
        ad = Advert.objects.get(pk=ad_id)
        com = Comment(
            user = request.user,
            advert = ad,
            text = request.POST['text'],
        )
        com.save()

    return HttpResponseRedirect('/adverts/display_advert/%s' % (request.POST['ad_id']))


def search(request, query):
    return HttpResponse(query)

