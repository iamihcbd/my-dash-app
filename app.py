import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd
from ibrahim_assignment import prepare_data # Import the function to process data

# Initialize Dash app
app = dash.Dash(__name__)

# Use the function from ibrahim_assignment.py to load and prepare data
df = prepare_data('gdp_1960_2020.csv')  # Assuming this function processes your CSV file and returns a DataFrame

# Define the layout of the app
app.layout = html.Div([
    html.H1("gdp of All Countries (1960-2020)"),
    dcc.Graph(
        id='gdp-scatter',
        figure=px.scatter(df, x='year', y='gdp', color='country Name', title="gdp Over the years")
    )
])

# Expose the Flask server for deployment
server = app.server

# Run the app locally for development
if __name__ == "__main__":
    app.run_server(debug=True)
    
