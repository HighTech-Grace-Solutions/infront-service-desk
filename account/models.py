from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.


class MyAccountManager(BaseUserManager):

    # the parameter will contains things that are required upon registration
    def create_user(self, email, first_name=None, last_name=None, full_name=None, role=None, company_link = None, group='Not Set', password=None, is_pic=None):

        if not email:
            raise ValueError("Users must have email address")

        user = self.model(
            email=self.normalize_email(email),

            # additional information
            role=role,
            full_name=full_name,
            group=group,
            company_link=company_link,
            last_name=last_name,
            first_name=first_name,
            is_pic=is_pic,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, role, first_name=None, last_name=None, group='Not Set'):

        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            role=role,
            group=group,
            last_name=last_name,
            first_name=first_name,
        )

        #! NEED TO KNOW SUPER USER NEED TO BE ATTACHED TO COMPANY OR NOT

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True

        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):

    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    first_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    full_name = models.CharField(
        max_length=200, null=True, blank=True, unique=True)
    role = models.CharField(max_length=200, null=True)
    group = models.CharField(max_length=200, null=True, blank=True, default="Not Set")
    company_link = models.ForeignKey("administrator.Company", on_delete=models.CASCADE, null=True, blank=True)
    date_joined = models.DateTimeField(
        verbose_name="date joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)

    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_pic = models.BooleanField(default=False)

    # this is used for whatever you use login for, in this case I will be using email
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['role']

    # telling where to find the manager

    objects = MyAccountManager()

    def __str__(self):
        return self.email

    # permission by default set to the admin only
    def has_perm(self, perm, obj=None):
        return True
        # if (self.is_admin):
        #     return True
        # else:
        #     return False

    def has_perms(self, perm, obj=None):
        return True

    def get_full_name(self):
        return self.full_name

    # checking simple permission to view app
    def has_module_perms(self, app_label):
        return True
