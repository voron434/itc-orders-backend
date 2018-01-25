from django.contrib.auth.backends import ModelBackend
from .models import User


class PasswordlessAuthBackend(ModelBackend):
    """Log in to Django without providing a password.
    """
    def authenticate(self, vk_id=None):
        try:
            return User.objects.get(vk_id=vk_id)
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(id=user_id)
        except User.DoesNotExist:
            return None


class PasswordAuthBackend(ModelBackend):
    """Log in to Django without providing a password.
    """
    def authenticate(self, username=None, password=None):
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            # Run the default password hasher once to reduce the timing
            # difference between an existing and a nonexistent user (#20760).
            User().set_password(password)
            return None
        else:
            if user.check_password(password) and self.user_can_authenticate(user):
                return user
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(id=user_id)
        except User.DoesNotExist:
            return None
