from tapipy.tapis import Tapis
import tapipy.errors

#checks that size of file is >0
#returns None if size >0
#assumes that there is only 1 file in each dir
def not_zero(file, tapis_list):
    ts = tapis_list[0]
    if ts.size > 0 and ts.type == "file":
        return None
    else:
        return 'File is size 0'
            

#checks that file exists and is size >0
#returns issue with file or None if no issues           
def exists(file, t):
    try:
        tapis_list = t.files.listFiles(systemId=file['system_id'], path=file['new_path'])
    except tapipy.errors.NotFoundError:
        return 'File not found'
    else:
        return not_zero(file, tapis_list)