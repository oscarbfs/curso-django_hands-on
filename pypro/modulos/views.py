from django.shortcuts import render

from pypro.modulos import facade


def detalhe(request, slug):
    modulo = facade.encontrar_modulo(slug)
    videos = facade.listar_videos_de_modulo_ordenadas(modulo)
    return render(request, 'modulos/modulo_detalhe.html', {'modulo': modulo, 'videos': videos})


def video(request, slug):
    video = facade.encontrar_video(slug)
    return render(request, 'modulos/video_detalhe.html', {'video': video})


def indice(request):
    ctx = {'modulos': facade.listar_modulos_com_videos()}
    return render(request, 'modulos/indice.html', ctx)
