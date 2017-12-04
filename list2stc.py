import csv
with open("input.csv",'r') as f: indat=[i for i in csv.reader(f)]
header=indat[0]+['PolygonSTC']
body=indat[1:]
toSTC=lambda q: ['Polygon UNKNOWNFrame '+q.replace('[','').replace(']','').replace(',','')]
outdat=[i+toSTC(i[-1]) for i in body]
outdat=[header]+outdat
with open("output.csv",'w') as outfile: csv.writer(outfile).writerows(outdat)
