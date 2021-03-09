from django.shortcuts import render


def video(request, slug):
    videos = {
        'demonstracao': {'titulo': 'Video Básico: Demonstração', 'vimeo_id': 519943040},
        'desinteligencia-artificial': {'titulo': 'Bugs do FIFA 21: Desinteligência artificial', 'vimeo_id': 521383814}
    }
    video = videos[slug]
    return render(request, 'aperitivos/video.html', context={'video': video})
