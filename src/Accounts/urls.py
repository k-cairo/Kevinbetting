from django.urls import path, include
from Accounts.views import signup, profile

urlpatterns = [
    path("accounts/new/", signup, name="accounts-signup"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/profile/', profile, name='accounts-profile')
]

