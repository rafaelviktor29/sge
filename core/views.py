import json
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from . import metrics


@login_required(login_url='login')
def home(request):
    product_metrics = metrics.get_product_metrics()
    sales_metrics = metrics.get_sales_metrics()
    daily_sales_data = metrics.get_daily_sales_data()
    daily_sales_quantity_data = metrics.get_daily_sales_quantity_data()
    product_count_by_category = metrics.get_product_count_by_category()
    product_count_by_brand = metrics.get_product_count_by_brand()

    return render(
        request, 'home.html', context={
            'product_metrics': product_metrics,
            'sales_metrics': sales_metrics,
            'daily_sales_data': json.dumps(daily_sales_data),
            'daily_sales_quantity_data': json.dumps(daily_sales_quantity_data),
            'product_count_by_category': json.dumps(product_count_by_category),
            'product_count_by_brand': json.dumps(product_count_by_brand)
        }
    )
