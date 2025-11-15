from django.shortcuts import render
from django.http import JsonResponse


def hello(request):
    return render(request,"index.html")

def ajax_for_json(request):
    return JsonResponse({"status":"INDEX.HTML ajax for  THIS RESPONSE IS FOR INDEX.HTML"})


def test_ajax(request):
    context = {"status":"AJAX.HTML Ajax is working ajax for AJAX.HTML"}
    return render(request,'ajax.html',context)