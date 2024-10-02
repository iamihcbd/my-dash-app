import dash
from dash import dcc, html
import plotly.express as px
from ibrahim_assignment import prepare_data

# Initialize Dash app
app = dash.Dash(__name__)

# Use the function to load and prepare data
df = prepare_data('gdp_1960_2020.csv')

# Optionally filter data to improve performance (uncomment to limit data)
# df = df[df['country'].isin(['the United States', 'China', 'Japan', 'Germany', 'India'])]

# Adjust GDP values to make bubble sizes more manageable (normalizing)
df['gdp_scaled'] = df['gdp'] / 1e9  # Scale GDP by billions for better bubble size management

# Define the layout of the app
app.layout = html.Div([
    html.H1("GDP of All Countries (1960-2020)"),
    
    # Interactive scatter plot with animation
    dcc.Graph(
        id='gdp-scatter',
        figure=px.scatter(df, x='year', y='gdp_scaled', color='country', 
                          title="GDP Over the Years (scaled in billions)",
                          labels={'year': 'Year', 'gdp_scaled': 'GDP (in billions)', 'country': 'Country'},
                          hover_name='country',  # Allows hover interaction to show country name
                          size='gdp_scaled',  # Size of the bubbles based on scaled GDP
                          size_max=60,  # Adjust max size for better visibility
                          animation_frame='year',  # Enables the animation over the years
                          animation_group='country',  # Group bubbles by country
                          range_y=[0, df['gdp_scaled'].max() + 5000],  # Adjusted y-axis range
                          height=600  # Increased plot height for better visibility
                          )
    )
])

# Expose the Flask server for deployment
server = app.server

# Run the app locally for development
if __name__ == "__main__":
    app.run_server(debug=True)
