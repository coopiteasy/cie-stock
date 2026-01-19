# SPDX-FileCopyrightText: 2026 Coop IT Easy SC
#
# SPDX-License-Identifier: AGPL-3.0-or-later

from openupgradelib import openupgrade


@openupgrade.migrate()
def migrate(env, version):

    # update the stock coverage for all products
    templates = env["product.template"].search([])
    for template in templates:
        if template.virtual_available <= 0:
            template.stock_coverage = 0
        elif template.daily_sales == 0:
            template.stock_coverage = 9999
        else:
            template.stock_coverage = template.virtual_available / template.daily_sales
