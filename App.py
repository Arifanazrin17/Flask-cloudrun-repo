from flask import Flask,request,jsonify
from google.cloud import bigquery

PROJECT="acoustic-apex-469415-m0"
DATASET="Flask"
TABLE="Customer"
TABLE_REF=f"{PROJECT}.{DATASE}.{TABLE}"

app=Flask(__name__)

@app.route("/")
def home():
  return <h1>"Flask Api :)"<\h1>

@app.route("/customer")
def call_customer():
  client=bigquery.Client()
  query=""" Select * from '{TABLE_REF}' """
  job_client = client.query( query)
  results=job_client.result()
  return results

@app.route("/add")
def add_customer():
  data = request.get_json()
  id=data.get("id")
  name=data.get("name")
  phone=data.get("phone")
  dob=data.get("dob")
  query="""INSERT INTO '{TABLE_REF}'(name,phone,dob) VALUES (@name, @phone, @dob)"""
  job_client = client.query( query)
  results=job_client.result()
  return results
  
if __name__=="__main__":
  app.run(debug=True, host="0.0.0.0", port="8080")
