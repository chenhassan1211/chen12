from cnvrgv2 import Cnvrg
cnvrg = Cnvrg()
e = Experiment()

loss_vals = []
# experiment loop:
for epoch in range(8):
    loss_vals.append(loss_func())

# attach the chart to the experiment
loss_chart = LineChart('loss')
loss_chart.add_series(loss_vals, 's1')
e.log_metric(loss_chart)
 

print("hello")
