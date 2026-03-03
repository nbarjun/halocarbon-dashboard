import plotly.graph_objs as go
from dash import dcc, html
import logging
logging.basicConfig(level=logging.INFO)

def build_figure(df, selected_traces, trace_library):
    fig = go.Figure()

    for key in selected_traces:
        if trace_library[key]["uncertainty"]:
            xvals = df.index
            yvals = df[key]

            # Upper bound (invisible line)
            fig.add_trace(
                go.Scatter(
                    x=df.index,
                    y=yvals+df[key+'_std'],
                    mode="lines",
                    line=dict(width=0),
                    showlegend=False,
                    hoverinfo="skip"
                )
            )
            alpha =.3
            # Lower bound (filled to upper)
            fig.add_trace(
                go.Scatter(
                    x=df.index,
                    y=yvals-df[key+'_std'],
                    mode="lines",
                    fill="tonexty",
                    fillcolor=trace_library[key]['line_color'].replace("rgb", "rgba")\
                        .replace(")", f", {alpha})"),
                    line=dict(width=0),
                    showlegend=False,
                    hoverinfo="skip"
                )
            )
        else:
            xvals = df.index
            yvals = df[key]

        fig.add_trace(
            go.Scatter(
                x=xvals, y=yvals,
                name=trace_library[key]["label"], mode="lines",
                line=dict(width=3, color=trace_library[key]["line_color"],\
                    dash=trace_library[key]["line_style"])
            )
        )

    fig.update_layout(
        title=df.attrs["title"],
        autosize=True,
        margin=dict(l=40, r=40, t=60, b=40),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        yaxis_title=f"{df.attrs["long_name"]}[{df.attrs["units"]}]",
        xaxis_title=f"{df.index.name}",
        legend=dict(yanchor="top", y=0.99, xanchor="right", x=.9)
    )

    return fig


def figure_with_text(figure, title, description, fig_key, text_position="right"):
    plot = html.Div(
        className="box plot-box",
        children=dcc.Graph(
            id={"type":"gas-figure","key":fig_key},
            figure=figure,
            config={"displayModeBar": False, "responsive": False},
            style = {"width": "98%","height":'100%'},
        )
    )

    text = html.Div(
        className="box text-box",
        children=[html.H3(title), html.P(description)]
    )

    return html.Div(
        className="figure-row",
        children=[plot, text] if text_position == "right" else [text, plot]
    )
