from django.http import JsonResponse
from datetime import datetime, timezone

def my_info(request):
    response_data = {
        "email": "yanmife.at@gmail.com",
        "current_datetime": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "github_url": "https://github.com/Miife/HNG12"
    }
    return JsonResponse(response_data, json_dumps_params={"indent": 2})

