# Google CKMS
  
Este módulo se conecta al API de Google CKMS. Puedes usarlo para gestionar las claves de tu organización.  

*Read this in other languages: [English](Manual_GoogleCKMS.md), [Português](Manual_GoogleCKMS.pr.md), [Español](Manual_GoogleCKMS.es.md)*
  
<!-- ![banner](imgs/Banner_GoogleCKMS.png o jpg) -->
## Como instalar este módulo
  
Para instalar el módulo en Rocketbot Studio, se puede hacer de dos formas:
1. Manual: __Descargar__ el archivo .zip y descomprimirlo en la carpeta modules. El nombre de la carpeta debe ser el mismo al del módulo y dentro debe tener los siguientes archivos y carpetas: \__init__.py, package.json, docs, example y libs. Si tiene abierta la aplicación, refresca el navegador para poder utilizar el nuevo modulo.
2. Automática: Al ingresar a Rocketbot Studio sobre el margen derecho encontrara la sección de **Addons**, seleccionar **Install Mods**, buscar el modulo deseado y presionar install.  

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
    - En el menú arriba a la derecha, dar click en 
**Menu** > **APIs & Services** > **Credentials**
    - Click en el botón **Create credentials**
    - Click en **OAuth client ID**
    - En el campo **Application type**, seleccionar **Desktop Application**
    - Escribir un nombre en el campo **Name**
    - Aparecerá una ventana con los datos de la credencial. Dar click en **Download JSON**
    - Utilizar este archivo como credenciales en el módulo

## Descripción de los comandos

### Configurar credenciales G-Suite
  
Configura credenciales para conectar con el API de Google CKMS.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Ruta archivo de credenciales|Archivo json con las credenciales de acceso a la API de Google Admin. Revisar la documentación para obtener más información.|C:\Usuario\Desktop\credenciales.json|
|Nombre de la sesión|Nombre de la sesión que se creará con las credenciales.|session_1|
|Asignar resultado a variable|Nombre de la variable donde se asignará el resultado de la execución del comando.|result|

### Crear llavero de claves
  
Crea un llavero de claves en Google CKMS. El comando retornará la ruta del llavero de claves creado.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Nombre del proyecto|Nombre del proyecto donde se creará el llavero de claves.|mi_proyecto|
|Nombre de la Ubicación|Nombre de la ubicación donde se creará el llavero de claves.|global|
|Nombre de llavero de claves|Nombre del llavero de claves que se creará en el proyecto.|my_key_ring|
|Nombre de la sesión|Sesión que se utilizará para la ejecución del comando.|session_1|
|Asignar resultado a variable|Nombre de la variable donde se asignará el resultado de la execución del comando.|result|

### Obtener todos los llaveros de claves
  
Obtiene todos los llaveros de claves de un proyecto en Google CKMS. El comando retornará una lista con los llaveros de claves.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Nombre del proyecto|Nombre del proyecto donde se buscarán los llaveros de claves.|mi_proyecto|
|Nombre de la Ubicación|Nombre de la ubicación donde se buscarán los llaveros de claves.|global|
|Nombre de la sesión|Sesión que se utilizará para la ejecución del comando.|session_1|
|Asignar resultado a variable|Nombre de la variable donde se asignará el resultado de la execución del comando.|result|

### Crear clave simétrica
  
Crea una clave simétrica en Google CKMS.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Nombre del proyecto|Nombre del proyecto donde se creará la clave simétrica.|mi_proyecto|
|Nombre de la Ubicación|Nombre de la ubicación donde se creará la clave simétrica|global|
|Nombre del llavero de claves|Nombre del llavero donde se creará la clave simétrica.|mi_key_ring|
|Nombre de la clave simétrica|Nombre de la clave simétrica que se creará en el proyecto.|mi_clave_simetrica|
|Nombre de la sesión|Sesión que se utilizará para la ejecución del comando.|session_1|
|Asignar resultado a variable|Nombre de la variable donde se asignará el resultado de la execución del comando.|result|

### Encriptar texto plano
  
Encripta un texto plano con una clave simétrica en Google CKMS. El comando retornará el texto encriptado.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Nombre del proyecto|Nombre del proyecto que contiene la clave simétrica utilizada para encriptar el texto.|mi_proyecto|
|Nombre de la Ubicación|Nombre de la ubicación donde se encuentra la clave simétrica utilizada para encriptar el texto.|global|
|Nombre del llavero de claves|Nombre del llavero donde se encuentra la clave simétrica utilizada para encriptar el texto.|mi_key_ring|
|Nombre de la clave simétrica|Nombre de la clave simétrica que se utilizará para encriptar el texto.|mi_clave_simetrica|
|Texto a encriptar|Texto que será encriptado con la clave simétrica proporcionada.|Automatización de procesos optimiza tareas repetitivas, reduce errores y aumenta la eficiencia operativa.|
|Nombre de la sesión|Sesión que se utilizará para la ejecución del comando.|session_1|
|Asignar resultado a variable|Nombre de la variable donde se asignará el resultado de la execución del comando.|result|

### Desencriptar texto encriptado
  
Desencripta un texto encriptado con una clave simétrica en Google CKMS. El comando retornará el texto plano.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Nombre del proyecto|Nombre del proyecto donde se encuentra la clave simétrica utilizada para desencriptar el texto.|mi_proyecto|
|Nombre de la Ubicación|Nombre de la ubicación donde se encuentra la clave simétrica utilizada para desencriptar el texto.|global|
|Nombre del llavero de claves|Nombre del llavero donde se encuentra la clave simétrica utilizada para desencriptar el texto.|mi_key_ring|
|Nombre de la clave simétrica|Nombre de la clave simétrica que se utilizará para desencriptar el texto.|mi_clave_simetrica|
|Texto encriptado|Texto que será desencriptado con la clave simétrica proporcionada.|QW1CrUJ6/wXsDHEkRxXXAnGY7fe1dX23vNmrCXkR8NcBDpcTL0FTkwFB|
|Nombre de la sesión|Sesión que se utilizará para la ejecución del comando.|session_1|
|Asignar resultado a variable|Nombre de la variable donde se asignará el resultado de la execución del comando.|result|
