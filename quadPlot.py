from bokeh.plotting import figure
from bokeh.io import output_file,show
from bokeh.models.tools import HoverTool

import pandas as pd

dataset=pd.read_excel("Sample_of_the_produced_time_values.xlsx")
xStart_= dataset['Start']
xEnd_=dataset['End']

f=figure(x_axis_type='datetime')
plot_=f.quad(top=1,bottom=0,left=xStart_,right=xEnd_,fill_color='red')


output_file('File1.html')
show(f)