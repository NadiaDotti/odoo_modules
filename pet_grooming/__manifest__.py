{
    'name': 'Pet Grooming',
    'version': '1.0',
    'summary': 'Animal grooming management.',
    'depends': [
        'base', 
        'contacts',
        'calendar',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/pet_views.xml',
        # 'views/pet_breed_views.xml',
        'views/pet_type_views.xml',
        'views/res_config_settings_views.xml',
    ],
    'installable': True,
    'application': True,
}
