from django.shortcuts import render
from .models import Order
from .forms import OrderForms


# Create your views here.
def first_page(request):
    object_list = Order.objects.all()
    form = OrderForms()
    return render(request, "./index.html", {"object_list": object_list, "form": form})


def thanks_page(request):
    return (request, "./thank_page.html")
