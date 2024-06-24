from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run_code', methods=['POST'])
def run_code():
    url = "https://sbx-nxos-mgmt.cisco.com/ins"
    switchuser = 'admin'
    switchpassword = 'Admin_1234!'

    headers = {"Content-Type": "application/json-rpc"}
    payload = [{
        "jsonrpc": "2.0",
        "method": "cli",
        "params": {
            "cmd": "show interface brief",
            "version": 1
        },
        "id": 1
    }]

    response = requests.post(url, headers=headers, data=json.dumps(payload), auth=(switchuser, switchpassword), verify=False)

    if response.status_code == 200:
        output_data = json.dumps(response.json(), indent=4)
    else:
        output_data = f"Error: {response.status_code}"

    return output_data

@app.route('/run_data', methods=['POST'])
def run_data():
    url = "https://sbx-nxos-mgmt.cisco.com/ins"
    switchuser = 'admin'
    switchpassword = 'Admin_1234!'

    headers = {"Content-Type": "application/json-rpc"}
    payload = [{
        "jsonrpc": "2.0",
        "method": "cli",
        "params": {
            "cmd": "show hardware",
            "version": 1
        },
        "id": 1
    }]

    response = requests.post(url, headers=headers, data=json.dumps(payload), auth=(switchuser, switchpassword), verify=False)

    if response.status_code == 200:
        output_data = json.dumps(response.json(), indent=4)
    else:
        output_data = f"Error: {response.status_code}"

    return output_data

@app.route('/run_non-vlan', methods=['POST'])
def run_non_vlan():
    url = "https://sbx-nxos-mgmt.cisco.com/ins"
    switchuser = 'admin'
    switchpassword = 'Admin_1234!'

    headers = {"Content-Type": "application/json-rpc"}
    payload = [{
        "jsonrpc": "2.0",
        "method": "cli",
        "params": {
            "cmd": "show interface brief",
            "version": 1
        },
        "id": 1
    }]

    response = requests.post(url, headers=headers, data=json.dumps(payload), auth=(switchuser, switchpassword), verify=False)

    if response.status_code == 200:
        interfaces = response.json()["result"]["body"]["TABLE_interface"]["ROW_interface"]
        
        null_vlan_interfaces = [interface for interface in interfaces if interface.get("vlan", "").strip() == ""]
        
        if null_vlan_interfaces:
            output_data = json.dumps(null_vlan_interfaces, indent=4)
        else:
            output_data = "No interfaces with null or empty VLAN found."
    else:
        output_data = f"Error: {response.status_code} - {response.text}"
    return output_data

if __name__ == '__main__':
    app.run(debug=True)
