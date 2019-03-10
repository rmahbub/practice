from bokeh.plotting import figure, output_file, show
from bokeh.embed import components


def fig(df,title):
	plot = figure(plot_width=800, plot_height=400, x_axis_type="datetime", title=title)
	plot.yaxis.axis_label = "Closing Price"
	plot.xaxis.axis_label = "Date"
    
    #C = df
    #c1=C[1]
    #c0= pd.to_datetime(C[0])

    #plot.line(c0, c1)
	plot.line(df.index, df['closing'])

	script, div = components(plot)

    
	return script, div