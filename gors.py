import requests
import json
import os
import sys

print('''
 __   __   __   __  
/ _` /  \ |__) /__` 
\__> \__/ |  \ .__/ 

GitHub Organization Repositories Scanner by @thwinhtet_                    
	''')
if len(sys.argv) == 1:
	print('Usage : python3 gors.py <OrgName>')

	exit()
	
if sys.argv[1] == '-h' or sys.argv[1] == '--help':
	print('Usage : python3 gors.py <OrgName>')
	exit()
else:
	org_name = sys.argv[1]

clonable_gits = []
print(f"\nWe are going to collect the git repos which are not forked by the organization and are public.\n{'-'*15}\nForked? : False\nPrivate? :False\n{'-'*15}")
requests = requests.get(f'https://api.github.com/orgs/{org_name}/repos').text
json_obj = json.loads(requests)

#json_formatted_str = json.dumps(json_obj,indent=2)
f = open(f'{org_name}-public-repos.txt','w')

for i in json_obj:
	if i['private'] == False and i['fork'] == False:

		f.write(f"{i['clone_url']}\n")
		print(f"{i['clone_url']}")
		clonable_gits.append(i['clone_url'])

print(f'\n{"-"*100}\n[*] These gits are stored at {org_name}-public-repos.txt in the current directory.\n[*] We are going to run Trufflehog.\n{"-"*100}\n')

#print(clonable_gits)

for i in clonable_gits:
	print(i)
	os.system(f"/usr/bin/trufflehog git --concurrency 30 {i}")
	print('-'*100)
