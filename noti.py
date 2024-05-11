import requests

htmlTrippleQuoted = """ 
<html> 
    <head> 
        <script> 
             function f1() { 
                 return "hello"; 
             } 
        </script> 
        <style> 
            div { 
                background-color: #FFFF00; 
            } 
        </style> 
    </head> 
    <body> 
        <div id='title'> 
            <a href='/' onclick='f1();'>Title</a> 
        </div> 
    </body> 
</html>""" 
print (htmlTrippleQuoted) 

response = requests.post("https://studynotification.app.n8n.cloud/webhook/64e9e6b2-0695-415a-a82e-9e498942915f", json={
    "userId": 1,
    "title": "New Try",
    "completed": False
}, headers={
    "Content-type": "application/json; charset=UTF-8"
})
