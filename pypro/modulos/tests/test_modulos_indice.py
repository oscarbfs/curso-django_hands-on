from typing import List

import pytest
from django.urls import reverse
from model_mommy import mommy

from pypro.django_assertions import assert_contains
from pypro.modulos.models import Video, Modulo


@pytest.fixture
def modulos(db):
    return mommy.make(Modulo, 2)


@pytest.fixture
def videos_detalhe(modulos):
    videos = []
    for modulo in modulos:
        videos.extend(mommy.make(Video, 3, modulo=modulo))
        return videos


@pytest.fixture
def resp(client, modulos, videos_detalhe):
    resp = client.get(reverse('modulos:indice'))
    return resp


def test_indice_disponivel(resp):
    assert resp.status_code == 200


def test_titulo(resp, modulos: List[Modulo]):
    for modulo in modulos:
        assert_contains(resp, modulo.titulo)


def test_descricao(resp, modulos: List[Modulo]):
    for modulo in modulos:
        assert_contains(resp, modulo.descricao)


def test_publico(resp, modulos: List[Modulo]):
    for modulo in modulos:
        assert_contains(resp, modulo.publico)


def test_videos_titulos(resp, videos_detalhe: List[Video]):
    for video in videos_detalhe:
        assert_contains(resp, video.titulo)


def test_videos_urls(resp, videos_detalhe: List[Video]):
    for video in videos_detalhe:
        assert_contains(resp, video.get_absolute_url())
