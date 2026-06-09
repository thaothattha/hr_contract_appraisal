{
    'name': 'HR Contract Evaluation',
    'version': '16.0.1.1.0',
    'summary': 'Đánh giá hợp đồng nhân viên mới nhất',
    'description': 'Module quản lý và đánh giá hợp đồng nhân viên định kỳ.',
    'author': 'Your Company',
    'category': 'Human Resources',
    'depends': ['hr_contract'],
    'data': [
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'views/contract_evaluation_views.xml',
        'views/menu.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
