from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from recap.forms import UserForm, UserProfileForm, ProjectForm, RequirementForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from recap.models import RecapProject, UserProfile, User, Requirement, Category
import datetime


def index(request):
    context = RequestContext(request)
    if not request.user.is_authenticated():
        return render_to_response('recap/index.html', {}, context)

    else:
        user = request.user
        project_list = RecapProject.objects.filter(userprofile__user=user)

    if request.method == 'POST':
        project_form = ProjectForm(data=request.POST)
        if project_form.is_valid():
            project_data = project_form.save(commit=False)
            project_data.url = project_form.cleaned_data['name'].replace(' ', '-').lower()
            project_data.save()
            users = project_form.cleaned_data['participants']
            for u in users:
                user_profile = UserProfile.objects.get(user=u)
                user_profile.participates_in.add(project_data)
                user_profile.save()

        else:
            print project_form.errors

    else:
        project_form = ProjectForm()

    return render_to_response('recap/developer.html', {'project_list': project_list, 'project_form': project_form}, context)


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

@login_required
def project(request, project_name_url):
    context = RequestContext(request)
    # if new participant added:
    if request.method == 'POST':
        if(request.POST.__contains__('new_participant')):
            new_participant(request, project_name_url)
        if(request.POST.__contains__('new_requirement')):
            reqForm = RequirementForm(data=request.POST)
            newRequirementAdded = new_requirement(reqForm, project_name_url)
        if(request.POST.__contains__('del_requirement')):
            delete_requirement(request)
    else:
        reqForm = RequirementForm()
    requirements_by_category = []
    categorys = Category.objects.all().order_by('index')
    requirements_list = Requirement.objects.filter(belongs_to=project_name_url)
    # Group requirements by category
    for category in categorys:
        requirements_by_category.append({"name":category.name,
                                         "requirements":requirements_list
                                                        .filter(category=category.name)
                                                        .order_by('index')})
    project = get_object_or_404(RecapProject, url=project_name_url)
    participants = User.objects.filter(userprofile__participates_in__url=project_name_url)
    
    if request.method == 'POST' and newRequirementAdded:
        return HttpResponseRedirect(reverse('project', args=[project_name_url]), 
                                    render_to_response('recap/project.html', {'participants': participants,
                                                         'project': project,
                                                         'reqs_by_category' : requirements_by_category,
                                                         'requirement_form' : reqForm}, context))    
    else:
        return render_to_response('recap/project.html', {'participants': participants,
                                                         'project': project,
                                                         'reqs_by_category' : requirements_by_category,
                                                         'requirement_form' : reqForm}, context)

def new_participant(request, project_name_url):
    new_user = request.POST['new_user']
    userprofil = get_object_or_404(UserProfile, user__username=new_user)
    project1 = RecapProject.objects.get(url=project_name_url)
    userprofil.participates_in.add(project1)

def new_requirement(requirement_form, project_name_url):
    if(requirement_form.is_valid()):
        requirement_data = requirement_form.save(commit=False)
        requirement_data.creation_date = datetime.datetime.now()
        requirement_data.modified_date = datetime.datetime.now()
        requirement_data.index = Requirement.objects.filter(belongs_to=project_name_url).filter(category=requirement_data.category).count()
        req_index = Requirement.objects.filter(belongs_to=project_name_url).count() + 1
        requirement_data.reqid = project_name_url.upper()[:3] + str(req_index)
        requirement_data.belongs_to = RecapProject.objects.get(url=project_name_url)
        requirement_data.save()
        return True;
    else:
        return False;

def delete_requirement(request):
    req_id = None
    if request.method == 'POST':
        req_id = request.POST['req_id']
        Requirement.objects.get(reqid=req_id).delete()
    return HttpResponse('Deleted: ' + req_id)
        
@login_required
def change_category(request):
    req_id = None
    category = None
    if request.method == 'POST':
        req_id = request.POST['req_id']
        category = request.POST['category']
    
    if req_id and category:
        requirement = Requirement.objects.get(reqid=req_id)
        category = Category.objects.get(name=category)
        requirement.category = category
        requirement.save()
    
    return HttpResponse("Updated category!");

@login_required    
def update_indexes(request):
    data = None
    msg = "Ajax failed."
    if request.method == 'POST':
        data = request.POST['data']
    
    if data:
        categoryName = data.split("[]=")[0]
        data = data.replace(categoryName + "[]=", "")
        data = data.split("&");
        category = Category.objects.get(name=categoryName)
        for x in xrange(0, len(data)):
            req = Requirement.objects.get(reqid=data[x])
            req.index = x
            req.save()
        msg = "Updated indexes."
    
    return HttpResponse(msg);

@login_required
def requirement(request, project_name_url, requirement_name_url):
    context = RequestContext(request)
    project_name = project_name_url
    requirement_object = Requirement.objects.get(reqid=requirement_name_url)
    return render_to_response('recap/requirement.html', {'req_url': requirement_name_url, 'req_obj': requirement_object, 'project': project_name}, context)


def edit_requirement(request, project_name_url, requirement_name_url):
    if request.method == 'POST':
        data = request.POST['sdf']

    context = RequestContext(request)
    pro = RecapProject.objects.get(url=project_name_url)
    req = Requirement.objects.get(reqid=requirement_name_url)

    return render_to_response('recap/edit_req.html', {'project':pro, 'requirement': req}, context)


def edit_project(request, project_name_url):
    if request.method == 'POST':
        data = request.POST['sdf']

    context = RequestContext(request)
    pro = RecapProject.objects.get(url=project_name_url)

    return render_to_response('recap/edit_project.html', {'project':pro}, context)
