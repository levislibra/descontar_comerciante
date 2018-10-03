# -*- coding: utf-8 -*-

from openerp import models, fields, api
from datetime import datetime, timedelta
from dateutil import relativedelta
from openerp.exceptions import UserError, ValidationError
import time
# import numpy as np
# import math

# class DescontarComerciante(models.Model):
# 	_name = 'descontar.comerciante'


class Liquidacion(models.Model):
	_name = 'descontar.liquidacion'

	_order = 'id desc'
	id = fields.Integer('Nro Liquidacion')
	fecha_liquidacion = fields.Date('Fecha', default=lambda *a: time.strftime('%Y-%m-%d'))
	fecha_efectivo = fields.Date('Fecha que necesita el efectivo', default=lambda *a: time.strftime('%Y-%m-%d'))
	active = fields.Boolean('Activa', default=True)
	current_user_id = fields.Many2one('res.users','Current User', default=lambda self: self.env.user)
	cheque_ids = fields.One2many('descontar.liquidacion.cheque', 'liquidacion_id', 'Cheques')
	total = fields.Float('Importe', digits=(16, 2), compute='_compute_total')
	state = fields.Selection([('borrador', 'Borrador'), ('enviada', 'Enviada'), ('evaluacion', 'Evaluacion'), ('presupuesto', 'Presupuesto'), ('confirmada', 'Confirmada'), ('cancelada', 'Cancelada')], string='Estado', default='borrador')

	@api.one
	def _compute_total(self):
		total = 0
		for cheque_id in self.cheque_ids:
			total += cheque_id.importe
		self.total = total

	@api.one
	def cancelar(self):
		self.state = 'cancelada'

	@api.one
	def enviar(self):
		self.state = 'enviada'

	@api.one
	def evaluacion(self):
		self.state = 'evaluacion'

	@api.one
	def presupuesto(self):
		self.state = 'presupuesto'

	@api.one
	def confirmar(self):
		self.state = 'confirmada'

class Cheque(models.Model):
	_name = 'descontar.liquidacion.cheque'

	liquidacion_id = fields.Many2one('descontar.liquidacion', "Liquidacion")
	frente = fields.Binary('Imagen frontal')
	dorso = fields.Binary('Imagen dorso')
	importe = fields.Float('Importe', digits=(16, 2))