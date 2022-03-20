from django.urls import path

from pages.views import HomePageView, AdminView


app_name = 'pages'

urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    path('painel_admin/', AdminView.as_view(), name="painel_admin")
]
