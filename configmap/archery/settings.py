# -*- coding: UTF-8 -*-
# 在这里写配置可以覆盖 archery/settings.py 内的配置

# https://archerydms.com/installation/manual/#_7
# 修改SECRET_KEY
SECRET_KEY = 'hfusaf2m4ot#7)fkw#di2bu6(cv0@opwmafx5n#6=3d%x^hpl6'
# 关闭debug模式
DEBUG = True
# 设置ALLOWED_HOSTS，建议限制内网访问
ALLOWED_HOSTS = [
    '*'
]
# 请求大小限制，如果提交SQL语句过大可以修改该值
DATA_UPLOAD_MAX_MEMORY_SIZE = 15728640
# 密码校验，用户注册和添加密码校验规则
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 9,
        }
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# https://archerydms.com/installation/manual/#mysql
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'archerydms', # 数据库名称
        'USER': 'archerydms', # 数据库用户
        'PASSWORD': '123456', # 数据库密码
        'HOST': 'localhost', # 数据库HOST，如果是docker启动并且关联，可以使用容器名连接
        'PORT': '3306',  # 数据库端口
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'", # SQL_MODE，为了兼容select * group by，可以按需调整
            'charset': 'utf8mb4'
        },
        'TEST': {
            'NAME': 'test_archery',
            'CHARSET': 'utf8mb4',
        },
    }
}

# https://archerydms.com/installation/manual/#_8
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://localhost:6379/188",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "PASSWORD": "123456"

        }
    }
}
