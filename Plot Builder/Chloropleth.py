import plotly.graph_objects as go
import pandas as pd
import plotly.offline as ply


def getCode():
    ##Nothing for now
    print()


df = pd.read_csv("Data Files\\new_file_correct_codes.csv")

fig = go.Figure(data=go.Choropleth(
    locations = df['CORRECT'],
    z = df['Trust..Government.Corruption.'],
    text = df['Country'],
    colorscale = 'Reds',
    autocolorscale=False,
    reversescale=False,
    marker_line_color='darkgray',
    marker_line_width=0.5,
    colorbar_title = 'Trust in Government',
))

ply.plot(fig, filename='Trust_in_gov.html')

