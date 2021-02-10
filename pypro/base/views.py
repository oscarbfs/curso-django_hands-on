from django.http import HttpResponse

# Create your views here.


def home(request):
    return HttpResponse('<html><body>Olá Django, meu nome é Oscar</body></html>', content_type='text/html')
