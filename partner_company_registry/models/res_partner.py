# -*- coding: utf-8 -*-
from openerp import api, fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    @api.model
    def _commercial_fields(self):
        return ['company_registry'] + super(
            ResPartner, self)._commercial_fields()

    company_registry = fields.Char()
