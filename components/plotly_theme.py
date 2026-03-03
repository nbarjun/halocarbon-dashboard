import plotly.io as pio

def register_plotly_theme():
    pio.templates["site_theme"] = pio.templates["plotly_white"]

    pio.templates["site_theme"].layout.update(
        font=dict(
            family="Helvetica Neue, Helvetica, Arial, sans-serif",
            size=16,
            color="#111"
        ),
        title=dict(
            font=dict(
                size=20,
                family="Helvetica Neue, Helvetica, Arial, sans-serif",
            )
        )
    )
    pio.templates["site_theme"].layout.update(
        xaxis=dict(
            title_font=dict(size=14),
            tickfont=dict(size=12)
        ),
        yaxis=dict(
            title_font=dict(size=14),
            tickfont=dict(size=12)
        ),
        legend=dict(
            font=dict(size=13)
        )
    )
    pio.templates.default = "site_theme"
