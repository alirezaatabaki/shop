from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password=None):
        """
        Creates and saves a User with the given email, first name,
        last name and password.
        """
        if not email:
            raise ValueError('ایمیل برای ایجاد حساب کاربری الزامی است')

        if not first_name:
            raise ValueError('نام خانوادگی برای ایجاد حساب کاربری الزامی است')

        if not last_name:
            raise ValueError('نام برای ایجاد حساب کاربری الزامی است')

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, password=None):
        """
        Creates and saves a superuser with the given email, first name,
        last name and password.
        """
        user = self.create_user(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            password=password
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    "My shop customized user model"

    class Meta:
        verbose_name = 'نمایه کاربر'
        verbose_name_plural = 'نمایه کاربر'

    email = models.EmailField(verbose_name='آدرس ایمیل', max_length=100, unique=True)
    first_name = models.CharField(verbose_name='نام', max_length=100)
    last_name = models.CharField(verbose_name='نام خانوادگی', max_length=100)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

    def get_full_name(self):
        return self.first_name + ' ' + self.last_name


class Address(models.Model):
    address = models.TextField(verbose_name="آدرس")
    user_fk = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر')
    is_default = models.BooleanField(verbose_name='پیش‌فرض')

    class Meta:
        verbose_name = 'آدرس'
        verbose_name_plural = 'آدرس‌ها'

    def __str__(self):
        return f'آدرس: {self.address} || کاربر: {self.user_fk}'