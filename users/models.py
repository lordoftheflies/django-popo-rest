from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class PopoFoo():
    class Meta:
        managed = False

    def __init__(self, first='Duck', second='Donald'):
        self.first = first
        self.last = second
