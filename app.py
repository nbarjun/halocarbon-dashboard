import dash
from dash import html

from data.loader import (atmosConc,
                        lifeTimes,
                        prod)
from data.traces import (gas_to_label,
                build_trace_library_gas,
                build_trace_library_production)
from pages.home import home_page
from callbacks.navigation import register_navigation
from callbacks.gas_plot import register_gas_plot

trace_library_gases = build_trace_library_gas(atmosConc.columns)
trace_library_prod = build_trace_library_production()
trace_library = {'gases':trace_library_gases,\
                'production':trace_library_prod}

app = dash.Dash(__name__, suppress_callback_exceptions=True)
app.title = "Bayesian Assessment of Halocarbon Banks"
app.layout = html.Div(id="page-content", children=home_page())

register_navigation(app, atmosConc, lifeTimes, prod, trace_library)
register_gas_plot(app, atmosConc, lifeTimes, prod, trace_library)

if __name__ == "__main__":
    app.run(debug=True)
