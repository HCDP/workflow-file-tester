import json
from tapipy.tapis import Tapis

# Load config data from json files
with open('config.json', 'r') as configfile:
    configData = json.load(configfile)
    
# Load the upload.json config file 
# ADD NEW CODE HERE

# Create tapis instance
t = Tapis(base_url=configData["tapis_instance"]["base_url"], username=configData["tapis_instance"]["username"], password=configData["tapis_instance"]["password"], tenant_id=configData["tapis_instance"]["tenant_id"])

# Generate access token
t.get_tokens()

# Read the upload field and loop through each entry
# for each entry construct a new path for a file by combining the remote_path field with the rename field with a back slash between them
# replace each occurence of %y, %m, %d with the correpsonding current year, month or day
# then using the Tapis Files API check the existence of the newly created filepathed filename and that it's size is > 0

# Access the file system
tapis_files = t.files.listFiles(systemId="SYSTEM_ID_GOES_HERE", path="NEW_PATH_GOES_HERE")
for ts in tapis_files:
    if ts.size > 0 and ts.type == "file":
        print("this file exists with path: " + ts.path + " size: " + str(ts.size))
     
# If the filepath doesn't exist or the file size is 0 generate an email notification
