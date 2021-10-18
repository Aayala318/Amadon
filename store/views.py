from django.shortcuts import redirect, render
from . models import *
from django.db.models import Sum

# Create your views here.
def amadon(request):
    context = {
        "all_items": Item.objects.all()
    }
    return render(request, "main.html", context)

def checkout(request):
    last = Order.objects.last()
    price = last.total_price
    full_order = Order.objects.aggregate(Sum('quantity_ordered'))['quantity_ordered__sum']
    full_price = Order.objects.aggregate(Sum('total_price'))['total_price__sum']
    context = {
        'orders':full_order,
        'total':full_price,
        'bill':price,
    }
    return render(request, 'purchase.html', context)

def purchase(request):
    if request.method == 'POST':
        this_product = Item.objects.filter(id=request.POST["id"])
        if not this_product:
            return redirect('/')
        else:
            quantity = int(request.POST["quantity"])
            total_charge = quantity*(float(this_product[0].price))
            Order.objects.create(quantity_ordered=quantity, total_price=total_charge)
            return redirect('/checkout')
    else:
        return redirect('/')