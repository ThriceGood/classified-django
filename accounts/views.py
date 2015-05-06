from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth.models import User
from classified.forms import MyRegistrationForm
from .models import profile, PersonalMessage
from adverts.models import Advert
from .forms import profileForm


def login(request):
    context = {}
    context.update(csrf(request))
    return render(request, 'registration/login.html')


def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/accounts/invalid')


def invalid_login(request):
    return render(request, 'registration/invalid_login.html')


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')


def register_user(request):
    if request.method == 'POST':
        form = MyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/register_success')

    args = {}
    args.update(csrf(request))
    args['form'] = MyRegistrationForm()
    return render(request, 'registration/register.html', args)


def register_success(request):
    return render(request, 'registration/register_success.html')


@login_required
def view_profile(request):
    c = {}
    if profile.objects.filter(user=request.user).exists():
        c['profile'] = profile.objects.get(user=request.user)
        return render(request, 'view_profile.html', c)
    else:
        return HttpResponseRedirect('/accounts/edit_profile/')


def public_profile(request, user_id):
    c = {}
    c['user_id'] = user_id
    if profile.objects.filter(user=user_id).exists():
            c['profile'] = profile.objects.get(user=user_id)

    return render(request, 'public_profile.html', c)


@login_required()
def edit_profile(request):
    c = {}
    if profile.objects.filter(user=request.user).exists():
        profModel = profile.objects.get(user=request.user)
        c['proform'] = profileForm(instance=profModel)
    else:
        c['proform'] = profileForm()

    if request.POST:
        proform = profileForm(request.POST, instance=profModel)
        if proform.is_valid():
            prof = proform.save(False)
            prof.user = request.user
            prof.save()

        return HttpResponseRedirect('/accounts/view_profile/')
    else:

        return render(request, 'edit_profile.html', c)


@login_required()
def send_message(request):
    c = {}
    c.update(csrf(request))
    if request.POST:
        recipient = User.objects.get(pk=request.POST['recipient'])
        pm = PersonalMessage(
            sender = request.user,
            recipient = recipient,
            text = request.POST['text']
        )
        pm.save()

    return HttpResponseRedirect('/accounts/public_profile/%s/' % request.POST['recipient'])


@login_required()
def inbox(request):
    c = {}
    c['messages'] = PersonalMessage.objects.filter(recipient=request.user.pk).order_by('-sent_date')
    return render(request, 'inbox.html', c)


@login_required()
def outbox(request):
    c = {}
    c['messages'] = PersonalMessage.objects.filter(sender=request.user.pk).order_by('-sent_date')
    return render(request, 'outbox.html', c)


