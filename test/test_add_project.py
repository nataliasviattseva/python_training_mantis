from model.project import Project

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
