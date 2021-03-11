import pytest
from django.urls import reverse

from pypro.django_assertions import assert_contains


@pytest.fixture
def resp(client):
    return client.get(reverse('aperitivos:indice'))


def test_status_code(resp):
    assert resp.status_code == 200


@pytest.mark.parametrize(
    'titulo',
    [
        'Video Básico: Demonstração',
        'Bugs do FIFA 21: Desinteligência artificial'
    ]
)
def test_title_video(resp, titulo):
    assert_contains(resp, titulo)

# def test_conteudo_video(resp):
#     assert_contains(resp, '<iframe src="https://player.vimeo.com/video/519943040')
