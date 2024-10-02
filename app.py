import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd
import numpy as np  # Import numpy for logarithmic scaling
from ibrahim_assignment import prepare_data

# Initialize Dash app
app = dash.Dash(__name__)

# Use the function to load and prepare data
df = prepare_data('gdp_1960_2020.csv')

# 1. Create pie chart for region distribution
pie_chart_fig = px.pie(df, names='state', title='GDP Distribution by Region')

# 2. Create bar chart for country-wise GDP comparison
bar_chart_fig = px.bar(df, x='country', y='gdp', title='GDP Comparison by Country')

# 3. Apply logarithmic scaling to the GDP values to compress the range for the scatter plot
df['gdp_scaled'] = df['gdp'].apply(lambda x: x if x <= 0 else max(1, x)).apply(np.log10)  # Logarithmic scaling

# 4. Create scatter plot for GDP over the years (with log scale for better bubble visibility)
scatter_fig = px.scatter(
    df, 
    x='year', 
    y='gdp_scaled', 
    color='country', 
    title="GDP Over the Years (Logarithmic Scaling)",
    labels={'year': 'Year', 'gdp_scaled': 'GDP (Log Scale)', 'country': 'Country'},
    hover_name='country',
    size='gdp_scaled',  # Bubble size based on log-scaled GDP
    size_max=60,  # Adjust max size for better visibility
    animation_frame='year',  # Enables the animation over the years
    animation_group='country',  # Group bubbles by country
    range_y=[0, df['gdp_scaled'].max() + 1],  # Adjusted y-axis range
    height=600  # Increased plot height for better visibility
)

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
