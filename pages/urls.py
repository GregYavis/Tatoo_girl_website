from django.contrib import admin
from django.urls import path, include
from .views import main_page, Home, PortfolioPage, \
    AdvicesView, LoginRegisterChoice, ServiceDetails, ServicesAll, \
    add_to_cart, remove_from_cart, UserOrderedServices

app_name = 'tattoo'
urlpatterns = [
    path('', Home.as_view(), name='main-page'),
    path('services/', ServicesAll.as_view(), name='services-page'),
    path('portfolio/', PortfolioPage.as_view(), name='portfolio-page'),
    path('advices/', AdvicesView.as_view(), name='advices-page'),
    path('login-or-register/', LoginRegisterChoice.as_view(),
         name='login-or-register'),
    path('service/<slug>/', ServiceDetails.as_view(), name='service-details'),
    path('add-service-to-cart/<slug>/', add_to_cart,
         name='add-service-to-cart'),
    path('my-ordered-services/', UserOrderedServices.as_view(),
         name='user-ordered-services'),
    path('remove-service-from-cart/<slug>', remove_from_cart,
         name='remove-service-from-cart')
]
