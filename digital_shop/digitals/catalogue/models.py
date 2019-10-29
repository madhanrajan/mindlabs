from django.db import models
from oscar.apps.catalogue.abstract_models import AbstractProduct



class Product(AbstractProduct):
    file = models.FileField(upload_to='files/%Y/%m/%d')

    def get_product_url(self):
        return self.file.url

from oscar.apps.catalogue.models import *  # noqa isort:skip
