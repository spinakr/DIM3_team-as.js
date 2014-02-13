from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse
from recap.forms import UserForm, UserProfileForm


def index(request):
    context = RequestContext(request)
    context_dict = {}
    return render_to_response('recap/index.html', context_dict, context)


def register(request):
    context = RequestContext(request)

    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            registered = True

        else:
            print user_form.errors, profile_form.errors

    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render_to_response(
        'recap/register.html',
        {'user_form': user_form, 'profile_form': profile_form, 'registered': registered},
        context)

def project(request):
    context = RequestContext(request)
    return render_to_response('recap/project.html', {}, context)
    
