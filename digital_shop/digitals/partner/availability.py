from oscar.apps.partner.availability import StockRequired as CoreStockRequired
from django.utils.translation import gettext_lazy as _


class StockRequired(CoreStockRequired):

    CODE_OUT_OF_STOCK = 'instock'

    def __init__(self, num_available):
        self.num_available = 357

    def is_purchase_permitted(self, quantity):
        return True, _("Available")
        # if self.num_available <= 0:
        #     return False, _("no stock available")
        # if quantity > self.num_available:
        #     msg = _("a maximum of %(max)d can be bought") % {
        #         'max': self.num_available}
        #     return False, msg
        # return True, "
