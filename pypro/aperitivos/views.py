from django.shortcuts import render

from pypro.aperitivos.models import Video

videos = [
    Video(slug='demonstracao', titulo='Video Básico: Demonstração', vimeo_id='519943040'),
    Video(slug='desinteligencia-artificial', titulo='Bugs do FIFA 21: Desinteligência artificial', vimeo_id='521383814')
]

videos_dct = {v.slug: v for v in videos}


def indice(request):
    return render(request, 'aperitivos/indice.html', context={'videos': videos})


def video(request, slug):
    video = videos_dct[slug]
    return render(request, 'aperitivos/video.html', context={'video': video})
