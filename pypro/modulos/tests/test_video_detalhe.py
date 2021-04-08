import pytest
from django.urls import reverse
from model_mommy import mommy

from pypro.django_assertions import assert_contains
from pypro.modulos.models import Video, Modulo


@pytest.fixture
def modulo(db):
    return mommy.make(Modulo)


@pytest.fixture
def video_detalhe(modulo):
    return mommy.make(Video, modulo=modulo)


@pytest.fixture
def resp(client, video_detalhe):
    resp = client.get(reverse('modulos:video', kwargs={'slug': video_detalhe.slug}))
    return resp


def test_titulo(resp, video_detalhe: Video):
    assert_contains(resp, video_detalhe.titulo)


def test_vimeo(resp, video_detalhe: Video):
    assert_contains(resp, f'src="https://player.vimeo.com/video/{video_detalhe.vimeo_id}')


def test_modulo_breadcrumb(resp, modulo: Modulo):
    assert_contains(resp,
                    f'<li class="breadcrumb-item"><a href="{video.modulo.get_absolute_url()}">{modulo.titulo}</a></li>')
