# import json
# def add(args):
#     with open('karyawan.json', mode='r', encoding='utf-8') as feedsjson:
#         feeds = json.load(feedsjson)
#     with open('karyawan.json', mode='w', encoding='utf-8') as feedsjson:
#         entry = {}
#         entry['name'] = args.name
#         entry['url'] = args.url
#         json.dump(entry, feedsjson)

import json
 
def write_json(new_data, filename='karyawan.json'):
    with open(filename,'r+') as file:
          
        file_data = json.load(file)
   
        file_data["rina"].append(new_data)
        
        file.seek(0)
        
        json.dump(file_data, file, indent = 4)
 
    
y = {"emp_name":"Nikhil",
     "email": "nikhil@geeksforgeeks.org",
     "job_profile": "Full Time"
    }
     
write_json(y)