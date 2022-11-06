import json


f = open("overview.json", encoding="utf8")
data = json.load(f)
json_list = []
json_file = open("json_with_hyperlink.json","w")
count = 0
for asn_str in data:
    temp = asn_str['asn']
    asn_str['asn'] = "<button class=\"btn btn-outline-secondary btn-sm\" onClick=\"asn_details(" + str(temp) + ")\">" + str(temp) + "</button>"
    asn_str['ratio']  = asn_str['ratio']*100
    #json.dump(asn_str, json_file, indent=4, separators=(',',': '))
    json_list.append(asn_str)
    # count = count+1
    # if(count>10):
    #     break


jsonString = json.dumps(json_list, indent=4)
json_file.write(jsonString)
f.close()
json_file.close()