from tronpy import Tron
from tronpy.keys import PrivateKey
from tronpy.providers import HTTPProvider
from tronpy import keys
import pymysql
import json
import requests

### configs
TRON_ADDRESS = ''
url1 = "https://api.trongrid.io/v1/accounts/" + TRON_ADDRESS +"/transactions/trc20"
url2 = 'https://api.trongrid.io/v1/accounts/' + TRON_ADDRESS
tron_pro_api_key = ""
usdt_contract_address = "TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t"
contract_address = ""
wallet_private_key = ""
n = 0
db_host = ""
db_user = ""
db_pass = ""
db_port = 3306
db_name = ""
querystring1 = {"only_confirmed":"true","only_unconfirmed":"false","only_to":"true","only_from":"false","limit":"200","order_by":"block_timestamp,desc","contract_address":usdt_contract_address, "max_timestamp": ""}
headers1 = {"Accept": "application/json", "TRON-PRO-API-KEY": tron_pro_api_key}
### configs

response1 = requests.request("GET", url1, headers = headers1, params = querystring1)
response1 = json.loads(response1.text)

### connect to db
db = pymysql.connect(host=db_host,user=db_user,passwd=db_pass,db=db_name,port=db_port,charset='utf8')
cursor = db.cursor()
cursor.execute('SELECT * FROM `address`')
### connect to db

### init
client = Tron(HTTPProvider(api_key=tron_pro_api_key))
contract = client.get_contract(contract_address)
priv_key = keys.PrivateKey.fromhex(wallet_private_key)
### init

while True:
	while n <= len(response1["data"]) - 1:
		try:
			if int(response1["data"][n]['value']) == 500000 and int(response1["data"][n]['block_timestamp']) > 1620078000 :
				cursor.execute('SELECT * FROM `address` where tron_address = \'' + response1["data"][n]['from'] + '\'')
				results = cursor.fetchall()
				if results:
					print("地址 " + response1["data"][n]['from'] + " 存在，跳过。\n")
				else:
					print("地址 " + response1["data"][n]['from'] + " 不存在，空投。\n")
					respose2 = requests.request("GET", url2, headers = headers1)
					respose2 = json.loads(respose2.text)
					if int(respose2['data'][0]['balance']) < 15000000:
						print("没有足够的 TRX。")
						exit()
					txn = (
						contract.functions.transfer(response1["data"][n]['from'], 10000000000)
						.with_owner(TRON_ADDRESS)
						.fee_limit(5_000_000)
						.build()
						.sign(priv_key)
						)
					txn.broadcast()
					sql = "INSERT INTO address (tron_address) VALUES ('" + response1["data"][n]['value'] + "')"
					cursor.execute(sql)
					db.commit()
		except Exception as e:
			raise
		n = n + 1
	if len(response1["data"]) == 200:
		querystring1["max_timestamp"] = response1["data"]["block_timestamp"]
		n = 0
		response1 = requests.request("GET", url1, headers = headers1, params = querystring1)
		response1 = json.loads(response1.text)
		continue
	else:
		break
