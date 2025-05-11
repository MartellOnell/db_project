import json

from django.views import View
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import get_user_model
from django.http import JsonResponse

from apps.deals.models import OrderMenuItem, Booking


User = get_user_model()


@method_decorator(csrf_exempt, name='dispatch')
class MyOrdersView(View):
    """
    View to render the login template.
    """
    def get(self, request):
        try:
            user = User.objects.get(pk=request.COOKIES.get('user_id'))
        except User.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'User not found!'}, status=404)

        bookings = Booking.objects.filter(guest=user)
        order_menus = OrderMenuItem.objects.filter(guest=user)

        return render(
            request,
            'deals/my_orders.html',
            {
                'bookings': bookings,
                'order_menus': order_menus,
            },
        )

    