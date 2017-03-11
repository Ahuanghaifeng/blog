from __future__ import unicode_literals
from django.db import models


class Article(models.Model):
    # 博客标题定义为字符串，最大长度为32默认值是title
    title = models.CharField(max_length=32, default='Title')
    # 定义blog的内容，内容可以为空
    content = models.TextField(null=True)
    pub_time = models.DateTimeField(null=True)

    def __str__(self):
        return self.title
