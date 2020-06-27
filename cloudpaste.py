import pyperclip
from firebase_admin import db
import firebase_admin
from firebase_admin import credentials
import keyboard
#import pytesseract
import cv2
class cloudtext():
    def __init__(self):
        t = {
  "type": "service_account",
  "project_id": "titanchat21032000",
  "private_key_id": "8b154e9abd0523eb6d4f98960b0a34cb1a55225c",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQCksXskziQEFmlL\np6YuNtdNtFVh+eKO1VeBu9N1OGzlKNmP8MCP1ruW0eGba4GYzKE1Sri6qNpQ5zkv\ndAet+2CfJwuPhuunNPluFzvy52iYY19FUbe77pt5fvxpc899QV+WtIkS1SvgALqz\nJ37xgqL0qKXlbSp9NxjsnXml79U9cGzkBOIjox+u3WQQm/aNj9MF9rx3t5RYFifv\n/CTR2rXCuukESYPi0uw4oYI4qMxoExVS5d377PNGv58o/FPEdMvOCFUonX7NkmqN\n5cSYcYGMxjckOzrQmlp0uxJ80fOVQ8dDFE4LsMsmG2Yf0sDTuys46Kdlu5q7MLky\nq5pN7gldAgMBAAECggEATzlpSY04WhcF0/TzxetvqtuC7zyrtZX/IFNgJ1VbXOlH\nryxbFVZwqt6PrpoKn5xgOCiXsIMlciGoqqEgSJtSIX1A3GxE1AxxqHnYxsJ22EeF\nPu1Oe0MO22UwuvGQ8GoQN4jlH4AYOQtgxGnNcRQsm5C9LR5UgCOPA9PE/wPeCk1T\nI7XBXu3c8iWNQSt12AP1M4quzJuPkPQNACj1t4pcshd3CDN9x6XlzBKeCtyrMion\n4dB25q6XR2iBmoQ3opNCT1kJeOPMRTeTYeCrq2sD9G1ipvEePDMy4RwcuxKSBUKT\n6thL6elgiLEhgA460wP+s6oACHQlT5Xhp3uvFLL2qQKBgQDP5mWutApV1MQquvXX\naHhC9Rm2EyTWB7L4EyXb3yVdIaNkVHf8LRR2UjGceguVmfw8bwtKpBOm5ihAEW0i\npSjfGw2XhYdRx3hK4ymR83Yq803+gphuiJLsFoHiUhoZeOO8oEp3HyMXpS0+A7z9\nlZfE1ysrbtcmogdNYoUu2cbDuwKBgQDKzAQUGjGlS1suh1sANfvc2vY+aY5fj/js\n4oWFiZ10VPy+pu4+W7mkQD55+fe0vmwgRH+jirwQzpL6cOJHAhKSbd1rfi2BD32G\n/mweibVUjsW+sdA6wVWavBofCilZMdL3aWimXPGoghozFCVD6BbQ12nhWb9MCPXU\nv59f9/H5xwKBgFDAvV5OsHUGX+v5EuTIv23CpmoCpZw9AVc6mMn+sxSprD2cUb6y\nA/CxnHObNES3uzH+L/SeJsP9QkUgf7OlU2rVp0Hjq9woDqGH+u2mE5A7UWA6edr1\nUZxCYdD28wxR2KO73zDF92uHzTr5WL9nC7x5l1sXgpqO9ScpzXGVRY9hAoGAdIwL\nTAJBxd0o6fSgN97OgH7WRcgkKodzZ7BHTBdqhhDRsD//a5cLeXnybedalGVbfq/f\nKv3wVzhg/80gPe7S/ZRmTACX5jQg0BQnzuUVcSMcQhuusBWsPOEdofkVCk24ELhj\njDieKVmb9P7+66fWdO9XykrpxajgnwQBdAXq6sECgYBrFxZKzwz8U64X69g7Miba\nXWln7OTdcantq11wuIYWGfSCG4osBHhC8iNYYqgc06gFYvqu9Aabi5R6IYryqwbK\nZC7wXaGHUH6iLpts4C07hvIHBp3lrtNlcpmsBHQxpKtxj/c4G3P1S1evPPiK8FoW\neQgQhPJ9nPe8mLrVMqgwDQ==\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-e3e6l@titanchat21032000.iam.gserviceaccount.com",
  "client_id": "103723327998241254840",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-e3e6l%40titanchat21032000.iam.gserviceaccount.com"
}

        cred = credentials.Certificate(t)
        firebase_admin.initialize_app(cred ,{'databaseURL': 'https://{}.firebaseio.com/'.format('titanchat21032000')})
        self.dbb = db.reference("cloudtext")
        
    def text(self):
        a = self.dbb.get()
        return a
        
    def listen(self):
        #cam = cv2.VideoCapture(0)
        #cv2.namedWindow("image")
        while True:
            a = self.dbb.get()
            s = pyperclip.paste()
            if a != s:
                self.dbb.set(s)
                pyperclip.copy(s)
            
            #ret, frame = cam.read()
            #cv2.imshow("image", frame)
            '''elif cv2.waitKey(1)%256 == 27:
                print("Escape hit, closing...")
                break'''
        #cam.release()
        #cv2.destroyAllWindows()
m = cloudtext()
m.listen()
                
