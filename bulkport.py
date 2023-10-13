import json
import pandas as pd
import requests

url = "http://inventory-add.angelbroking.com/items/ports_inventory"

data = pd.read_excel (r'/Users/22B-MACABL-0214/PycharmProjects/angelbrokingtest/venv/lib/python3.10/Port monitorin12.xlsx')
df = pd.DataFrame(data, columns= ['ip','port','tag_name','tag_group'])
for _, data in df.iterrows():
    ip = data.ip
    port = data.port
    tag_name = data.tag_name
    tag_group = data.tag_group
    payload = json.dumps({
        'ip': ip,
        'port': port,
        'dc': 'GPX',
        'tag_name': tag_name,
        'tag_group': tag_group,
        'tag_owner': 'AMX Team',
        'description': 'AMX Ports.'
    })
    headers = {
        'Authorization': 'Bearer i2uh4iu23h4u2u252u5yiu534iu5h35uh34uh534u',
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
print(df)
