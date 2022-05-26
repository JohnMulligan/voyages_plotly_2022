import plotly.express as px
from dash import Input, Output, callback, dash_table,State
import pandas as pd
import requests
import json
from app_secrets import *
import dash
from vars import *
import dash_core_components as dcc
import dash_html_components as html


'''
donut_value_vars=[
	'voyage_dates__imp_length_home_to_disembark',
	'voyage_dates__length_middle_passage_days',	
	'voyage_ship__tonnage_mod',
	'voyage_crew__crew_voyage_outset',
	'voyage_crew__crew_first_landing',					
	'voyage_slaves_numbers__imp_total_num_slaves_embarked',
	'voyage_slaves_numbers__imp_total_num_slaves_disembarked',
	'voyage_slaves_numbers__imp_jamaican_cash_price'
]

donut_name_vars=[
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
	'voyage_itinerary__region_of_return__region'
	]
'''

app = dash.Dash()
app.layout = html.Div([
	dcc.Graph(id='fizz'),
	html.Label('X variables'),
	dcc.Dropdown(
		id='bar_Xvar',
		options=bar_x_vars,
		value=bar_x_vars[0],
		multi=False
	),
	html.Label('Y variables'),
	dcc.Dropdown(
		id='bar_Yvar',
		options=bar_y_abs_vars,
		value=bar_y_abs_vars[0],
		multi=False
	),
	html.Label('Totals/Sums or Averages'),
	dcc.RadioItems(
		id='bar_agg_mode',
		options=[{'label': i, 'value': i} for i in ['Totals/Sums','Averages']],
		value='Totals/Sums',
		labelStyle={'display': 'inline'}
	)
])

@app.callback(
	Output('fizz', 'figure'),
	Input('bar_Xvar', 'value'),
	Input('bar_Yvar', 'value'),
	Input('bar_agg_mode', 'value'),
	)
def update_bar_graph(x_var,y_var,agg_mode):
	global headers
	data={
		'selected_fields':[x_var,y_var],
		'cachename':['voyage_bar_and_donut_charts']
	}
	
	url="https://voyages3-api.crc.rice.edu/voyage/caches"
	
	r=requests.post(url,data=data,headers=headers)
	j=r.text
	df=pd.read_json(j)

	if agg_mode=='Averages':
		df2=df.groupby(x_var)[y_var].mean()
		df2=df2.reset_index()
	elif agg_mode=='Totals/Sums':
		df2=df.groupby(x_var)[y_var].sum()
		df2=df2.reset_index()

	'''
	print("!!!!!!")
	print(df.head(10))
	print("!!!!!!")
	print(df2.head(10))
	print("!!!!!!")
	'''

	'''
	yvarlabel=md[y_var]['flatlabel']
	xvarlabel=md[x_var]['flatlabel']
	
	fig=px.bar(df2,x=x_var,y=y_var,
		labels={
			y_var:yvarlabel,
			x_var:xvarlabel
			}
		)
	'''
	fig=px.bar(df2,x=x_var,y=y_var)


	fig.update_layout(
		xaxis_title='',
		yaxis_title='',
		height=700
	)
	del df2, df
	return fig



app.run_server(debug=True, use_reloader=False)  # Turn off reloader if inside Jupyter

