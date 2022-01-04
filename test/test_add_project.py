def test_add_project(app, json_projects):
    project = json_projects
    old_projects = app.project.get_projects_list()
    app.project.create_project(project)
    new_projects = app.project.get_projects_list()
    old_projects.append(project)
    assert old_projects == new_projects
