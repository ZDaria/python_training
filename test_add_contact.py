# -*- coding: utf-8 -*-
from contact import Contact
import pytest
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.login(username="admin", password="secret")
    app.create_new_contact(Contact(firstname="Ivan",
                                   middlename="Ivanovich",
                                   lastname="Ivanov",
                                   nickname="Vany123",
                                   title="QA",
                                   company="Alfa Bank",
                                   address="Russion Federation\nMoscow\nRead sq 1",
                                   telephone_home="84955123545",
                                   telephone_mobile="89105121211",
                                   telephone_work="84957121911",
                                   email="test@gmail.com",
                                   homepage="-",
                                   bday="23",
                                   bmonth="March", byear="1990",
                                   aday="1", amonth="September", ayear="2021",
                                   address2="-",
                                   phone2="-",
                                   notes="-",
                                   fax="-",
                                   email2="-",
                                   email3="-"))

    app.gout()
