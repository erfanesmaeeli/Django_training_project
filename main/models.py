from django.db import models
from django.contrib.auth.models import User
from django_jalali.db import models as jmodels


STATE_TYPES = (
    ('P', 'در حال انتظار'),
    ('A', 'مورد قبول'),
    ('R', 'عدم تایید')
)


class Blog(models.Model):
    title = models.CharField(max_length=120, null=True, unique=False, verbose_name="عنوان")
    author = models.ForeignKey(User, related_name='blogs', on_delete=models.CASCADE, null=True, verbose_name="نویسنده")
    description = models.TextField(verbose_name="توضیحات")
    price = models.IntegerField(default=0, null=True, verbose_name="قیمت")
    state = models.CharField(max_length=1, choices=STATE_TYPES, default='P', null=True, verbose_name="وضعیت")
    DateCreated = jmodels.jDateTimeField(null=True, verbose_name="زمان ایجاد")
    file = models.FileField(null=True, blank=True, upload_to='blog/files/', verbose_name="فایل")
    image = models.ImageField(null=True, blank=True, upload_to='blog/images/', verbose_name="عکس")

    def __str__(self):
        return str(self.id)
    
    class Meta:
        verbose_name = "بلاگ"
        verbose_name_plural = "بلاگ‌ها"
        ordering = ('title', '-price')


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="comments")
    content = models.TextField()

    def __str__(self):
        return self.user.get_full_name()

    class Meta:
        verbose_name = "کامنت"
        verbose_name_plural = "کامنت‌ها"



