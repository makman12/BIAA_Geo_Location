import pandas as pd
getty=pd.read_excel("api/Data/getty.xlsx")

from math import sin, cos, sqrt, atan2, radians
def distance(xy1,xy2):
    x1=xy1[0]
    y1=xy1[1]
    x2=xy2[0]
    y2=xy2[1]
    R = 6373.0

    lat1 = radians(x1)
    lon1 = radians(y1)
    lat2 = radians(x2)
    lon2 = radians(y2)

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c
    return distance

def getcoo(x):
    x=x.split(",")
    x=list(map(float,x))
    return x

def getgetty(Name, Coordinates,deneme=getty):
    Name=Name.split(" ")[0]
    results=[]
    deneme["Distance"] = deneme["X Y"].map (getcoo)
    deneme["Distance"] = deneme["Distance"].map (lambda x: distance (Coordinates, x))
    deneme = deneme.sort_values ("Distance")
    yakın = deneme['Distance'] < 10
    deneme=deneme[yakın]
    deneme["Subs"]= deneme["Butun Adları"].str.find(Name)
    searchname=deneme["Subs"]>-1
    searchname=deneme[searchname]
    if Name!=" " and len(searchname)>0 :
        yeradı = searchname.iloc[0, 3]
        id = searchname.iloc[0, 2]
        bad = searchname.iloc[0, 4]
        cord=searchname.iloc[0, -4]
        results.append([id,yeradı,bad,cord])
    else:
        yeradı = deneme.iloc[0, 3]
        id = deneme.iloc[0, 2]
        bad = deneme.iloc[0, 4]
        cord=deneme.iloc[0, -4]
        results.append([id,yeradı,bad,cord])



    return results

def gettytype(Type,Coordinates,deneme=getty):
    thisdict = {"City": "300387064"}
    key=thisdict[Type]
    results=[]
    deneme["Distance"] = deneme["X Y"].map (getcoo)
    deneme["Distance"] = deneme["Distance"].map (lambda x: distance (Coordinates, x))
    deneme = deneme.sort_values ("Distance")
    deneme["Subs"]= deneme["Yer Tipi"].str.find(key)
    searchname=deneme["Subs"]>-1
    deneme=deneme[searchname]
    yeradı = deneme.iloc[0, 3]
    id = deneme.iloc[0, 2]
    bad = deneme.iloc[0, 4]
    results.append([id,yeradı,bad])
    return results