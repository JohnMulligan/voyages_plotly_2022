# import plotly.express as px
# df = px.data.gapminder().query("year == 2007").query("continent == 'Europe'")
# df.loc[df['pop'] < 2.e6, 'country'] = 'Other countries' # Represent only large countries]

# print(df)

# fig = px.pie(df, values='pop', names='country', title='Population of European continent')
# fig.show()


import plotly.express as px
from dash import Dash, dcc, html, Input, Output, callback,dash_table,State
import requests
import json
import pandas as pd

import dash
# import dash_core_components as dcc
from dash import dcc
# import dash_html_components as html
from dash import html



bar_x_vars=[
	'voyage_ship__imputed_nationality__name',
	'voyage_ship__rig_of_vessel__name',
	'voyage_outcome__particular_outcome__name',
	'voyage_outcome__outcome_slaves__name',
	'voyage_outcome__outcome_owner__name',
	'voyage_outcome__vessel_captured_outcome__name',
	'voyage_outcome__resistance__name',
	'voyage_itinerary__imp_port_voyage_begin__place',
	'voyage_itinerary__imp_region_voyage_begin__region',
	'voyage_itinerary__imp_principal_place_of_slave_purchase__place',
	'voyage_itinerary__imp_principal_region_of_slave_purchase__region',
	'voyage_itinerary__imp_principal_port_slave_dis__place',
	'voyage_itinerary__imp_principal_region_slave_dis__region',
	'voyage_itinerary__imp_broad_region_slave_dis__broad_region',
	'voyage_itinerary__place_voyage_ended__place',
	'voyage_itinerary__region_of_return__region',
	'voyage_dates__imp_arrival_at_port_of_dis_yyyy',
	'voyage_dates__voyage_began_mm',
	'voyage_dates__slave_purchase_began_mm',
	'voyage_dates__date_departed_africa_mm',
	'voyage_dates__first_dis_of_slaves_mm',
	'voyage_dates__voyage_completed_mm'
]

bar_y_abs_vars=[
	'voyage_dates__imp_length_home_to_disembark',
	'voyage_dates__length_middle_passage_days',	
	'voyage_ship__tonnage_mod',
	'voyage_crew__crew_voyage_outset',
	'voyage_crew__crew_first_landing',					
	'voyage_slaves_numbers__imp_total_num_slaves_embarked',
	'voyage_slaves_numbers__imp_total_num_slaves_disembarked',
	'voyage_slaves_numbers__imp_jamaican_cash_price'
	]

app = dash.Dash()

app.layout = html.Div([
    dcc.Graph(id="bar_chart"),
    dcc.Dropdown(
        id="bar_x",
        options=[i for i in bar_x_vars],
        value=bar_x_vars[0],
        multi=False,
    ),
    dcc.Dropdown(
        id="bar_y",
        options=[i for i in bar_y_abs_vars],
        value=bar_y_abs_vars[0],
        multi=False,
    ),
])

@app.callback(
    Output("bar_chart", "figure"), 
    Input("bar_x", "value"),
    Input("bar_y", "value")
)
def update_bar_chart(bar_x, bar_y):
    data = {
        'selected_fields': [bar_x,bar_y],
        'cachename': ['voyage_bar_and_donut_charts']
    }

    # print(data)
    # mask = df["day"] == day

    headers={'Authorization': 'Token xxx'}

    url='https://voyages3-api.crc.rice.edu/voyage/caches'

    r = requests.post(url, data=data, headers=headers)
    j = r.text

    df = pd.read_json(j)
    # print(df)
    fig = px.bar(df, x=bar_x, y=bar_y)
    fig.update_layout({
		'plot_bgcolor': 'rgba(0, 0, 0, 0)',
		'paper_bgcolor': 'rgba(0, 0, 0, 0)',
	})
    return fig

app.run_server(debug=True, use_reloader = False)    