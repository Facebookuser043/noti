import requests

import commands 
 
print "content-type: text/html" 
print 
 
#Now you can write html code in print statement 
print """ 
<table> 
<form action=""> 
<input type="pass" name="pass"> 
<input type="Submit"> 
</form> 
</table>  
""" 

print("HTML file successfully written.")

response = requests.post("https://studynotification.app.n8n.cloud/webhook/64e9e6b2-0695-415a-a82e-9e498942915f", json={
    "userId": 1,
    "title": "New Try",
    "completed": False
}, headers={
    "Content-type": "application/json; charset=UTF-8"
})
