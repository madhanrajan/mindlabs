import oscar.apps.catalogue.apps as apps


class CatalogueConfig(apps.CatalogueConfig):
    label = 'catalogue'
    name = 'digitals.catalogue'
    verbose_name = 'Catalogue'
