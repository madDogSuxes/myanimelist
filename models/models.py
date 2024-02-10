# -*- coding: utf-8 -*-

from odoo import models, fields, api

class myanimelist_demografia(models.Model):
    _name="myanimelist.demografia"

    name=fields.Char(string="Demografía",required=True,help="Indicamos la demografía de la obra que estamos viendo/leyendo")
    descripcion=fields.Text(string="Descripción de la demografía")

class myanimelist_anime(models.Model):
    _name="myanimelist.anime"

    name=fields.Char(string="Título",required=True)
    synopsis=fields.Char(string="Una breve sinopsis del anime")
    score=fields.Selection([('0','Select'),('1','Appaling'),('2','Horrible'),('3','Very bad'),('4','Bad'),('5','Average')
                             ,('6','Fine'),('7','Good'),('8','Very good'),('9','Great'),('10','Masterpiece')],
                             string="Puntuación",default="0")
    status=fields.Selection([('0','Select'),('1','Watching/Reading'),('2','Completed'),('3','Plan to watch'),('4','Dropped')],
                            string="Estado",default="0")
    chapters=fields.Integer(string="Capítulos")
    release_date=fields.Char(string="Fecha de estreno")
    started_watching=fields.Date(string="Fecha en la que empezó a verlo")
    finished_watching=fields.Date(string="Fecha en la que terminó de verlo")
    demografia=fields.Many2one("myanimelist.demografia",string="Demografia")
    image=fields.Binary()

    mean_score=fields.Float(string="Media de puntuación", compute="_calculated_mean_score", store=True)

    @api.depends('score')
    def _calculated_mean_score(self):
        for record in self:
            numeric_score={
                '1':1, '2':2, '3':3, '4':4, '5': 5, '6': 6, 
                '7': 7, '8': 8, '9': 9, '10': 10
            }
            scores=[score for score in record.score.split(',') if score != 0]
            total_score = sum(numeric_score.get(score, 0) for score in scores)
            record.mean_score=total_score/len(scores) if scores else 0

class myanimelist_mangaShop(models.Model):
    _name="myanimelist.mangashop"

    name=fields.Char(string="Título",required=True)
    author=fields.Char()
    synopsis=fields.Char(string="Una breve sinopsis del manga")
    chapters=fields.Integer(string="Capítulos")
    volumes=fields.Integer(string="Volúmenes de la obra")
    unit_price=fields.Float()
    units=fields.Integer()
    amount=fields.Float(compute="_calculateAmount",store=True)
    demografia=fields.Many2one("myanimelist.demografia",string="Demografia")
    image=fields.Binary()

    @api.depends('unit_price', 'units')
    def _calculateAmount(self):
         for record in self:
             record.amount = float(record.units) * record.unit_price
    
            



# class myanimelist(models.Model):
#     _name = 'myanimelist.myanimelist'
#     _description = 'myanimelist.myanimelist'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
