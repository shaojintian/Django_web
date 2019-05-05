from django.db import models

from django.template.defaultfilters import  slugify
#只有当model层改变的时候，才需要makemigrations

class Category(models.Model):

    name = models.CharField(max_length=128,unique=True)
    views =models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField()

    #这个意思就是并不知道原来父类的传入参数是什么，override不能修改传入参数列表，（*agrs,**kwargs）标明传入的所有可能性
    #动态改变需要save
    def save(self,*agrs,**kwargs):
        self.slug = slugify(self.name)
        super().save(*agrs,**kwargs)


    def __str__(self):
        return  self.name


class Page(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    title = models.CharField(max_length=128)

    url = models.URLField()

    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title



