import oscar.apps.dashboard.catalogue.apps as apps


class CatalogueDashboardConfig(apps.CatalogueDashboardConfig):
    label = 'catalogue_dashboard'
    name = 'digitals.dashboard.catalogue'
    verbose_name = 'Catalogue'
