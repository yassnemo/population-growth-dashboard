from dash import Dash, dcc, html, Input, Output
import pandas as pd 
from scripts.visualization import create_choropleth, create_line_chart

app = Dash(__name__, suppress_callback_exceptions=True)
df = pd.read_csv("data/processed/cleaned_population.csv")

app.layout = html.Div([
    html.H1("Global Population Dashboard", className='header'),
    dcc.Dropdown(
        id='country-dropdown',
        options=[{'label': c, 'value': c} for c in df['Country'].unique()],
        value='World'
    ),
    dcc.Slider(
        id='year-slider',
        min=df['Year'].min(),
        max=df['Year'].max(),
        value=df['Year'].max(),
        marks={year: str(year) for year in range(1950, 2101, 10)}
    ),
    dcc.Graph(id='choropleth-map'),
    dcc.Graph(id='line-chart')
])

@app.callback(
    Output('choropleth-map', 'figure'),
    Input('year-slider', 'value')
)
def update_map(year):
    return create_choropleth(df, year)

@app.callback(
    Output('line-chart', 'figure'),
    Input('country-dropdown', 'value')
)
def update_line_chart(country):
    return create_line_chart(df, country)

if __name__ == '__main__':
    app.run_server(debug=True)