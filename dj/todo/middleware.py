from django.http import JsonResponse
from django.utils.deprecation import MiddlewareMixin


#
"""
- tracker handle in django
- epoch : done
- add entry to table
"""

import time
import math
from encrypted_id import encode


class TrackerMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.COOKIES.get("tid", None) is None:
            request.tid = encode(math.floor(time.time()), "kameri-service-tracker")
        else:
            request.tid = request.COOKIES.get("tid")
        return None

    def process_response(self, request, response: JsonResponse):
        if not request.COOKIES.get("tid", None):
            import datetime

            max_age = 365 * 24 * 60 * 60  # 10 years
            expires = datetime.datetime.now() + datetime.timedelta(seconds=max_age)
            response.set_cookie(
                "tid",
                request.tid,
                expires=expires.strftime("%a, %d-%b-%Y %H:%M:%S GMT"),
            )
            print("process_response", response.cookies)
        return response
