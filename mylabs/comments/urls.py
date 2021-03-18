from django.urls import path

from . import views

urlpatterns = [
    path("", views.ServMonView.as_view()),
    path("<slug:slug>", views.ServDetail.as_view(), name='serv_mon_detail'),
    path("create/", views.ServCreateView.as_view(), name='serv_mon_add'),
    path("export/", views.export, name='serv_mon_download'),
    path("pdf_list", views.PdfMakerList.as_view()),
    path('pdf_list/<slug:slug>', views.PdfMakerDetail.as_view(), name='pdf_detail'),
    path("pdf/", views.PdfMakerCreateView.as_view(), name='pdf_create'),
    path("pdf_export/", views.pdf_export, name='pdf_export'),
]
