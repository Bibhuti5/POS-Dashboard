from odoo import models, fields, api
from odoo.osv import expression


class DashboardMenu(models.Model):
    _name = "dashboard.menu"
    _description = "Dashboard Menu"
    _rec_name = "name"

    name = fields.Char(string="Name")
    menu_id = fields.Many2one('ir.ui.menu', string="Menu")
    group_ids = fields.Many2many('res.groups', string='Groups',
                                 related='menu_id.groups_id',
                                 help="User need to be at least in one of these groups to see the menu")
    client_action = fields.Many2one('ir.actions.client')

    @api.model
    def create(self, vals):
        """This code is to create menu"""
        values = {
            'name': vals['name'],
            'tag': 'dynamic_dashboard',
        }
        action_id = self.env['ir.actions.client'].create(values)
        vals['client_action'] = action_id.id
        menu_id = self.env['ir.ui.menu'].create({
            'name': vals['name'],
            'parent_id': vals['menu_id'],
            'action': 'ir.actions.client,%d' % (action_id.id,)
        })
        return super(DashboardMenu, self).create(vals)
