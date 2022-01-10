from model.project import Project
import random


def test_delete_project(app):
    username = "administrator"
    password = "root"
    app.session.login(username, password)
    if len(app.project.get_projects_list()) == 0:
        app.project.create_project(Project(name="test"))
    old_projects = app.soap.get_projects_list(username, password)
    project = random.choice(old_projects)
    app.project.delete_project(project.name)
    new_projects = app.soap.get_projects_list(username, password)
    old_projects.remove(project)
    assert old_projects == new_projects
    app.session.ensure_logout()
