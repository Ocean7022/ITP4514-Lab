import torch
import pyro

def marks():
    lab0 = pyro.sample('Lab Completion', pyro.distributions.Bernoulli(0.6))
    lab = 'Lab completed' if lab0.item() == 1.0 else 'Lab not completed'
    mean_mark = {'Lab completed': 70.0, 'Lab not completed': 55.0}[lab]
    scale_mark = {'Lab completed': 5.0, 'Lab not completed': 10.0}[lab]
    mark = pyro.sample('Exam Mark', pyro.distributions.Normal(mean_mark, scale_mark))
    return lab, mark.item()


for _ in range(30):
    print(marks())