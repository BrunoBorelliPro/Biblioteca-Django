from django.urls import path

from pages.views import home_page


app_name = 'pages'

urlpatterns = [
    path('', home_page, name="home")
]
