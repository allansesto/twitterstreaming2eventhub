# TS2MAEV - Twitter Streaming to Microsoft Azure Event Hub

## Pré-requisitos
- (1) Registro como um aplicativo do Twitter
    - Você precisa registrar a ferramenta como um novo aplicativo em <http://apps.twitter.com/>. Depois de escolher um nome e um aplicativo para seu aplicativo, você receberá uma * twitter_consumer_key *, * twitter_consumer_secret *, * twitter_access_token * e * twitter_access_token_secret * - que precisam ser preenchidas em * TS2MAEV.json * para fornecer acesso programático ao aplicativo Twitter.
- (2) criar um hub de eventos
    - Você precisa criar um namespace para o tipo Event Hubs e obter as credenciais de gerenciamento que seu aplicativo precisa para se comunicar com o hub de eventos. Para criar um namespace e um hub de eventos, siga o procedimento deste documento - [Criar um namespace de Hubs de Eventos e um hub de eventos usando o portal do Azure] (https://docs.microsoft.com/en-us/azure/event-hubs / event-hubs-create)


Este programa transmite feed do Twitter para o EventHub

argumentos opcionais:
  -h, --help mostra esta mensagem de ajuda e sai
  -v, --version mostra o número da versão do programa e sai
  --init Criar modelo de cliente conf TS2MAEV.json somente se
                        não existe um
  -c CONF, --conf CONF arquivo de configuração TS2MAEV. Padrão: TS2MAEV.json
  -s, - silencioso modo silencioso - executando a ferramenta sem exibir tweets json que você está fluindo para o seu Hub de Eventos

## Arquivo de configuração - TS2MAEV.json
Para executar a ferramenta, você precisa configurar um arquivo de configuração para a ferramenta e especificar o arquivo na execução da ferramenta.
`` `
{
    "twitter_consumer_key": "<Chave do Consumidor para o Twitter App>",
    "twitter_consumer_secret": "<Segredo do Consumidor para Twitter App>",
    "twitter_access_token": "<Token de Acesso do Twitter App>",
    "twitter_access_secret": "<Segredo de Acesso para o Twitter App>",
    "track_keywords": [
        "<Palavra-chave ou hashtag>",
        "<Palavra-chave ou hashtag>",
        "<Palavra-chave ou hashtag>"
    ]
    "eventhub_namespace": "<Event Hub Namespace>",
    "eventhub_entity": "<Event Entity Hub Name>",
    "eventhub_sas_key": "<Nome da Chave SAS do Hub de Eventos>",
    "eventhub_sas_value": "<Valor SAS do Hub de Eventos>"
}
`` `

Por favor, consulte [exemplo de arquivo de configuração] (TS2MAEV.json.example) e execute a ferramenta assim:

`` `
% TS2MAEV --conf ./TS2MAEV.json
`` `

Ou rode com a opção `-s | --silient` se você quiser rodar a ferramenta sem exibir os tweets que você está enviando para o seu Event Hub

`` `
% TS2MAEV --conf ./TS2MAEV.json --silent