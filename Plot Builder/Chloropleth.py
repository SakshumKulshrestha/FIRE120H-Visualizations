import plotly.graph_objects as go
import pandas as pd


def getCode():
    ##Nothing for now
    print()


df = pd.read_csv("Data Files\\2017_trust_in_gov.csv")

fig = go.Figure(data=go.Choropleth(
    locations = df[''],
    z = df['Trust..Government.Corruption.'],
    text = df['COUNTRY'],
    colorscale = 'Blues',
    autocolorscale=False,
    reversescale=True,
    marker_line_color='darkgray',
    marker_line_width=0.5,
    colorbar_tickprefix = '$',
    colorbar_title = 'GDP<br>Billions US$',
))


