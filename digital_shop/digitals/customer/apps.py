import oscar.apps.customer.apps as apps


class CustomerConfig(apps.CustomerConfig):
    label = 'customer'
    name = 'digitals.customer'
    verbose_name = 'Customer'
