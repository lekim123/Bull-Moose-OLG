from django.http import Http404
from django.utils.deprecation import MiddlewareMixin
from .models import IPAddress

def get_ip(request):    
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

class ProtectAdminMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.META['PATH_INFO'].startswith('/admin'):
            if get_ip(request) in list(IPAddress.objects.all()):
                return None
            raise Http404()