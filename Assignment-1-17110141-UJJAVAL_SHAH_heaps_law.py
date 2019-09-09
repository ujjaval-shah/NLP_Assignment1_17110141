import enchant
import csv
import re
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

d = enchant.Dict("en_US")

with open('tweets-dataset.csv', 'r', encoding="utf-8") as f:
	reader = csv.reader(f)
	your_list = list(reader)

# print(your_list)

newlist=[]
line=""

for i in your_list:
	for j in i:
		line = j
		# line = re.sub(r"@", " ", line)
		# line = re.sub(r"#", " ", line)
		line = re.sub(r"@[^\s]*", " ", line)
		line = re.sub(r"#[^\s]*", " ", line)
		line = re.sub(r"http[^\s]*", " ", line)
		line = re.sub(r"[^A-Za-z][^A-Za-z]*", " ", line)
		newlist+=[k.lower() for k in line.split()]

dic={}

for i in newlist:
	if i in dic.keys():
		dic[i]+=1
	else:
		dic[i]=1

print()
types = len(dic)
print("Types: "+str(types))
token = len(newlist)
print("Tokens: "+str(token))
print("TTR: "+str(types/token))
print()

### Heap's law plot

count = 0

plot=[[],[]]
voc=set()
ending=0
toks=0
while(True):
	linels=[]
	for i in range(200):
		try:
			line = your_list[count*200+i][0]
			line = re.sub(r"@[^\s]*", " ", line)
			line = re.sub(r"#[^\s]*", " ", line)
			line = re.sub(r"http[^\s]*", " ", line)
			line = re.sub(r"[^A-Za-z][^A-Za-z]*", " ", line)
			linels += [j.lower() for j in line.split()]
		except:
			ending=1
	count=count+1
	for j in linels:
		toks=toks+1
		voc.add(j)
	plot[0].append(toks)
	plot[1].append(len(voc))
	if ending:
		break

def func(x,a,b):
	return(a*(x**b))

# print()
# print(len(voc))
# print()

arrx = plot[0]
arry = plot[1]
# print(len(arrx),len(arry))
param, param_cov=curve_fit(func, np.array(arrx), np.array(arry))
print("Curve Fitting Coefficients:")
print(param[0],param[1])
plt.scatter(arrx, arry)
plt.title("Heap's law: (dictionary size -> size of courpus) graph:")
plt.xlabel("size of courpus")
plt.ylabel("dictionary size")
plt.show()


# following code is useful for ZIPF's law
z=open("eng.txt","w+")
lst = sorted(dic.items(), key = lambda kv:(kv[1], kv[0]))
lst = lst[::-1]
z.write("Rank  Word  Freq\n")
for i in range(len(lst)):
	if d.check(lst[i][0]):
		z.write(str(i)+" "+lst[i][0]+" "+str(lst[i][1])+"\n")
z.close()