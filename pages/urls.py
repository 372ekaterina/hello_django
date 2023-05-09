from django.urls import path
from .views import HomePageView,  AboutPageView, LogInPageView #,LogoutView

urlpatterns = [
#    path('about/', AboutPageView.as_view(), name='about'), # new
    path('homepage/', HomePageView.as_view(), name='home'),
    path('accounts/', LogInPageView.as_view(), name='login'),
    #path('accounts/logout/', LogoutView.as_view(), name='logout'),
]
