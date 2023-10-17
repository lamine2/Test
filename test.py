



intro={}
f=open("/Users/awadiop/Downloads/verification1.txt","r")
chain={}
intro={}
f=open("/Users/awadiop/Downloads/verification1.txt","r")
for l in f:
	a=l.strip("\n").split("\t")
	if a[0] == "introgression":

		file=a[1]
		sp=a[2]
		if file not in intro:
			intro[file] = [sp]
			chain[file]={}
			chain[file][sp]=a[-1]
		else:
			intro[file].append(sp)
			chain[file][sp]=a[-1]
	#print(a)


f.close()


intro2={}
f=open("/Users/awadiop/Downloads/verification2.txt","r")
for l in f:
	a=l.strip("\n").split("\t")
	if a[0] == "introgression":
		file=a[1]
		sp=a[2]
		if file not in intro2:
			intro2[file] = [sp]
		else:
			intro2[file].append(sp)
	#print(a)


f.close()


for file in intro:
	if file in intro2:
		for sp in intro[file]:
			tot+=1
			if sp in intro[file]:
				print(chain[file][sp])
				sub = chain[file][sp].split(" ")
				for st in sub:
			


h=open("/Users/awadiop/Downloads/filtered_introgression.txt","w")
compteur={}
for file in intro2:
	for sp in intro2[file]:
		if sp not in compteur:
			compteur[sp]=0
		compteur[sp]+=1
		h.write(file + "\t" + sp + "\n")
		
for sp in compteur:
	print(sp,compteur[sp])
		h.write(+ sp + "\t" + compteur[sp] "\t" + chain[file][sp] + "\n")
