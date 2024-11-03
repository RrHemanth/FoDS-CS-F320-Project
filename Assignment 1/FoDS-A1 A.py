#importing libraries
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import beta

#Taking Input of parameters of Beta Distribution and number of surveys
print("Enter the assumed Beta distribution :")
a = int(input("a :"))
b = int(input("b :"))
n = int(input("Number of surveys :"))
x = np.linspace(0, 1.0, 100)
y = beta.pdf(x, a, b)
plt.plot(x, y, label='Assumed distribution')

#Taking Input of Survey results to plot posterior probababilities of s
for i in range(n-1):
	print("Enter results of survey " + (i+1) + " :")
	c = int(input("Liked by :"))
	d = int(input("Disliked by :"))
	a += c
	b += d
	y = beta.pdf(x, a, b)
	plt.plot(x, y, label='After survey ' + (i+1) + ' :')

#Printing graph
plt.xlabel("x")
plt.ylabel("y-Prob.")
plt.title("Distribution")
plt.legend()
plt.show()