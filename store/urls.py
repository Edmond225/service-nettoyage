from django.urls import path
from .views import contact_view, detail_service_view, home_view, about_view, demande_devis_view

urlpatterns = [
    path("", home_view, name="home"),
    path("servicenettoyage/", contact_view, name="servicenettoyage"),
    path("detail/", detail_service_view, name="detail"),
    path("about/", about_view, name="about"),
    path("demande-devis/", demande_devis_view, name="demande_devis"),
]
