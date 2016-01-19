# -*- coding: utf-8 -*-
# © 2016 Dynapps nv, Onderdelenwinkel B.V.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from openerp import fields, models


class ResCompany(models.Model):
    _inherit = 'res.company'

    company_registry = fields.Char(
        related='partner_id.company_registry', store=True)
