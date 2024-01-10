from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'djangoapp'
urlpatterns = [
    # route is a string contains a URL pattern
    # view refers to the view function
    # name the URL
     path(route='', view=static, name='static'),

    path('about/', views.about, name='about'),

    path('contact/', views.contact, name='contact'),

    path('login/', views.login_request, name='login'),
    path('logout/', views.logout_request, name='logout'),

    # path for login

    # path for logout

    path('index/', views.index, name='Index'),

    path('add_review/', views.add_review, name='add a review'),
    path('dealer_reviews/', views.dealerreviews, name='Dealer reviews'),
    # path for add a review view

from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings

    path('admin/', admin.site.urls),
    path('templates/', include('templates.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
