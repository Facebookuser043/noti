import requests

import cgi 
print "Content-type: text/html" 
print """<html> 
<head><title>My first Python CGI app</title></head> 
<body> 
<p>Hello, 'world'!</p> 
</body> 
</html>""" 

print("HTML file successfully written.")

response = requests.post("https://studynotification.app.n8n.cloud/webhook/64e9e6b2-0695-415a-a82e-9e498942915f", json={
    "userId": 1,
    "title": "New Try",
    "completed": False
}, headers={
    "Content-type": "application/json; charset=UTF-8"
})
