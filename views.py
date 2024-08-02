from django.shortcuts import render, redirect

from django.http import HttpResponse, JsonResponse, HttpResponseRedirect, FileResponse
from django.urls import reverse
from django.template.response import TemplateResponse, SimpleTemplateResponse


# Create your views here.

def http_ref(request):
    return HttpResponse("This is what Http response")


def json_resp(request):
    details = {
        "user name": "user1",
        "Email": "user1@gmail.com"
    }
    return JsonResponse(details)


def redirect_res(request):
    return HttpResponseRedirect(reverse(json_resp))


def file_res(request):
    image_file = ('imagedj.jpeg')
    f = open(image_file, 'rb')
    data = FileResponse(f, content_type='application/jbg')
    data['Content-Disposition'] = 'attachment; filename="image.jpg"'
    return data


def html_resp(request):
    return render(request, 'index.html')


def redirect_resp(request):
    return redirect('https://www.youtube.com/')


def emp_detail(request):
    context = {
        'name': "hari",
        'email': "hari@123gmail.com",
        'salary': "850000"
    }
    return TemplateResponse(request, 'emp_details.html', context)

def http_refr(request):
    return HttpResponse("All is Well")

