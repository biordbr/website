# Biord — site multilíngue

Site estático com identidade azul, navegação compartilhada e versões em português, inglês e espanhol. Cada diretório contém seu `index.html`; CSS, JavaScript e imagens ficam em `assets/`.

## Publicação

Publique os arquivos na raiz pública do domínio, preservando a estrutura das pastas. A hospedagem deve servir URLs por diretório, como `/pt/servicos/`. O acesso à raiz redireciona para `/pt/`.

## Navegação

- Serviços reúne os submenus Soluções e Rastreabilidade.
- Restaurantes reúne Visão geral e Benefícios.
- A plataforma e os cadastros apontam para `https://app.biord.com.br`.
- Notícias aponta para `https://noticias.biord.com.br/`, onde será servido o WordPress. O código e a configuração desse WordPress não fazem parte deste repositório.
- O seletor de idiomas mantém o visitante na página equivalente.

## Sitemap e Search Console

O `sitemap.xml` contém **27 URLs canônicas: 9 páginas em 3 idiomas**. Existem 28 arquivos HTML nos diretórios de idiomas: `/en/fornecimento-uco/` é uma versão antiga que declara `/en/sourcing/` como canônica, portanto não é contada novamente. A raiz redireciona para `/pt/` e também não é uma página adicional.

Para atualizar o arquivo com as páginas canônicas e os `hreflang` declarados no HTML:

```sh
python3 scripts/update-sitemap.py
```

O gerador verifica os destinos dos alternates e preserva as datas `lastmod` existentes. Quando houver mudanças reais em uma página, atualize sua data; páginas novas entram sem uma data presumida.

O sitemap deste projeto não lista posts do WordPress, que são gerenciados por outro sistema. Depois de publicar o WordPress em `noticias.biord.com.br`, envie também o sitemap que ele disponibilizar ao Search Console. A contagem de URLs descobertas em um sitemap não é uma confirmação de que todas foram indexadas.

## Marca e compartilhamento

O favicon usa o símbolo quadrado da Biord. As páginas têm metadados Open Graph e Twitter com cartões de 1200 × 630 pixels em cada idioma. Para gerar novamente os cartões com Chrome/Chromium e Pillow instalados:

```sh
python3 scripts/generate-social-cards.py --render
```

## Conteúdo

As versões em inglês e espanhol foram traduzidas mantendo o sentido do conteúdo original. Referências a ISCC e UDB não declaram certificação nem integração ativa.
