import requests

# Open the file in write mode
file = open("output.html", "w")

# Write HTML content
file.write("<html>")
file.write("<head>")
file.write("<title>My Webpage</title>")
file.write("</head>")
file.write("<body>")
file.write("<h1>Welcome to my webpage!</h1>")
file.write("</body>")
file.write("</html>")

# Close the file
file.close()

print("HTML file successfully written.")

response = requests.post("https://studynotification.app.n8n.cloud/webhook/64e9e6b2-0695-415a-a82e-9e498942915f", json={
    "userId": 1,
    "title": "New Try",
    "completed": False
}, headers={
    "Content-type": "application/json; charset=UTF-8"
})
