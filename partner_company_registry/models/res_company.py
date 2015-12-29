# -*- coding: utf-8 -*-
from openerp import fields, models


class ResCompany(models.Model):
    _inherit = 'res.company'

    company_registry = fields.Char(
        related='partner_id.company_registry', store=True)
