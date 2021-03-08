from django.shortcuts import render


def video(request, slug):
    video = {'titulo': 'Video Básico: Demonstração', 'vimeo_id': 519943040}
    return render(request, 'aperitivos/video.html', context={'video': video})
