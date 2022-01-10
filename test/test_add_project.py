from model.project import Project
import string
import random

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def test_add_project(app, json_projects):
    username = "administrator"
    password = "root"
    app.session.login(username, password)
    project = json_projects
    old_projects = app.soap.get_projects_list(username, password)
    app.project.create_project(project)
    new_projects = app.soap.get_projects_list(username, password)
    old_projects.append(project)
    assert sorted(old_projects, key=Project.name_or_max) == sorted(new_projects, key=Project.name_or_max)
    app.session.ensure_logout()
