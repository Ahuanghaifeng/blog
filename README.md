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
https://github.com/Ahuanghaifeng/blog/raw/master/K%604%7DAMGGI%25SZRB8%5DJ%60DE37M.png
浏览器输入loaclhost:8000执行效果如图
https://github.com/Ahuanghaifeng/blog/blob/master/%7B(2%60OE_H7%7BVVQFRNU%40G((6O.png
