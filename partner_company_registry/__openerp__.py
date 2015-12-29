{
    'name': 'Company registry on Partners',
    'data': [
        'views/res_partner.xml',
    ],
    'pre_init_hook': 'pre_init_hook',
    'post_init_hook': 'post_init_hook',
    'external_dependencies': {
        'python': [
            'openupgradelib',
        ]},
}
