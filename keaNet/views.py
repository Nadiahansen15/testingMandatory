from .models import keaNet, keaNetForm
from django.views.generic import ListView, CreateView

# Create your views here.
# https://simpleisbetterthancomplex.com/tutorial/2016/08/29/how-to-work-with-ajax-request-with-django.html


class keaNetFormView(CreateView):
    model = keaNet
    template_name = "keaNet/createkeaNet.html"
    form_class = keaNetForm
    success_url = "/keanetoverview"

    # Checks if data input is valid and saves object
    def form_valid(self, form):
        obj = form.save(commit=False)
        print(obj.InternetConnection, "heeeeeeeeeey!!!!!", obj.cellphone.price)
        if (obj.InternetConnection is True):
            intcon = 200
        else:
            intcon = 0

        obj.totalPrice = + obj.PhoneLines * 150 + obj.cellphone.price + intcon

        obj.save()
        return super().form_valid(form)


class keaNetView(ListView):
    model = keaNet
    template_name = "keaNet/keanetoverview.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        LastAdded = keaNet.objects.all().order_by('-created_at',)[0:1]
        context['last_added'] = LastAdded
        return context
