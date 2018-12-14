from __future__ import division,print_function
import numpy as np
import matplotlib.pyplot as plt
"""
must copy-paste in:
import scipy as sp
import numpy.linalg as npla
import scipy.linalg as spla
"""

import subprocess
import collections

PlotData = collections.namedtuple('PlotData', ('x', 'y', 'format', 'label') )

def makePlot(title, xlabel, ylabel, iterableOfPlotData,
             filename=None, loglog=False,
             legendloc=0):
  fig = plt.figure()
  plt.xlabel(xlabel, figure=fig)
  plt.ylabel(ylabel, figure=fig)
  plt.title(title, figure=fig)
  if loglog: plotFunc = plt.loglog
  else: plotFunc = plt.plot
  for data in iterableOfPlotData:
    if len(data) == 2:
      plotFunc(data[0], data[1])
    else:
      data = PlotData._make(data)
      if data.format is None: plotFunc(data.x, data.y, label=data.label)
      else: plotFunc(data.x, data.y, data.format, label=data.label)
  # plt.legend must be after plots exist to get their labels
  # could pass **kwargs to makePlot and pass on
#  plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3)
  plt.legend(loc=legendloc)
  if filename is not None:
    assert(filename[-4:] == '.pdf')
    plt.savefig(filename)
    subprocess.call( ('pdfcrop', filename, filename) )
  plt.show()

"""
character 	description
'-' 	solid line style
'--' 	dashed line style
'-.' 	dash-dot line style
':' 	dotted line style
'.' 	point marker
',' 	pixel marker
'o' 	circle marker
'v' 	triangle_down marker
'^' 	triangle_up marker
'<' 	triangle_left marker
'>' 	triangle_right marker
'1' 	tri_down marker
'2' 	tri_up marker
'3' 	tri_left marker
'4' 	tri_right marker
's' 	square marker
'p' 	pentagon marker
'*' 	star marker
'h' 	hexagon1 marker
'H' 	hexagon2 marker
'+' 	plus marker
'x' 	x marker
'D' 	diamond marker
'd' 	thin_diamond marker
'|' 	vline marker
'_' 	hline marker
The following color abbreviations are supported:
character 	color
b 	blue
g 	green
r 	red
c 	cyan
m 	magenta
y 	yellow
k 	black
w 	white
In addition, you can specify colors in many weird and wonderful ways, including full names ('green'), hex strings ('#008000'), RGB or RGBA tuples ((0,1,0,1)) or grayscale intensities as a string ('0.8'). Of these, the string specifications can be used in place of a fmt group, but the tuple forms can be used only as kwargs.

You do not need to use format strings, which are just abbreviations. All of the line properties can be controlled by keyword arguments. For example, you can set the color, marker, linestyle, and markercolor with:
plot(x, y, color='green', linestyle='dashed', marker='o',
     markerfacecolor='blue', markersize=12)

If you make multiple lines with one plot command, the kwargs apply to all those lines, e.g.:
plot(x1, y1, x2, y2, antialised=False)
"""
