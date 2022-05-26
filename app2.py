import dash_bootstrap_components as dbc
from dash import Dash, dcc, html, Input, Output, callback
from vars import *
import plotly.express as px
from app_secrets import *
from tools import *
from callbacks import *


app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP],suppress_callback_exceptions=True)
server = app.server

app.layout = dbc.Container(
    [
        dbc.Row([
            dbc.Col(
                html.Div([
                    html.Label('X variable'),
                    dcc.Dropdown(
                        id='scatter_x_var',
                        options=[{'label':md[i]['flatlabel'],'value':i} for i in scatter_plot_x_vars],
                        value=scatter_plot_x_vars[0],
                        multi=False
                    )
                ]),
                width=4,xs=12,sm=12,md=12,lg=6
            ),
            dbc.Col(
                html.Div([
                    html.Label('Y variable'),
                    dcc.Dropdown(
                        id='scatter_y_var',
                        options=[{'label':md[i]['flatlabel'],'value':i} for i in scatter_plot_y_vars],
                        value=scatter_plot_y_vars[0],
                        multi=False
                    )
                ]),
                width=4,xs=12,sm=12,md=12,lg=6
            ),

            dbc.Col(
                html.Div([
                    html.Label('Factor'),
                    dcc.Dropdown(
                        id='scatter_factor',
                        options=[{'label':md[i]['flatlabel'],'value':i} for i in scatter_plot_factors],
                        value=scatter_plot_factors[0],
                        multi=False
                    )
                ]),
                width=4,xs=12,sm=12,md=12,lg=6
            )
        ]),
        dbc.Row([
            html.Div([
                html.Label('Totals/Sums or Averages'),
                dcc.RadioItems(
                    id='scatter_agg_mode',
                    options=[{'label': i, 'value': i} for i in ['Totals/Sums','Averages']],
                    value='Totals/Sums',
                    labelStyle={'display': 'inline'}
                )
            ])
        ]),
        # dbc.Row(
        #     dcc.Graph(id="bar-graph")
        # )
        dcc.Graph(id="bar-graph")
    ]
)

@callback(
    Output('bar-graph', 'figure'),
    Input('scatter_x_var', 'value'),
    Input('scatter_y_var', 'value'),
    Input('scatter_factor', 'value'),
    Input('scatter_agg_mode', 'value')
)
def update_bar_graph(x_var, y_var, factor, agg_mode):
    global md

    data={
        'selected_fields':[x_var, y_var, factor],
        'cachename':['voyage_xyscatter']
    }

    print(data)

    df, results_count=update_df(base_url+'voyage/caches', data=data)


    yvarlabel=md[y_var]['flatlabel']
    xvarlabel=md[x_var]['flatlabel']

    if agg_mode=='Averages':
        df2=df.groupby(x_var)[y_var].mean()
        df2=df2.reset_index()
        df2[factor]=df[factor]
    elif agg_mode=='Totals/Sums':
        df2=df.groupby(x_var)[y_var].sum()
        df2=df2.reset_index()
        df2[factor]=df[factor]
        # df3=df2.groupby(factor)

    print('!!!!!!!!!!!!!!!')
    print(factor)
    print(df2)

    fig = px.scatter(df2, x=x_var, y=y_var, color=factor,
        labels={
            y_var:yvarlabel,
			x_var:xvarlabel
            }
        )


    del df

    return fig

app.run_server(debug=True, use_reloader=False)  # Turn off reloader if inside Jupyter
