# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class proyecto_odoo_alumno(models.Model):
    _name = "proyecto_odoo.alumno"

    name = fields.Char(string = "Nombre", required = True, help = "Introduce el nombre del alumno")
    apellidos = fields.Char(string = "Apellidos", required = True, help = "Introduce los apellidos del alumno")
    fecha_nac = fields.Date(string = "Fecha de nacimiento", required = True, help = "Introduce la fecha de nacimiento del alumno")
    ciclo = fields.Selection([('0', 'DAM'), ('1', 'DAW'), ('2', 'ASI')], string = "Ciclo formativo", default = "0", help = "Selecciona el ciclo formativo al que pertenece el alumno")
    
    @api.constrains("nota_media")
    def checkNotaMedia(self):
        for inp in self:
            if inp.nota_media < 0:
                raise ValidationError("La nota de un alumno no puede ser negativa.")
            elif inp.nota_media > 10:
                raise ValidationError("La nota de un alumno no puede ser superior a 10.")
    nota_media = fields.Integer(string = "Nota media", help = "Introduce la nota media del alumno")
    nota_media_txt = fields.Char(string = "Nota", compute = "conseguirNotaMedia")
    empresa = fields.Many2one('proyecto_odoo.empresa', string = "Empresa")
    
    @api.depends("nota_media")
    def conseguirNotaMedia(self):
        resultado = ""
        
        try: 
            if self.nota_media < 5:
                resultado = "No apto"
            elif self.nota_media < 7:
                resultado = "Aprobado"
            elif self.nota_media < 9:
                resultado = "Notable"
            elif self.nota_media <= 10:
                resultado = "Sobresaliente"
        except:
            resultado = "Nota media no introducida"

        self.nota_media_txt = resultado

class proyecto_odoo_empresa(models.Model):
    _name = "proyecto_odoo.empresa"

    name = fields.Char(string = "Nombre", required = True, help = "Introduce el nombre de la empresa")
    direccion = fields.Char(string = "Direccion", help = "Introduce la dirección de la empresa")
    alumnos = fields.Many2many('proyecto_odoo.alumno', string = "Lista de alumnos que han hecho la práctica en esta empresa")