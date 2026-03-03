from components.figures import build_figure
from dash import Input, Output, State, MATCH

def register_gas_plot(app, aconc, lts, prod, trace_library):

    @app.callback(
        Output({"type": "gas-figure", "key": MATCH}, "figure"),
        Input({"type": "trace-selector", "key": MATCH}, "value"),
        State("active-gas", "data"),
        State({"type": "trace-selector", "key": MATCH}, "id"),
    )
    def update_plot(selected, gas, selector_id):
        # if not selected:
        #     selected = [gas]

        fig_key = selector_id["key"]

        if fig_key == "aconc":
            if not selected:
                selected = [gas]
            return build_figure(aconc, selected, trace_library['gases'])
        elif fig_key == "lts":
            if not selected:
                selected = [gas]
            return build_figure(lts, selected, trace_library['gases'])
        elif fig_key == "prod":
            # Ensure selected is a list of valid columns
            if not selected or not any(s in prod[gas].columns for s in selected):
                selected = sorted(set(prod[gas].columns) & \
                    set(list(trace_library['production'].keys())[:-3]))
            return build_figure(prod[gas], selected, trace_library['production'])