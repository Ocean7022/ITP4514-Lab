import torch
import torch.distributions.constraints as constraints
import pyro
import pyro.distributions as dist
from pyro.optim import Adam
from pyro.infer import SVI, Trace_ELBO

observations = torch.tensor([61.5, 67.0, 63.6, 62.4, 66.8])

def model(observations):
    weight_prior = dist.Uniform(60.0, 70.0)   
    weight = pyro.sample("weight", weight_prior)
    
    my_dist = dist.Normal(weight, 1.5)
    
    for i, obs in enumerate(observations):
        measurement = pyro.sample(f'obs_{i}', my_dist, obs=obs)

def guide(observations):

    mean_parameter = pyro.param("mu", torch.tensor(65.0))
    std_parameter = pyro.param("sigma", torch.tensor(1.5), constraint=constraints.positive)
    
    weight_distribution = dist.Normal(mean_parameter, std_parameter)    
    weight = pyro.sample("weight", weight_distribution)

pyro.clear_param_store()

svi = SVI(model=model,
          guide=guide,
          optim=Adam({"lr": 0.0005}),
          loss=Trace_ELBO())

n_steps = 5000
for i in range(n_steps):
    loss = svi.step(observations)
    if (i % 100 == 0):
        print(f'iter: {i}, loss: {round(loss,2)}', end="\r")

print("Body scale is %.3f +- %.3f" % (pyro.param("mu"), pyro.param("sigma")))