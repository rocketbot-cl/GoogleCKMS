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
    - Click on the **Create credentials** button
    - Click on **OAuth client ID**
    - In the **Application type** field, select **Desktop Application**
    - Enter a name in the **Name** field
    - A window with the credential data will appear. Click on **Download JSON**
    - Use this file as credentials in the module