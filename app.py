
import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

# Define the function to prepare the data
def prepare_data(file_path):
    df = pd.read_csv(file_path)
    df = df[['year', 'country', 'gdp']]
    df = df.dropna()
    df['year'] = df['year'].astype(int)
    return df

# Initialize Dash app
app = dash.Dash(__name__)

# Use the function to load and prepare data
df = prepare_data('gdp_1960_2020.csv')

# Define the layout of the app
app.layout = html.Div([
    html.H1("GDP of All Countries (1960-2020)"),
    dcc.Graph(
        id='gdp-scatter',
        figure=px.scatter(df, x='year', y='gdp', color='country', 
                          title="GDP Over the Years",
                          labels={'year':'Year', 'gdp':'GDP', 'country':'Country'},
                          hover_name='country',
                          size='gdp',
                          animation_frame='year',
                          animation_group='country')
    )
])

# Expose the Flask server for deployment
server = app.server

# Run the app locally for development
if __name__ == "__main__":
    app.run_server(debug=True)
