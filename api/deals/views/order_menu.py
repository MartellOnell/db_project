import json

from django.views import View
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import get_user_model
from django.http import JsonResponse

from apps.deals.models import MenuItem, OrderMenuItem


User = get_user_model()


@method_decorator(csrf_exempt, name='dispatch')
class OrderMenuView(View):
    """
    View to render the login template.
    """
    def get(self, request):
        menu_items = MenuItem.objects.all()

        return render(
            request,
            'deals/order_menu.html',
            {
                'menu_items': menu_items,
            },
        )
    
    def post(self, request):
        print(request.body)
    
        data = json.loads(request.body)

        user = User.objects.get(pk=data['guest'])
        dish = MenuItem.objects.get(pk=data['dish'])
        quantity = data['quantity']
        OrderMenuItem.objects.create(
            guest=user,
            dish=dish,
            quantity=quantity,
        )

        return JsonResponse({'status': 'success', 'message': 'Order menu item created successfully!'}) 