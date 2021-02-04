from django.http import HttpResponse

# Create your views here.


def home(request):
    return HttpResponse('Olá Django, meu nome é Oscar')
