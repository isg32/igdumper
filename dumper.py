from definationsx import *

initi()

# Specify the file path where you want to create and write to the file
file_path = f'{username}.txt'

# Open the file in write mode ('w')
# If the file does not exist, it will be created; if it exists, its contents will be truncated
with open(file_path, 'w', encoding="utf-8") as file:
    # Write content to the file
    file.write(f"""
               
=================================================               
    Output Generated using isg32's igdumper
=================================================
Target Name: {name}
====================================
    Userame: [ {username} ]
    Bio: [ {BioG} ]
    UseID: [ {iD} ]
    is_private: [ {is_private} ]
    is_verified: [ {is_verified} ]
    mutual_follower_count: [ {edge_mutual_followed_by_count} ]
    Mutual Follewers [First 3]: [ {mutual_followed_by_user1}, {mutual_followed_by_user2}, {mutual_followed_by_user3} ]
    profile_pic_url_hd: [ {profile_pic_url_hd} ]
    postcount: [ {postcount} ]
====================================

All Post Links:
{postDump}
""")

print(f'File "{file_path}" has been created and written to.')
