"""Cria HTML dos cartões Biord; renderize no Chrome em 1200 x 630.
Uso: python3 scripts/generate-social-cards.py [--render]
--render requer Chrome/Chromium e Pillow; exporta os PNGs para assets/img.
Os HTMLs temporários são gravados em /tmp/biord-social-cards.
"""
from pathlib import Path
import base64
import html

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = Path('/tmp/biord-social-cards')
OUTPUT.mkdir(exist_ok=True)
LOGO = base64.b64encode((ROOT / 'assets/img/biord-logo-footer.png').read_bytes()).decode()
COPY = {
 'pt': ('UCO do Brasil.', 'Rastreabilidade de ponta a ponta.', 'Origem documentada · Cadeia de custódia digital'),
 'en': ('UCO from Brazil.', 'End-to-end traceability.', 'Documented origin · Digital chain of custody'),
 'es': ('UCO de Brasil.', 'Trazabilidad de extremo a extremo.', 'Origen documentado · Cadena de custodia digital'),
}
for language, (headline, slogan, detail) in COPY.items():
    (OUTPUT / f'{language}.html').write_text(f'''<!doctype html><html lang="{language}"><head><meta charset="utf-8"><style>
*{{box-sizing:border-box}}html,body{{margin:0;width:1200px;height:630px;overflow:hidden}}
body{{font-family:Arial,Helvetica,sans-serif;background:#EEF2FA;color:#0A1930}}
.card{{height:630px;position:relative;padding:62px 72px;background:radial-gradient(ellipse at 95% 5%,#cce9fa,transparent 60%)}}
.logo{{display:block;width:430px;height:auto}}.domain{{position:absolute;right:72px;top:88px;font-size:24px;font-weight:600;color:#1B3F9E}}
h1{{margin:42px 0 14px;font-size:62px;letter-spacing:-2px;line-height:1.08}}
p{{margin:0;font-size:44px;letter-spacing:-1px;line-height:1.2;font-weight:600}}
.footer{{position:absolute;bottom:0;left:0;right:0;height:116px;background:#0A1930;color:#EDF1FA;display:flex;align-items:center;padding:0 72px;gap:18px;font-size:25px}}
.dot{{width:12px;height:12px;border-radius:50%;background:#F0B84E;flex-shrink:0}}
</style></head><body><div class="card"><img class="logo" src="data:image/png;base64,{LOGO}" alt="Biord"><span class="domain">biord.com.br</span><h1>{html.escape(headline)}</h1><p>{html.escape(slogan)}</p><div class="footer"><span class="dot"></span>{html.escape(detail)}</div></div></body></html>''')
print(OUTPUT)

# --render exporta o HTML para PNG sem alterar a marca original.
if '--render' in __import__('sys').argv:
    import shutil
    import subprocess
    import tempfile
    from PIL import Image
    chrome = shutil.which('google-chrome') or shutil.which('chromium')
    if not chrome:
        raise SystemExit('Chrome ou Chromium não encontrado.')
    for language in COPY:
        with tempfile.TemporaryDirectory(prefix='biord-social-chrome-') as profile:
            rendered = OUTPUT / f'{language}.png'
            subprocess.run([
                chrome, '--headless', '--no-sandbox', '--disable-gpu',
                '--disable-dev-shm-usage', f'--user-data-dir={profile}',
                '--hide-scrollbars', '--force-device-scale-factor=1',
                '--window-size=1200,717', '--virtual-time-budget=1000',
                f'--screenshot={rendered}', (OUTPUT / f'{language}.html').as_uri(),
            ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)
            # A janela inclui 87px do navegador; exporta apenas a área do cartão.
            with Image.open(rendered) as image:
                image.crop((0, 0, 1200, 630)).save(
                    ROOT / f'assets/img/biord-share-{language}.png', optimize=True)
