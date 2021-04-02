from django.db import models
from django.contrib.auth.models import User


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

    def __str__(self):
        return str(self.id)
    
    class Meta:
        verbose_name = "بلاگ"
        verbose_name_plural = "بلاگ‌ها"




