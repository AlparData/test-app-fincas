from odoo import models, fields

class FincaParcela(models.Model):
    _name = 'finca.parcela'
    _description = 'Parcelas de la Finca'
    
    name = fields.Char(string='Nombre de la Parcela', required=True)
    descripcion = fields.Text(string='Descripción')