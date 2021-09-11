import urllib.request
import json

def getAnimalPrediction(zero_crossings, spectral_centroids, spectral_rolloff, mfccs):
    data = {
            "Inputs": {
                    "input1":
                    [
                        {
                                'animal': "",   
                                'zero_crossings': zero_crossings,
                                'spectral_centroids': spectral_centroids,   
                                'spectral_rolloff': spectral_rolloff,    
                                'mfccs': mfccs 
                        }
                    ],
            },
        "GlobalParameters":  {
        }
    }

    body = str.encode(json.dumps(data))

    url = 'https://ussouthcentral.services.azureml.net/workspaces/efb544568963405a9bbf817f2308678d/services/6dd0b06503cd4467a43990b0e2fc6700/execute?api-version=2.0&format=swagger'
    api_key = 'xpMjn6KzRVIIOSj4ItJfY6uP/WA4GC5ZDB342ZxRv+jJFTqidQqokLsac48iplDqDeQvXVmms69xDWe9qQexmw==' # Replace this with the API key for the web service
    headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

    req = urllib.request.Request(url, body, headers)

    try:
        response = urllib.request.urlopen(req)

        result = response.read()
        prediction = json.loads(result.decode())
        #print(prediction['Results']['output1'][0]['Scored Labels'])
        predictedAnimal = prediction['Results']['output1'][0]['Scored Labels']
        return predictedAnimal

    except urllib.error.HTTPError as error:
        print("The request failed with status code: " + str(error.code))

        # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
        print(error.info())
        print(json.loads(error.read().decode("utf8", 'ignore')))
        return "none"