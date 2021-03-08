import pytest
# from django.test import Client
from django.urls import reverse

from pypro.django_assertions import assert_contains


@pytest.fixture
def resp(client):
    resp = client.get(reverse('base:home'))
    return resp


def test_status_code(resp):
    assert resp.status_code == 200


def test_title(resp):
    assert_contains(resp, '<title>OBFS - Home</title>')

# def test_home_link(resp):
#     assert_contains(resp,
#                     f'href="{reverse("base:home")}" style="margin-left:25px;"><img src="{
#                     % static 'img/favicon_obfs.png' %}" alt="Favicon" width="50" height="50"/></a>'
