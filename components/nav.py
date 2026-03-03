from dash import html

def nav_buttons(active_page="home"):
    def btn(label, btn_id, page):
        return html.Button(
            label,
            id=btn_id,
            className=f"nav-button{' active' if active_page == page else ''}",
            n_clicks=0
        )

    return html.Div(
        id="nav-buttons",
        children=[
            btn("Home", "btn-home", "home"),
            btn("CFC-11", "btn-cfc11", "cfc11"),
            btn("CFC-12", "btn-cfc12", "cfc12"),
            btn("CFC-113", "btn-cfc113", "cfc113"),
            btn("CFC-114", "btn-cfc114", "cfc114"),
            btn("CFC-115", "btn-cfc115", "cfc115"),
            btn("HCFC-22", "btn-hcfc22", "hcfc22"),
            btn("HCFC-141b", "btn-hcfc141b", "hcfc141b"),
            btn("HCFC-142b", "btn-hcfc142b", "hcfc142b"),
            btn("Halon-1211", "btn-h1211", "h1211"),
            btn("Halon-1301", "btn-h1301", "h1301"),
        ]
    )
