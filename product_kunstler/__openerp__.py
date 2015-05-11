# -*- encoding: utf-8 -*-
###############################################################################
# #                                                                           #
# product_kunstler for Odoo #                                                 #
# Copyright (C) 2015 Designxomplex                                            #
# Contributors                                                                #
# Thomas Klosinsky, thomas@designcomplex.de                                   #
# #                                                                           #
# This program is free software: you can redistribute it and/or modify #      #
# it under the terms of the GNU Affero General Public License as #            #
# published by the Free Software Foundation, either version 3 of the #        #
# License, or (at your option) any later version. #                           #
# #                                                                           #
# This program is distributed in the hope that it will be useful, #           #
# but WITHOUT ANY WARRANTY; without even the implied warranty of #            #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the #              #
# GNU Affero General Public License for more details. #                       #
# #                                                                           #
# You should have received a copy of the GNU Affero General Public License #  #
# along with this program. If not, see <http://www.gnu.org/licenses/>. #      #
# #                                                                           #
###############################################################################
###############################################################################
# Product KŸnstler is an Openobject module wich enable KŸnstler management for#
# products                                                                    #
###############################################################################
{
    'name': 'Product Kunstler Addon',
    'version': '0.1',
    'category': 'Product',
    'summary': 'Add Kunstler to products',
    'description':'This module adds artist management to products and purchase order view',
    'author': 'Designcomplex',
    'license': 'AGPL-3',
    'depends': ['product'],
    'data': [
        'product_kunstler_view.xml',
    ],
    'installable': True,
    'website': 'http://www.designcomplex.de',
}
