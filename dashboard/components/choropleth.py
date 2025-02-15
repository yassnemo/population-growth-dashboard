import plotly.express as px

def choropleth_component(df, selected_year):
    return px.choropleth(
        df[df['Year'] == selected_year],
        locations="ISO3",
        color="Population",
        scope="world",
        hover_name="Country"
    )