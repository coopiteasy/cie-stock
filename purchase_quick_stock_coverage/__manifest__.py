# SPDX-FileCopyrightText: 2026 Coop IT Easy SC
#
# SPDX-License-Identifier: AGPL-3.0-or-later

{
    "name": "Purchase Quick Stock Coverage",
    "summary": "Add stock coverage to the purchase quick view",
    "version": "16.0.1.0.0",
    "category": "Purchase",
    "website": "https://coopiteasy.be",
    "author": "Coop IT Easy SC",
    "maintainers": ["mihien"],
    "license": "AGPL-3",
    "depends": ["product_stock_coverage", "purchase_quick"],
    "data": [
        "views/product_view.xml",
    ],
    "auto-install": True,
}
