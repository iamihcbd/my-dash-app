import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd
from ibrahim_assignment import prepare_data

# Initialize Dash app
app = dash.Dash(__name__)

# Use the function to load and prepare data
df = prepare_data('gdp_1960_2020.csv')

# Create pie chart for region distribution
pie_chart_fig = px.pie(df, names='state', title='GDP Distribution by Region')

# Create bar chart for country-wise GDP comparison
bar_chart_fig = px.bar(df, x='country', y='gdp', title='GDP Comparison by Country')

# Create scatter plot for GDP over the years
scatter_fig = px.scatter(df, x='year', y='gdp', title="GDP Over the Years", labels={'year': 'Year', 'gdp': 'GDP'})

# Define the layout of the app with all three graphs
app.layout = html.Div([
    html.H1("GDP Visualizations (1960-2020)"),
    
    # Pie chart
    dcc.Graph(id='pie-chart', figure=pie_chart_fig),
    
    # Bar chart
    dcc.Graph(id='bar-chart', figure=bar_chart_fig),
    
    # Scatter plot
    dcc.Graph(id='gdp-scatter', figure=scatter_fig)
])

# Expose the Flask server for deployment
server = app.server

# Run the app locally for development
if __name__ == "__main__":
    app.run_server(debug=True)
