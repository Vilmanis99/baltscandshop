#!/usr/bin/env python3
"""
Baltscand Web Shop — Static Site Generator v4
Bilingual (EN/FI) with language switcher, SEO, series pages, visual polish, accessibility
"""

import json, os, html as h

BASE = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(BASE, 'data', 'products.json')) as f:
    data = json.load(f)

SITE_URL = 'https://YOURDOMAIN.baltscand.com'  # Update when domain decided

LANGS = ['en', 'fi']

# ─── UI Translations ────────────────────────────────────────────────────

UI = {
    'en': {
        'lang_name': 'English',
        'lang_flag': '🇬🇧',
        'other_lang': 'fi',
        'other_lang_name': 'Suomi',
        'other_flag': '🇫🇮',
        'html_lang': 'en',
        'products': 'Products',
        'about': 'About Baltscand',
        'contact_sales': 'Contact Sales',
        'hero_title': 'Storage Solutions<br>for <span>Every Scale</span>',
        'hero_desc': 'From light shelving to heavy-duty pallet racking, platforms and partitions. European quality, local service in Finland and the Baltics.',
        'talk_experts': 'Talk to Our Experts',
        'browse_products': 'Browse Products',
        'product_ranges': 'Product Ranges',
        'products_label': 'Products',
        'max_frame': 'Max Frame Capacity',
        'platform_load': 'Platform Load',
        'view_range': 'View {name} Range',
        'catalog_pdf': 'Catalog PDF',
        'n_products': '{n} products',
        'home': 'Home',
        'key_features': 'Key Features',
        'finishes': 'Finishes',
        'products_in': 'Products in {name}',
        'view_details': 'View Details',
        'get_quote_for': 'Get a Quote for {name}',
        'download_catalog': 'Download Full Catalog (PDF)',
        'download_catalog_series': 'Download {name} Catalog (PDF)',
        'interested_in': 'Interested in: ',
        'interested_in_product': 'Interested in {name}?',
        'contact_note': '<strong>Contact our sales team for pricing and project consultation.</strong><br>All sizes and specifications shown below. Our experts will help you choose the right configuration and provide competitive pricing for your project.',
        'available_sizes': 'Available sizes',
        'get_quote': 'Get a Quote',
        'consult_desc': 'Our experts will help you choose the right sizes, configurations and accessories. Get a personalised quote.',
        'tech_specs': 'Technical Specifications',
        'load_capacity': 'Load Capacity (kg per shelf)',
        'load_note': 'All loads evenly distributed, in kg. Values from official technical documentation. Contact us for project-specific load calculations.',
        'accessories': 'Accessories & Options',
        'applications': 'Applications',
        'more_in': 'More in {name}',
        'need_help': 'Need help choosing?',
        'need_help_desc': 'Our experts will help you select the right products, sizes and configurations for your space. Get a personalised quote with competitive pricing for Finland and the Baltics.',
        'talk_expert': 'Talk to an Expert',
        'modal_title': 'Talk to Our Experts',
        'modal_subtitle': 'Our sales team will help you find the right solution. We typically respond within 1 business day.',
        'name_label': 'Name *',
        'company_label': 'Company',
        'email_label': 'Email *',
        'phone_label': 'Phone',
        'message_label': 'Tell us about your needs',
        'name_ph': 'Your full name',
        'company_ph': 'Company name',
        'email_ph': 'your@email.com',
        'phone_ph': '+358...',
        'message_ph': 'What products are you interested in? Quantities? Any specific requirements?',
        'send': 'Send Inquiry',
        'sending': 'Sending...',
        'sent': "Sent! We'll be in touch.",
        'copyright': '&copy; 2026 Baltscand Oy. All rights reserved.',
        'shelving': 'Shelving',
        'page_not_found': 'Page not found',
        '404_desc': "The page you're looking for doesn't exist or has been moved. Browse our products or contact our sales team for assistance.",
        'general_inquiry': 'General Inquiry',
        'site_title': 'Baltscand — Professional Storage & Shelving | Finland & Baltics',
        'site_desc': 'Professional storage and shelving solutions for Finland and the Baltics. PROSPACE+, PRORACK+, PROPAL 3, PROPLUS LP3 and MODUL+ product ranges. Contact our experts for a quote.',
        'org_desc': 'Professional storage and shelving solutions for Finland and the Baltics.',
    },
    'fi': {
        'lang_name': 'Suomi',
        'lang_flag': '🇫🇮',
        'other_lang': 'en',
        'other_lang_name': 'English',
        'other_flag': '🇬🇧',
        'html_lang': 'fi',
        'products': 'Tuotteet',
        'about': 'Tietoa Baltscandista',
        'contact_sales': 'Ota yhteyttä',
        'hero_title': 'Varastoratkaisut<br>jokaiseen <span>tarpeeseen</span>',
        'hero_desc': 'Kevyistä hyllyistä raskaisiin kuormalavahyllyihin, välikerroksiin ja osastointiin. Eurooppalainen laatu, paikallinen palvelu Suomessa ja Baltiassa.',
        'talk_experts': 'Kysy asiantuntijoiltamme',
        'browse_products': 'Selaa tuotteita',
        'product_ranges': 'Tuotesarjat',
        'products_label': 'Tuotetta',
        'max_frame': 'Kehikon maks. kantavuus',
        'platform_load': 'Tason kuormitus',
        'view_range': 'Näytä {name} -tuotteet',
        'catalog_pdf': 'Katalogi PDF',
        'n_products': '{n} tuotetta',
        'home': 'Etusivu',
        'key_features': 'Keskeiset ominaisuudet',
        'finishes': 'Pintakäsittelyt',
        'products_in': 'Tuotteet: {name}',
        'view_details': 'Näytä tiedot',
        'get_quote_for': 'Pyydä tarjous: {name}',
        'download_catalog': 'Lataa katalogi (PDF)',
        'download_catalog_series': 'Lataa {name} -katalogi (PDF)',
        'interested_in': 'Kiinnostuksen kohde: ',
        'interested_in_product': 'Kiinnostaako {name}?',
        'contact_note': '<strong>Ota yhteyttä myyntitiimiimme hinnoittelua ja projektisuunnittelua varten.</strong><br>Kaikki mitat ja tekniset tiedot alla. Asiantuntijamme auttavat valitsemaan oikean kokoonpanon ja tarjoavat kilpailukykyisen hinnoittelun.',
        'available_sizes': 'Saatavilla olevat mitat',
        'get_quote': 'Pyydä tarjous',
        'consult_desc': 'Asiantuntijamme auttavat valitsemaan oikeat mitat, kokoonpanot ja lisävarusteet. Pyydä henkilökohtainen tarjous.',
        'tech_specs': 'Tekniset tiedot',
        'load_capacity': 'Kantavuus (kg hyllyä kohti)',
        'load_note': 'Kaikki kuormat tasaisesti jakautuneet, kg. Arvot virallisesta teknisestä dokumentaatiosta. Ota yhteyttä projektikohtaisiin kuormituslaskelmiin.',
        'accessories': 'Lisävarusteet ja vaihtoehdot',
        'applications': 'Käyttökohteet',
        'more_in': 'Lisää sarjassa {name}',
        'need_help': 'Tarvitsetko apua valinnassa?',
        'need_help_desc': 'Asiantuntijamme auttavat valitsemaan oikeat tuotteet, mitat ja kokoonpanot tilaasi. Pyydä henkilökohtainen tarjous kilpailukykyiseen hintaan Suomessa ja Baltiassa.',
        'talk_expert': 'Kysy asiantuntijalta',
        'modal_title': 'Kysy asiantuntijoiltamme',
        'modal_subtitle': 'Myyntitiimimme auttaa löytämään oikean ratkaisun. Vastaamme yleensä 1 arkipäivän kuluessa.',
        'name_label': 'Nimi *',
        'company_label': 'Yritys',
        'email_label': 'Sähköposti *',
        'phone_label': 'Puhelin',
        'message_label': 'Kerro tarpeistasi',
        'name_ph': 'Koko nimesi',
        'company_ph': 'Yrityksen nimi',
        'email_ph': 'sinun@sahkoposti.fi',
        'phone_ph': '+358...',
        'message_ph': 'Mistä tuotteista olet kiinnostunut? Määrät? Erityisvaatimuksia?',
        'send': 'Lähetä tiedustelu',
        'sending': 'Lähetetään...',
        'sent': 'Lähetetty! Otamme yhteyttä.',
        'copyright': '&copy; 2026 Baltscand Oy. Kaikki oikeudet pidätetään.',
        'shelving': 'Hyllyjärjestelmät',
        'page_not_found': 'Sivua ei löydy',
        '404_desc': 'Etsimääsi sivua ei ole tai se on siirretty. Selaa tuotteitamme tai ota yhteyttä myyntitiimiimme.',
        'general_inquiry': 'Yleinen tiedustelu',
        'site_title': 'Baltscand — Ammattitason varastointi ja hyllyjärjestelmät | Suomi ja Baltia',
        'site_desc': 'Ammattitason varasto- ja hyllyratkaisut Suomeen ja Baltiaan. PROSPACE+, PRORACK+, PROPAL 3, PROPLUS LP3 ja MODUL+ tuotesarjat. Kysy tarjous asiantuntijoiltamme.',
        'org_desc': 'Ammattitason varasto- ja hyllyratkaisut Suomeen ja Baltiaan.',
    }
}


# ─── Data Helpers (language-aware) ──────────────────────────────────────

def t(lang, key, **kwargs):
    """Get translated UI string."""
    s = UI[lang].get(key, UI['en'].get(key, key))
    if kwargs:
        for k, v in kwargs.items():
            s = s.replace('{' + k + '}', str(v))
    return s

def s_get(obj, key, lang):
    """Get field with fallback: fi_X → X."""
    if lang == 'fi':
        fi_key = f'fi_{key}'
        val = obj.get(fi_key)
        if val:
            return val
    return obj.get(key, '')

def s_list(obj, key, lang):
    """Get list field with fallback."""
    if lang == 'fi':
        fi_key = f'fi_{key}'
        val = obj.get(fi_key)
        if val:
            return val
    return obj.get(key, [])


# ─── Shared Helpers ────────────────────────────────────────────────────

def esc(s):
    return h.escape(str(s))

def meta_tags(title, description, image, url, og_type='website'):
    abs_img = f'{SITE_URL}/{image}' if image and not image.startswith('http') else (image or '')
    abs_url = f'{SITE_URL}/{url}' if url and not url.startswith('http') else (url or SITE_URL)
    return f"""<meta property="og:type" content="{og_type}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(description)}">
<meta property="og:image" content="{abs_img}">
<meta property="og:url" content="{abs_url}">
<meta property="og:site_name" content="Baltscand">
<meta name="twitter:card" content="summary_large_image">
<link rel="canonical" href="{abs_url}">"""

def jsonld_org(lang):
    desc = esc(t(lang, 'org_desc'))
    return f"""<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"Organization","name":"Baltscand","url":"https://www.baltscand.com","description":"{desc}","contactPoint":{{"@type":"ContactPoint","contactType":"sales","availableLanguage":["English","Finnish"]}}}}
</script>"""

def jsonld_product(product, series, url, lang):
    img = product.get('gallery', [product.get('image', '')])[0]
    pname = esc(s_get(product, 'name', lang))
    pdesc = esc(s_get(product, 'description', lang)[:200])
    cat = esc(s_get(series, 'category', lang))
    return f"""<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"Product","name":"{pname}","description":"{pdesc}","image":"{SITE_URL}/{img}","brand":{{"@type":"Brand","name":"Baltscand"}},"category":"{cat}","url":"{SITE_URL}/{url}"}}
</script>"""


# ─── Shared HTML Components ──────────────────────────────────────────

def lang_switcher(lang, current_path):
    """Generate language switcher link."""
    other = t(lang, 'other_lang')
    other_name = t(lang, 'other_lang_name')
    other_flag = t(lang, 'other_flag')
    # Replace /en/ with /fi/ or vice versa
    other_path = current_path.replace(f'/{lang}/', f'/{other}/', 1)
    return f'<a class="lang-switch" href="{other_path}" title="{other_name}">{other_flag} {other_name}</a>'

def nav(lang, prefix='', current_path=''):
    ls = lang_switcher(lang, current_path)
    gi = t(lang, 'general_inquiry')
    return f"""
<header>
  <div class="nav-inner">
    <a class="logo" href="{prefix}index.html">BALT<span>SCAND</span></a>
    <button class="hamburger" onclick="this.classList.toggle('open');document.getElementById('navLinks').classList.toggle('open')" aria-label="Toggle menu">
      <span></span><span></span><span></span>
    </button>
    <nav id="navLinks">
      <a href="{prefix}index.html" class="active">{t(lang, 'products')}</a>
      <a href="https://www.baltscand.com/shelving">{t(lang, 'about')}</a>
      <a href="https://www.baltscand.com">baltscand.com</a>
      {ls}
    </nav>
    <a class="nav-cta" href="javascript:void(0)" onclick="openQuoteModal('{gi}')">{t(lang, 'contact_sales')}</a>
  </div>
</header>"""

def foot(lang):
    gi = t(lang, 'general_inquiry')
    return f"""
<footer>
  <div class="footer-inner">
    <div>
      <span>{t(lang, 'copyright')}</span>
      <span class="footer-sep">&middot;</span>
      <a href="https://www.baltscand.com">baltscand.com</a>
    </div>
    <div class="footer-links">
      <a href="https://www.baltscand.com/shelving">{t(lang, 'shelving')}</a>
      <span class="footer-sep">&middot;</span>
      <a href="javascript:void(0)" onclick="openQuoteModal('{gi}')">{t(lang, 'contact_sales')}</a>
    </div>
  </div>
</footer>"""

def back_to_top():
    return """<button class="btt" onclick="window.scrollTo({top:0,behavior:'smooth'})" aria-label="Back to top">&uarr;</button>
<script>
(function(){var b=document.querySelector('.btt');window.addEventListener('scroll',function(){b.classList.toggle('show',window.scrollY>400)})})();
</script>"""

def modal(lang):
    return f"""
<div class="modal-overlay" id="quoteModal" role="dialog" aria-modal="true" aria-labelledby="modalTitle" onclick="if(event.target===this)closeModal()">
  <div class="modal">
    <button class="close" onclick="closeModal()" aria-label="Close dialog">&times;</button>
    <h2 id="modalTitle">{t(lang, 'modal_title')}</h2>
    <p class="sub">{t(lang, 'modal_subtitle')}</p>
    <div class="summary" id="quoteSummary"></div>
    <label for="formName">{t(lang, 'name_label')}</label><input id="formName" name="name" type="text" placeholder="{t(lang, 'name_ph')}" required>
    <label for="formCompany">{t(lang, 'company_label')}</label><input id="formCompany" name="company" type="text" placeholder="{t(lang, 'company_ph')}">
    <label for="formEmail">{t(lang, 'email_label')}</label><input id="formEmail" name="email" type="email" placeholder="{t(lang, 'email_ph')}" required>
    <label for="formPhone">{t(lang, 'phone_label')}</label><input id="formPhone" name="phone" type="tel" placeholder="{t(lang, 'phone_ph')}">
    <label for="formMessage">{t(lang, 'message_label')}</label>
    <textarea id="formMessage" name="message" placeholder="{t(lang, 'message_ph')}"></textarea>
    <button class="btn-submit" id="btnSubmit" onclick="submitQ()">{t(lang, 'send')}</button>
  </div>
</div>
<script>
function openQuoteModal(p){{
  document.getElementById('quoteSummary').innerHTML='<strong>{t(lang, "interested_in")}'+p+'</strong>';
  document.getElementById('quoteModal').classList.add('show');
  document.getElementById('formName').focus();
}}
function closeModal(){{
  document.getElementById('quoteModal').classList.remove('show');
  document.querySelectorAll('#quoteModal input,#quoteModal textarea').forEach(function(el){{el.value=''}});
  var b=document.getElementById('btnSubmit');b.textContent='{t(lang, "send")}';b.style.background='';b.disabled=false;
}}
function submitQ(){{
  var n=document.getElementById('formName').value.trim();
  var e=document.getElementById('formEmail').value.trim();
  if(!n){{document.getElementById('formName').focus();document.getElementById('formName').style.borderColor='#e85d04';return}}
  if(!e||!/^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$/.test(e)){{document.getElementById('formEmail').focus();document.getElementById('formEmail').style.borderColor='#e85d04';return}}
  var b=document.getElementById('btnSubmit');
  b.textContent='{t(lang, "sending")}';b.disabled=true;b.style.background='#999';
  setTimeout(function(){{
    b.textContent='{t(lang, "sent")}';b.style.background='#2d6a4f';b.disabled=true;
    setTimeout(function(){{closeModal()}},2000);
  }},800);
}}
document.addEventListener('keydown',function(e){{if(e.key==='Escape')closeModal()}});
</script>"""

def consult(lang, prefix=''):
    gi = t(lang, 'general_inquiry')
    return f"""
<div class="consult-banner">
  <div>
    <h2>{t(lang, 'need_help')}</h2>
    <p>{t(lang, 'need_help_desc')}</p>
  </div>
  <a class="btn-primary" href="javascript:void(0)" onclick="openQuoteModal('{gi}')" style="white-space:nowrap">{t(lang, 'talk_expert')}</a>
</div>"""


# ═══════════════════════════════════════════════════════════════════════════
# EXTERNAL CSS (shared, generated once at root)
# ═══════════════════════════════════════════════════════════════════════════

def gen_css():
    css = """@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:'Inter',system-ui,-apple-system,sans-serif;color:#1a1a2e;background:#f5f6f8;-webkit-font-smoothing:antialiased}
img{max-width:100%;display:block}
a{text-decoration:none;color:inherit}

/* Header */
header{background:#0c0c1d;color:white;position:sticky;top:0;z-index:100;backdrop-filter:blur(12px)}
.nav-inner{max-width:1320px;margin:0 auto;display:flex;align-items:center;justify-content:space-between;padding:18px 40px}
.logo{font-size:22px;font-weight:800;letter-spacing:3px}
.logo span{color:#e85d04}
nav{display:flex;gap:32px;align-items:center}
nav a{color:rgba(255,255,255,0.8);font-size:13px;font-weight:600;text-transform:uppercase;letter-spacing:1.5px;padding:4px 0;border-bottom:2px solid transparent;transition:all 0.2s}
nav a:hover,nav a.active{color:white;border-bottom-color:#e85d04}
.nav-cta{background:#e85d04;color:white;padding:10px 24px;border-radius:8px;font-size:13px;font-weight:700;letter-spacing:0.5px;transition:background 0.2s}
.nav-cta:hover{background:#d14e00}
.lang-switch{background:rgba(255,255,255,0.1);padding:6px 14px;border-radius:6px;font-size:12px;font-weight:600;letter-spacing:0.5px;text-transform:none;border:1px solid rgba(255,255,255,0.15);transition:all 0.2s}
.lang-switch:hover{background:rgba(255,255,255,0.2);border-color:rgba(255,255,255,0.3);border-bottom-color:rgba(255,255,255,0.3)}

/* Hamburger */
.hamburger{display:none;background:none;border:none;cursor:pointer;padding:8px;flex-direction:column;gap:5px}
.hamburger span{display:block;width:24px;height:2px;background:white;transition:all 0.3s}
.hamburger.open span:nth-child(1){transform:rotate(45deg) translate(5px,5px)}
.hamburger.open span:nth-child(2){opacity:0}
.hamburger.open span:nth-child(3){transform:rotate(-45deg) translate(5px,-5px)}

/* Footer */
footer{background:#0c0c1d;color:rgba(255,255,255,0.5);padding:48px 40px 32px}
.footer-inner{max-width:1320px;margin:0 auto;display:flex;justify-content:space-between;align-items:center;font-size:13px;flex-wrap:wrap;gap:16px}
.footer-inner a{color:#e85d04;transition:color 0.2s}
.footer-inner a:hover{color:#ff7b2e}
.footer-sep{margin:0 8px;opacity:0.3}
.footer-links{display:flex;align-items:center}

/* Buttons */
.btn-primary{display:inline-flex;align-items:center;gap:10px;background:#e85d04;color:white;padding:16px 36px;border-radius:12px;font-size:16px;font-weight:700;border:none;cursor:pointer;transition:all 0.25s;box-shadow:0 4px 16px rgba(232,93,4,0.3)}
.btn-primary:hover{background:#d14e00;transform:translateY(-1px);box-shadow:0 6px 24px rgba(232,93,4,0.4)}
.btn-ghost{display:inline-flex;align-items:center;gap:10px;background:transparent;color:#1a1a2e;padding:14px 32px;border-radius:12px;font-size:15px;font-weight:600;border:2px solid #d0d0d8;cursor:pointer;transition:all 0.2s}
.btn-ghost:hover{border-color:#1a1a2e;background:#1a1a2e;color:white}

/* Consultation banner */
.consult-banner{background:linear-gradient(135deg,#1a1a2e,#0f3460);border-radius:20px;padding:48px;display:flex;align-items:center;justify-content:space-between;gap:40px;margin:60px 40px;max-width:1240px;color:white}
.consult-banner h2{font-size:28px;font-weight:800;margin-bottom:8px}
.consult-banner p{color:rgba(255,255,255,0.65);font-size:15px;line-height:1.6;max-width:540px}
.consult-banner .btn-primary{background:white;color:#1a1a2e;box-shadow:0 4px 16px rgba(0,0,0,0.2)}
.consult-banner .btn-primary:hover{background:#f0f0f0;transform:translateY(-1px)}

/* Modal */
.modal-overlay{display:none;position:fixed;top:0;left:0;right:0;bottom:0;background:rgba(0,0,0,0.6);z-index:1000;align-items:center;justify-content:center;backdrop-filter:blur(4px)}
.modal-overlay.show{display:flex}
.modal{background:white;border-radius:20px;padding:44px;max-width:520px;width:92%;max-height:90vh;overflow-y:auto;position:relative;box-shadow:0 24px 64px rgba(0,0,0,0.2)}
.modal h2{font-size:24px;font-weight:800;margin-bottom:4px}
.modal .sub{color:#666;font-size:14px;margin-bottom:28px}
.modal .summary{background:#f5f6f8;border-radius:12px;padding:16px 20px;margin-bottom:24px;font-size:14px;line-height:1.7;border-left:4px solid #e85d04}
.modal label{display:block;font-size:12px;font-weight:700;color:#888;margin-bottom:6px;text-transform:uppercase;letter-spacing:1px}
.modal input,.modal textarea{width:100%;padding:13px 16px;border:2px solid #e8e8ee;border-radius:10px;font-size:15px;font-family:inherit;margin-bottom:16px;transition:border 0.2s}
.modal input:focus,.modal textarea:focus{outline:none;border-color:#e85d04}
.modal textarea{height:80px;resize:vertical}
.modal .btn-submit{width:100%;background:#e85d04;color:white;border:none;padding:16px;border-radius:12px;font-size:16px;font-weight:700;cursor:pointer;transition:all 0.2s}
.modal .btn-submit:hover{background:#d14e00}
.modal .btn-submit:disabled{cursor:not-allowed}
.modal .close{position:absolute;top:20px;right:20px;background:#f5f6f8;border:none;width:36px;height:36px;border-radius:50%;font-size:18px;cursor:pointer;color:#666;display:flex;align-items:center;justify-content:center}

/* Back to top */
.btt{position:fixed;bottom:32px;right:32px;width:48px;height:48px;border-radius:50%;background:#1a1a2e;color:white;border:none;font-size:20px;cursor:pointer;opacity:0;transform:translateY(20px);transition:all 0.3s;z-index:90;box-shadow:0 4px 16px rgba(0,0,0,0.2)}
.btt.show{opacity:1;transform:translateY(0)}
.btt:hover{background:#e85d04}

/* ===== INDEX PAGE ===== */

.hero{background:linear-gradient(135deg,#0c0c1d 0%,#162040 40%,#1a3a60 100%);color:white;padding:100px 40px 80px;text-align:center;position:relative;overflow:hidden}
.hero::after{content:'';position:absolute;bottom:0;left:0;right:0;height:120px;background:linear-gradient(transparent,#f5f6f8)}
.hero h1{font-size:52px;font-weight:900;letter-spacing:-1px;margin-bottom:16px;position:relative;z-index:1}
.hero h1 span{color:#e85d04}
.hero p{font-size:19px;color:rgba(255,255,255,0.6);max-width:640px;margin:0 auto 40px;line-height:1.6;position:relative;z-index:1}
.hero-cta{position:relative;z-index:1;display:flex;gap:16px;justify-content:center;flex-wrap:wrap}
.hero-stats{display:flex;justify-content:center;gap:64px;margin-top:56px;position:relative;z-index:1;flex-wrap:wrap}
.hero-stat{text-align:center}
.hero-stat .n{font-size:36px;font-weight:900;color:#e85d04}
.hero-stat .l{font-size:12px;color:rgba(255,255,255,0.45);text-transform:uppercase;letter-spacing:2px;margin-top:6px}

.series-section{padding:48px 40px}
.series-section.odd{background:white}
.series-inner{max-width:1240px;margin:0 auto}

/* Series compact header */
.series-header{display:flex;align-items:flex-start;justify-content:space-between;gap:24px;margin-bottom:24px;flex-wrap:wrap}
.series-header-left{flex:1;min-width:0}
.series-header-top{display:flex;align-items:center;gap:12px;margin-bottom:8px;flex-wrap:wrap}
.series-title{font-size:28px;font-weight:900;letter-spacing:-0.5px;margin:0}
.series-title a{color:inherit;transition:color 0.2s}
.series-title a:hover{color:#e85d04}
.series-cat-badge{display:inline-block;background:#fff3e6;color:#e85d04;padding:4px 14px;border-radius:6px;font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:1px}
.prod-count{font-size:13px;font-weight:500;color:#999}
.series-desc{color:#555;font-size:14px;line-height:1.6;margin:0;max-width:680px}
.series-header-right{display:flex;gap:10px;align-items:center;flex-shrink:0;padding-top:4px}
.standards-row{display:flex;flex-wrap:wrap;gap:6px;margin-bottom:16px}
.std-badge{display:inline-block;padding:4px 12px;background:#e8f5e9;color:#2d6a4f;border-radius:6px;font-size:11px;font-weight:700;letter-spacing:0.5px}
.btn-catalog{display:inline-flex;align-items:center;gap:8px;padding:10px 20px;background:#f5f6f8;border:1px solid #d0d0d8;border-radius:10px;font-size:13px;font-weight:600;color:#555;transition:all 0.2s}
.btn-catalog:hover{background:#1a1a2e;color:white;border-color:#1a1a2e}
.btn-catalog svg{width:16px;height:16px}
.btn-view-all{display:inline-flex;align-items:center;gap:6px;padding:10px 22px;background:#e85d04;color:white;border-radius:10px;font-size:13px;font-weight:700;transition:all 0.2s}
.btn-view-all:hover{background:#d14e00;transform:translateY(-1px)}

/* Product cards grid on homepage */
.series-products-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:16px}
.series-pcard{background:white;border-radius:14px;overflow:hidden;border:1px solid #e8e8ee;transition:all 0.25s;display:flex;flex-direction:column}
.series-section.odd .series-pcard{background:#fafafc}
.series-pcard:hover{transform:translateY(-4px);box-shadow:0 12px 32px rgba(0,0,0,0.08);border-color:#e85d04}
.series-pcard img{width:100%;height:160px;object-fit:contain;padding:16px;background:#fafafc}
.series-section.odd .series-pcard img{background:white}
.series-pcard-body{padding:14px 16px;flex:1;display:flex;flex-direction:column}
.series-pcard-body h3{font-size:14px;font-weight:700;margin-bottom:4px;line-height:1.3;flex:1}
.series-pcard-body .card-link{display:inline-flex;align-items:center;gap:4px;color:#e85d04;font-size:12px;font-weight:700;margin-top:6px}

/* ===== SERIES LANDING PAGE ===== */

.series-hero{background:linear-gradient(135deg,#0c0c1d 0%,#162040 40%,#1a3a60 100%);color:white;padding:80px 40px 60px;position:relative}
.series-hero-inner{max-width:1240px;margin:0 auto;display:grid;grid-template-columns:1fr 1fr;gap:48px;align-items:center}
.series-hero-text .eyebrow{display:inline-block;background:rgba(232,93,4,0.2);color:#e85d04;padding:5px 16px;border-radius:8px;font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:1.5px;margin-bottom:16px}
.series-hero-text h1{font-size:44px;font-weight:900;margin-bottom:12px}
.series-hero-text p{font-size:16px;color:rgba(255,255,255,0.6);line-height:1.7;margin-bottom:28px}
.series-hero-text .btn-primary{margin-right:12px}
.series-hero-img{border-radius:16px;overflow:hidden;box-shadow:0 8px 40px rgba(0,0,0,0.3)}
.series-hero-img img{width:100%;height:360px;object-fit:cover}

.series-body{max-width:1240px;margin:0 auto;padding:60px 40px}
.series-features{margin-bottom:48px}
.series-features h2{font-size:24px;font-weight:800;margin-bottom:20px}
.feat-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:12px}
.feat-item{display:flex;align-items:flex-start;gap:12px;padding:14px 18px;background:white;border-radius:10px;border:1px solid #e8e8ee;font-size:14px;color:#555}
.feat-item::before{content:'\\2713';color:#2d6a4f;font-weight:800;font-size:16px;flex-shrink:0;margin-top:1px}

.products-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:20px;margin-bottom:48px}
.product-card{background:white;border-radius:16px;overflow:hidden;border:1px solid #e8e8ee;transition:all 0.25s}
.product-card:hover{transform:translateY(-4px);box-shadow:0 12px 32px rgba(0,0,0,0.08);border-color:#e85d04}
.product-card img{width:100%;height:220px;object-fit:contain;padding:20px;background:#fafafc}
.product-card-body{padding:20px}
.product-card-body h3{font-size:17px;font-weight:700;margin-bottom:6px}
.product-card-body p{font-size:13px;color:#666;line-height:1.5;margin-bottom:14px}
.product-card-body .card-link{display:inline-flex;align-items:center;gap:6px;color:#e85d04;font-size:13px;font-weight:700}

/* ===== PRODUCT DETAIL PAGE ===== */

.breadcrumb{padding:14px 40px;font-size:13px;color:#888;max-width:1320px;margin:0 auto}
.breadcrumb a{color:#e85d04;transition:color 0.2s}
.breadcrumb a:hover{color:#d14e00}

.product-hero{max-width:1320px;margin:0 auto;padding:40px;display:grid;grid-template-columns:1.1fr 0.9fr;gap:56px;align-items:start}
.gallery{position:sticky;top:100px}
.main-img{background:white;border-radius:16px;overflow:hidden;box-shadow:0 4px 24px rgba(0,0,0,0.06);margin-bottom:14px;cursor:zoom-in}
.main-img img{width:100%;height:460px;object-fit:contain;padding:28px}
.thumbs{display:flex;gap:10px;flex-wrap:wrap}
.thumb{width:80px;height:64px;border-radius:10px;overflow:hidden;cursor:pointer;border:2px solid transparent;background:white;box-shadow:0 1px 4px rgba(0,0,0,0.05);transition:border 0.2s}
.thumb:hover,.thumb.active{border-color:#e85d04}
.thumb img{width:100%;height:100%;object-fit:contain;padding:4px}

.info{padding-top:4px}
.eyebrow{display:inline-block;background:#fff3e6;color:#e85d04;padding:5px 16px;border-radius:8px;font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:1.5px;margin-bottom:14px}
.info h1{font-size:32px;font-weight:900;letter-spacing:-0.5px;margin-bottom:10px;line-height:1.2}
.info .desc{color:#555;font-size:15px;line-height:1.7;margin-bottom:24px}

.info .feats{list-style:none;margin-bottom:28px;display:grid;grid-template-columns:1fr 1fr;gap:4px 16px}
.info .feats li{font-size:13px;color:#555;padding:5px 0 5px 22px;position:relative}
.info .feats li::before{content:'\\2713';color:#2d6a4f;position:absolute;left:0;font-weight:800}

.size-group{margin-bottom:16px}
.size-label{font-size:12px;font-weight:700;color:#888;text-transform:uppercase;letter-spacing:1.5px;margin-bottom:8px}
.size-tags{display:flex;flex-wrap:wrap;gap:6px}
.size-tag{padding:7px 14px;background:white;border:1px solid #e0e0e8;border-radius:8px;font-size:13px;font-weight:500;color:#333}

.fins{display:flex;gap:12px;margin-bottom:28px}
.fin{display:flex;align-items:center;gap:10px;padding:12px 18px;background:white;border:1px solid #e0e0e8;border-radius:10px;flex:1}
.fin-dot{width:28px;height:28px;border-radius:50%;border:1px solid #ddd;flex-shrink:0}
.fin-name{font-size:13px;font-weight:700}
.fin-code{font-size:11px;color:#999}

.consult-box{background:linear-gradient(135deg,#1a1a2e,#0f3460);border-radius:16px;padding:32px;color:white;margin-top:28px}
.consult-box h3{font-size:20px;font-weight:800;margin-bottom:6px}
.consult-box p{font-size:14px;color:rgba(255,255,255,0.6);margin-bottom:20px;line-height:1.5}
.consult-box .btn-primary{width:100%;justify-content:center}

.detail-section{max-width:1320px;margin:0 auto;padding:0 40px 60px}
.section-block{margin-bottom:48px}
.section-heading{font-size:22px;font-weight:800;margin-bottom:20px;padding-bottom:12px;border-bottom:2px solid #e8e8ee;color:#1a1a2e}

.specs{width:100%;border-collapse:collapse}
.specs tr{border-bottom:1px solid #f0f0f5}
.specs td{padding:14px 18px;font-size:14px}
.specs td:first-child{font-weight:600;color:#555;width:260px;background:#fafafc;border-radius:4px 0 0 4px}

.lt{width:100%;border-collapse:collapse;font-size:13px;margin-top:8px}
.lt th{background:#1a1a2e;color:white;padding:11px 12px;text-align:center;font-size:11px;text-transform:uppercase;letter-spacing:0.5px}
.lt th:first-child{text-align:left;border-radius:8px 0 0 0}
.lt th:last-child{border-radius:0 8px 0 0}
.lt td{padding:9px 12px;text-align:center;border-bottom:1px solid #f0f0f5}
.lt td:first-child{text-align:left;font-weight:600}
.lt tr:hover{background:#fafafc}

.acc-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:14px}
.acc{background:white;border-radius:12px;padding:20px;border:1px solid #eee}
.acc strong{display:block;margin-bottom:4px;font-size:14px}
.acc span{font-size:13px;color:#666;line-height:1.5}

.uc-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:16px}
.uc{border-radius:14px;overflow:hidden;position:relative}
.uc img{width:100%;height:220px;object-fit:cover}
.uc-label{position:absolute;bottom:0;left:0;right:0;background:linear-gradient(transparent,rgba(0,0,0,0.75));color:white;padding:32px 18px 14px;font-size:13px;font-weight:700}

.note-box{background:#fff8f0;border:1px solid #f0d8b8;border-radius:12px;padding:20px 24px;margin-bottom:24px;font-size:14px;color:#8a6530;line-height:1.6}
.note-box strong{color:#1a1a2e}

.related-section{max-width:1320px;margin:0 auto;padding:0 40px 60px}
.related-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:16px}
.related-card{background:white;border-radius:14px;overflow:hidden;border:1px solid #e8e8ee;transition:all 0.25s;text-decoration:none;color:inherit}
.related-card:hover{transform:translateY(-3px);box-shadow:0 8px 24px rgba(0,0,0,0.08);border-color:#e85d04}
.related-card img{width:100%;height:180px;object-fit:contain;padding:16px;background:#fafafc}
.related-card-info{padding:16px}
.related-card-info h4{font-size:15px;font-weight:700;margin-bottom:4px}
.related-card-info p{font-size:12px;color:#888;line-height:1.4}

.uprights-section{margin-bottom:24px;padding:20px 24px;background:white;border:1px solid #e0e0e8;border-radius:12px}
.uprights-section h4{font-size:14px;font-weight:700;color:#1a1a2e;margin-bottom:12px}
.upright-item{display:flex;justify-content:space-between;padding:8px 0;border-bottom:1px solid #f0f0f5;font-size:13px}
.upright-item:last-child{border-bottom:none}
.upright-name{font-weight:600}
.upright-load{color:#e85d04;font-weight:600}

.std-badges-product{display:flex;flex-wrap:wrap;gap:6px;margin-bottom:20px}
.std-badges-product .std-badge{padding:5px 14px;background:#e8f5e9;color:#2d6a4f;border-radius:8px;font-size:12px;font-weight:700}

/* Lightbox */
.lightbox{display:none;position:fixed;top:0;left:0;right:0;bottom:0;background:rgba(0,0,0,0.9);z-index:1001;align-items:center;justify-content:center;flex-direction:column}
.lightbox.show{display:flex}
.lightbox img{max-width:90vw;max-height:80vh;object-fit:contain;border-radius:8px}
.lightbox-close{position:absolute;top:20px;right:24px;background:none;border:none;color:white;font-size:32px;cursor:pointer;z-index:1002}
.lightbox-nav{position:absolute;top:50%;transform:translateY(-50%);background:rgba(255,255,255,0.15);border:none;color:white;font-size:28px;cursor:pointer;padding:16px 20px;border-radius:12px;transition:background 0.2s}
.lightbox-nav:hover{background:rgba(255,255,255,0.3)}
.lightbox-prev{left:20px}
.lightbox-next{right:20px}

/* Catalog download */
.catalog-dl{display:inline-flex;align-items:center;gap:8px;padding:12px 24px;background:#fff3e6;border:1px solid #f0d8b8;border-radius:10px;font-size:13px;font-weight:600;color:#8a6530;transition:all 0.2s;margin-top:8px}
.catalog-dl:hover{background:#e85d04;color:white;border-color:#e85d04}

/* ===== RESPONSIVE ===== */

@media(max-width:900px){
  .nav-inner{padding:14px 20px}
  .hamburger{display:flex}
  nav{display:none;position:absolute;top:100%;left:0;right:0;background:#0c0c1d;flex-direction:column;padding:20px;gap:16px;border-top:1px solid rgba(255,255,255,0.1)}
  nav.open{display:flex}
  .nav-cta{display:none}
  .hero{padding:60px 20px 50px}
  .hero h1{font-size:32px}
  .hero-stats{gap:32px}
  .series-section{padding:32px 20px}
  .series-header{flex-direction:column}
  .series-header-right{width:100%}
  .series-products-grid{grid-template-columns:repeat(auto-fill,minmax(150px,1fr));gap:12px;overflow-x:auto;-webkit-overflow-scrolling:touch}
  .consult-banner{flex-direction:column;text-align:center;margin:40px 20px;padding:32px 24px}
  .product-hero{grid-template-columns:1fr;padding:20px;gap:24px}
  .gallery{position:static}
  .main-img img{height:300px}
  .info .feats{grid-template-columns:1fr}
  .detail-section{padding:0 20px 40px}
  .breadcrumb{padding:10px 20px}
  .series-hero-inner{grid-template-columns:1fr}
  .series-hero-img{display:none}
  .series-body{padding:40px 20px}
  .footer-inner{flex-direction:column;text-align:center}
}

@media(max-width:480px){
  .hero h1{font-size:26px}
  .hero p{font-size:16px}
  .hero-stats{gap:20px}
  .hero-stat .n{font-size:28px}
  .series-title{font-size:26px}
  .info h1{font-size:24px}
  .fins{flex-direction:column}
}

/* ===== PRINT ===== */

@media print{
  header,footer,.consult-banner,.consult-box,.modal-overlay,.btt,.nav-cta,.btn-primary,.btn-ghost,.btn-catalog,.catalog-dl,.lightbox,.hamburger,.series-actions,.note-box{display:none!important}
  body{background:white;color:black}
  .product-hero{grid-template-columns:1fr;gap:20px}
  .gallery{position:static}
  .thumbs{display:none}
  .main-img{box-shadow:none;border:1px solid #ccc}
  .series-section,.series-section.odd{background:white;padding:20px 0}
  .series-pcard{border:1px solid #ccc}
  a{color:inherit}
}
"""
    with open(os.path.join(BASE, 'styles.css'), 'w') as f:
        f.write(css)
    print('  styles.css')


# ═══════════════════════════════════════════════════════════════════════════
# ROOT INDEX (language redirect)
# ═══════════════════════════════════════════════════════════════════════════

def gen_root_index():
    page = """<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Baltscand — Professional Storage & Shelving</title>
<link rel="stylesheet" href="styles.css">
<script>
// Auto-detect language from browser
var lang = (navigator.language || navigator.userLanguage || 'en').toLowerCase();
if (lang.startsWith('fi')) {
  window.location.replace('fi/index.html');
} else {
  window.location.replace('en/index.html');
}
</script>
</head>
<body style="background:#0c0c1d;color:white;display:flex;align-items:center;justify-content:center;min-height:100vh;text-align:center;font-family:Inter,sans-serif">
  <div>
    <h1 style="font-size:28px;font-weight:800;margin-bottom:24px">BALT<span style="color:#e85d04">SCAND</span></h1>
    <p style="color:rgba(255,255,255,0.6);margin-bottom:32px">Choose your language / Valitse kieli</p>
    <div style="display:flex;gap:16px;justify-content:center">
      <a href="en/index.html" style="background:#e85d04;color:white;padding:16px 36px;border-radius:12px;font-weight:700;font-size:16px">🇬🇧 English</a>
      <a href="fi/index.html" style="background:white;color:#1a1a2e;padding:16px 36px;border-radius:12px;font-weight:700;font-size:16px">🇫🇮 Suomi</a>
    </div>
  </div>
</body>
</html>"""
    with open(os.path.join(BASE, 'index.html'), 'w') as f:
        f.write(page)
    print('  index.html (root redirect)')


# ═══════════════════════════════════════════════════════════════════════════
# INDEX PAGE (per language)
# ═══════════════════════════════════════════════════════════════════════════

def gen_index(lang):
    lang_dir = os.path.join(BASE, lang)
    os.makedirs(lang_dir, exist_ok=True)
    total_products = sum(len(s['products']) for s in data['series'])
    current_path = f'/{lang}/index.html'

    cards = ''
    for i, s in enumerate(data['series']):
        alt = 'odd' if i % 2 else ''
        sname_display = esc(s['name'])
        desc = esc(s_get(s, 'description', lang))
        category = esc(s_get(s, 'category', lang))

        stds = ''
        if s.get('standards'):
            stds = "<div class='standards-row' style='margin-bottom:0'>" + "".join(f"<span class='std-badge'>{esc(st)}</span>" for st in s['standards']) + "</div>"

        brochure_btn = ''
        if s.get('brochure'):
            brochure_btn = f'<a class="btn-catalog" href="../{s["brochure"]}" target="_blank" download><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>{t(lang, "catalog_pdf")}</a>'

        # Product cards with images
        pcards = ''
        for p in s['products']:
            pname = esc(s_get(p, 'name', lang))
            pimg = p.get('gallery', [p.get('image', '')])[0]
            pcards += f"""
          <a href="products/{s['slug']}/{p['id']}.html" class="series-pcard">
            <img src="../{pimg}" alt="{pname}" loading="lazy">
            <div class="series-pcard-body">
              <h3>{pname}</h3>
              <span class="card-link">{t(lang, 'view_details')} &rarr;</span>
            </div>
          </a>"""

        cards += f"""
    <section class="series-section {alt}">
      <div class="series-inner">
        <div class="series-header">
          <div class="series-header-left">
            <div class="series-header-top">
              <h2 class="series-title"><a href="products/{s['slug']}/index.html">{sname_display}</a></h2>
              <span class="series-cat-badge">{category}</span>
              <span class="prod-count">{t(lang, 'n_products', n=len(s['products']))}</span>
              {stds}
            </div>
            <p class="series-desc">{desc}</p>
          </div>
          <div class="series-header-right">
            <a class="btn-view-all" href="products/{s['slug']}/index.html">{t(lang, 'view_range', name=s['name'])} &rarr;</a>
            {brochure_btn}
          </div>
        </div>
        <div class="series-products-grid">{pcards}
        </div>
      </div>
    </section>"""

    site_desc = t(lang, 'site_desc')
    og = meta_tags(t(lang, 'site_title'), site_desc, data['series'][0]['heroImage'], f'{lang}/index.html')
    gi = t(lang, 'general_inquiry')

    html_out = f"""<!DOCTYPE html>
<html lang="{t(lang, 'html_lang')}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{t(lang, 'site_title')}</title>
<meta name="description" content="{esc(site_desc)}">
{og}
{jsonld_org(lang)}
<link rel="stylesheet" href="../styles.css">
</head>
<body>
{nav(lang, '', current_path)}

<div class="hero">
  <h1>{t(lang, 'hero_title')}</h1>
  <p>{t(lang, 'hero_desc')}</p>
  <div class="hero-cta">
    <a class="btn-primary" href="javascript:void(0)" onclick="openQuoteModal('{gi}')">{t(lang, 'talk_experts')}</a>
    <a class="btn-ghost" href="#products" style="color:white;border-color:rgba(255,255,255,0.3)">{t(lang, 'browse_products')}</a>
  </div>
  <div class="hero-stats">
    <div class="hero-stat"><div class="n">5</div><div class="l">{t(lang, 'product_ranges')}</div></div>
    <div class="hero-stat"><div class="n">{total_products}</div><div class="l">{t(lang, 'products_label')}</div></div>
    <div class="hero-stat"><div class="n">18 t</div><div class="l">{t(lang, 'max_frame')}</div></div>
    <div class="hero-stat"><div class="n">850 kg/m&sup2;</div><div class="l">{t(lang, 'platform_load')}</div></div>
  </div>
</div>

<div id="products">
{cards}
</div>

{consult(lang)}
{modal(lang)}
{foot(lang)}
{back_to_top()}
</body>
</html>"""

    with open(os.path.join(lang_dir, 'index.html'), 'w') as f:
        f.write(html_out)
    print(f'  {lang}/index.html')


# ═══════════════════════════════════════════════════════════════════════════
# SERIES LANDING PAGES
# ═══════════════════════════════════════════════════════════════════════════

def gen_series_page(series, lang):
    slug = series['slug']
    out = os.path.join(BASE, lang, 'products', slug)
    os.makedirs(out, exist_ok=True)
    P = '../../../'  # from /lang/products/series/ to root
    current_path = f'/{lang}/products/{slug}/index.html'

    feats = ''.join(f'<div class="feat-item">{esc(f)}</div>' for f in s_list(series, 'features', lang))

    product_cards = ''
    for p in series['products']:
        img = P + p.get('gallery', [p.get('image', '')])[0]
        pname = esc(s_get(p, 'name', lang))
        pdesc = esc(s_get(p, 'description', lang)[:120])
        product_cards += f"""
        <a href="{p['id']}.html" class="product-card">
          <img src="{img}" alt="{pname}" loading="lazy">
          <div class="product-card-body">
            <h3>{pname}</h3>
            <p>{pdesc}...</p>
            <span class="card-link">{t(lang, 'view_details')} &rarr;</span>
          </div>
        </a>"""

    stds = ''
    if series.get('standards'):
        stds = '<div class="standards-row" style="margin-bottom:24px">' + ''.join(f'<span class="std-badge">{esc(s)}</span>' for s in series['standards']) + '</div>'

    fins = ''
    if series.get('finishes'):
        fin_items = ''.join(
            f'<div class="fin"><div class="fin-dot" style="background:{f["color"]}"></div><div><div class="fin-name">{esc(f["name"])}</div><div class="fin-code">{esc(f["code"])}</div></div></div>'
            for f in series['finishes']
        )
        fins = f'<div style="margin-bottom:32px"><h2 style="font-size:20px;font-weight:800;margin-bottom:14px">{t(lang, "finishes")}</h2><div class="fins">{fin_items}</div></div>'

    brochure_btn = ''
    if series.get('brochure'):
        brochure_btn = f'<a class="catalog-dl" href="{P}{series["brochure"]}" target="_blank" download>{t(lang, "download_catalog")}</a>'

    sname = esc(series['name'])
    desc = s_get(series, 'description', lang)
    category = esc(s_get(series, 'category', lang))
    meta_desc = f"{sname}: {desc[:140]}"
    og = meta_tags(f"{sname} — Baltscand", meta_desc, series['heroImage'], f'{lang}/products/{slug}/index.html')

    page = f"""<!DOCTYPE html>
<html lang="{t(lang, 'html_lang')}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{sname} — Baltscand | Finland & Baltics</title>
<meta name="description" content="{esc(meta_desc)}">
{og}
{jsonld_org(lang)}
<link rel="stylesheet" href="{P}styles.css">
</head>
<body>
{nav(lang, '../../', current_path)}

<div class="series-hero">
  <div class="series-hero-inner">
    <div class="series-hero-text">
      <div class="eyebrow">{category}</div>
      <h1>{sname}</h1>
      <p>{esc(desc)}</p>
      <a class="btn-primary" href="javascript:void(0)" onclick="openQuoteModal('{sname}')">{t(lang, 'get_quote_for', name=sname)}</a>
      {brochure_btn}
    </div>
    <div class="series-hero-img">
      <img src="{P}{series['heroImage']}" alt="{sname}">
    </div>
  </div>
</div>

<div class="series-body">
  <div class="breadcrumb">
    <a href="../../index.html">{t(lang, 'home')}</a> &rsaquo; {sname}
  </div>

  {stds}

  <div class="series-features">
    <h2>{t(lang, 'key_features')}</h2>
    <div class="feat-grid">{feats}</div>
  </div>

  {fins}

  <h2 style="font-size:24px;font-weight:800;margin-bottom:20px">{t(lang, 'products_in', name=sname)}</h2>
  <div class="products-grid">{product_cards}</div>

  {consult(lang, P)}
</div>

{modal(lang)}
{foot(lang)}
{back_to_top()}
</body>
</html>"""

    path = os.path.join(out, 'index.html')
    with open(path, 'w') as f:
        f.write(page)
    print(f'  {lang}/products/{slug}/index.html')


# ═══════════════════════════════════════════════════════════════════════════
# PRODUCT DETAIL PAGES
# ═══════════════════════════════════════════════════════════════════════════

def gen_product(series, product, lang):
    slug = series['slug']
    pid = product['id']
    out = os.path.join(BASE, lang, 'products', slug)
    os.makedirs(out, exist_ok=True)
    P = '../../../'  # from /lang/products/series/ to root
    current_path = f'/{lang}/products/{slug}/{pid}.html'

    pname = esc(s_get(product, 'name', lang))
    sname = esc(series['name'])
    ptype = esc(s_get(product, 'type', lang))
    pdesc = esc(s_get(product, 'description', lang))

    # Gallery
    gallery = product.get('gallery', [product.get('image', '')])
    main_img = P + gallery[0]
    thumbs = ''.join(
        f'<div class="thumb{" active" if i==0 else ""}" onclick="chImg(\'{P}{img}\',this)"><img src="{P}{img}" alt="{pname} - {i+1}"></div>'
        for i, img in enumerate(gallery)
    )
    gallery_js = ','.join(f"'{P}{img}'" for img in gallery)

    # Specs
    specs = product.get('specs', {})
    spec_rows = ''.join(f'<tr><td>{esc(k)}</td><td>{esc(str(v))}</td></tr>' for k, v in specs.items())

    # Available sizes
    opts = product.get('options', {})
    sizes_html = ''
    for opt_name, vals in opts.items():
        label = opt_name.replace('_', ' ').replace('Types', '').replace('types', '').title()
        tags = ''.join(
            f'<span class="size-tag">{v} mm</span>' if isinstance(v, int) else f'<span class="size-tag">{esc(str(v))}</span>'
            for v in vals
        )
        sizes_html += f'<div class="size-group"><div class="size-label">{esc(label)}</div><div class="size-tags">{tags}</div></div>'

    # Load table
    lt = product.get('loadTable')
    lt_html = ''
    if lt:
        cols = ''.join(f'<th>{esc(c)}</th>' for c in lt['columns'])
        for sec in ['standard', 'reinforced']:
            rows_data = lt.get(sec)
            if not rows_data:
                continue
            rows = ''
            for row in rows_data:
                cells = f'<td>{esc(str(row[0]))}</td>'
                for v in row[1:]:
                    cells += f'<td>{"—" if v is None else esc(str(v))}</td>'
                rows += f'<tr>{cells}</tr>'
            lt_html += f'<h4 style="margin:20px 0 8px;font-size:14px;color:#1a1a2e">{sec.title()}</h4><table class="lt"><thead><tr>{cols}</tr></thead><tbody>{rows}</tbody></table>'

    # Accessories
    accs = product.get('accessories', [])
    acc_html = ''.join(
        f'<div class="acc"><strong>{esc(a["name"])}</strong><span>{esc(a["description"])}</span></div>'
        for a in accs
    )

    # Use cases
    ucs = product.get('useCases', [])
    uc_html = ''.join(
        f'<div class="uc"><img src="{P}{uc["image"]}" alt="{esc(uc["label"])}" loading="lazy"><div class="uc-label">{esc(uc["label"])}</div></div>'
        for uc in ucs
    )

    # Features
    feats = ''.join(f'<li>{esc(f)}</li>' for f in s_list(series, 'features', lang))

    # Finishes
    fins = series.get('finishes', [])
    fin_html = ''.join(
        f'<div class="fin"><div class="fin-dot" style="background:{f["color"]}"></div><div><div class="fin-name">{esc(f["name"])}</div><div class="fin-code">{esc(f["code"])}</div></div></div>'
        for f in fins
    )

    # Uprights
    uprights = product.get('uprights')
    uprights_html = ''
    if uprights:
        items = ''.join(
            f'<div class="upright-item"><span class="upright-name">{esc(u["name"])}</span><span class="upright-load">{esc(u["load"])}</span></div>'
            for u in uprights.get('types', [])
        )
        feats_up = ''.join(f'<li style="font-size:12px;color:#666;margin:3px 0">{esc(f)}</li>' for f in uprights.get('features', []))
        uprights_html = f'<div class="uprights-section"><h4>Upright Types</h4>{items}<ul style="list-style:disc;margin:10px 0 0 18px">{feats_up}</ul></div>'

    # Related products
    related_html = ''
    siblings = [p for p in series['products'] if p['id'] != product['id']]
    if siblings:
        cards = ''
        for sib in siblings:
            sib_img = P + sib.get('gallery', [sib.get('image', '')])[0]
            sib_name = esc(s_get(sib, 'name', lang))
            sib_desc = esc(s_get(sib, 'description', lang)[:100])
            cards += f'<a href="{sib["id"]}.html" class="related-card"><img src="{sib_img}" alt="{sib_name}" loading="lazy"><div class="related-card-info"><h4>{sib_name}</h4><p>{sib_desc}...</p></div></a>'
        related_html = f'<div class="related-section"><h2 class="section-heading">{t(lang, "more_in", name=sname)}</h2><div class="related-grid">{cards}</div></div>'

    # Standards
    stds = series.get('standards', [])
    stds_html = ''
    if stds:
        stds_html = '<div class="std-badges-product">' + ''.join(f'<span class="std-badge">{esc(s)}</span>' for s in stds) + '</div>'

    # Brochure link
    brochure_html = ''
    if series.get('brochure'):
        brochure_html = f'<a class="catalog-dl" href="{P}{series["brochure"]}" target="_blank" download>{t(lang, "download_catalog_series", name=sname)}</a>'

    meta_desc = s_get(product, 'metaDescription', lang) or s_get(product, 'description', lang)[:155]
    url = f'{lang}/products/{slug}/{pid}.html'
    og = meta_tags(f"{pname} — Baltscand", meta_desc, gallery[0], url, og_type='product')
    jld = jsonld_product(product, series, url, lang)

    page = f"""<!DOCTYPE html>
<html lang="{t(lang, 'html_lang')}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{pname} — Baltscand | Finland & Baltics</title>
<meta name="description" content="{esc(meta_desc)}">
{og}
{jld}
<link rel="stylesheet" href="{P}styles.css">
</head>
<body>
{nav(lang, '../../', current_path)}

<div class="breadcrumb">
  <a href="../../index.html">{t(lang, 'home')}</a> &rsaquo;
  <a href="index.html">{sname}</a> &rsaquo;
  {pname}
</div>

<div class="product-hero">
  <div class="gallery">
    <div class="main-img" onclick="openLightbox(0)"><img id="mainImg" src="{main_img}" alt="{pname}"></div>
    <div class="thumbs">{thumbs}</div>
  </div>

  <div class="info">
    <div class="eyebrow">{ptype}</div>
    <h1>{pname}</h1>
    <p class="desc">{pdesc}</p>

    <ul class="feats">{feats}</ul>

    {stds_html}
    {uprights_html}

    <div class="note-box">
      {t(lang, 'contact_note')}
    </div>

    {f'<div style="margin-bottom:20px"><div class="size-label">{t(lang, "available_sizes")}</div>{sizes_html}</div>' if sizes_html else ''}

    {f'<div style="margin-bottom:20px"><div class="size-label">{t(lang, "finishes")}</div><div class="fins">{fin_html}</div></div>' if fin_html else ''}

    {brochure_html}

    <div class="consult-box">
      <h3>{t(lang, 'interested_in_product', name=pname)}</h3>
      <p>{t(lang, 'consult_desc')}</p>
      <a class="btn-primary" href="javascript:void(0)" onclick="openQuoteModal('{pname}')">{t(lang, 'get_quote')}</a>
    </div>
  </div>
</div>

<div class="detail-section">
  <div class="section-block">
    <h2 class="section-heading">{t(lang, 'tech_specs')}</h2>
    <table class="specs">{spec_rows}</table>
  </div>

  {"<div class='section-block'><h2 class='section-heading'>" + t(lang, 'load_capacity') + "</h2>" + lt_html + "<p style='margin-top:16px;font-size:13px;color:#888'>" + t(lang, 'load_note') + "</p></div>" if lt_html else ""}

  {"<div class='section-block'><h2 class='section-heading'>" + t(lang, 'accessories') + "</h2><div class='acc-grid'>" + acc_html + "</div></div>" if acc_html else ""}

  {"<div class='section-block'><h2 class='section-heading'>" + t(lang, 'applications') + "</h2><div class='uc-grid'>" + uc_html + "</div></div>" if uc_html else ""}
</div>

{related_html}

{consult(lang, P)}
{modal(lang)}
{foot(lang)}
{back_to_top()}

<!-- Lightbox -->
<div class="lightbox" id="lightbox" onclick="if(event.target===this)closeLightbox()">
  <button class="lightbox-close" onclick="closeLightbox()" aria-label="Close">&times;</button>
  <button class="lightbox-nav lightbox-prev" onclick="navLightbox(-1)" aria-label="Previous">&lsaquo;</button>
  <img id="lbImg" src="" alt="">
  <button class="lightbox-nav lightbox-next" onclick="navLightbox(1)" aria-label="Next">&rsaquo;</button>
</div>

<script>
var gallery=[{gallery_js}],lbIdx=0;
function chImg(s,el){{document.getElementById('mainImg').src=s;document.querySelectorAll('.thumb').forEach(function(t){{t.classList.remove('active')}});el.classList.add('active');lbIdx=gallery.indexOf(s);if(lbIdx<0)lbIdx=0}}
function openLightbox(i){{lbIdx=i;document.getElementById('lbImg').src=gallery[lbIdx];document.getElementById('lightbox').classList.add('show');document.body.style.overflow='hidden'}}
function closeLightbox(){{document.getElementById('lightbox').classList.remove('show');document.body.style.overflow=''}}
function navLightbox(d){{lbIdx=(lbIdx+d+gallery.length)%gallery.length;document.getElementById('lbImg').src=gallery[lbIdx]}}
document.addEventListener('keydown',function(e){{if(!document.getElementById('lightbox').classList.contains('show'))return;if(e.key==='ArrowLeft')navLightbox(-1);if(e.key==='ArrowRight')navLightbox(1);if(e.key==='Escape')closeLightbox()}});
</script>
</body>
</html>"""

    path = os.path.join(out, f'{pid}.html')
    with open(path, 'w') as f:
        f.write(page)
    print(f'  {lang}/products/{slug}/{pid}.html')


# ═══════════════════════════════════════════════════════════════════════════
# SEO FILES
# ═══════════════════════════════════════════════════════════════════════════

def gen_robots():
    content = f"""User-agent: *
Allow: /
Sitemap: {SITE_URL}/sitemap.xml
"""
    with open(os.path.join(BASE, 'robots.txt'), 'w') as f:
        f.write(content)
    print('  robots.txt')

def gen_sitemap():
    urls = [('index.html', '1.0')]
    for lang in LANGS:
        urls.append((f'{lang}/index.html', '1.0'))
        for s in data['series']:
            urls.append((f'{lang}/products/{s["slug"]}/index.html', '0.9'))
            for p in s['products']:
                urls.append((f'{lang}/products/{s["slug"]}/{p["id"]}.html', '0.8'))

    entries = ''
    for url, priority in urls:
        entries += f'  <url><loc>{SITE_URL}/{url}</loc><priority>{priority}</priority></url>\n'

    content = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{entries}</urlset>
"""
    with open(os.path.join(BASE, 'sitemap.xml'), 'w') as f:
        f.write(content)
    print('  sitemap.xml')


# ═══════════════════════════════════════════════════════════════════════════
# 404 PAGE
# ═══════════════════════════════════════════════════════════════════════════

def gen_404(lang):
    lang_dir = os.path.join(BASE, lang)
    os.makedirs(lang_dir, exist_ok=True)
    gi = t(lang, 'general_inquiry')
    current_path = f'/{lang}/404.html'

    page = f"""<!DOCTYPE html>
<html lang="{t(lang, 'html_lang')}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{t(lang, 'page_not_found')} — Baltscand</title>
<link rel="stylesheet" href="../styles.css">
</head>
<body>
{nav(lang, '', current_path)}
<div style="text-align:center;padding:120px 40px 80px;max-width:600px;margin:0 auto">
  <h1 style="font-size:72px;font-weight:900;color:#e8e8ee;margin-bottom:16px">404</h1>
  <h2 style="font-size:28px;font-weight:800;margin-bottom:12px">{t(lang, 'page_not_found')}</h2>
  <p style="color:#666;font-size:16px;line-height:1.6;margin-bottom:32px">{t(lang, '404_desc')}</p>
  <div style="display:flex;gap:16px;justify-content:center;flex-wrap:wrap">
    <a class="btn-primary" href="index.html">{t(lang, 'browse_products')}</a>
    <a class="btn-ghost" href="javascript:void(0)" onclick="openQuoteModal('{gi}')">{t(lang, 'contact_sales')}</a>
  </div>
</div>
{modal(lang)}
{foot(lang)}
</body>
</html>"""

    with open(os.path.join(lang_dir, '404.html'), 'w') as f:
        f.write(page)
    print(f'  {lang}/404.html')


# ═══════════════════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════════════════

if __name__ == '__main__':
    print('Generating Baltscand site v4 (bilingual EN/FI)...\n')

    gen_css()
    gen_robots()
    gen_sitemap()
    gen_root_index()

    for lang in LANGS:
        print(f'\n  [{lang.upper()}]')
        gen_index(lang)
        for s in data['series']:
            gen_series_page(s, lang)
            for p in s['products']:
                gen_product(s, p, lang)
        gen_404(lang)

    total = sum(len(s['products']) for s in data['series'])
    series_count = len(data['series'])
    per_lang = f'{series_count} series + {total} products + 404'
    print(f'\nDone! root index + styles.css + robots.txt + sitemap.xml')
    print(f'  EN: {per_lang}')
    print(f'  FI: {per_lang}')
    print(f'  Total: {2 * (1 + series_count + total + 1) + 4} files')
