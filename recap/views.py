from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from recap.forms import UserForm, UserProfileForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from recap.models import RecapProject, UserProfile

def index(request):
    context = RequestContext(request)
    if not request.user.is_authenticated():
        return render_to_response('recap/index.html', {}, context)

    else:
        user = request.user
        project_list = RecapProject.objects.filter(userprofile__user=user)
        return render_to_response('recap/developer.html', {'project_list': project_list}, context)



def about(request):
    context = RequestContext(request)
    return render_to_response('recap/about.html', {}, context)


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


def user_login(request):
    context = RequestContext(request)

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
            else:
                return HttpResponse("Your account is disabled.")
        else:

            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/recap/'))

    else:
        return render_to_response(request.META.get('HTTP_REFERER', '/recap/'), {}, context)


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/recap/')


def project(request, project_name_url):
    context = RequestContext(request)
    return render_to_response('recap/project.html', {'project': project_name_url}, context)

