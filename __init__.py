# coding: utf-8
"""
Base para desarrollo de modulos externos.
Para obtener el modulo/Funcion que se esta llamando:
     GetParams("module")

Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(variable)
    Las "variable" se define en forms del archivo package.json

Para modificar la variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")

Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)

Para obtener la Opcion seleccionada:
    opcion = GetParams("option")


Para instalar librerias se debe ingresar por terminal a la carpeta "libs"

    pip install <package> -t .

"""

GetParams = GetParams #type:ignore
SetVar = SetVar #type:ignore
PrintException = PrintException #type:ignore

import os
import sys
import json

# Add the libs folder to the system path
base_path = tmp_global_obj["basepath"] #type:ignore
google_ckms_path = os.path.join(base_path, "modules", "GoogleCKMS")
gckms_libs_path = os.path.join(google_ckms_path, "libs") #type:ignore

if gckms_libs_path not in sys.path:
    sys.path.append(gckms_libs_path)

from google.cloud import kms

"""
The code of each module works as a local scope. Each command that is executed resets the data.
To share information between commands, declare the variable as global. The sintax will be 'mod_modulename' or similar
"""
global mod_google_ckms

"""
To connect to multiple databases, a dictionary is created and stores the instance of each connection.
The syntax is {"session name": {data}}
"""
SESSION_DEFAULT = "default"
try:
    if not mod_google_ckms : #type:ignore
        mod_google_ckms = {SESSION_DEFAULT:{}}
except NameError:
    mod_google_ckms = {SESSION_DEFAULT:{}}

class GoogleCKMS:
    """
    Google Cloud Key Management Service (CKMS) class.

    This class is used to interact with the Google Cloud Key Management Service.
    """
    
    def __init__(self, credential_path, token_path="token.json"):
        """Initialize the class."""
        self.SCOPES = [
            "https://www.googleapis.com/auth/cloudkms",
        ]
        self.creds = None
        self.credential_path = credential_path
        self.token_path = token_path
        self.service = None

    def config_credentials(self):
        """Configure the credentials."""
        from google_auth_oauthlib.flow import InstalledAppFlow #type:ignore
        from google.oauth2.credentials import Credentials #type:ignore
        from google.auth.transport.requests import Request #type:ignore
        from googleapiclient.discovery import build #type:ignore

        self.creds = None
        # The file token.json stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists(self.token_path):
            print("Loading credentials from token.json")
            self.creds = Credentials.from_authorized_user_file(self.token_path, self.SCOPES)
        # If there are no (valid) credentials available, let the user log in.
        if not self.creds or not self.creds.valid:
            if self.creds and self.creds.expired and self.creds.refresh_token:
                self.creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    self.credential_path, self.SCOPES)
                self.creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open(self.token_path, 'w') as token:
                token.write(self.creds.to_json())

        self.service = build('cloudkms', 'v1', credentials=self.creds)
        print("Credentials configured successfully.", self.service)
    
    def create_key_ring(self, project_id, location_id, key_ring_id):
        """Create a new key ring."""
        parent = f"projects/{project_id}/locations/{location_id}"
        
        request = self.service.projects().locations().keyRings().create(
            parent=parent, keyRingId=key_ring_id, 
        )
        response = request.execute()

        return response
    
    def get_all_key_rings(self, project_id, location_id):
        """Get all key rings."""
        parent = f"projects/{project_id}/locations/{location_id}"
        
        request = self.service.projects().locations().keyRings().list(
            parent=parent
        )
        response = request.execute()
        print("Key rings retrieved successfully.", response)
        if response.get("keyRings"):
            key_rings = response["keyRings"]
            key_rings_names = [key_ring["name"].split('/')[-1] for key_ring in key_rings]
            return key_rings_names
        else:
            return []
        
    def create_symmetric_key(self, project_id, location_id, key_ring_id, key_id):
        """Create a new symmetric key."""
        parent = f"projects/{project_id}/locations/{location_id}/keyRings/{key_ring_id}"

        crypto_key = {
            "purpose": "ENCRYPT_DECRYPT",
            "versionTemplate": {
                "algorithm": "GOOGLE_SYMMETRIC_ENCRYPTION",
            },
        }
        
        request = self.service.projects().locations().keyRings().cryptoKeys().create(
            parent=parent, 
            cryptoKeyId=key_id,
            body=crypto_key
        )
        response = request.execute()
        if response.get("name"):
            return response["name"].split('/')[-1]
    
    def encrypt(self, project_id, location_id, key_ring_id, key_id, plaintext):
        """Encrypt the plaintext."""
        import base64
        parent = f"projects/{project_id}/locations/{location_id}/keyRings/{key_ring_id}/cryptoKeys/{key_id}"
        
        plaintext_base64 = base64.b64encode(plaintext.encode()).decode()

        request = self.service.projects().locations().keyRings().cryptoKeys().encrypt(
            name=parent,
            body={"plaintext": plaintext_base64}
        )
        response = request.execute()

        if response.get("ciphertext"):
            return response["ciphertext"]
        
    
    def decrypt(self, project_id, location_id, key_ring_id, key_id, ciphertext):
        """Decrypt the ciphertext."""
        import base64
        parent = f"projects/{project_id}/locations/{location_id}/keyRings/{key_ring_id}/cryptoKeys/{key_id}"

        request = self.service.projects().locations().keyRings().cryptoKeys().decrypt(
            name=parent,
            body={"ciphertext": ciphertext}
        )
        response = request.execute()

        if response.get("plaintext"):
            plaintext = base64.b64decode(response["plaintext"]).decode()
            return plaintext
        
    

    

try:
    module = GetParams("module") # Get command executed
    session = GetParams("session") # Get Session name
    result = GetParams("result") # Get variable name where save results

    if not session:
        session = SESSION_DEFAULT # Set default session

    # Execure the selected command
    if module == "config":
        credentials_path = GetParams("credentials_path")
        token_path = "token.json" if session == SESSION_DEFAULT else f"{session}_token.json"

        google_ckms = GoogleCKMS(
            credentials_path,
            os.path.join(google_ckms_path, token_path)
            )
        try:
            google_ckms.config_credentials()
            mod_google_ckms[session] = google_ckms
            SetVar(result, True)
        except Exception as e:
            SetVar(result, False)
            PrintException()
            raise e
    else:
        if session not in mod_google_ckms:
            SetVar(result, "Session not found.")
            raise Exception("Session not found.")
        else:
            google_ckms = mod_google_ckms[session]
        
    if module == "create_key_ring":
        project_name = GetParams("project_name")
        location_name = GetParams("location_name")
        key_ring_name = GetParams("key_ring_name")

        response = google_ckms.create_key_ring(project_name, location_name, key_ring_name)
        SetVar(result, response)

    elif module == "get_all_key_rings":
        project_name = GetParams("project_name")
        location_name = GetParams("location_name")

        response = google_ckms.get_all_key_rings(project_name, location_name)
        SetVar(result, response)

    elif module == "create_symmetric_key":
        project_name = GetParams("project_name")
        location_name = GetParams("location_name")
        key_ring_name = GetParams("key_ring_name")
        key_name = GetParams("key_name")

        response = google_ckms.create_symmetric_key(project_name, location_name, key_ring_name, key_name)
        SetVar(result, response)

    elif module == "encrypt":
        project_name = GetParams("project_name")
        location_name = GetParams("location_name")
        key_ring_name = GetParams("key_ring_name")
        key_name = GetParams("key_name")
        text = GetParams("text")

        response = google_ckms.encrypt(project_name, location_name, key_ring_name, key_name, text)
        SetVar(result, response)
        
    elif module == "decrypt":
        project_name = GetParams("project_name")
        location_name = GetParams("location_name")
        key_ring_name = GetParams("key_ring_name")
        key_name = GetParams("key_name")
        text = GetParams("text")

        response = google_ckms.decrypt(project_name, location_name, key_ring_name, key_name, text)
        SetVar(result, response)

        

except Exception as e:
    SetVar(result, False)
    PrintException()
    raise e
