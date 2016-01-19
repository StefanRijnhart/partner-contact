# -*- coding: utf-8 -*-
# © 2016 Dynapps nv, Onderdelenwinkel B.V.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from openerp import api, fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    @api.model
    def _commercial_fields(self):
        return ['company_registry'] + super(
            ResPartner, self)._commercial_fields()

    company_registry = fields.Char()
