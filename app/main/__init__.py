from flask import Blueprint

# 创建主蓝本
main = Blueprint('main', __name__)
from . import views, errors
