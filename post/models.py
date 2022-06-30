from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from django.utils.text import slugify



