import json

from django.views import View
from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from apps.staff.models import Gender


@method_decorator(csrf_exempt, name='dispatch')
class RegisterView(View):
    def get(self, request):
        """
        Render the registration template.
        """
        return render(request, 'deals/register.html', {'genders': Gender.objects.all()})

    def post(self, request):
        """
        Handle the registration form submission.
        """
        data = json.loads(request.body)

        phone = data['phone']
        gender = data['gender']
        birthday = data['birthday']
        username = data['username']
        password = data['password']
        passport_series = data['passport_series']
        passport_number = data['passport_number']
        email = data['email']
        
        User = get_user_model()

        try:
            user = User.objects.create_user(
                username=username,
                password=password,
                email=email,
                phone=phone,
                gender=Gender.objects.get(pk=int(gender)),
                birthday=birthday,
                passport_series=passport_series,
                passport_number=passport_number,
            )
            return JsonResponse({'status': 'success', 'message': 'Registration successful!', 'user_id': user.id})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)