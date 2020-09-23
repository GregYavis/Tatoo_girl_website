from django.shortcuts import render, redirect, get_object_or_404
from .models import Service, Order, OrderedService
from django.views.generic import TemplateView, ListView, DetailView, View
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
def main_page(request):
    context = {}
    return render(request, 'pages/main.html', context)


class Home(TemplateView):
    template_name = 'pages/main.html'


"""def services_page(request):
    services = Service.objects.all()
    context = {'services': services}
    return render(request, 'pages/services.html', context)"""


class ServicesAll(ListView):
    model = Service
    template_name = 'pages/services.html'
    context_object_name = 'services'


class ServiceDetails(DetailView):
    model = Service
    template_name = 'pages/service.html'


class UserOrderedServices(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        try:
            order = Order.objects.get(customer=self.request.user)
            context = {'object': order}
            return render(self.request, 'pages/user-ordered-services.html',
                          context)
        except ObjectDoesNotExist:
            messages.error(self.request, 'Вы еще не записывались на тату, '
                                         'коррекцию или разработку ескиза')
            return redirect('/')


@login_required()
def add_to_cart(request, slug):
    service = get_object_or_404(Service, slug=slug)
    ordered_service, created = OrderedService.objects.get_or_create(
        service=service,
        customer=request.user)
    order_query_set = Order.objects.filter(customer=request.user)
    if order_query_set.exists():
        order = order_query_set[0]
        # check if service already ordered
        if order.services.filter(service__slug=service.slug).exists():
            ordered_service.save()
            messages.warning(request, 'Вы уже записаны')
            return redirect('tattoo:services-page')
        else:
            messages.info(request, f'Запись прошла успешно')
            order.services.add(ordered_service)
            return redirect('tattoo:services-page')
    else:
        order_date = timezone.now()
        order = Order.objects.create(customer=request.user,
                                     ordered_date=order_date)
        order.services.add(ordered_service)
        messages.info(request, f'Запись прошла успешно')
        return redirect('tattoo:services-page')





"""
class PortfolioPage(ListView):
    template_name = 'pages/portfolio.html'
"""


class PortfolioPage(TemplateView):
    template_name = 'pages/portfolio.html'


class AdvicesView(TemplateView):
    template_name = 'pages/advices.html'


class LoginRegisterChoice(TemplateView):
    template_name = 'pages/login-or-register.html'
