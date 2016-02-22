from __future__ import unicode_literals

from django.contrib import messages
from django.core.urlresolvers import reverse
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import redirect
from django.views.generic import View, RedirectView, TemplateView, FormView
from braces.views import LoginRequiredMixin

from addressbook.models import Address
from .forms import CustomerCreateForm
from .models import Customer


class DashBoardView(TemplateView):
    template_name = 'index.html'

    def get(self, *args, **kwargs):
        redirect_url = None
        if self.request.user.is_authenticated:
            if self.request.user.groups.filter(name='Customers').exists():
                redirect_url = 'customers:dashboard'
            elif self.request.user.groups.filter(name='Officers').exists():
                redirect_url = 'officers:dashboard'
        if redirect_url:
            return redirect(redirect_url)
        else:
            return super(DashBoardView, self).get(*args, **kwargs)


class VerificationView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return reverse('social:complete', args=('email',)) + '?verification_code={}'.format(kwargs['token'])


class ValidationSentView(View):
    def get(self, *args, **kwargs):
        messages.success(self.request,
                         "An email has been sent to you. "
                         "Check your mailbox and click on the link to complete the login process.")
        return redirect('home')


class CustomerCreateView(LoginRequiredMixin, FormView):
    template_name = 'customer_create.html'
    success_url = reverse_lazy('home')
    form_class = CustomerCreateForm

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            # save top level user details
            user = request.user
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.save()

            # address
            address_data = form.get_address_data()
            address = Address(**address_data)
            address.save()

            # customer
            customer_data = form.get_customer_data()
            customer = Customer(**customer_data)
            customer.user = user
            customer.residential_address = address
            customer.save()

            return redirect('home')

        else:
            messages.error(request, "Please correct the error belows.")
            return self.form_invalid(form)
