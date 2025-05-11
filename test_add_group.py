# -*- coding: utf-8 -*-
import pytest
from group import Group
from application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer (fixture.destroy)
    return fixture

    def test_add_group(app):
        app.open_home_page()
        app.login("admin", "secret")
        app.open_groups_page()
        app.create_group(Group(name=u"мир", header=u"мирный",footer=u"счастье"))
        app.return_to_group_page()
        app.logout()

    def test_add_empty_group(app):
        app.open_home_page()
        app.login("admin", "secret")
        app.open_groups_page()
        app.create_group(Group(name=u"", header=u"",footer=u""))
        app.return_to_group_page()
        app.logout()