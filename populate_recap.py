import os


def populate():
    recapProject = add_project('Project1')






def add_category(name):
    c = Category.objects.get_or_create(name=name)
    return c


def add_requirement(regid, name, description, creation_date, modified_date, priority, status, belongs_to, category, responsible_person)
    r = Requirement.objects.get_or_create(regid=regid, name=name, description=description, creation_date=creation_date, modified_date=modified_date, priority=priority, status=status, belongs_to=belongs_to, category=category, responsible_person=responsible_person)
    return r


def add_project(name):
    p = RecapProject.objects.get_or_create(name=name, url=name, description='This is a description for project 1.'[0])
    return p


def add_user(uname, role, participates_in):
    u = UserProfile.objects.get_or_create(uname=uname, role=role, participates_in=participates_in)[0]
    return u


if __name__ == '__main__':
    print "Starting ReCap population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'recap.settings')
    from recap.models import RecapProject, UserProfile, Category, Requirement
    populate()
