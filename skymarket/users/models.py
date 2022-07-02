from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from django.db import models
from users.managers import UserManager
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _


class UserRoles:
    # TODO закончите enum-класс для пользователя
    USER = "user"
    ADMIN = "admin"
    choices = {
        (USER, USER),
        (ADMIN, ADMIN),
    }


class User(AbstractBaseUser):
    # TODO переопределение пользователя.
    # TODO подробности также можно поискать в рекоммендациях к проекту

    # эта константа определяет поле для логина пользователя
    USERNAME_FIELD = 'email'

    # эта константа содержит список с полями,
    # которые необходимо заполнить при создании пользователя
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone', "role"]

    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

    # для корректной работы нам также необходимо
    # переопределить менеджер модели пользователя

    objects = UserManager()

    @property
    def is_admin(self):
        return self.role == UserRoles.ADMIN  #

    @property
    def is_user(self):
        return self.role == UserRoles.USER

    first_name = models.CharField(max_length=200, verbose_name="Имя",)
    last_name = models.CharField(max_length=200, verbose_name="Фамилия",)
    phone = PhoneNumberField(verbose_name="Телефон",)
    email = models.CharField(max_length=200, verbose_name="Почта", unique=True,)
    role = models.CharField(max_length=200, verbose_name="Роль", choices=UserRoles.choices, default=UserRoles.USER)
    is_active = models.BooleanField(verbose_name="Аккаунт активен", help_text="Укажите, активен ли аккаунт", default=False)
    image = models.ImageField(upload_to="photos/", verbose_name="фото", null=True, blank=True,)