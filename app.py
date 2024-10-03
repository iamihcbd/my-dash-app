import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd
import numpy as np

# Initialize Dash app
app = dash.Dash(__name__)

# Load the CSV file directly
df = pd.read_csv('gdp_1960_2020.csv')  # Ensure this file is in the same directory as your app.py

# 1. Pie Chart for Region Distribution
pie_chart_fig = px.pie(df, names='state', title='GDP Distribution by Region')

# 2. Bar Chart for GDP Comparison by Country
bar_chart_fig = px.bar(df, x='country', y='gdp', title='GDP Comparison by Country')

# 3. Scatter Plot for GDP Over the Years
# Apply log scaling to GDP for better visualization
df['gdp_scaled'] = df['gdp'].apply(lambda x: np.log10(x) if x > 0 else 0)

scatter_fig = px.scatter(df, x='year', y='gdp_scaled', color='country', 
                         title="GDP Over the Years (Log Scale)",
                         labels={'year': 'Year', 'gdp_scaled': 'GDP (Log Scale)', 'country': 'Country'},
                         hover_name='country',
                         size='gdp_scaled',
                         size_max=60,
                         animation_frame='year',
                         animation_group='country',
                         range_y=[df['gdp_scaled'].min() - 1, df['gdp_scaled'].max() + 1])

# Define the layout of the app with all three graphs
app.layout = html.Div([
    html.H1("GDP Visualizations (1960-2020)"),
    
    # Pie chart
    dcc.Graph(id='pie-chart', figure=pie_chart_fig),
    
    # Bar chart
    dcc.Graph(id='bar-chart', figure=bar_chart_fig),
    
    # Scatter plot (with log scale for better visibility)
    dcc.Graph(id='gdp-scatter', figure=scatter_fig)
])

# Expose the Flask server for deployment
server = app.server

# Run the app locally for development
if __name__ == "__main__":
    app.run_server(debug=True)
