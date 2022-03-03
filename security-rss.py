import json
import requests

def get_api_key():
    with open('./config.json', 'r') as f:
        data = json.load(f)
    apikey = data["api-key"]
    return apikey

# Save to files
def write_to_file(obj, filename):
    with open(filename, 'w') as f:
        f.write(json.dumps(obj, indent=4, separators=(',',':')))

def get_rss_cves():
    apikey = get_api_key()
    url = "https://services.nvd.nist.gov/rest/json/cves/1.0/"
    #header = {"API-Key" : apikey} # may not need this
    response = requests.get(url).json()
    list_of_returned_cves_dictionary = {}
    for count in enumerate(response['result']['CVE_Items']):
        cve_id = response['result']['CVE_Items'][count[0]]['cve']['CVE_data_meta']['ID']
        cve_description = count[1]['cve']['description']['description_data'][0]['value']
        reference_url = count[1]['cve']['references']['reference_data'][0]['url']
        
        list_of_returned_cves_dictionary[count[0]] = [cve_id, cve_description, reference_url]

    write_to_file(list_of_returned_cves_dictionary, "rssfeed.json")

get_rss_cves()