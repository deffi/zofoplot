from elements import Chart
from renderer.dumper import Dumper
 
# Create a chart with some series
chart = Chart(None)
chart.create_series(["even"], "square", x = [-2, -1, 0, 1, 2, 3], y = [4,1,0,1,4,9])
chart.create_series(["odd" ],           x = [-1, 0, 1, 2]       , y = [-1, 0, 1, 8])
 
# Set the styles directly
chart.style.background_color = "white"
chart.serien[0].style.color = "red"
 
# Show the chart with all properties
Dumper().dump(chart)
 
# Set a style sheet
 
# Render the chart
