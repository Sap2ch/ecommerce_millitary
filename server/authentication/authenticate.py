from django.contrib.auth.models import User
from django.contrib.auth.backends import ModelBackend

class CaseInsensitiveAuthBackend(ModelBackend):
    """
        КАСТОМНИЙ AUTHENTICATE, ЯКИЙ БУДЕ ЗДІЙСНЮВАТИ ВХІД БЕЗ ВРАХУВАННЯ РЕГІСТРУ
    """
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(username__iexact=username)  # `iexact` — регістронезалежний
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None
