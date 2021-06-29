# Add the functions in this file

import json
import math

def load_journal(name):
	f=open(name,)
	data = json.load(f)
	f.close()
	return data
	
def compute_phi(name,event):
	data = load_journal(name)
	n11=n00=n10=n01=n1p=n0p=np1=np0=0
	for i in data:
		if event in i['events']:
			n1p += 1
			if i['squirrel'] == True:
				np1 += 1
				n11 += 1
			else:
				np0 += 1
				n10 += 1
		else:
			n0p += 1
			if i['squirrel'] == True:
				np1 += 1
				n01 += 1
			else:
				np0 += 1
				n00 += 1
		
	return (n11*n00 - n10*n01) / math.sqrt(n1p*n0p*np1*np0)
	
def compute_correlations(name):
	data = load_journal(name)
	dic = {}
	for i in data:
		for event in i['events']:
			if event not in dic.keys():
				dic[event] = compute_phi(name,event)
	return dic

def diagnose(name):
	dic = compute_correlations(name)
	ma=max(dic, key=dic.get)
	mi=min(dic, key=dic.get)
	return ma,mi
def main():
	print(diagnose('journal.json'))
	
if __name__ == "__main__":
	main()
