from dash import Output, Input, ctx
from pages.home import home_page
from pages.gas import gas_page

def register_navigation(app, aconc, lts, prod, trace_library):

    @app.callback(
        Output("page-content", "children"),
        Input("btn-home", "n_clicks"),
        Input("btn-cfc11", "n_clicks"),
        Input("btn-cfc12", "n_clicks"),
        Input("btn-cfc113", "n_clicks"),
        Input("btn-cfc114", "n_clicks"),
        Input("btn-cfc115", "n_clicks"),
        Input("btn-hcfc22", "n_clicks"),
        Input("btn-hcfc141b", "n_clicks"),
        Input("btn-hcfc142b", "n_clicks"),
        Input("btn-h1211", "n_clicks"),
        Input("btn-h1301", "n_clicks"),
        prevent_initial_call=True
    )
    def navigate(*_):
        trigger = ctx.triggered_id
        mapping = {
            "btn-cfc11": "cfc-11",
            "btn-cfc12": "cfc-12",
            "btn-cfc113": "cfc-113",
            "btn-cfc114": "cfc-114",
            "btn-cfc115": "cfc-115",
            "btn-hcfc22": "hcfc-22",
            "btn-hcfc141b": "hcfc-141b",
            "btn-hcfc142b": "hcfc-142b",
            "btn-h1211": "h-1211",
            "btn-h1301": "h-1301",
        }

        if trigger in mapping:
            return gas_page(mapping[trigger], aconc, lts, prod, trace_library)

        return home_page()