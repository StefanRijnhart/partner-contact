# -*- coding: utf-8 -*-
# © 2016 Dynapps, Onderdelenwinkel B.V.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).


def pre_init_hook(cr):
    from openupgradelib.openupgrade import rename_columns
    rename_columns(cr, {'res_company': [('company_registry', None)]})


def post_init_hook(cr, pool):
    """ Migrate the company's registry number to the related partner
    as the partner field now masks the company field """
    from openupgradelib.openupgrade import get_legacy_name, drop_columns
    legacy_name = get_legacy_name('company_registry')
    cr.execute(
        """
        UPDATE res_company SET company_registry = %(company_registry)s;
        UPDATE res_partner rp
        SET company_registry = rc.%(company_registry)s
        FROM res_company rc
        WHERE rc.partner_id = rp.id
        """ % {'company_registry': legacy_name})
    drop_columns(cr, [('res_company', legacy_name)])
