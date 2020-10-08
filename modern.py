
import pandas as pd




df=pd.read_excel("api/Data/yerlesimfinal.xlsx")




def adreslist(adres, end=False,  df=df):
    level=len(adres)
    if level==0:
        sehirler=df[(df['Tipi'] == 1)]
        sehirlist=list(sehirler["YerAdi"])
        return sehirlist
    elif level==1:
        ilçeler=df[(df['Tipi'] == 2) & (df['adm_1'] == adres[0])]
        ilçelerlist=list(ilçeler["YerAdi"])
        if end:
            yer=df[(df['Tipi'] == 1) & (df['YerAdi'] == adres[0])]
            return yer.to_dict()
        else:
            return ilçelerlist
    elif level==2:
        koyler=df[(df['Tipi'] == 3) & (df['adm_1'] == adres[0]) & (df['adm_2'] == adres[1])]
        koylerlist=list(koyler["YerAdi"])
        if end:
            yer=df[(df['Tipi'] == 2) & (df['adm_1'] == adres[0]) & (df['YerAdi'] == adres[1])]
            return yer.to_dict()
        else:
            return koylerlist
    elif level==3:
        yer=df[(df['Tipi'] == 3) & (df['adm_1'] == adres[0]) & (df['adm_2'] == adres[1]) & (df['YerAdi'] == adres[2])]
        return yer.fillna(0).to_dict("r")
    else:
        raise("Invalid list")




