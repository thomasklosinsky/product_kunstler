# -*- encoding: utf-8 -*-
###############################################################################
#                                                                             #
# product_kunstler for Odoo                                                   #
# Copyright (C) 2015 Designcomplex                                            #
# Contributors                                                                #
# Thomas Klosinsky, thomas@designcomplex.de                                   #
#                                                                             #
# This program is free software: you can redistribute it and/or modify        #
# it under the terms of the GNU Affero General Public License as              #
# published by the Free Software Foundation, either version 3 of the          #
# License, or (at your option) any later version.                             #
#                                                                             #
# This program is distributed in the hope that it will be useful,             #
# but WITHOUT ANY WARRANTY; without even the implied warranty of              #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the                #
# GNU Affero General Public License for more details.                         #
#                                                                             #
# You should have received a copy of the GNU Affero General Public License    #
# along with this program. If not, see <http://www.gnu.org/licenses/>.        #
#                                                                             #
###############################################################################
###############################################################################
# Product Kunstler is an Openobject module wich enable KŸnstler management for#
# products                                                                    #
###############################################################################
from openerp import models, fields, api


class ProductKunstler(models.Model):
    _name = 'product.kunstler'

    name = fields.Char('KŸnstler Name', required=True)
    product_ids = fields.One2many(
        'product.template',
        'product_kunstler_id',
        string='KŸnstler Produkte',
    )
    products_count = fields.Integer(
        string='Number of products',
        compute='_get_products_count',
    )

    @api.one
    @api.depends('product_ids')
    def _get_products_count(self):
        self.products_count = len(self.product_ids)


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    product_kunstler_id = fields.Many2one(
        'product.kunstler',
        string='Kunstler',
        help='Select a KŸnstler for this product'
    )
class PurchaseTemplate(models.Model):
    _inherit = 'purchase.order'
    
    product_kunstler_name = fields.Many2one(
        'product.kunstler',
        string='Kunstler',
        related='product_kunstler.name'
    )
