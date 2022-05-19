import requests

# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "ZU5CROQ7Q_wFqmHrCTCzb5Amc2oRRgRZ8q-Nm4krNaTb"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey": API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

# NOTE: manually define and pass the array(s) of values to be scored in the next line
payload_scoring = {"input_data": [{"field": [['at','v','ap','rh']], "values": [[14.96,41.76,1024.07,73.17]]}]}

response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/2838ab87-1193-450b-9047-912f6e393058/predictions?version=2022-03-06')
print("Scoring response")

print(response_scoring.json())
predictions =response_scoring.json()
print(predictions)
print('Final Prediction Result',predictions['predictions'][0]['values'][0][0])
