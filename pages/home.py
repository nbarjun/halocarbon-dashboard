from dash import html, dcc
from components.nav import nav_buttons

intro_markdown = '''
Halocarbons are synthetic compounds composed of carbon bonded to halogen atoms such as chlorine, fluorine, and bromine. Their chemical stability, low toxicity, and non-flammability led to widespread use during the 20th century in refrigeration and air conditioning, aerosol propellants, foam production, and fire suppression. For decades, these compounds were considered environmentally benign. This view changed in the 1970s, when atmospheric research showed that many halocarbons are long-lived and can reach the stratosphere, where ultraviolet radiation breaks them apart and releases chlorine and bromine. These atoms catalytically destroy ozone, allowing increased levels of harmful ultraviolet radiation to reach Earth's surface.

The global consequences of halocarbon emissions became clear in the mid-1980s with the discovery of severe ozone depletion over Antarctica. In response, the international community adopted the Montreal Protocol on Substances that Deplete the Ozone Layer in 1987. The agreement established binding controls on the production and use of ozone-depleting substances, with phased timelines and support for developing countries. The Montreal Protocol has driven large reductions in atmospheric halocarbons and remains one of the most successful environmental treaties to date, though continued monitoring is essential as legacy emissions and emerging compounds persist.

Estimating halocarbon emissions and remaining banks has traditionally relied on either bottom-up accounting methods based on reported production, equipment inventories, and assumed leakage rates, or top-down approaches that infer emissions from atmospheric observations and lifetimes. Both methods are subject to substantial uncertainties arising from reporting biases, poorly constrained release rates, and uncertainties in atmospheric lifetimes. The Bayesian framework applied here integrates reported production, prior knowledge of emission processes, and atmospheric concentration measurements within a single probabilistic model. By conditioning simulated banks and emissions on observed atmospheric data, this approach provides statistically consistent estimates of production, emissions, and remaining banks, along with quantified uncertainties.
'''

ref_markdown = '''
1. Lickley, M. J., Daniel, J. S., Fleming, E. L., Reimann, S., & Solomon, S. (2022). Bayesian assessment of chlorofluorocarbon (CFC), hydrochlorofluorocarbon (HCFC) and halon banks suggest large reservoirs still present in old equipment. Atmospheric Chemistry and Physics, 22(17), 11125-11136.
2. Lickley, M., Fletcher, S., Rigby, M., & Solomon, S. (2021). Joint inference of CFC lifetimes and banks suggests previously unidentified emissions. Nature Communications, 12(1), 2920.
3. Lickley, M., Solomon, S., Fletcher, S., Velders, G. J., Daniel, J., Rigby, M., ... & Stone, K. (2020). Quantifying contributions of chlorofluorocarbon banks to emissions and impacts on the ozone layer and climate. Nature communications, 11(1), 1380.
'''
def home_page():
    return html.Div(
        className="hero",
        children=[
            html.Div(
                className="hero-header",
                children=[
                    html.H1("Bayesian Assessment of Halocarbon Banks",
                            className="hero-title"),
                    nav_buttons("home"),
                    dcc.Markdown(intro_markdown),
                    html.H3("External References", style={"margin-top": "1px", "margin-bottom": "0px"}),
                    dcc.Markdown(ref_markdown)
                ]
            )
        ]
    )
