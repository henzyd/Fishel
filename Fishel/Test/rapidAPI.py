import http.client

conn = http.client.HTTPSConnection("image-to-base64.p.rapidapi.com")

payload = "-----011000010111000001101001\rContent-Disposition: form-data; name=\"file\"\r\r\r-----011000010111000001101001--\r\r"

headers = {
    'content-type': "multipart/form-data; boundary=---011000010111000001101001",
    'X-RapidAPI-Key': "d86c44d443msh8d66420de4502f7p1b6d28jsn66b19c7382ac",
    'X-RapidAPI-Host': "image-to-base64.p.rapidapi.com"
    }

conn.request("POST", "/imgtob64", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))