# SPDX-FileCopyrightText: 2026 Coop IT Easy SC
#
# SPDX-License-Identifier: AGPL-3.0-or-later

from odoo import api, fields, models
from odoo.tools import get_lang


class StockMove(models.Model):
    _inherit = "stock.move"

    product_name = fields.Char(
        compute="_compute_product_name_and_code",
        readonly=True,
        store=True,
    )
    product_code = fields.Char(
        compute="_compute_product_name_and_code",
        readonly=True,
        store=True,
    )

    # simplified version of PurchaseOrderLine's
    # _compute_price_unit_and_date_planned_and_name
    @api.depends(
        "product_id", "product_uom_qty", "picking_type_id.code", "picking_id.partner_id"
    )
    def _compute_product_name_and_code(self):
        for move in self:
            if not move.product_id or not move.company_id:
                continue
            product = move.product_id
            partner = move.picking_id.partner_id
            seller = False
            if product and partner and move.picking_type_id.code == "incoming":
                seller = product.with_company(move.company_id)._select_seller(
                    partner_id=partner,
                    quantity=move.product_uom_qty,
                    uom_id=product.uom_po_id,
                )
            ctx = {"display_default_code": False}

            if seller:
                ctx["seller_id"] = seller.id

            if partner:
                ctx["lang"] = get_lang(move.env, partner.lang).code
            move.product_name = product.with_context(**ctx).display_name
            move.product_code = seller and seller.product_code or product.default_code
