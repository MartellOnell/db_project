import json

from django.views import View
from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from apps.staff.models import Gender


@method_decorator(csrf_exempt, name='dispatch')
class LoginView(View):
    """
    View to render the login template.
    """
    def get(self, request):
        return render(request, 'deals/login.html', {'genders': Gender.objects.all()})
    

    def post(self, request):
        """
        Handle the login form submission.
        """
        data = json.loads(request.body)

        username = data['username']
        password = data['password']
        
        User = get_user_model()
        try:
            user = User.objects.get(username=username)
            if user.check_password(password):
                return JsonResponse({'status': 'success', 'message': 'Login successful!', 'user_id': user.id})
            else:
                return JsonResponse({'status': 'error', 'message': 'Invalid password!'}, status=401)
        except User.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'User does not exist!'}, status=404)