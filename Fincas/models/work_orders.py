from odoo import models, fields

class FincaOrdenTrabajo(models.Model):
    _name = 'finca.orden.trabajo'
    _description = 'Orden de Trabajo de Finca'
    
    name = fields.Char(string='Referencia', required=True, copy=False, default=lambda self: self.env['ir.sequence'].next_by_code('finca.orden.trabajo'))
    fecha = fields.Date(string='Fecha', required=True, default=fields.Date.context_today)
    responsable_id = fields.Many2one('res.users', string='Responsable', required=True)
    implementos_ids = fields.Many2many('product.product', string='Implementos')
    productos_aplicados_ids = fields.One2many('finca.producto.aplicado', 'orden_id', string='Productos Aplicados')
    parcela_id = fields.Many2one('finca.parcela', string='Parcela')
    state = fields.Selection([
        ('borrador', 'Borrador'),
        ('progreso', 'En Progreso'),
        ('finalizado', 'Finalizado')
    ], string='Estado', default='borrador', tracking=True)