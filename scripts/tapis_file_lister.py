import json
import os
from tapipy.tapis import Tapis
import tapipy.errors
import update_date_string
import check_file
import message

# Get the current dir of the script file
current_dir = os.path.dirname(os.path.abspath(__file__))
    
# Load the upload.json config file 
if (os.path.exists(os.path.join(current_dir, '../data/upload.json'))):
    upload_path = os.path.join(current_dir, '../data/upload.json')
else:
    upload_path = os.path.join(current_dir, '../data/default.json')
with open(upload_path, 'r') as upload_file:
    upload_data = json.load(upload_file)

# Create tapis instance
t = Tapis(base_url=os.environ.get('TAPIS_BASE_URL'), username=os.environ.get('TAPIS_USERNAME'), password=os.environ.get('TAPIS_PASSWORD'), tenant_id=os.environ.get('TAPIS_TENANT_ID'))

# Generate access token
t.get_tokens()

# Create list of files from upload.json
upload_list = upload_data['upload']
missing_list = []

# Replace %y, %m, %d with current year, month, day
# Uses yesterday's date to conform with file upload schedule
# Create new_path from combining remote_path and rename
for e in upload_list:
    remote_path = update_date_string.update(e['remote_path'])
    rename = update_date_string.update(e['rename'])
    system_id = e['system_id']
    
    new_path = remote_path + '/' + rename
    
    e['new_path'] = new_path
    e['file_found'] = False
    e['error_message'] = ''

# Check if each file exists and is not 0 size
# If doesn't exist or is 0 size add to missing list and with appropriate error message
for e in upload_list:
    error_message = check_file.exists(e, t)
    
    if error_message == None:
        e['file_found'] = True
    else:
        e['error_message'] = error_message
        missing_list.append(e)

# If files not found, email missing file details and error message
if len(missing_list) != 0:
    message.send_email(missing_list)
else:
    print('No issues found')