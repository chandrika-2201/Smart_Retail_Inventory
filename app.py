from flask import Flask,render_template,jsonify
import pandas as pd
from sklearn.cluster import KMeans
app=Flask(__name__)
def df(): return pd.read_csv("data/products.csv")
@app.route("/")
def home():
 d=df(); return render_template("index.html",p=d.to_dict("records"),
 m={"revenue":10640000,"customers":4338,"products":len(d),"low":int((d.stock<=d.reorder_level).sum()),"value":int((d.stock*d.unit_price).sum())})
@app.route("/api/forecast")
def forecast():
 d=df(); return jsonify([{"product":r.product_name,"predicted":int(max(r.reorder_level*1.15,r.stock*.75)),"action":"REORDER" if r.stock<=r.reorder_level else "MONITOR"} for r in d.itertuples()])
@app.route("/api/segments")
def segments():
 x=pd.DataFrame({"r":[8,22,45,70,12,31,55,18,90,6,40,27],"f":[42,30,18,7,35,22,12,28,4,48,15,25],"m":[5200,3900,2100,500,4400,2700,1200,3200,300,6100,1700,3000]})
 k=KMeans(n_clusters=4,random_state=42,n_init=10).fit(x); x["c"]=k.labels_
 return jsonify([{"segment":f"Segment {i+1}","customers":int((x.c==i).sum())} for i in range(4)])
@app.route("/api/insights")
def insights(): return jsonify(["Prioritize replenishment for high-demand products.","Monitor products near their reorder threshold.","Use customer segments for targeted campaigns.","Retrain forecasting when current stock and supplier lead-time data are available."])
app.run(debug=True)
