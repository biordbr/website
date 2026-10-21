# Biord — website estático multilíngue

Site pronto para publicar na raiz do domínio `https://biord.com.br`, usando a publicação estática existente da Hostinger/GitHub.

## Estrutura
- `/pt/`, `/en/`, `/es/`: versões independentes e indexáveis.
- Cada idioma contém: início, soluções, geradores, rastreabilidade, fornecimento UCO e sobre.
- `/assets/css/site.css`: estilos globais.
- `/assets/js/site.js`: menu mobile e interações leves.
- `/assets/img/favicon.png`: favicon extraído do HTML fornecido.
- `sitemap.xml`, `robots.txt`, `llms.txt`, `llms-full.txt`: descoberta e contexto de indexação.
- `index.html`: entrada que encaminha para `/pt/` com links para outros idiomas.

## Publicação
1. Faça backup da versão atual. Copie o conteúdo desta pasta para a raiz de publicação do repositório (ou adapte o `public`/`dist` conforme a configuração do deploy).
2. Confirme que a Hostinger publica os subdiretórios e serve `index.html` em `/pt/`, `/en/` etc.
3. Confirme o domínio canônico. Este pacote assume `https://biord.com.br` sem `www`. Configure 301 de `www` para o domínio escolhido se o painel permitir.
4. Teste as páginas, botões externos, SEO e sitemap em produção.
5. Envie `https://biord.com.br/sitemap.xml` ao Google Search Console e ao Bing Webmaster Tools.
6. Se houver links antigos `/#/servicos`, `/#/restaurantes`, `/#/sobre`, atualize os links de referência externos para as novas páginas, pois fragmentos (`#`) não podem ser redirecionados via servidor.

## Atenção
- Nenhuma alteração foi enviada ao GitHub ou à Hostinger.
- A arquitetura é inspirada em conceitos ISCC; não declara certificação. UDB: preparação, não conexão concluída.
- A propriedade `keywords` foi incluída por solicitação, mas mecanismos como Google não a utilizam como fator de classificação. A ênfase está no texto visível, títulos, descrições, URLs, `hreflang`, sitemap e links internos.
- Ajuste as páginas com informações verificadas sobre cobertura geográfica, disponibilidade, certificações e condições comerciais antes de anunciar novas operações.
- O ícone foi extraído do arquivo original; as demais peças visuais foram recriadas em CSS para reduzir dependências.


## Identidade visual
A versão atual mantém a paleta original da Biord: azul-marinho `#0A1930`, azul `#2E63E7`, fundo azulado `#EEF2FA` e dourado `#F0B84E` para detalhes. O logo azul fornecido pela empresa é utilizado no cabeçalho, no rodapé e no favicon. As páginas multilíngues e os metadados de SEO foram preservados.
