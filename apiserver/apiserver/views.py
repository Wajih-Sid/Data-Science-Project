from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

import json

from HRProject import PersistentModel


@csrf_exempt
def get_churn(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        persistent_model = PersistentModel()

        try:
            predictions = persistent_model.predict_from_persistedmodel(data)
            return JsonResponse({'status': 'OK', 'predictions': predictions, 'data': data})

        except Exception:
            print "Failed!"

    else:
        return JsonResponse({'status': 'OK'})