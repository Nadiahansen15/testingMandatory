from django.views.generic.edit import CreateView
from django.views.generic.edit import ListView
from .models import keaNet, keaNetForm
from django.views.generic import FormView, ListView, CreateView
from django.http import JsonResponse


# Create your views here.
# https://simpleisbetterthancomplex.com/tutorial/2016/08/29/how-to-work-with-ajax-request-with-django.html


class keaNetFormView(CreateView):
    model = keaNet
    template_name = "keaNet/createkeaNet.html"
    form_class = keaNetForm
    success_url = "/keanetoverview"

    # Checks if data input is valid and saves object
    def form_valid(self, form):
        obj = form.save(commit = False)
        print(obj.InternetConnection, "heeeeeeeeeey!!!!!", obj.cellphone.price)
        if (obj.InternetConnection == True):
            obj.totalPrice += 200

        obj.totalPrice += obj.PhoneLines * 150 + obj.cellphone.price
        
        obj.save()
        return super().form_valid(form)

'''
def cal_Total_Price(request):
    InternetConnection = request.GET.get('InternetConnection', None)
    PhoneLines = request.GET.get('PhoneLines', None)
    cellphone = request.GET.get('cellphone', None)
    totalPrice = request.GET.get('totalPrice', None)
    
    print(InternetConnection)

    if (InternetConnection == 'on'):
        totalPrice =+ 200
    elif (PhoneLines < 8):
        sumf = PhoneLines*150
        sumf =+ totalPrice

    data = {
        "totalPrice": totalPrice 
    }
    return JsonResponse(data)
'''

class keaNetView(ListView):
    model = keaNet
    template_name = "keaNet/keanetoverview.html"
