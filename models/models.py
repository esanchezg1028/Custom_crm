import datetime

from odoo import models, fields, api


class visit(models.Model):
    _name = 'custom_crm.visit'
    _description = 'visit'

    name = fields.Char(string='Descripción')
    customer = fields.Many2one(string='Cliente', comodel_name='res.partner')
    date = fields.Datetime(string='Fecha')
    type = fields.Selection([('P', 'Presencial'), ('W', 'WhatsApp'), ('T', 'Telefónico')], string='Tipo', required=True)
    done = fields.Boolean(string='Realizada', readonly=True)
    image = fields.Binary(string= 'Imagen')



    def toggle_state(self):
        self.done = not self.done

    def f_create(self):
        visit = {
            'name': 'ORM test',
            'customer': 1,
            'date': str(datetime.datetime(2021, 8, 6)),
            'type': 'P',
            'done': False
        }
        print(visit)
        self.env['custom_crm.visit'].create(visit)

    def f_search_update(self):
        visit = self.env['custom_crm.visit'].search([('name', '=', 'ORM test')])
        print('search()', visit, visit.name)

        visit_b = self.env['custom_crm.visit'].browse([4])
        print('browse()', visit_b, visit_b.name)

        visit.write({
            'name': 'ORM test write'
        })

    def f_delete(self):
        visit = self.env['custom_crm.visit'].browse([3])
        visit.unlink()


class VisitReport(models.AbstractModel):
    _name = 'report.custom_crm.report_visit_card'

    @api.model
    def _get_report_values(self, docids, data=None):
        report_obj = self.env['ir.actions.report']
        report = report_obj._get_report_from_name('custom_crm.report_visit_card')
        return {
            'doc_ids': docids,
            'doc_model': self.env['custom_crm.visit'],
            'docs': self.env['custom_crm.visit'].browse(docids)
        }














