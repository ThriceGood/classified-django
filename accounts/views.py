from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth.models import User
from classified.forms import MyRegistrationForm
from .models import profile, PersonalMessage
from .forms import profileForm


# renders login page
def login(request):
    context = {}
    context.update(csrf(request))
    return render(request, 'registration/login.html')


# authenticates user based on username and password POSTed from
# login form on login template, no related template
def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    # using django's standard user auth system
    user = auth.authenticate(username=username, password=password)
    # if user exits then authenticate them and redirect to home page
    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/')
    # else redirect to invalid login page
    else:
        return HttpResponseRedirect('/accounts/invalid')


# renders invalid login template
def invalid_login(request):
    return render(request, 'registration/invalid_login.html')


# logs out user and redirects to home page, no related template
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')


# handles user registration, renders registration template, receives POST
# from registration form and renders registration success template
def register_user(request):
    # if request is POST, or, registration form was POSTed
    if request.method == 'POST':
        # create new form instance based on POST data
        form = MyRegistrationForm(request.POST)
        # if form is valid
        if form.is_valid():
            # save the form/new user and redirect to success page
            form.save()
            return HttpResponseRedirect('/accounts/register_success')
    # context dict to be passed to template
    args = {}
    # csrf, i dont think its needed when using the 'render()' function
    args.update(csrf(request))
    # pass over empty form to be rendered by template language
    # if a user POSTs a form that is not valid, form will now be rendered
    # with the appropriate error messages
    args['form'] = MyRegistrationForm()
    # render registration template and pass over form
    return render(request, 'registration/register.html', args)


# renders the registration success template
def register_success(request):
    return render(request, 'registration/register_success.html')


# view users personal profile
@login_required
def view_profile(request):
    # context dict to be passed to template
    c = {}
    # if user has a profile (request.user is currently logged in user)
    if profile.objects.filter(user=request.user).exists():
        # get that profile
        c['profile'] = profile.objects.get(user=request.user)
        # render the view profile template passing in the profile
        return render(request, 'view_profile.html', c)
    # else redirect to create profile page
    else:
        return HttpResponseRedirect('/accounts/create_profile/')


# users public profile page that other users can see, takes in the users id
def public_profile(request, user_id):
    # context dict to be passed to template
    c = {}
    c['user_id'] = user_id
    # if the profile with the passed in user name exists
    if profile.objects.filter(user=user_id).exists():
        # get that profile
        c['profile'] = profile.objects.get(user=user_id)
    # render public profile page and pass in the profile to display
    return render(request, 'public_profile.html', c)


# create profile page, loads profile creation form and
# saves profile if form is POSTed
@login_required()
def create_profile(request):
    # if form is POSTed
    if request.POST:
        # create new instance of profile form containing POST data
        form = profileForm(request.POST)
        # if form validates
        if form.is_valid():
            # add the user to the form before committing the save
            prof = form.save(commit=False)
            prof.user = request.user
            prof.save()
            # redirect to view profile page after creation
            return HttpResponseRedirect('/accounts/view_profile/')
    # else create empty instance of profile form
    else:
        form = profileForm()
    # render the create profile page and pass in the form
    return render(request, 'create_profile.html', {'form': form})


# edit profile page, allows user to make edits to their profile
@login_required()
def edit_profile(request):
    # context dict to be passed to template
    c = {}
    # if the users profile exists
    if profile.objects.filter(user=request.user).exists():
        # get that profile instance to populate form
        profModel = profile.objects.get(user=request.user)
        # create a profile form instance containing the profile model data
        c['proform'] = profileForm(instance=profModel)
    # else redirect to profile creation page
    else:
        return HttpResponseRedirect('/accounts/create_profile/')
    # if the request is POST, or, form is submitted
    if request.POST:
        # create a profile form containing the POST data
        # 'instance' argument tells the form to update that particular profile instance
        c['proform'] = proform = profileForm(request.POST, instance=profModel)
        # if teh form validates
        if proform.is_valid():
            # add the user to the form before committing the save
            prof = proform.save(False)
            prof.user = request.user
            prof.save()
            # redirect to view profile page
            return HttpResponseRedirect('/accounts/view_profile/')
    # render edit profile template and pass in the form, if teh POSTed for
    # does not validate, the template will be rendered again containing
    # appropriate error messages
    return render(request, 'edit_profile.html', c)


# function that handles sending personal messages to users, receives a
# POST request from the message box on the public profile page
# no related template
@login_required()
def send_message(request):
    # context dict to be passed to template
    c = {}
    c.update(csrf(request))
    # if request is POST, or, message form is submitted
    if request.POST:
        # set the recipient to the recipient user in the POST data
        recipient = User.objects.get(pk=request.POST['recipient'])
        # create personal message instance
        pm = PersonalMessage(
            # sender is the user who submitted the form
            sender = request.user,
            recipient = recipient,
            # message body in the POST data
            text = request.POST['text']
        )
        # save the message
        pm.save()
    # redirect to recipients public profile page
    return HttpResponseRedirect('/accounts/public_profile/%s/' % request.POST['recipient'])


# users inbox page, containing their received pms
@login_required()
def inbox(request):
    c = {}
    # get the users received personal messages, order by sent_date
    c['messages'] = PersonalMessage.objects.filter(recipient=request.user.pk).order_by('-sent_date')
    # render inbox template and pass in messages
    return render(request, 'inbox.html', c)


# users outbox page, containing their sent pms
@login_required()
def outbox(request):
    c = {}
    # get the users sent personal messages, order by sent_date
    c['messages'] = PersonalMessage.objects.filter(sender=request.user.pk).order_by('-sent_date')
    # render outbox template and pass in messages
    return render(request, 'outbox.html', c)


