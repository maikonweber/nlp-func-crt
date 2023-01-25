# nlp-func-crt
Processamento de Linguagem Natural.
Com Objetivo de Analise Semantica e Produção de Orações com mesmo valor semantico.

Referencia:
**https://www.stoodi.com.br/blog/portugues/valor-semantico/
** https://www.portalsaofrancisco.com.br/portugues/semantica

Foco em Programa Funcional e Microserviços.
  Ideia Inicial : 
    Oração é formalmente relacionada por verbo,sujeito e predicato.
  é possivel localizar isso nas frase com spacy já implmentado agora é indificar 
  entre os tri-grams e bi-grams o Verbo e correlacionar com um possível frase depois relacionar com sentido valido 
  e alternativa para treinando assim um modelo possível.
  
- Timeline - 
- * Isolar o maior número de funções possiveis :(X) - Doing
- * Criar objetos caso necessário maior abstração : () - Review
- * Criar e isolar funções para registro em banco de dados persistent[Postgres]: () - TODO
- * Deep Lerning Functions () - TODO
- * Incorporar Microserviço com RabbitMq para ingerir o Texto Registrar e Processar e Gerar Orações Validas. () - TODO
- * Configurar Ambiente para produção com Terraforms e Ansible e docker-compose () - TODO;
- * 

