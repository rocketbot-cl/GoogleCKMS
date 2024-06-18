## Como usar este módulo

- Criar um projeto no Google Cloud Console (Pular se você já tiver um projeto criado)
  - No menu à esquerda, clique em Menu > IAM & Admin > Create a project

  - No campo Project Name, adicione um nome para o projeto

  - Complete os campos a seguir conforme necessário

- Habilitar a faturação no projeto
    - No menu à esquerda, clique em Menu > Billing
    - Siga as etapas para habilitar a faturação

- Habilitar a API:
    - Acesse [Google Cloud Console](https://console.cloud.google.com/)
    - No menu no canto superior direito, clique em **Menu** > **APIs & Services** > **Library**
    - No campo de busca, procure por **Cloud Key Management Service (KMS) API**
    - Clique no resultado **Cloud Key Management Service (KMS) API**
    -  Clique no botão **Habilitar**

- Criar credenciais do Google:
    - Acesse [Google Cloud Console](https://console.cloud.google.com/)
    - No menu no canto superior direito, clique em **Menu** > **APIs & Services** > **Credentials**
    - Clique no botão **Create credentials**
    - Clique em **OAuth client ID**
    - No campo **Application type**, selecione **Desktop Application**
    - Insira um nome no campo **Name**
    - Uma janela com os dados da credencial será exibida. Clique em **Download JSON**
    - Use este arquivo como credenciais no módulo