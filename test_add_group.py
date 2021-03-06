# -*- coding: utf-8 -*-
from group import Group
from application import Application
import pytest


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="qwe", header="qwe1", footer="qwee"))
    app.logout()


def test_empty_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="qwe", header="qwe1", footer="qwee"))
    app.logout()
