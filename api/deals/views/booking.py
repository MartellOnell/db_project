import json

from django.views import View
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import get_user_model
from django.http import JsonResponse

from apps.deals.models import Room, OrderMenuItem, Booking


User = get_user_model()


@method_decorator(csrf_exempt, name='dispatch')
class BookingView(View):
    """
    View to render the login template.
    """
    def get(self, request):
        rooms = Room.objects.all()
        order_menu = OrderMenuItem.objects.filter(
            guest=User.objects.get(pk=request.GET.get('user_id'))
        )
        print(order_menu)

        return render(
            request,
            'deals/booking.html',
            {
                'rooms': rooms,
                'dishes': order_menu,
            },
        )
    
    def post(self, request):
        data = json.loads(request.body)

        user = User.objects.get(pk=data['guest'])
        room = Room.objects.get(pk=data['room'])
        order_menu = OrderMenuItem.objects.get(
            pk=data['order_menu'],
        )
        checkin = data['checkin']
        checkout = data['checkout']
        Booking.objects.create(
            guest=user,
            room=room,
            order_menu=order_menu,
            checkin=checkin,
            checkout=checkout,
        )

        return JsonResponse({'status': 'success', 'message': 'Booking created successfully!'})
    