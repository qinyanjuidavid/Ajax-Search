import json

from django.http import HttpResponse,JsonResponse
from django.shortcuts import render

from myapp.models import Expense


def AjaxIndexView(request):
    if request.method == "POST":
        search_str = json.loads(request.body).get('searchText', '')
        expenses = Expense.objects.filter(amount__istartswith=search_str, owner=request.user) | Expense.objects.filter(date__istartswith=search_str, owner=request.user) | Expense.objects.filter(
            description__icontains=search_str, owner=request.user) | Expense.objects.filter(category__icontains=search_str, owner=request.user)
    data=expenses.values()
    return JsonResponse(list(data),safe=False)

def IndexView(request):
    qs=Expense.objects.all().order_by('-date')
    context = {
    'expenses':qs
    }
    return render(request, 'myapp/home.html', context)
