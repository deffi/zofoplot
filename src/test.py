from elements import Chart, Series
 
# Create a chart with some series
chart = Chart(None)
chart.add_series(Series(["even"], "square", x = [-2, -1, 0, 1, 2, 3], y = [4,1,0,1,4,9]))
chart.add_series(Series(["odd" ],           x = [-1, 0, 1, 2]       , y = [-1, 0, 1, 8]))
 
# Set the styles directly
chart.style.background_color = "white"
chart.serien[0].style.color = "red"
 
# Show the chart with all properties
chart.dump()
 
# Set a style sheet
 
# Render the chart
