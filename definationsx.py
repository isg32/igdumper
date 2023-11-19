import json

def initi():
    print("""
============================================
██╗███████╗ ██████╗ ██████╗ ██████╗ ███████╗                                  
██║██╔════╝██╔════╝ ╚════██╗╚════██╗██╔════╝                                  
██║███████╗██║  ███╗ █████╔╝ █████╔╝███████╗                                  
██║╚════██║██║   ██║ ╚═══██╗██╔═══╝ ╚════██║                                  
██║███████║╚██████╔╝██████╔╝███████╗███████║                                  
╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚══════╝╚══════╝                                  
                                                                              
██╗███╗   ██╗███████╗████████╗ █████╗  ██████╗ ██████╗  █████╗ ███╗   ███╗    
██║████╗  ██║██╔════╝╚══██╔══╝██╔══██╗██╔════╝ ██╔══██╗██╔══██╗████╗ ████║    
██║██╔██╗ ██║███████╗   ██║   ███████║██║  ███╗██████╔╝███████║██╔████╔██║    
██║██║╚██╗██║╚════██║   ██║   ██╔══██║██║   ██║██╔══██╗██╔══██║██║╚██╔╝██║    
██║██║ ╚████║███████║   ██║   ██║  ██║╚██████╔╝██║  ██║██║  ██║██║ ╚═╝ ██║    
╚═╝╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝    
                                                                              
████████╗ ██████╗  ██████╗ ██╗                                                
╚══██╔══╝██╔═══██╗██╔═══██╗██║                                                
   ██║   ██║   ██║██║   ██║██║                                                
   ██║   ██║   ██║██║   ██║██║                                                
   ██║   ╚██████╔╝╚██████╔╝███████╗                                           
   ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝                                           
============================================""")
    usernamex = input("    Enter Username > ")
    print(f"""
============================================
      Target Username: [ {username} ] 
      Target Data: [ https://www.instagram.com/{usernamex}/?__a=1&__d=dis ]

      [Go to the Data Link &]
      [THEN PASTE THE Text CONTENT TO import.json]
      
      [Then re-run dumper to get the output in {usernamex}.txt]
      
      Note: If run for 2nd time, ignore the first 3 msgs and the prompt.

============================================
""")

f = open('import.json')
data = json.load(f)

postcount = data["graphql"]["user"]["edge_owner_to_timeline_media"]["count"]

def getPostUrls():
    result = ""  # Initialize an empty string to store the output
    for i in range(postcount):
        result += "\n====================================\n"
        result += f"Post {i} | Location given: {data['graphql']['user']['edge_owner_to_timeline_media']['edges'][i]['node']['location']}\n"
        result += f"Post Thumbnail: [{data['graphql']['user']['edge_owner_to_timeline_media']['edges'][i]['node']['display_url']}]\n"
        if "edge_sidecar_to_children" in data["graphql"]["user"]["edge_owner_to_timeline_media"]["edges"][i]["node"]:
            for j, edge in enumerate(data["graphql"]["user"]["edge_owner_to_timeline_media"]["edges"][i]["node"]["edge_sidecar_to_children"]["edges"]):
                result += f"Subpost {j} Url: [{edge['node']['display_url']}]\n"

    return result
postDump = getPostUrls()

BioG = data["graphql"]["user"]["biography_with_entities"]["raw_text"]
fwlrs = data["graphql"]["user"]["edge_followed_by"]["count"]
fwlng = data["graphql"]["user"]["edge_follow"]["count"]
name = data["graphql"]["user"]["full_name"]
iD = data["graphql"]["user"]["id"]
is_professional_account = data["graphql"]["user"]["is_professional_account"]
is_private = data["graphql"]["user"]["is_private"]
is_verified = data["graphql"]["user"]["is_verified"]
edge_mutual_followed_by_count = data["graphql"]["user"]["edge_mutual_followed_by"]["count"]
mutual_followed_by_user1 = data["graphql"]["user"]["edge_mutual_followed_by"]["edges"][0]["node"]["username"]
mutual_followed_by_user2 = data["graphql"]["user"]["edge_mutual_followed_by"]["edges"][1]["node"]["username"]
mutual_followed_by_user3 = data["graphql"]["user"]["edge_mutual_followed_by"]["edges"][2]["node"]["username"]
profile_pic_url_hd = data["graphql"]["user"]["profile_pic_url_hd"]
username = data["graphql"]["user"]["username"]
