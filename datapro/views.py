from django.http import HttpResponse


def detail(request, DataPro_id):
    return HttpResponse("You're looking at question %s." % DataPro_id)
