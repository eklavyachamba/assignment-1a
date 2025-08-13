#Name-Eklavya Chauhan, Roll no-2311067
#Ques1
import numpy as np
import matplotlib.pyplot as plt

def random_generator(c, x0, n):
    x=np.zeros(n)  #creates now numpy array with n zeros
    x[0]=x0
    for i in range(1, n):
        x[i] = c * x[i-1] * (1 - x[i-1]) 
    return x    # changes the value of list x to the new value of x[i] at each iteration
# Parameters
x0 = 0.1
n = 10000
cvalue = [1.9, 2.7, 3.7, 4.0, 4.4]
kvalue = [5, 10, 15, 20]


for c in cvalue:
    x = random_generator(c, x0, n)
    print(x)
    for k in kvalue:
        plt.figure()
        plt.scatter(x[:-k], x[k:], s=1) # makes a scatter plot s=1 sets the size of the points in the scatter plot
        plt.xlabel("$x_i$")
        plt.ylabel(f"$x_{{i+{k}}}$")
        plt.title(f"Output Map: c= {c}, k={k}")
        plt.grid(True)
        plt.show()

#Ques2
def lcg(a, c, m, seed, n):
    Numbers=[]
    x=seed
    for j in range(n):
        x= (a * x + c) % m # Linear Congruential Generator formula
        Numbers.append(x) # appends the generated number to the list
    return Numbers # returns the list of generated numbers
a = 1103515245
c = 12345
m = 32768
seed= 1
k=5

nums = np.array(lcg(a, c, m, seed, n))


plt.scatter(nums[:-k], nums[k:], s=1) # makes a scatter plot s=1 sets the size of the points in the scatter plot
plt.grid(True)
plt.xlabel("$x_i$")
plt.ylabel(f"$x_{{i+{k}}}$")
plt.title("LCG Random Numbers (k=5)")
plt.show()