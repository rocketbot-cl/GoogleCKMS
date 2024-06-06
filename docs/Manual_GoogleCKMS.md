# Google CKMS
  
This module connects to the Google CKMS API. You can use it to manage your organization's keys.  

*Read this in other languages: [English](Manual_GoogleCKMS.md), [Português](Manual_GoogleCKMS.pr.md), [Español](Manual_GoogleCKMS.es.md)*
  
<!-- ![banner](imgs/Banner_GoogleCKMS.png o jpg) -->
## How to install this module
  
To install the module in Rocketbot Studio, it can be done in two ways:
1. Manual: __Download__ the .zip file and unzip it in the modules folder. The folder name must be the same as the module and inside it must have the following files and folders: \__init__.py, package.json, docs, example and libs. If you have the application open, refresh your browser to be able to use the new module.
2. Automatic: When entering Rocketbot Studio on the right margin you will find the **Addons** section, select **Install Mods**, search for the desired module and press install.  

## How to use this module

- Create a project in Google Cloud Console (Skip if you already have a project created)
  - In the left menu, click on Menu > IAM & Admin > Create a project

  - In the Project Name field, add a name for the project

  - Complete the following fields as needed

- Enable billing in the project
    - In the left menu, click on Menu > Billing
    - Follow the steps to enable billing

- Enable the API:
    - Go to [Google Cloud Console](https://console.cloud.google.com/)
    - In the menu at the top right, click on **Menu** > **APIs & Services** > **Library**
    - In the search field, look for **Cloud Key Management Service (KMS) API**
    - Click on the result **Cloud Key Management Service (KMS) API**
    - Click on the **Enable** button

- Create Google credentials:
    - Go to [Google Cloud Console](https://console.cloud.google.com/)
    - In the menu at the top right, click on **Menu** > **APIs & Services** > **Credentials**
    - Click on the **Create 
credentials** button
    - Click on **OAuth client ID**
    - In the **Application type** field, select **Desktop Application**
    - Enter a name in the **Name** field
    - A window with the credential data will appear. Click on **Download JSON**
    - Use this file as credentials in the module
## Description of the commands

### Setup G-Suite credentials
  
Configure credentials to connect with the Google CKMS API.
|Parameters|Description|example|
| --- | --- | --- |
|Credentials file path|JSON file with the credentials to access the Google Admin API. See the documentation for more information.|C:\User\Desktop\credentials.json|
|Session name|Name of the session that will be created with the credentials.|session_1|
|Assign result to variable|Name of the variable where the result of the execution of the command will be assigned.|result|

### Create key ring
  
Create a key ring in Google CKMS. The command will return the path of the key ring created.
|Parameters|Description|example|
| --- | --- | --- |
|Project name|Name of the project where the key ring will be created.|my_project|
|Location name|Name of the location where the key ring will be created.|global|
|Key ring name|Name of the key ring that will be created in the project.|my_key_ring|
|Session name|Session that will be used for the execution of the command.|session_1|
|Assign result to variable|Name of the variable where the result of the execution of the command will be assigned.|result|

### Get all key rings
  
Get all key rings from a project in Google CKMS. The command will return a list with the key rings.
|Parameters|Description|example|
| --- | --- | --- |
|Project name|Name of the project where the key rings will be searched.|my_project|
|Location name|Name of the location where the key rings will be searched.|global|
|Session name|Session that will be used for the execution of the command.|session_1|
|Assign result to variable|Name of the variable where the result of the execution of the command will be assigned.|result|

### Create symmetric key
  
Create a symmetric key in Google CKMS.
|Parameters|Description|example|
| --- | --- | --- |
|Project name|Name of the project where the symmetric key will be created.|my_project|
|Location name|Name of the location where the symmetric key will be created.|global|
|Key ring name|Name of the key ring where the symmetric key will be created.|my_key_ring|
|Symmetric key name|Name of the symmetric key that will be created in the project.|my_symmetric_key|
|Session name|Session that will be used for the execution of the command.|session_1|
|Assign result to variable|Name of the variable where the result of the execution of the command will be assigned.|result|

### Encrypt plain text
  
Encrypts plain text with a symmetric key in Google CKMS. The command returns the encrypted text.
|Parameters|Description|example|
| --- | --- | --- |
|Project name|Name of the project that contains the symmetric key used to encrypt the text.|my_project|
|Location name|Name of the location where the symmetric key used to encrypt the text is located.|global|
|Key ring name|Name of the key ring where the symmetric key used to encrypt the text is located.|my_key_ring|
|Symmetric key name|Name of the symmetric key that will be used to encrypt the text.|my_symmetric_key|
|Text to encrypt|Text that will be encrypted with the provided symmetric key.|Process automation optimizes repetitive tasks, reduces errors, and increases operational efficiency.|
|Session name|Session that will be used for the execution of the command.|session_1|
|Assign result to variable|Name of the variable where the result of the execution of the command will be assigned.|result|

### Decrypt encrypted text
  
Decrypts encrypted text with a symmetric key in Google CKMS. The command returns the plain text.
|Parameters|Description|example|
| --- | --- | --- |
|Project name|Name of the project where the symmetric key used to decrypt the text is located.|my_project|
|Location name|Name of the location where the symmetric key used to decrypt the text is located.|global|
|Key ring name|Name of the key ring where the symmetric key used to decrypt the text is located.|my_key_ring|
|Symmetric key name|Name of the symmetric key that will be used to decrypt the text.|my_symmetric_key|
|Encrypted text|Text that will be decrypted with the provided symmetric key.|QW1CrUJ6/wXsDHEkRxXXAnGY7fe1dX23vNmrCXkR8NcBDpcTL0FTkwFB|
|Session name|Session that will be used for the execution of the command.|session_1|
|Assign result to variable|Name of the variable where the result of the execution of the command will be assigned.|result|
