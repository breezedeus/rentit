# RentIt

---
published: true
layout: post
title:  "Python Web开发框架：Django"
date:   2015-05-18 22:25
categories: python web开发框架 Django
---

**Django**，**Tornado**和**Flask**是Python里比较著名的三个Web开发框架，本文我主要介绍Django里最重要的一些基本概念。






下面我介绍使用Django v1.8版本[^django1_8]来开发一个租借平台**rentit**（注册用户可以发布出租东西的消息，想借此东西的人可以申请求借）。Django1.8兼容Python 2.7, 3.2, 3.3, 3.4。

# 准备工作

## 运行环境

* Mac OS 10.10.2；
* Python 2.7；
* Django1.8；
* SQLite3；Python2.7默认会安装sqlite3包。

## 安装
在有**pip**的Linux/Mac下，安装Django很容易，只要下面一个命令就行：

```
$ pip install django
```


# 项目

## 创建新项目**rentit**

Django有个叫**django-admin**的工具来帮助创建初始的项目。

```
$ django-admin startproject rentit
```

上面的命令会在当前目录下创建项目目录rentit，rentit里也已经生成了初步的文件和文件夹：

<pre>
$ tree rentit/
rentit/
├── manage.py
└── rentit
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py
</pre>

其中`rentit/settings.py`中包含了rentit项目的各种参数设置。

## 创建系统应用（apps）所需要的数据表

<pre>
$ cd rentit
$ python manage.py migrate
</pre>

涉及到的系统应用是在`settings.py`中的`INSTALLED_APPS`指定的。

## 开启服务器

```
$ python manage.py runserver 127.0.0.1:8000
```

这会开启Django自带的轻量级的开发服务器。

> 此服务器仅用于系统开发时使用，不适用于生成环境！

访问浏览器的话，可以看到：

![It worked!][worked]



# 创建应用**rentout**

```
$ python manage.py startapp rentout
```

新的代码结构如下：

<pre>
$ tree .
.
├── db.sqlite3
├── manage.py
├── rentit
│   ├── __init__.py
│   ├── __init__.pyc
│   ├── settings.py
│   ├── settings.pyc
│   ├── urls.py
│   ├── urls.pyc
│   ├── wsgi.py
│   └── wsgi.pyc
└── rentout
    ├── __init__.py
    ├── admin.py
    ├── migrations
    │   └── __init__.py
    ├── models.py
    ├── tests.py
    └── views.py
</pre>

通过rentout，用户可以发布出租东西的消息，想借此东西的人可以申请求借。

### 创建模型（Models）

编辑文件`rentout/models.py`：
[TODO]

### 修改配置文件

然后，在`settings.py`的`INSTALLED_APPS`中加入对应的应用名称。

### 创建对表的变化指令

<pre>
$ python manage.py makemigrations rentout
Migrations for 'rentout':
  0001_initial.py:
    - Create model Item
    - Create model OutOrder
</pre>

### 查看表变化指令对应的建表命令
<pre>
$ python manage.py sqlmigrate rentout 0001
</pre>

其中最后一个参数是创建表变化指令结果中对应的编号。

> 这一步只是为了保险起见，不是必须的。

如果发现模型要做调整，只要修改`rentout/models.py`文件后再运行上面两个命令就可以。

### 真正实施对表的变化操作

确认没问题后，跟前面介绍的一样，只要运行下面的命令真正创建新的数据表：

```
$ python manage.py migrate
```









[worked]: /images/django_worked.png "It worked!"


#References

[^django1_8]: [Django v1.8 Documentation](https://docs.djangoproject.com/en/1.8/contents/).