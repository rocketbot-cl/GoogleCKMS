## Como usar este módulo

- Crear un projecto en Google Cloud Console (Saltar si ya tienes un proyecto creado)
  - En el menú de la izquierda, dar click en Menu > IAM & Admin > Create a project

  - En el campo Project Name, agregar un nombre para el proyecto

  - Completar los siguientes campos según corresponda

- Habilitar la facturación en el proyecto
  - En el menú de la izquierda, dar click en Menu > Billing
  - Seguir los pasos para habilitar la facturación

- Habilitar la API:
    - Ir a [Google Cloud Console](https://console.cloud.google.com/)
    - En el menú arriba a la derecha, dar click en **Menu** > **APIs & Services** > **Library**
    - En el buscador, buscar **Cloud Key Management Service (KMS) API**
    - Dar click en el resultado **Cloud Key Management Service (KMS) API**
    -  Click en el botón **Habilitar**

- Crear credenciales de Google:
    - Ir a [Google Cloud Console](https://console.cloud.google.com/)
    - En el menú arriba a la derecha, dar click en **Menu** > **APIs & Services** > **Credentials**
    - Click en el botón **Create credentials**
    - Click en **OAuth client ID**
    - En el campo **Application type**, seleccionar **Desktop Application**
    - Escribir un nombre en el campo **Name**
    - Aparecerá una ventana con los datos de la credencial. Dar click en **Download JSON**
    - Utilizar este archivo como credenciales en el módulo
