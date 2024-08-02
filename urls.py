from django.urls import path, include
from .views import http_ref, json_resp, redirect_res, file_res, html_resp, redirect_resp, emp_detail, http_refr

urlpatterns = [
    path('http_ref/', http_ref),
    path('json_resp/', json_resp),
    path('redirect_res/', redirect_res),
    path('file_res/', file_res),
    path('html_resp/', html_resp),
    path('redirect_resp/', redirect_resp),
    path('emp_detail/', emp_detail),
    path('http_refr/', http_refr)

]