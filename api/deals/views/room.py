from django.shortcuts import render
from django.views import View

from api.deals.forms.room import RoomForm
from apps.deals.models import Room


class RoomView(View):
    form_class = RoomForm
    template_name = 'deals/room.html'

    def get(self, request):
        rooms = Room.objects.all()
        return render(request, self.template_name, {'rooms': rooms})