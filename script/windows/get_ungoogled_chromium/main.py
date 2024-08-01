import urllib.request
import zipfile
import os
import shutil
import sys
import subprocess

# Getting binary without dependency, want to make this run on vanilla python
fp = urllib.request.urlopen("https://ungoogled-software.github.io/ungoogled-chromium-binaries/releases/windows/64bit/")
github_page = fp.read()
github_html = github_page.decode("utf8")
fp.close()

for line in github_html.split("\n"):
    if "<li><a href=\"/ungoogled-chromium-binaries/releases/windows/64bit/" in line:
        url = line
        break

href = url.split("\"")[1]

fp = urllib.request.urlopen("https://ungoogled-software.github.io"+href)
github_page = fp.read()
github_html = github_page.decode("utf8")
fp.close()

url = [item for item in github_html.split("\n") if "<li><a href=\"https://github.com/ungoogled-software/ungoogled-chromium-windows/releases/download/116.0.5845.141-1.1/" in item][1].split("\"")[1]

urllib.request.urlretrieve(url, "ungoogle.zip")

# Move to permanent place
with zipfile.ZipFile("./ungoogle.zip" , 'r') as zip_ref:
    zip_ref.extractall("./")

for dirpath in os.listdir("./"):
    if "windows" in dirpath:
        os.rename(dirpath, "ungoogled-chromium")
        break

shutil.copytree("ungoogled-chromium", os.path.join(os.environ["ProgramW6432"], "ungoogled-chromium"))

# Powershell can do shortcut without dependency, hard in python
subprocess.run(["powershell.exe", ".\make_shortcut.ps1"])
