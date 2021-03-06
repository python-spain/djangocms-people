from django.conf.urls import url

from cms_people.views.profile import ProfileAboutView, ProfileSecurityView, ProfilePrivacyView
from ..views.profile import ProfileAddressView

urlpatterns = [
    url('^$', ProfileAboutView.as_view(), name='profile_about'),
    url('^security$', ProfileSecurityView.as_view(), name='profile_security'),
    url('^address$', ProfileAddressView.as_view(), name='profile_address'),
    url('^privacy', ProfilePrivacyView.as_view(), name='profile_privacy'),
]
