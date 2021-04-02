import os
from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.face import FaceClient

def get_face_client():
    """Create an authenticated FaceClient."""
    SUBSCRIPTION_KEY = os.environ["COGNITIVE_SERVICE_KEY"]
    ENDPOINT = os.environ["COGNITIVE_SERVICE_ENDPOINT"]
    credential = CognitiveServicesCredentials(SUBSCRIPTION_KEY)
    return FaceClient(ENDPOINT, credential)

face_client = get_face_client()

#image URL
url = "http://pm1.narvii.com/7332/f807b4ef737fdc7318b8a4655223b0ecbf7d9b55r1-540-540v2_uhq.jpg"


""" More than 10 attributes Available """

attributes = ["emotion","gender","makeup"]

# include face id (Boolean fx)
include_id = False

# include points for face element (Boolean fx)
include_landmarks = False

detected_faces = face_client.face.detect_with_url(url, include_id, include_landmarks, attributes, raw=True)

if not detected_faces:
    raise Exception('No face detected in image')

print(detected_faces.response.json())
