from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.models import User
from django.db import connection

class MySQLBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, department=None):
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Department WHERE username=%s AND password=%s AND department=%s", [username, password, department])
        result = cursor.fetchone()
        if result:
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                user = User(username=username)
                user.set_password(password)
                user.save()
            return user
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
