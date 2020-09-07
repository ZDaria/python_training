

def test_edit_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(edit_field="group_name", edit_value="Test_7")
    app.session.logout()
