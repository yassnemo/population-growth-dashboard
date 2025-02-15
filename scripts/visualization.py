import plotly.express as px

def create_choropleth(df, year):
    fig = px.choropleth(
        df[df['Year'] == year],
        locations="ISO3",
        color="Population",
        hover_name="Country",
        color_continuous_scale=px.colors.sequential.Plasma,
        title=f"World Population in {year}"
    )
    return fig

def create_line_chart(df, country):
    fig = px.line(
        df[df['Country'] == country],
        x="Year",
        y="Population",
        title=f"Population Trend: {country}"
    )
    return fig