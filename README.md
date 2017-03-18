# blog
基于Python和Django的blog项目
注意创建templates后再创建一个项目名字的目录以免多个项目templates起冲突
Models是ORM 数据对象映射
首先是创建模型，创建一个类，继承自models.Model，然后就是各个字段进行限制；
映射数据表，制作数据迁移python manage.py makemigrations app（应用名可选，不选则全部创建）
迁移动作python manage.py migrate
查看生成的数据表执行语句 python manage.py sqlmigrate 应用名 文件ID
在views.py 获取对象通过render返回，前端可以直接使用对象及对象（.）方法进行操作。
如图所示
![](https://github.com/Ahuanghaifeng/blog/raw/master/K%604%7DAMGGI%25SZRB8%5DJ%60DE37M.png)
浏览器输入loaclhost:8000执行效果如图</br>
![](https://github.com/Ahuanghaifeng/blog/raw/master/%7B(2%60OE_H7%7BVVQFRNU%40G((6O.png)

Admin是Django自带的管理界面，已在settings.py中自动生成。
创建用户 python manage.py createsuperuser ，然后设置用户名和密码。
管理员界面英文修改为中文，默认为‘en-us' 修改为‘zh-Hans’或者'zh-Hant'(繁体)。
想要操作应用，先将应用进行配置，在应用目录下的admin.py中引入自身的models模块，并将导入的模块进行注册admin.site.register(模块)。
针对admin界面的 Article object，可通过增加一个方法返回self.title。python3中用__str__(self),python2中用__unicode__(self)


之前获取单独的一个数据的语法
article = models.Article.objects.get(pk=1)
获取全部的数据 article = models.Article.objects.all()
模板的For循环
{%for xx in xx%}
HTML语句
{%endfor%}


模型：是以创建的Models,其中包含一个自动生成的ID
视觉：根据表的ID进行获取数据，article = models.Article.object.get(pk=article_id)，并通过render函数将数据返回，html中再通article.title和article.content进行显示。
控制：urls.py通过正则表达进行限制r'^article/(?P<article_id>[0-9]+)'.P大写，0-9中间不是逗号。

注册Admin配置类：
class ArticleAdmin(admin.ModelAdmin)
注册：admin.site.register(models.Article,ArticleAdmin)
显示其他字段
list_diplay = ('title','content')   （就是models里的字段名）具体看代码
然后在进行数据移植，就可以显示了。效果见csdn博客http://blog.csdn.net/u013692888/article/details/61416403
