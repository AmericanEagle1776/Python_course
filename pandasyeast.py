import pandas as pd 

df = pd.read_csv('./my_yeast_genome.tsv', sep="\t", names = ['organism', 'id', 'sys', 'standard', 'function', 'sequence', 'gene length', 'seq mrna', 'mrna length'])

print(df.head())
print()
print(df.columns)
print()
print('shape is:', df.shape)
print()

#avmrnalen = df['mrna length'].sum()/df.shape[0] 
#possible is np.mean(df['mrna length'])
avmrnalen = df['mrna length'].mean()
print('average mrna length of yeahboy is:', avmrnalen)
print()

ACount = 0

for row in df['sequence']:
	for char in row:
		if char == 'A':
			ACount += 1

print('no of A in coding genome', ACount)
print()
dupcount = 0
for true in df.duplicated():
	if true:
		dupcount +=1
print('amount of duplicate rows:', dupcount )
print()

