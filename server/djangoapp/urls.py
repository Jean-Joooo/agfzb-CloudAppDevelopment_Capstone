from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'djangoapp'
urlpatterns = [
    # route is a string contains a URL pattern
    # view refers to the view function
    # name the URL

   path('/', views.index, name='djangoapp'),
  
   path('index/', views.index, name='index'),

    path('about/', views.about, name='about'),

    path('contact/', views.contact, name='contact'),

    path('registration/', views.registration_request, name='registration'),
    path('login/', views.login_request, name='login'),
    path('logout/', views.logout_request, name='logout'),

    # path for login

    # path for logout

    path('index/', views.index, name='Index'),
   # path for add a review view
    path('add_review/', views.add_review, name='add a review'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
