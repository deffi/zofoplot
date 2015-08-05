from element import *

chart = Chart()
chart.add_series(Series(["even"], x = [-2, -1, 0, 1, 2, 3], y = [4,1,0,1,4,9]))
chart.add_series(Series(["odd" ], x = [-1, 0, 1, 2]       , y = [-1, 0, 1, 8]))

chart.dump()

# Create a chart with some series

# Set the styles directly
# Set a style sheet

# Render the chart