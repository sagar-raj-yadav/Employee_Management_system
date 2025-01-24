from django.http import JsonResponse

def home_page(request):
    friends="hello world"
    return JsonResponse(friends,safe=False)

