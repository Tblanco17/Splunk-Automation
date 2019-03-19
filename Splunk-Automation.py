import os

os.system("sudo wget -O splunk-7.2.5-088f49762779-Linux-x86_64.tgz 'https://www.splunk.com/bin/splunk/DownloadActivityServlet?architecture=x86_64&platform=linux&version=7.2.5&product=splunk&filename=splunk-7.2.5-088f49762779-Linux-x86_64.tgz&wget=true'"
os.system("sudo tar -xvf splunk-7.2.5-088f49762779-Linux-x86_64.tgz -C /opt")
os.system("/opt/splunk/bin/splunk start --accept-license")
os.system("Tblanco17")
os.system("enterpassword")

exit()

#Any errors aren't the code, just going to have to do splunk troubleshooting
#Errors can be that it exits with code(1)
#Or could not find ETC Home path
#MAKE SURE CHMOD +X TO THIS FILE



