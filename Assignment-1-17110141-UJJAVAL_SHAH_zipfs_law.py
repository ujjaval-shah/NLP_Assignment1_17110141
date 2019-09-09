import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

## following values are taken from eng.txt and https://dictionary.cambridge.org/dictionary/english/  E.G. 91 is rank of word "time" which has 15 meanings
m=[15, 4, 11, 2, 2, 4, 2, 1, 1, 2, 2, 6, 1, 3, 2, 1, 1, 3, 3, 4]
r=[91, 598, 1509, 2004, 2127, 2509, 3352, 4064, 4908, 5880, 6890, 7447, 7452, 7963, 9803, 9815, 13754, 15794, 18254, 30445]


arrx=["time","god","return","drama","conference","leader","request","resign","elimination","assault","currency","smoke","sky","motion","submit","strategy","yelling","surprises","process","adopt"]
# arry=[m[i]*((len(arrx[i]))**(1/2)) for i in range(20)]

arrm = m
arry = [(m[i]*((len(arrx[i]))**(1/2))) for i in range(20)]

def func(x,a):
	return(a)

param, param_cov=curve_fit(func, [i for i in range(1,21)], arry)
print("Curve Fitting Constant Line:")
print("y="+str(param[0]))
plt.plot([param[0] for i in range(21)],"r")
plt.scatter(arrx, arry)
plt.xticks(rotation=30)
plt.title("zipf's law: m*(L)^1/2 for random 20 words")
plt.ylabel("m*((L)^1/2)  [constant value]")
plt.xlabel("randomly picked words")
plt.subplots_adjust(bottom=0.20)
plt.show()