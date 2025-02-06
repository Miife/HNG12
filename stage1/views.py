from django.http import JsonResponse
from rest_framework.decorators import api_view
from stage1.utils import number_properties


# Create your views here.
@api_view(['GET'])
def number_properties_api(request):
    """API endpoint to classify a number."""
    number = request.GET.get("number")

    #validate input
    if number is None or not number.lstrip('-').isdigit() or (number[0]=='-' and len(number)==1):
        return JsonResponse({"number":number, "error":True}, json_dumps_params={"indent": 2}, status=400)
    
    number= int(number)
    result = number_properties(number)

    return JsonResponse(result, json_dumps_params={"indent": 2}, status=200)