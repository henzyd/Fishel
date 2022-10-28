from google.cloud import vision
client_options = {'api_endpoint': 'eu-vision.googleapis.com'}

client = vision.ImageAnnotatorClient(client_options=client_options)
# [END vision_set_endpoint]
image_source = vision.ImageSource(image_uri='gs://cloud-samples-data/vision/text/screen.jpg')
image = vision.Image(source=image_source)

response = client.text_detection(image=image)