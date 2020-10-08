from flask import Flask, request,redirect, url_for,render_template, jsonify
from createdata import createdata
import pandas as pd
import json
from modern import adreslist
app = Flask(__name__,static_url_path='/static')

cities=['Unknown' , 'Adana', 'Adıyaman', 'Afyon', 'Ağrı', 'Amasya', 'Ankara', 'Antalya', 'Artvin',
'Aydın', 'Balıkesir', 'Bilecik', 'Bingöl', 'Bitlis', 'Bolu', 'Burdur', 'Bursa', 'Çanakkale',
'Çankırı', 'Çorum', 'Denizli', 'Diyarbakır', 'Edirne', 'Elazığ', 'Erzincan', 'Erzurum', 'Eskişehir',
'Gaziantep', 'Giresun', 'Gümüşhane', 'Hakkari', 'Hatay', 'Isparta', 'Mersin', 'İstanbul', 'İzmir',
'Kars', 'Kastamonu', 'Kayseri', 'Kırklareli', 'Kırşehir', 'Kocaeli', 'Konya', 'Kütahya', 'Malatya',
'Manisa', 'Kahramanmaraş', 'Mardin', 'Muğla', 'Muş', 'Nevşehir', 'Niğde', 'Ordu', 'Rize', 'Sakarya',
'Samsun', 'Siirt', 'Sinop', 'Sivas', 'Tekirdağ', 'Tokat', 'Trabzon', 'Tunceli', 'Şanlıurfa', 'Uşak',
'Van', 'Yozgat', 'Zonguldak', 'Aksaray', 'Bayburt', 'Karaman', 'Kırıkkale', 'Batman', 'Şırnak',
'Bartın', 'Ardahan', 'Iğdır', 'Yalova', 'Karabük', 'Kilis', 'Osmaniye', 'Düzce']

@app.route('/')
def index():
    return render_template("index.html", cities=cities)


@app.route('/ssearch', methods=['POST', 'GET'])
def process():
    name=request.form["locname"]
    city=request.form["City"]
    modern=eval(request.form["Modern"])
    result=createdata (name,city,modern)
    try:
        coordinates=str(result["Getty Coordinates"][0]).replace(",", "%2C")
    except:
        try:
            coordinates=str(result["Google Coordinates"][0])[1:-1].replace(",", "%2C")
        except: coordinates=False
    table=result.to_html(index_names=False)
    return render_template("s_result.html", table=table, coordinates=coordinates, gettyid=result["Getty ID"][0])

@app.route('/msearch', methods=['POST', 'GET'])
def msearch():
    data=request.files["data"]
    df=pd.read_excel(data)
    df_result=pd.DataFrame()
    for i in range(len(df)):
        name=df.iloc[i,0]
        city=df.iloc[i,1]
        modern=(df.iloc[i,2])
        df_append=createdata(name,city,modern)
        df_result=pd.concat([df_result, df_append], ignore_index=True)
    table=df_result.to_html(index_names=False)
    global exceldownload
    exceldownload=df_result
    df_result.to_excel("static/results.xlsx", index=False)
    return  render_template ("m_results.html", table=table)

@app.route('/modern/<adm1>.json')
def modern(adm1):
    entry=adm1.split("-")
    if entry[-1]=="END":
        end=True
    else:
        end=False
    if entry[0]=="TUR":
        entry=[]
    liste=adreslist(entry,end=end)
    return jsonify(liste)


if __name__=="__main__":
    app.run(host='0.0.0.0',debug=True)
