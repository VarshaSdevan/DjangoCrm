from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):

    order=Order.objects.all()
    total_order=order.count()
    pending_order=order.filter(status="pending").count()
    delivered_order=order.filter(status="delivered").count()
    context={'total_order':total_order,
                'pending_order':pending_order,
                'delivered_order':delivered_order,
    }
    return render(request,'dashboard.html',context)