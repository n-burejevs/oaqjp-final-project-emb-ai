import requests
import json
"""
This function sends post to imb api service to calculate emotion
"""
def emotion_detector(text_to_analyze):
     # URL of the Emotion Predict service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict' 
    myobj = { "raw_document": { "text": text_to_analyze } }  # Create a dictionary with the text to be analyzed
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}  # Set the headers required for the API request
    response = requests.post(url, json = myobj, headers=header)  # Send a POST request to the API with the text and headers
    no_result = {
            "anger": None, 
            "disgust": None, 
            "fear": None, 
            "joy": None, 
            "sadness": None, 
            "dominant_emotion":None
            }
        # If the response status code is 200, extract the emotion from the response
    if response.status_code == 200:
        #return response.text  # Return the response text from the API
        formatted_response = json.loads(response.text)

        emotionPredictions = formatted_response['emotionPredictions']
        emotion = emotionPredictions[0]['emotion']

        dominant_emotion = ''
        temp = 0.0
        #x is emotion name, y is calculated probability
        for x,y in emotion.items():
            if float(y) > temp:
               temp = y
               dominant_emotion = x
    
        emotion['dominant_emotion'] = dominant_emotion

        return emotion #dominant_emotion
     # For any other unexpected status codes, return None
    elif response.status_code == 400:
        return no_result
    # For any other unexpected status codes, return None
    else:
       return no_result
    