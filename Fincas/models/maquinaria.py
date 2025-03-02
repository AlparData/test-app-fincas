from odoo import models, fields

class FincaProductoAplicado(models.Model):
    _name = 'finca.producto.aplicado'
    _description = 'Productos Aplicados en la Orden'
    
    orden_id = fields.Many2one('finca.orden.trabajo', string='Orden de Trabajo', required=True, ondelete='cascade')
    producto_id = fields.Many2one('product.product', string='Producto', required=True)
    cantidad = fields.Float(string='Cantidad', required=True)
    unidad_medida = fields.Many2one('uom.uom', string='Unidad de Medida', required=True)