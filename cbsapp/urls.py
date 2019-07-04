from django.urls import path, re_path, reverse
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.views.generic.base import TemplateView
from django_registration.backends.activation.views import ActivationView, RegistrationView
from . import forms, views

urlpatterns = [
    re_path(r'^$', views.home, name='home'),
    re_path(r'^user/', views.profile, name='profile'),
        path('register/', RegistrationView.as_view(form_class=forms.RegistrationForm), name='register'),
    # re_path(r'^profile/update/', views.update_profile, name='update_profile'),
    url(r'^register/complete/$', TemplateView.as_view(template_name='django_registration/registration_complete.html'), name='django_registration_complete'),
    url(r'^activate/(?P<activation_key>[-:\w]+)/$',ActivationView.as_view(),name='django_registration_activate'),
    url(r'^register/closed/$',TemplateView.as_view(template_name='django_registration/registration_closed.html'),name='django_registration_disallowed'),
]
