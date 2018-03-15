import requests
from requests.exceptions import ConnectionError as RequestsConnectionError

from django.conf import settings
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt


@method_decorator(csrf_exempt, name='dispatch')
class OpenDoorView(View):
    http_method_names = ['post', 'head', 'options', 'trace']

    def post(self, request, *args, **kwargs):
        data = {}
        data['success'] = False

        try:
            r = requests.post(settings.DOOR_MODULE_URL)
            data['success'] = r.json().get('status', False)
            if not data['success']:
                data['error'] = 'Already opened'

        except RequestsConnectionError as e:
            data['error'] = str(e)

        return JsonResponse(data)
