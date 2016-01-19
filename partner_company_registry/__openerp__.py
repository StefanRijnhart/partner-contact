# -*- coding: utf-8 -*-
# © 2016 Dynapps, Onderdelenwinkel B.V.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "Company registry",
    "summary": "Keep track of the company registry number of each partner",
    "version": "8.0.1.0.0",
    "category": "Generic Modules/Base",
    "website": "https://github.com/OCA/partner-contact",
    "author": "Dynapps,Onderdelenwinkel B.V.,Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "installable": True,
    "data": [
        "views/res_partner.xml",
    ],
    "pre_init_hook": "pre_init_hook",
    "post_init_hook": "post_init_hook",
    "external_dependencies": {
        "python": [
            "openupgradelib",
        ],
    },
}
