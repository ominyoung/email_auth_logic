from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import Thumbnail
from pilkit.processors import ResizeToFill


class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None):

        if not email:
            raise ValueError('사용자 아이디를 입력해주세요.')

        user = self.model(
            email=email,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(
            email=email,
            password=password,
        )
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser, PermissionsMixin):

    MyUser_ROLL_LABEL=[
        ('HQ', '본사'),
        ('SITE', '현장'),
        ('BO', '건축주'),
        ('NONE', '미등록')
    ]

    email = models.EmailField(verbose_name='회사 이메일 혹은 이메일', max_length=50, unique=True)
    name = models.CharField(verbose_name='회사 이름 혹은 이름', max_length=30)
    is_active = models.BooleanField(verbose_name='로그인 가능', default=True)
    profile = models.ImageField(verbose_name='프로필 사진', upload_to='profile/', blank=True, null=True)
    profile_thumbnail = ImageSpecField(source='profile',
                                        processors=[Thumbnail(100, 100)],
                                        format='JPEG',
                                        options={'quality': 60})
    profile_website = ImageSpecField(source='profile',
                                    format='JPEG',
                                    options={'quality': 60})

    is_superuser = models.BooleanField(verbose_name='최고관리자', default=False)
    is_staff = models.BooleanField(verbose_name='관리자페이지 접근', default=False)
    position = models.CharField(verbose_name='직책', max_length=30, choices=MyUser_ROLL_LABEL, default='NONE')
    last_login = models.DateTimeField(verbose_name='로그인 일시', blank=True, null=True)
    created = models.DateTimeField(verbose_name='등록 일시', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='수정 일시', auto_now=True)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'

    class Meta:
        verbose_name_plural = '사용자'

    def __str__(self):
        return f'{self.email}'

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True