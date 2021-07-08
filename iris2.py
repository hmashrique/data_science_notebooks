import dash
import dash_core_components as dcc 
import dash_html_components as html 
import pandas
import plotly.graph_objs as go

df = pandas.read_csv('/Users/vphan/Dropbox/datasets/iris.csv')

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.layout = html.Div(children=[
	html.H1(children='Iris'),
	html.Div(children='''
		A demo of Dash (Plotly)	
	'''),
	dcc.Graph(
		id='iris-graph',
		figure={
			'data': [
				go.Scatter(
					x = df[ df.Species == 'setosa' ].SepalWidth,
					y = df[ df.Species == 'setosa' ].SepalLength,
					mode = 'markers',
					name = 'setosa',
				),
				go.Scatter(
					x = df[ df.Species == 'versicolor' ].SepalWidth,
					y = df[ df.Species == 'versicolor' ].SepalLength,
					mode = 'markers',
					name = 'versicolor',
				),				
				go.Scatter(
					x = df[ df.Species == 'virginica' ].SepalWidth,
					y = df[ df.Species == 'virginica' ].SepalLength,
					mode = 'markers',
					name = 'virginica',
				),				
			],
			'layout': go.Layout(
				title = 'Iris dataset',
			),
		}
	)
])

if __name__ == '__main__':
	app.run_server(debug=True)