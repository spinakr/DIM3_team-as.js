import os


def populate():
    cat1 = add_category('must')
    cat2 = add_category('should')
    cat3 = add_category('could')
    cat4 = add_category("won't")

    project1 = add_project('Silly Pointless Flea')
    project2 = add_project('Brave Zeus')
    project3 = add_project('Golden Weather')
    project4 = add_project('Maximum Compass')
    project5 = add_project('Itchy Long Venus')

    user1 = add_user('snotty', '12345', 'snotty@foo.bar', 'DEV', [project1, project2, project3])
    user2 = add_user('clive', '12345', 'clive@foo.bar', 'DEV', [project2, project3])
    user3 = add_user('decanter', '12345', 'decanter@foo.bar', 'PO', [project1, project2, project3, project4, project5])

    add_requirement('SIL1', 'Add something something to anything.', "2014-03-02", "2014-03-02", 1, 'NS', project1, cat1, None)
    add_requirement('SIL2', 'Add something something to anything.', "2014-03-02", "2014-03-02", 2, 'IP', project1, cat1, user1.user)
    add_requirement('SIL3', 'Add something something to anything.', "2014-03-02", "2014-03-02", 3, 'IM', project1, cat1, user2.user)
    add_requirement('SIL4', 'Add something something to anything.', "2014-03-02", "2014-03-02", 4, 'DO', project1, cat1, user3.user)
    add_requirement('SIL5', 'Add something something to anything.', "2014-03-02", "2014-03-02", 5, 'IP', project1, cat1, user1.user)
    add_requirement('SIL6', 'Add something something to anything.', "2014-03-02", "2014-03-02", 6, 'NS', project1, cat1, None)
    add_requirement('SIL7', 'Add something something to anything.', "2014-03-02", "2014-03-02", 7, 'NS', project1, cat1, None)
    add_requirement('BRA1', 'Add something something to anything.', "2014-03-02", "2014-03-02", 1, 'IP', project2, cat1, user1.user)
    add_requirement('BRA2', 'Add something something to anything.', "2014-03-02", "2014-03-02", 2, 'IP', project2, cat1, user2.user)
    add_requirement('BRA3', 'Add something something to anything.', "2014-03-02", "2014-03-02", 3, 'NS', project2, cat1, None)
    add_requirement('BRA4', 'Add something something to anything.', "2014-03-02", "2014-03-02", 4, 'NS', project2, cat1, None)
    add_requirement('BRA5', 'Add something something to anything.', "2014-03-02", "2014-03-02", 5, 'DO', project2, cat1, user3.user)
    add_requirement('BRA6', 'Add something something to anything.', "2014-03-02", "2014-03-02", 6, 'DO', project2, cat1, user3.user)
    add_requirement('GOL1', 'Add something something to anything.', "2014-03-02", "2014-03-02", 1, 'NS', project3, cat1, None)
    add_requirement('GOL2', 'Add something something to anything.', "2014-03-02", "2014-03-02", 2, 'NS', project3, cat1, None)
    add_requirement('GOL3', 'Add something something to anything.', "2014-03-02", "2014-03-02", 3, 'DO', project3, cat1, user1.user)
    add_requirement('GOL4', 'Add something something to anything.', "2014-03-02", "2014-03-02", 4, 'IP', project3, cat1, user2.user)
    add_requirement('GOL5', 'Add something something to anything.', "2014-03-02", "2014-03-02", 5, 'IM', project3, cat1, user3.user)
    add_requirement('GOL6', 'Add something something to anything.', "2014-03-02", "2014-03-02", 6, 'DO', project3, cat1, user2.user)
    add_requirement('MAX1', 'Add something something to anything.', "2014-03-02", "2014-03-02", 1, 'NS', project4, cat1, None)


def add_category(name):
    c = Category.objects.get_or_create(name=name)[0]
    return c


def add_requirement(regid, name, creation_date, modified_date,
                    priority, status, belongs_to, category, responsible_person):
    r = Requirement.objects.get_or_create(regid=regid, name=name, creation_date=creation_date,
                                          modified_date=modified_date, priority=priority, status=status,
                                          belongs_to=belongs_to, category=category,
                                          responsible_person=responsible_person)
    return r


def add_project(name):
    p = RecapProject.objects.get_or_create(name=name, url=name.replace(' ', '-').lower(), description='This is a description for project 1.')[0]
    return p


def add_user(uname, pw, email, role, participates_in):
    user = User.objects.create_user(uname, email, pw)
    u = UserProfile.objects.get_or_create(user=user)[0]
    for project in participates_in:
        #Participates.objects.get_or_create(user=u, project=project, role=role)
        u.participates_in.add(project)
    return u


if __name__ == '__main__':
    print "Starting ReCap population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DIM3_project.settings')
    from recap.models import RecapProject, UserProfile, Category, Requirement, Participates
    from django.contrib.auth.models import User
    populate()
