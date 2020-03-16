from bokeh.plotting import figure
from bokeh.io import output_file,show
from bokeh.models.tools import HoverTool
from bokeh.models import ColumnDataSource, ColorBar
from bokeh.palettes import Spectral6
from bokeh.transform import linear_cmap
from bokeh.layouts import gridplot
import pandas as pd

class Plot:
    """First Lesson on Bokeh"""     
    def __init__(self):        
        print("Ploting With Bokeh")
        #create a figure object 
        self.f=figure(x_axis_type="datetime")
        #self.p=figure(x_axis_type="datetime")
        self.hover=HoverTool(formatters={'x':'datetime'})

    def plots(self,data,x,y):
        #data
        dataset=pd.read_excel(data,parse_dates=["Date"])                     
        x_axis=dataset[x]#/10       
        y_axis=dataset[y]#/10
        #z_axis=dataset[z]
        """x_scaled=[]
        y_scaled=[]
        scaler = lambda val:val/10
        for x,y in zip(x_axis,y_axis):
            x_scaled.append(scaler(x))
            y_scaled.append(scaler(y))"""
        #output
        output_file("File1.html")
        #customize plot
        #mapper = linear_cmap(field_name='y', palette=Spectral6 ,low=min(y) ,high=max(y))
        #customize hover
        self.hover.tooltips=[('x Value','@x{%F}'),('y Value','@y')]
        self.f.add_tools(self.hover)
        #self.p.add_tools(self.hover)
        #add features to figure     
        self.f.title.text="Olatunji's Plot"
        self.f.title.text_color="Gray"
        self.f.title.text_font="times"
        self.f.title.text_font_style="bold"
        self.f.xaxis.minor_tick_line_color=None
        self.f.yaxis.minor_tick_line_color=None
        self.f.xaxis.axis_label="XLabel"
        self.f.yaxis.axis_label="YLabel" 

        #pass x and y variables into figure
        self.f.line(x_axis,y_axis,color='red',alpha=0.5)
        #self.p.line(x_axis,z_axis,alpha=0.5,color='red')
        #gp=gridplot([self.f,self.p])
        #show(gp)
        show(self.f)
    
    def otherStuff(self):
        print(dir(self.f))

plot=Plot()
plot.plots("Data.xlsx",'Date','Close/Last')
#plot.otherStuff()
