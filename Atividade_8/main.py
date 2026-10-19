import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate
import random
from scipy.optimize import brentq
from scipy.optimize import curve_fit
from scipy.special import erfcinv

##### Problema 1 #####

with open('decay.txt', 'r') as f:
  lines = (line.strip() for line in f if line)
  t = [float(line) for line in lines]

figure, axis = plt.subplots(ncols=2, figsize=(12, 6))
axis[0].hist(t, bins=50)
axis[0].set(xlabel='t [s]', ylabel='N')
axis[0].set_title("Histogram")

counts_obs, bin_edges_obs = np.histogram(t, 50)
bin_centres_obs = (bin_edges_obs[:-1] + bin_edges_obs[1:]) / 2.
err = np.sqrt(counts_obs)

axis[1].set_title("Histogram with error bars")
axis[1].errorbar(bin_centres_obs, counts_obs, yerr=err, fmt='o')
axis[1].set(xlabel='t [s]', ylabel='N')

plt.savefig("E2_Problem_1.pdf")
plt.clf()

##### Problema 2 #####

def decay_pdf (t, tau) :
  return (1./ tau) * np . exp(-1.0*t / tau)
x = np.linspace(0. ,10. ,1000)
f1 = decay_pdf(x ,1.0)
f2 = decay_pdf(x ,2.0)
f3 = decay_pdf(x ,0.5)

plt.plot(x ,f1 ,label =r"$\tau$ = 1.0")
plt.plot(x ,f2 ,label =r"$\tau$ = 2.0")
plt.plot(x ,f3 ,label =r"$\tau$ = 0.5")
plt.xlabel('t [s]')
plt.ylabel('N')
plt.legend(loc = "upper right")
plt.savefig("E2_Problem_2.pdf")
plt.clf()

###### Problema 3 ######

def Likelihood(tau, N, sum_t):
    return pow((1 / tau), N)*np.exp(-sum_t / tau)

x = np.linspace(0.5, 1.5, 1000)
l = Likelihood(x, 1, 1.0)

plt.plot(x, l)
plt.xlabel(r'$\tau$ [s]')
plt.ylabel(r'L($\tau$)')
# plt.title(r'Likelihood para $t_1 = 1.0$ s')
plt.savefig("E2_Problem_3.pdf")
plt.clf()

##### Problema 4 #######

def lnL(tau, N, sum_t):
    return -2.0*N*np.log(tau) - 2.0*sum_t/tau

x = np.linspace(1.0, 2.5, 1000)
logLikelihood = lnL(x, len(t), sum(t))

plt.plot(x, logLikelihood)
plt.xlabel(r'$\tau$ [s]')
plt.ylabel(r'-2lnL($\tau$)')
plt.savefig("E2_Problem_4.pdf")
plt.clf()

index = np.argmax(np.array(logLikelihood))
tau_hat = x[index]
print(f"Maximum likelihood estimator for mean lifetime is = {round(tau_hat, 4)} s")

##### Problema 5 ######

def moved_lnL(tau):
   return lnL(tau, len(t), sum(t)) - logLikelihood[index] + 1.0
sigma_down = tau_hat - brentq(moved_lnL, 1.0, tau_hat)
sigma_up = brentq(moved_lnL, tau_hat, 1.5) - tau_hat
print(f"Sigma up uncertainty: {round(sigma_up, 4)} s" )
print(f"Sigma down uncertainty: {round(sigma_down, 4)} s\n" )

##### Problema 6 #####

def Gaussian(x, mu, sigma):
  return (1.0/(sigma*np.sqrt(2*np.pi)))*np.exp(-(x-mu)**2/(2*sigma**2))

x = np.linspace(-5, 5, 1000)
f1 = Gaussian(x, 0.0, 1.0)
f2 = Gaussian(x, 1.0, 1.0)
f3 = Gaussian(x, 0.0, 2.0)

plt.plot(x, f1, label="mu = 0, sigma = 1")
plt.plot(x, f2, label="mu = 1, sigma = 1")
plt.plot(x, f3, label="mu = 0, sigma = 2")
plt.legend(loc="upper left")
plt.savefig('E1_Problem_1.pdf')
plt.clf()

p_205 = integrate.quad(lambda x: Gaussian(x, 200.0, 2.0), 205.0, +np.inf)[0]
p_203_single = integrate.quad(lambda x: Gaussian(x, 200.0, 2.0), 203.0, +np.inf)[0]
p_203_double = p_203_single**2

print(f"Probability to produce the new particle with a mass of 205 GeV or more: {round(100 * p_205, 2)}%")
print(f"Probability to produce two particls with masses above 203 GeV: {round(100 * p_203_double, 2)}%\n")

##### Problema 7 #####

x_histo_3 = []
x_histo_30 = []
x_histo_60 = []
x_histo_100 = []

for i in range(10000):
    x_val = 0.0
    N = 3
    for j in range(N):
        x_val += np.random.exponential(scale=j + 1.0)
    x_histo_3.append(x_val / N)

    x_val = 0.0
    N = 30
    for j in range(N):
        x_val += np.random.exponential(scale=j + 1.0)
    x_histo_30.append(x_val / N)

    x_val = 0.0
    N = 60
    for j in range(N):
        x_val += np.random.exponential(scale=j + 1.0)
    x_histo_60.append(x_val / N)

    x_val = 0.0
    N = 100
    for j in range(N):
        x_val += np.random.exponential(scale=j + 1.0)
    x_histo_100.append(x_val / N)

figure, axis = plt.subplots(2, 2, constrained_layout=True)
axis[0, 0].hist(x_histo_3, bins=20)
axis[0, 0].set_title("N = 3")
axis[0, 0].set_xlabel("x")

axis[0, 1].hist(x_histo_30, bins=20)
axis[0, 1].set_title("N = 30")
axis[0, 1].set_xlabel("x")

axis[1, 0].hist(x_histo_60, bins=20)
axis[1, 0].set_title("N = 60")
axis[1, 0].set_xlabel("x")

axis[1, 1].hist(x_histo_100, bins=20)
axis[1, 1].set_title("N = 100")
axis[1, 1].set_xlabel("x")

plt.savefig('E1_Problem_2.pdf')
plt.clf()