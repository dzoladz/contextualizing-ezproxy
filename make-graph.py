from graphviz import Source
import os

input_file = 'contextualizing-ezproxy' + '.dot'
output_file = 'contextualizing-ezproxy' + '.png'

os.system('dot -Tpng ' + input_file + ' -o ' + output_file)

source = Source.from_file(input_file)
source.view()
