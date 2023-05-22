import json
from tapipy.tapis import Tapis

# Load data from json files
with open('config.json', 'r') as configfile:
    configData = json.load(configfile)
with open('system_config.json', 'r') as systemconfigfile:
    storage_system = json.load(systemconfigfile)
with open('cred_tmp.json', 'r') as credentialsfile:
    credentials = json.load(credentialsfile)

# Create tapis instance
t = Tapis(base_url=configData["tapis_instance"]["base_url"], username=configData["tapis_instance"]["username"], password=configData["tapis_instance"]["password"], tenant_id=configData["tapis_instance"]["tenant_id"])

# Generate access token
t.get_tokens()

# Access the file system
tapis_files = t.files.listFiles(systemId=configData["tapis_user_credentials"]["systemId"], path=configData["tapis_user_credentials"]["list_file_path"])
for ts in tapis_files:
    if ts.size > 0 and ts.type == "file":
        print("this file exists with path: " + ts.path + " size: " + str(ts.size))
