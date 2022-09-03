import pymongo
client = pymongo.MongoClient("mongodb+srv://sagar:sagar1234@mongo-cluster.inx6mzk.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    'name':'sagar',
    'email':'sagar@gmail.com',
    'subject' : ['data science', 'data analytics', 'data flow']
}

list_of_records = [
    {'companyName': 'iNeuron',
     'product': 'Affordable AI',
     'courseOffered': 'Machine Learning with Deployment'},

    {'companyName': 'iNeuron',
     'product': 'Affordable AI',
     'courseOffered': 'Deep Learning for NLP and Computer vision'},

    {'companyName': 'iNeuron',
     'product': 'Master Program',
     'courseOffered': 'Data Science Masters Program'}
]

#SQL:   Database >> Tables
#mongo: Database >> Collection

db1 = client['mongotest']   #database
coll = db1['test']          #collection

#coll.insert_one(d)
#coll.insert_many(list_of_records)

#data1 = {"packetType":"D","data":{"checkEngineLightFlag":"F","batteryVoltageStableTime":0,"batteryVoltageStable":"0","batteryVoltageOff":"12.42","batteryCrankParamTN":"-0.08","batteryCrankParamVN":"0.00","batteryCrankParamTP":"-0.08","batteryCrankParamVP":"0.00","batteryCrankParamTT":"-0.00008","batteryCrankParamV0":"0.00","batteryVoltageMaxOn":"13.05","batteryVoltageMinOn":"12.97","batteryVoltageMaxOff":"12.46","batteryVoltageMinOff":"12.36","batteryVoltageOnAverage":"13.02","engineLoadMax":"84","engineLoadAverage":"39.98","rpmMax":"3487","rpmAverage":"1431.29","gpsSpeedAverage":"21.99","vssMax":"53.44","vssAverage":"23.06","tcuTemperatureMin":"82.40","tcuTemperatureMax":"109.40","tcuTemperatureAverage":"104.87","coolantMin":"158.00","coolantMax":"188.60","coolantAverage":"180.20","packetStartLocal":1508143346000,"tripStartLocal":1508143346000,"milIndicator":"F","monitorsNotReady":0,"imei":"60DF5417","gatewayTs":1515613306592,"diagnosticTroubleCodeData":[345345],"diagnosticPidData":[[64768,47,100],[64768,1,517376],[64800,1,262144],[64768,5,125]]},"header":{"iwrapVer":"1.9.20","sourceSystem":"CDP","configVer":"1.1","oemName":"HUM","unitType":0,"cpVer":"7.50.1.9","igpsVer":"1.3.7","messageType":"Notification","pomVer":"1.0","headerVer":"V6","timestamp":0,"deviceType":"InDrive","visorVer":"1.4.35","transactionId":"53098471-7787-4160-94b3-cd69dcc70416","deviceSerialNo":"60DF5417","subOrganization":"HUM","organization":"HUM","imei":"60DF5417","operation":"Notification"}}

coll1 = db1['dpkt']

#coll1.insert_one(data1)

extract = coll.find()
extract1 = coll.find({'companyName': 'iNeuron'})
extract2 = coll1.find()
extract3 = coll.find({'courseOffered':{'$gt':'E'}}) #extract greater than

print('         all coll data')
for i in extract:
    print(i)

print('         coll data with filter')
for i in extract1:
    print(i)

print('         all coll2 data')
for i in extract2:
    print(i)

print('         coll data with advance filter')
for i in extract3:
    print(i)