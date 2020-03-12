

from flask import  Blueprint
# 1). 创建蓝图
auth = Blueprint('auth', __name__)


# 注意： 导入包的实质是执行包里面的__init__.py文件
from . import  views