from dash import html, dcc
from components.nav import nav_buttons
from data.traces import gas_to_label
from components.figures import build_figure, figure_with_text

def gas_page(gas, aconc, lifeT, prod, trace_library):
    page_key = gas.lower().replace("-", "")

    fig_aconc = build_figure(aconc, [gas], trace_library['gases'])
    fig_lts   = build_figure(lifeT, [gas], trace_library['gases'])

    default_production_plots = sorted(set(prod[gas].columns) & set(list(trace_library['production'].keys())[:-3]))
    all_production_plots = sorted(set(prod[gas].columns) & set(list(trace_library['production'].keys())))

    fig_prod = build_figure(prod[gas],\
         default_production_plots, trace_library['production'])
    return html.Div(
        className="gas-page",
        children=[
            dcc.Store(id="active-gas", data=gas),

            html.Div(className="gas-nav",
                     children=nav_buttons(page_key)),

            html.Div(
                className="box gas-intro",
                children=[
                    html.H2(f"About {gas_to_label(gas)}"),
                    html.P(f"{trace_library['gases'][gas]['about']}")
                ]
            ),

            html.Div(
                className="box gas-controls selector-box",
                children=[
                    html.Label("Select production category to display"),
                    dcc.Dropdown(
                        id={"type":"trace-selector","key":"prod"},
                        options=[
                            {"label": trace_library['production'][g]["label"], "value": g}
                            for g in all_production_plots
                        ],
                        value=default_production_plots,
                        multi=True,
                        clearable=False
                    )
                ]
            ),

            figure_with_text(
                fig_prod,
                "What does this figure show?",
                f"This plot shows atmospheric concentrations of {gas}.",
                "prod","right"
            ),

            html.Div(
                className="box gas-controls selector-box",
                children=[
                    html.Label("Select gases to display"),
                    dcc.Dropdown(
                        id={"type":"trace-selector","key":"aconc"},
                        options=[
                            {"label": trace_library['gases'][g]["label"], "value": g}
                            for g in aconc.columns
                        ],
                        value=[gas],
                        multi=True,
                        clearable=False
                    )
                ]
            ),

            figure_with_text(
                fig_aconc,
                "What does this figure show?",
                f"This plot shows atmospheric concentrations of {gas}.",
                "aconc","right"
            ),

            html.Div(
                className="box gas-controls selector-box",
                children=[
                    html.Label("Select gases to display"),
                    dcc.Dropdown(
                        id={"type":"trace-selector","key":"lts"},
                        options=[
                            {"label": trace_library['gases'][g]["label"], "value": g}
                            for g in aconc.columns
                        ],
                        value=[gas],
                        multi=True,
                        clearable=False
                    )
                ]
            ),
            figure_with_text(
                fig_lts,
                "What does this figure show?",
                f"This plot shows atmospheric concentrations of {gas}.",
                "lts","left"
            ),
        ]
    )
