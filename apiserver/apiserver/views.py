from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

import json

@csrf_exempt
def get_churn(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        return JsonResponse({'status': 'OK', 'data': data})
    else:
        return JsonResponse({'status': 'OK'})