from django.http import JsonResponse
from django.utils.deprecation import MiddlewareMixin

class TrackerMiddleware(MiddlewareMixin):
    def process_response(self, request, response: JsonResponse):
        if not request.COOKIES.get('tracker_id', None):
            import datetime

            max_age = 365 * 24 * 60 * 60  # 10 years
            expires = datetime.datetime.now() + datetime.timedelta(seconds=max_age)
            response.set_cookie('tracker_id', expires.strftime("%a, %d-%b-%Y %H:%M:%S GMT"), expires=expires.strftime("%a, %d-%b-%Y %H:%M:%S GMT"))

            print("process_response",response.cookies)
        return response
