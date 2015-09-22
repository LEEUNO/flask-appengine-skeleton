from flask import Blueprint

models = Blueprint('models', __name__)

from . import schema

# Nothing Here
# BUT DON'T DELETE THIS FILE.

# functions in this folder can be accessed by either one of followings.

# 1
# from app.models import model_name
# model_name.model_function(parameters)

# 2
# from app.models.model_name import *
# model_function(parameters)