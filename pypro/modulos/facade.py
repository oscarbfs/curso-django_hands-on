from typing import List

from pypro.modulos.models import Modulo, Video


def listar_modulos_ordenados() -> List[Modulo]:
    """
    Lista módulos ordenados por titulo
    :return:
    """

    return list(Modulo.objects.order_by('order').all())


def encontrar_modulo(slug: str) -> Modulo:
    return Modulo.objects.get(slug=slug)


def listar_videos_de_modulo_ordenadas(modulo: Modulo):
    return list(modulo.video_set.order_by('order').all())


def encontrar_video(slug):
    return Video.objects.select_related('modulo').get(slug=slug)


def listar_modulos_com_aulas():
    return Modulo.objects.order_by('order').prefetch_related('video_set').all()
