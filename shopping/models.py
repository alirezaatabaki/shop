from django.db import models
from django.urls import reverse


class Category(models.Model):
    sub_category = models.ForeignKey('self', verbose_name='زیرشاخه‌ها', on_delete=models.CASCADE,
                                     related_name='subcategory', null=True, blank=True)
    is_sub = models.BooleanField(verbose_name='زیرشاخه', default=False)
    name = models.CharField(verbose_name='نام', max_length=200)
    slug = models.SlugField(verbose_name='اسلاگ', max_length=200, unique=True, allow_unicode=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'دسته‌بندی'
        verbose_name_plural = 'دسته‌بندی‌ها'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shopping:category_filter', args=[self.slug, ])


class Product(models.Model):
    category = models.ManyToManyField(Category, related_name='products', verbose_name='دسته‌بندی',)
    # category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE, verbose_name='دسته‌بندی')
    name = models.CharField(verbose_name='نام', max_length=200)
    slug = models.SlugField(verbose_name='اسلاگ', max_length=200, unique=True, allow_unicode=True)
    image = models.ImageField(verbose_name='تصویر', upload_to='products/%Y/%m/%d/')
    description = models.TextField(verbose_name='توضیحات')
    price = models.IntegerField(verbose_name='قیمت')
    available = models.BooleanField(verbose_name='موجود', default=True)
    created = models.DateTimeField(verbose_name='تاریخ اضافه شدن', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='آخرین تغییر', auto_now=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'کالا'
        verbose_name_plural = 'کالاها'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shopping:product_detail', args=[self.slug, ])
