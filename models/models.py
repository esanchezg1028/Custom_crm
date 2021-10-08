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















