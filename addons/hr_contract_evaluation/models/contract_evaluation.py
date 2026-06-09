from odoo import models, fields, api

SCORE_SELECTION = [
    ('1', '⭐ 1 - Kém'),
    ('2', '⭐⭐ 2 - Yếu'),
    ('3', '⭐⭐⭐ 3 - Trung bình'),
    ('4', '⭐⭐⭐⭐ 4 - Khá'),
    ('5', '⭐⭐⭐⭐⭐ 5 - Xuất sắc'),
]


class HrContractEvaluation(models.Model):
    _name = 'hr.contract.evaluation'
    _description = 'Đánh giá hợp đồng nhân viên'

    name = fields.Char(
        string='Mã phiếu đánh giá',
        required=True,
        copy=False,
        default=lambda self: self.env['ir.sequence'].next_by_code('hr.contract.evaluation') or 'New',
    )
    employee_id = fields.Many2one(
        comodel_name='hr.employee',
        string='Nhân viên',
        required=True,
        ondelete='restrict',
    )
    contract_id = fields.Many2one(
        comodel_name='hr.contract',
        string='Hợp đồng',
        required=True,
        ondelete='restrict',
        domain="[('employee_id', '=', employee_id)]",
    )
    evaluation_date = fields.Date(
        string='Ngày đánh giá',
        required=True,
        default=fields.Date.today,
    )
    score_work = fields.Selection(
        selection=SCORE_SELECTION,
        string='Điểm hiệu suất công việc',
        required=True,
    )
    score_attitude = fields.Selection(
        selection=SCORE_SELECTION,
        string='Điểm thái độ',
        required=True,
    )
    final_recommendation = fields.Selection(
        selection=[
            ('renew', 'Gia hạn'),
            ('probation', 'Thử thách thêm'),
            ('terminate', 'Chấm dứt hợp đồng'),
        ],
        string='Kiến nghị cuối cùng',
        required=True,
    )
    note = fields.Text(string='Nhận xét chi tiết')
