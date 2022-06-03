from app_secrets import *

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
	'voyage_itinerary__imp_port_voyage_begin__geo_location__name',
	'voyage_itinerary__imp_region_voyage_begin__geo_location__name',
	'voyage_itinerary__imp_principal_place_of_slave_purchase__geo_location__name',
	'voyage_itinerary__imp_principal_region_of_slave_purchase__geo_location__name',
	'voyage_itinerary__imp_principal_port_slave_dis__geo_location__name',
	'voyage_itinerary__imp_principal_region_slave_dis__geo_location__name',
	'voyage_itinerary__imp_broad_region_slave_dis__geo_location__name',
	'voyage_itinerary__place_voyage_ended__geo_location__name',
	'voyage_itinerary__region_of_return__geo_location__name'
	]

scatter_plot_x_vars=[
	'voyage_dates__imp_arrival_at_port_of_dis_yyyy',
	'voyage_dates__imp_length_home_to_disembark',
	'voyage_dates__length_middle_passage_days',
	'voyage_crew__crew_voyage_outset',
	'voyage_crew__crew_first_landing',
	'voyage_slaves_numbers__imp_total_num_slaves_embarked',
	'voyage_slaves_numbers__imp_total_num_slaves_disembarked'
	]

scatter_plot_y_vars=[
	'voyage_slaves_numbers__imp_total_num_slaves_embarked',
	'voyage_slaves_numbers__imp_total_num_slaves_disembarked',
	'voyage_slaves_numbers__percentage_female',
	'voyage_slaves_numbers__percentage_male',
	'voyage_slaves_numbers__percentage_child',
	'voyage_slaves_numbers__percentage_men_among_embarked_slaves',
	'voyage_slaves_numbers__percentage_women_among_embarked_slaves',
	'voyage_slaves_numbers__imp_mortality_ratio',
	'voyage_slaves_numbers__imp_jamaican_cash_price',
	'voyage_slaves_numbers__percentage_boys_among_embarked_slaves',
	'voyage_slaves_numbers__percentage_girls_among_embarked_slaves',
	'voyage_ship__tonnage_mod',
	'voyage_crew__crew_voyage_outset',
	'voyage_crew__crew_first_landing'
]

scatter_plot_factors=[
	'voyage_ship__imputed_nationality__name',
	'voyage_itinerary__imp_principal_region_of_slave_purchase__geo_location__name',
	'voyage_itinerary__imp_broad_region_of_slave_purchase__geo_location__name',
	'voyage_itinerary__imp_broad_region_slave_dis__geo_location__name'
]


bar_x_vars=[
	'voyage_ship__imputed_nationality__name',
	'voyage_ship__rig_of_vessel__name',
	'voyage_outcome__particular_outcome__name',
	'voyage_outcome__outcome_slaves__name',
	'voyage_outcome__outcome_owner__name',
	'voyage_outcome__vessel_captured_outcome__name',
	'voyage_outcome__resistance__name',
	'voyage_itinerary__imp_port_voyage_begin__geo_location__name',
	'voyage_itinerary__imp_region_voyage_begin__geo_location__name',
	'voyage_itinerary__imp_principal_place_of_slave_purchase__geo_location__name',
	'voyage_itinerary__imp_principal_region_of_slave_purchase__geo_location__name',
	'voyage_itinerary__imp_principal_port_slave_dis__geo_location__name',
	'voyage_itinerary__imp_principal_region_slave_dis__geo_location__name',
	'voyage_itinerary__imp_broad_region_slave_dis__geo_location__name',
	'voyage_itinerary__place_voyage_ended__geo_location__name',
	'voyage_itinerary__region_of_return__geo_location__name',
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

pivot_table_categorical_vars=[
	'voyage_ship__imputed_nationality__name',
	'voyage_itinerary__imp_broad_region_voyage_begin__geo_location__name',
	'voyage_itinerary__imp_region_voyage_begin__geo_location__name',
	'voyage_itinerary__imp_port_voyage_begin__geo_location__name',
	'voyage_itinerary__imp_principal_region_of_slave_purchase__geo_location__name',
	'voyage_itinerary__imp_principal_place_of_slave_purchase__geo_location__name',
	'voyage_itinerary__imp_principal_region_slave_dis__geo_location__name',
	'voyage_itinerary__imp_broad_region_slave_dis__geo_location__name',
	'voyage_itinerary__imp_principal_port_slave_dis__geo_location__name',
]

pivot_table_numerical_vars=[
	'voyage_dates__length_middle_passage_days',
	'voyage_slaves_numbers__imp_total_num_slaves_embarked',
	'voyage_slaves_numbers__imp_total_num_slaves_disembarked'
]

voyage_table_default_vars=[
	'voyage_id',
	'voyage_dates__imp_arrival_at_port_of_dis_yyyy',
	'voyage_slaves_numbers__imp_total_num_slaves_embarked',
	'voyage_itinerary__imp_principal_place_of_slave_purchase__geo_location__name',
	'voyage_slaves_numbers__imp_total_num_slaves_disembarked',
	'voyage_itinerary__imp_principal_port_slave_dis__geo_location__name',
	'voyage_captainconnection__captain__name',
	'voyage_ship__ship_name',
	'voyage_outcome__outcome_slaves__name'
]

voyage_export_vars=[
	'voyage_id',
	'voyage_captainconnection__captain__name',
	'voyage_crew__crew_died_complete_voyage',
	'voyage_crew__crew_first_landing',
	'voyage_crew__crew_voyage_outset',
	'voyage_dates__date_departed_africa',
	'voyage_dates__length_middle_passage_days',
	'voyage_dates__imp_arrival_at_port_of_dis_yyyy',
	'voyage_dates__imp_length_home_to_disembark',
	'voyage_itinerary__first_landing_place__geo_location__name',
	'voyage_itinerary__first_place_slave_purchase__geo_location__name',
	'voyage_itinerary__imp_port_voyage_begin__geo_location__name',
	'voyage_itinerary__imp_principal_place_of_slave_purchase__geo_location__name',
	'voyage_itinerary__imp_principal_port_slave_dis__geo_location__name',
	'voyage_itinerary__place_voyage_ended__geo_location__name',
	'voyage_itinerary__port_of_call_before_atl_crossing__geo_location__name',
	'voyage_itinerary__second_landing_place__geo_location__name',
	'voyage_itinerary__second_place_slave_purchase__geo_location__name',
	'voyage_itinerary__third_landing_place__geo_location__name',
	'voyage_itinerary__third_place_slave_purchase__geo_location__name',
	'voyage_slaves_numbers__imp_total_num_slaves_embarked',
	'voyage_slaves_numbers__imp_total_num_slaves_disembarked',
	'voyage_slaves_numbers__num_slaves_carried_first_port',
	'voyage_slaves_numbers__imp_mortality_during_voyage',
	'voyage_slaves_numbers__imp_mortality_ratio',
	'voyage_ship__guns_mounted',
	'voyage_ship__ship_name',
	'voyage_ship__rig_of_vessel__name',
	'voyage_ship__imputed_nationality__name',
	'voyage_ship__registered_place__geo_location__name',
	'voyage_ship__registered_year',
	'voyage_ship__tonnage',
	'voyage_ship__tonnage_mod',
	'voyage_ship__vessel_construction_place__geo_location__name',
	'voyage_ship__year_of_construction',
	'voyage_outcome__outcome_owner__name',
	'voyage_outcome__vessel_captured_outcome__name',
	'voyage_outcome__outcome_slaves__name',
	'voyage_outcome__particular_outcome__name',
	'voyage_outcome__resistance__name',
	'voyage_sourceconnection__source__full_ref',
	'voyage_shipownerconnection__owner__name'
]

autocomplete_text_fields=[
	'voyage_itinerary__imp_principal_region_slave_dis__geo_location__name',
	'voyage_itinerary__imp_principal_region_of_slave_purchase__geo_location__name',
	'voyage_ship__ship_name',
	'voyage_ship__imputed_nationality__name',
	'voyage_outcome__resistance__name',
	'voyage_outcome__particular_outcome__name',
	'voyage_shipownerconnection__owner__name',
	'voyage_captainconnection__captain__name',
	'voyage_sourceconnection__source__full_ref'
]

rangeslider_numeric_fields=[
	'voyage_dates__imp_arrival_at_port_of_dis_yyyy',
	'voyage_slaves_numbers__imp_total_num_slaves_embarked',
	'voyage_slaves_numbers__imp_mortality_ratio',
	'voyage_crew__crew_first_landing',
	'voyage_dates__length_middle_passage_days'
]

map_tilesets=[
	{"label":i[0],"value":i[1]} for i in [
	["Modern Countries","https://api.mapbox.com/styles/v1/%s/tiles/{z}/{x}/{y}?access_token=%s" %("jcm10/cl2gmkgjt000014rstx5nmcj6",mapbox_access_token)],
	["Land & Sea Only","https://api.mapbox.com/styles/v1/%s/tiles/{z}/{x}/{y}?access_token=%s" %("jcm10/cl2glcidk000k14nxnr44tu0o",mapbox_access_token)]
	]
]

#We're going to bridge this and have shortened labels in here where applicable
md2={
	'voyage_id':'Voyage ID',
	'voyage_itinerary__imp_principal_region_slave_dis__geo_location__name':'Principal Region of Disembarkation *',
	'voyage_itinerary__imp_principal_region_of_slave_purchase__geo_location__name':'Principal Region of Purchase *',
	'voyage_captainconnection__captain__name':'Captain\'s name',
	'voyage_crew__crew_died_complete_voyage':'Crew deaths during voyage',
	'voyage_crew__crew_first_landing':'Crew at first landing of slaves',
	'voyage_crew__crew_voyage_outset':'Crew at voyage outset',
	'voyage_dates__date_departed_africa':'Date departed Africa',
	'voyage_dates__length_middle_passage_days':'Middle passage (days)',
	'voyage_dates__imp_arrival_at_port_of_dis_yyyy':'Year arrived with captives *',
	'voyage_dates__imp_length_home_to_disembark':'Days from homeport to landing (days) *',
	'voyage_itinerary__imp_port_voyage_begin__geo_location__name':'Place where voyage began *',
	'voyage_itinerary__port_of_call_before_atl_crossing__geo_location__name':'Port of call before Atlantic crossing',
	'voyage_itinerary__imp_principal_place_of_slave_purchase__geo_location__name':'Principal place of purchase *',
	'voyage_itinerary__first_place_slave_purchase__geo_location__name':'1st place of purchase',
	'voyage_itinerary__second_place_slave_purchase__geo_location__name':'2nd place of purchase',
	'voyage_itinerary__third_place_slave_purchase__geo_location__name':'3rd place of purchase',
	'voyage_itinerary__imp_principal_port_slave_dis__geo_location__name':'Principal place of landing *',
	'voyage_itinerary__first_landing_place__geo_location__name':'1st landing place',
	'voyage_itinerary__second_landing_place__geo_location__name':'2nd landing place',
	'voyage_itinerary__third_landing_place__geo_location__name':'3rd landing place',
	'voyage_itinerary__place_voyage_ended__geo_location__name':'Place voyage ended',
	'voyage_slaves_numbers__imp_total_num_slaves_embarked':'Total embarked *',
	'voyage_slaves_numbers__imp_total_num_slaves_disembarked':'Total disembarked *',
	'voyage_slaves_numbers__num_slaves_carried_first_port':'Arrived 1st port',
	'voyage_slaves_numbers__imp_mortality_during_voyage':'Mortality *',
	'voyage_slaves_numbers__imp_mortality_ratio':'Mortality ratio *',
	'voyage_ship__guns_mounted':'Guns mounted',
	'voyage_ship__ship_name':'Vessel name',
	'voyage_ship__rig_of_vessel__name':'Rig of vessel',
	'voyage_ship__imputed_nationality__name':'Ship nationality *',
	'voyage_ship__registered_place__geo_location__name':'Ship registration place',
	'voyage_ship__registered_year':'Ship registration year',
	'voyage_ship__tonnage':'Ship tonnage',
	'voyage_ship__tonnage_mod':'Ship modern tonnage',
	'voyage_ship__vessel_construction_place__geo_location__name':'Ship constructin place',
	'voyage_ship__year_of_construction':'Ship construction year',
	'voyage_outcome__outcome_owner__name':'Owner outcome',
	'voyage_outcome__vessel_captured_outcome__name':'Vessel captured outcome',
	'voyage_outcome__outcome_slaves__name':'Captives\' outcome',
	'voyage_outcome__particular_outcome__name':'Particular outcome',
	'voyage_outcome__resistance__name':'Resistance',
	'voyage_sourceconnection__source__full_ref':'Source(s)',
	'voyage_shipownerconnection__owner__name':'Owner name(s)'
}