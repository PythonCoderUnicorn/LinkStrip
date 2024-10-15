import re
from rich.console import Console
console = Console()

def get_github_username(url):
  # Decode the URL-encoded parts
  decoded_url = url.replace("%2F", "/")
  # Split the URL based on "/"
  parts = decoded_url.split("/")
  # Check if it's a valid GitHub URL with username and domain
  if len(parts) >= 4 and parts[0] == "github.com":
    return f"\nhttps://github.com/{parts[1]}/{parts[2]}"

  else:
    return None


st = """
ooooo       o88               oooo         oooooooo8    o8               o88               
 888        oooo  oo oooooo    888  ooooo 888         o888oo oo oooooo   oooo  ooooooooo   
 888         888   888   888   888o888     888oooooo   888    888    888  888   888    888 
 888      o  888   888   888   8888 88o           888  888    888         888   888    888 
o888ooooo88 o888o o888o o888o o888o o888o o88oooo888    888o o888o       o888o  888ooo88   
                                                                               o888     
"""
print(st)
url = input("Enter url: ")


pattern = r'github.com\S+'
string = url
m = re.search(pattern, string).group(0)
m2 = m.replace("2F","/").replace("%","").replace("tree/main/","\t")

username = get_github_username(m2)

if username:
  console.print(f"\n [cyan]{username} \n")
else:
  console.print("[warning] Invalid GitHub URL format[/] \n")
