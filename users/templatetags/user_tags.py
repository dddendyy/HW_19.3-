# import string
# import random
#
# from django import template
# from django.contrib.auth.hashers import make_password
#
# from users.models import User
#
# register = template.Library()
#
#
# def generate_password():
#     """Генерация рандомного пароля"""
#     characters = string.ascii_letters + string.digits + string.punctuation
#     list_of_characters = ('_'.join(characters).split('_'))
#     random.shuffle(list_of_characters)
#     generated_password = ''.join([character for character in list_of_characters[:random.randint(8, 14)]])
#     return generated_password
#
#
# @register.simple_tag
# def get_random_password():
#     new_password = generate_password()
#     new_hashed_password = make_password(new_password)
#     return new_hashed_password
