import os

# 获取当前项目的绝对路径;
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    """
    所有配置环境的基类, 包含通用配置
    """
    # 尤其是涉及(flask-wtf)登录注册里面提交敏感信息时，一定要加
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'westos secret key'
    # flask-sqlchemy
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    PER_PAGE = 5


    FLASKY_MAIL_SUBJECT_PREFIX = '[TodoList]'
    FLASKY_MAIL_SENDER = '1104213995@qq.com'


class DevelopmentConfig(Config):
    """
   开发环境的配置信息
   """
    # 启用了调试支持,服务器会在代码修改后自动重新载入,并在发生错误时提供一个相当有用的调试器。
    DEBUG = True
    # MAIL_SERVER = 'smtp.qq.com'
    MAIL_SERVER = 'smtp.163.com'
    # MAIL_PORT = 587/465
    MAIL_PORT = 25
    # MAIL_USE_SSL = True   # 163邮箱不能打开这个参数
    MAIL_USERNAME =  '13679127704@163.com'
    MAIL_PASSWORD =  '13279443585lh'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')


class TestingConfig(Config):
    """
   测试环境的配置信息
   """
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')


class ProductionConfig(Config):
    """
   生产环境的配置信息
   """
    #生产环境是False
    DEBUG = False
    # MAIL_SERVER = 'smtp.qq.com'
    MAIL_SERVER = 'smtp.163.com'
    # MAIL_PORT = 587/465
    MAIL_PORT = 25
    # MAIL_USE_SSL = True   # 163邮箱不能打开这个参数
    MAIL_USERNAME = '13679127704@163.com'
    MAIL_PASSWORD = '13279443585lh'
    #'mysql://用户名：密码@主机/数据库名'
    SQLALCHEMY_DATABASE_URI = 'mysql://flask:123lh@47.105.62.144/todolist'


config = {
   'development': DevelopmentConfig,
   'testing': TestingConfig,
   'production': ProductionConfig,
   'default': DevelopmentConfig
}

