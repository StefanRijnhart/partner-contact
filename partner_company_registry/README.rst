.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

=========================================================
Keep track of the company registry number of each partner
=========================================================

This module adds a company registry field on the *partner* level (in standard
Odoo, this field only exist on the *company* level).

This field is integrates with this existing field on the company level, so
that the company registry number is guaranteed to be the same between the
company itself and the related partner.

Usage
=====

After installation of this module, you can enter your customers' and suppliers'
company registry numbers on the Sales & Purchases tab. The field is marked as a
*commercial field*, which means that it is synchronized between a partner that
is a company and its contacts. To emphasize this, the field is only visible on
the so called *commercial partner*.

This module also allows you to display the field wherever addresses are
rendered using the contact widget (e.g. on report headers, or on the contact
page of your odoo website). to do so, add *company_registry* to the *fields*
parameter of the widget options in the template where it is called:

.. code:: xml
        
    <div t-field="res_company.partner_id" t-field-options='{
        "widget": "contact",
        "fields": ["name", "address", "phone", "mobile", "fax", "email", "company_registry"]}'
    />

.. image:: https://odoo-community.org/website/image/ir.attachment/5784_f2813bd/datas
   :alt: Try me on Runbot
   :target: https://runbot.odoo-community.org/runbot/134/8.0

Bug Tracker
===========

Bugs are tracked on `GitHub Issues
<https://github.com/OCA/partner-contact/issues>`_. In case of trouble, please
check there if your issue has already been reported. If you spotted it first,
help us smashing it by providing a detailed and welcomed `feedback
<https://github.com/OCA/
partner-contact/issues/new?body=module:%20
partner_company_registry%0Aversion:%20
8.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**>`_.

Credits
=======

Images
------

* Odoo Community Association: `Icon <https://github.com/OCA/maintainer-tools/blob/master/template/module/static/description/icon.svg>`_.

Contributors
------------

* Stefan Rijnhart <stefan@opener.amsterdam>

Maintainer
----------

.. image:: https://odoo-community.org/logo.png
   :alt: Odoo Community Association
   :target: https://odoo-community.org

This module is maintained by the OCA.

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

To contribute to this module, please visit https://odoo-community.org.
