import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

# Step 1: Load the dataset
df = pd.read_csv('gdp_1960_2020.csv')  # Ensure this file is in the same folder as app.py

# Step 2: Create a Dash app
app = dash.Dash(__name__)

# Step 3: Define the layout of the app
app.layout = html.Div([
    html.H1("GDP of All Countries (1960-2020)"),

    # Scatter Plot of GDP Data over the years
    html.H2("Scatter Plot of GDP Data"),
    dcc.Graph(
        id='gdp-scatter',
        figure=px.scatter(df, x='Year', y='GDP', color='Country Name', title="GDP Over the Years")
    ),

    # Bar Chart for GDP in the year 2020
    html.H2("Bar Chart of GDP for the Year 2020"),
    dcc.Graph(
        id='gdp-bar',
        figure=px.bar(df[df['Year'] == 2020], x='Country Name', y='GDP', title="GDP for 2020")
    )
])

# Expose the Flask server object for gunicorn
server = app.server

# Step 4: Run the Dash app
if __name__ == '__main__':
    app.run_server(debug=True)
    
