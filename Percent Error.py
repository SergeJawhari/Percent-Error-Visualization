import plotly.graph_objects as go
import pandas as pd
import plotly.express as px

# approx = Time we got.
# exact = Time we set.
def percentage_error(approx, exact):
    error = (((approx - exact) / exact)*100)
    return error

data = pd.read_csv("EvT.csv")

fig = px.line(data, x=data['Sprint'], y=percentage_error(data['Approximate'], data['Exact']))

fig.update_layout(
    title="Percent Errors Visualization",
    xaxis_title="Sprint",
    yaxis_title="Percent Error",
    font=dict(
        size=18,
    )
)

fig.write_html('Percent Error.html', auto_open=True)