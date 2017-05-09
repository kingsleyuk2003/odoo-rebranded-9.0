# -*- coding: utf-8 -*-

from openerp import api, fields, models

class stock_picking_return_wizard(models.TransientModel):
    _name = 'stock.picking.return.wizard'
    _description = 'Stock Picking Return Wizard'

    @api.multi
    def action_wizard_return_notice(self):
        picking_ids = self.env.context['active_ids']
        msg = self.msg
        pickings = self.env['stock.picking'].browse(picking_ids)
        for pick in pickings :
            pick.action_return_notice(msg)
        return

    msg = fields.Text(string='Reason for Return', required=True)
