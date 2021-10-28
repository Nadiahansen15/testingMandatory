from django.views.generic.edit import CreateView
from django.views.generic.edit import ListView
from .models import keaNet, keaNetForm

# Create your views here.
# https://simpleisbetterthancomplex.com/tutorial/2016/08/29/how-to-work-with-ajax-request-with-django.html


class keaNetFormView(CreateView):
    model = keaNet
    template_name = "keaNet/createkeaNet.html"
    form_class = keaNetForm
    success_url = "keaNet/keaNetoverview.html"

    # Checks if data input is valid and saves object
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super().form_valid(form)


class keaNetView(ListView):
    model = keaNet
    template_name = "keaNet/keanetoverview.html"
