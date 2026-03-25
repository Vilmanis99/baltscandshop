#!/usr/bin/env python3
"""
Baltscand Web Shop — Static Site Generator v4
Bilingual (EN/FI) with language switcher, SEO, series pages, visual polish, accessibility
"""

import json, os, html as h

BASE = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(BASE, 'data', 'products.json')) as f:
    data = json.load(f)

SITE_URL = 'https://baltscandshop.vercel.app'  # Vercel deployment URL

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
        'trust_certified': 'Bureau Veritas Certified',
        'trust_made_in': 'Made in France',
        'trust_standards': 'EN 15512 / EN 15620',
        'trust_since': 'Since 1969',
        'why_baltscand': 'Why Baltscand?',
        'why_1_title': 'Expert Consultation',
        'why_1_desc': 'Professional project planning and product selection by our experienced team.',
        'why_2_title': 'Finland & Baltics Delivery',
        'why_2_desc': 'Direct delivery and logistics across Finland, Estonia, Latvia and Lithuania.',
        'why_3_title': 'Installation Support',
        'why_3_desc': 'Professional installation services and on-site technical support available.',
        'distributor_line': 'Baltscand — Official Provost distributor for Finland and the Baltics.',
        'sticky_quote': 'Get a Quote',
        'call_us': 'Call Us',
        # Services page
        'services': 'Services',
        'services_title': 'Our Services',
        'services_subtitle': 'From initial consultation to installation and beyond — we support your project at every stage.',
        'svc_consult_title': 'Consultation & Project Planning',
        'svc_consult_desc': 'Our experts assess your space, understand your storage needs, and recommend the optimal shelving and racking configuration. Free site assessment and detailed project proposals.',
        'svc_delivery_title': 'Delivery & Logistics',
        'svc_delivery_desc': 'Direct delivery across Finland, Estonia, Latvia and Lithuania. We coordinate logistics from Provost\'s European factories to your site, handling customs and transport.',
        'svc_install_title': 'Professional Installation',
        'svc_install_desc': 'Trained assembly teams handle the complete installation — from unloading to final inspection. Full compliance with safety regulations and site protocols.',
        'svc_support_title': 'After-Sales Support',
        'svc_support_desc': 'Need to expand, reconfigure, or maintain your system? We provide ongoing support, spare parts, and modification services as your business evolves.',
        'start_project': 'Start Your Project',
        # About page
        'about_title': 'About Baltscand',
        'about_intro': 'Baltscand is the official Provost distributor for Finland and the Baltic states. We bring European-quality industrial storage solutions with local expertise and service.',
        'about_provost_title': 'About Provost',
        'about_provost_desc': 'Founded in 1963 in Halluin, France, Provost has grown into one of Europe\'s leading manufacturers of industrial shelving and storage solutions. With over 800 employees, 6 European factories, and 80% in-house manufacturing, Provost delivers quality and reliability across 10,000+ product references.',
        'about_provost_stats': '800+ employees | 6 factories | 60+ years | 80,000 customers',
        'about_why_title': 'Why Choose Baltscand?',
        'about_why_1': 'Local expertise — Finnish and English-speaking team with deep knowledge of Nordic industrial requirements.',
        'about_why_2': 'Regional delivery network — direct logistics to Finland, Estonia, Latvia, and Lithuania.',
        'about_why_3': 'Professional installation — trained teams for safe, compliant assembly on your site.',
        'about_why_4': 'Single point of contact — from consultation to after-sales, one team handles everything.',
        'about_certs_title': 'Certifications & Standards',
        'about_cert_1': 'Origine France Garantie — certified French manufacturing for key product ranges',
        'about_cert_2': 'EN 15512 / EN 15620 — European racking design and usage standards compliance',
        'about_cert_3': 'EcoVadis evaluated — corporate social responsibility commitment',
        # Industry pages
        'industries': 'Industries',
        'ind_warehousing': 'Warehousing & Logistics',
        'ind_warehousing_desc': 'Maximise your warehouse capacity with pallet racking, long-span shelving, and multi-tier platforms designed for high-volume logistics operations.',
        'ind_warehousing_challenge': 'Warehouses need to store more in less space while maintaining fast access for picking and dispatch. The right racking system can double or triple your usable storage area.',
        'ind_retail': 'Retail & Distribution',
        'ind_retail_desc': 'Organise your back-of-store and distribution centre with versatile shelving for varied product sizes — from small parts bins to bulk goods.',
        'ind_retail_challenge': 'Retail environments demand flexibility: seasonal stock changes, varied product dimensions, and fast restocking cycles. Modular shelving adapts to your needs.',
        'ind_manufacturing': 'Manufacturing & Automotive',
        'ind_manufacturing_desc': 'Heavy-duty racking for raw materials, components, and finished goods. Tire storage, parts shelving, and workshop organisation for production environments.',
        'ind_manufacturing_challenge': 'Manufacturing facilities handle heavy loads, oversized parts, and high-value inventory. Industrial-grade racking with verified load capacities keeps operations safe and efficient.',
        'ind_archive': 'Archives & Office',
        'ind_archive_desc': 'Compact archive shelving and document storage for offices, libraries, and records management. Space-efficient solutions that keep files organised and accessible.',
        'ind_archive_challenge': 'Document archives grow continuously while floor space stays the same. Purpose-built archive shelving maximises vertical space with easy file retrieval.',
        'recommended_products': 'Recommended Products',
        'industry_challenge': 'The Challenge',
        'explore_solutions': 'Explore Solutions',
        # Solutions by Need (homepage)
        'solutions_by_need': 'Solutions by Need',
        'sbn_heavy_title': 'Heavy-Duty Storage',
        'sbn_heavy_desc': 'Pallet racking and long-span shelving for warehouses and logistics centres.',
        'sbn_light_title': 'Light Shelving',
        'sbn_light_desc': 'Versatile industrial shelving for workshops, stockrooms, and archives.',
        'sbn_bins_title': 'Bins & Small Parts',
        'sbn_bins_desc': 'Modular bin storage for organised small parts, tools, and components.',
        'sbn_platforms_title': 'Platforms & Mezzanines',
        'sbn_platforms_desc': 'Multi-level platforms to double your floor space without building extensions.',
        # Enhanced form
        'industry_label': 'Industry *',
        'industry_ph': 'Select your industry',
        'ind_opt_warehousing': 'Warehousing & Logistics',
        'ind_opt_retail': 'Retail & Distribution',
        'ind_opt_manufacturing': 'Manufacturing & Automotive',
        'ind_opt_archive': 'Archives & Office',
        'ind_opt_other': 'Other',
        'project_type_label': 'Project Type',
        'project_type_ph': 'Select project type',
        'pt_new': 'New Installation',
        'pt_expansion': 'Expansion / Addition',
        'pt_replacement': 'Replacement / Upgrade',
        # Pricing
        'from_price': 'From',
        'price_excl_tax': 'excl. tax',
        'price_note': 'Starting prices shown for reference. Final pricing depends on configuration, quantity and delivery location. Contact us for a detailed quote.',
        'starting_from': 'Starting from',
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
        'trust_certified': 'Bureau Veritas -sertifioitu',
        'trust_made_in': 'Valmistettu Ranskassa',
        'trust_standards': 'EN 15512 / EN 15620',
        'trust_since': 'Vuodesta 1969',
        'why_baltscand': 'Miksi Baltscand?',
        'why_1_title': 'Asiantunteva konsultointi',
        'why_1_desc': 'Ammattimainen projektisuunnittelu ja tuotevalinta kokeneelta tiimiltämme.',
        'why_2_title': 'Toimitus Suomeen ja Baltiaan',
        'why_2_desc': 'Suorat toimitukset Suomeen, Viroon, Latviaan ja Liettuaan.',
        'why_3_title': 'Asennustuki',
        'why_3_desc': 'Ammattimainen asennuspalvelu ja paikan päällä tapahtuva tekninen tuki.',
        'distributor_line': 'Baltscand — Provostin virallinen jakelija Suomessa ja Baltiassa.',
        'sticky_quote': 'Pyydä tarjous',
        'call_us': 'Soita meille',
        # Services page
        'services': 'Palvelut',
        'services_title': 'Palvelumme',
        'services_subtitle': 'Alkukonsultaatiosta asennukseen ja sen jälkeen — tuemme projektiasi jokaisessa vaiheessa.',
        'svc_consult_title': 'Konsultointi ja projektisuunnittelu',
        'svc_consult_desc': 'Asiantuntijamme arvioivat tilasi, selvittävät varastointitarpeesi ja suosittelevat optimaalisen hylly- ja telinekokoonpanon. Ilmainen tilanarviointi ja yksityiskohtaiset projektiehdotukset.',
        'svc_delivery_title': 'Toimitus ja logistiikka',
        'svc_delivery_desc': 'Suorat toimitukset Suomeen, Viroon, Latviaan ja Liettuaan. Koordinoimme logistiikan Provostin Euroopan tehtailta kohteellesi, huolehdimme tullauksesta ja kuljetuksesta.',
        'svc_install_title': 'Ammattimainen asennus',
        'svc_install_desc': 'Koulutetut asennustiimimme hoitavat koko asennuksen — purkamisesta lopputarkastukseen. Täysi turvallisuusmääräysten ja työmaakäytäntöjen noudattaminen.',
        'svc_support_title': 'Jälkimyyntituki',
        'svc_support_desc': 'Tarvitsetko laajennusta, uudelleenjärjestelyä tai huoltoa? Tarjoamme jatkuvaa tukea, varaosia ja muutospalveluita liiketoimintasi kehittyessä.',
        'start_project': 'Aloita projektisi',
        # About page
        'about_title': 'Tietoa Baltscandista',
        'about_intro': 'Baltscand on Provostin virallinen jakelija Suomessa ja Baltian maissa. Tuomme eurooppalaisen laadun teollisiin varastoratkaisuihin paikallisella asiantuntemuksella ja palvelulla.',
        'about_provost_title': 'Tietoa Provostista',
        'about_provost_desc': 'Vuonna 1963 Halluinissa, Ranskassa perustettu Provost on kasvanut yhdeksi Euroopan johtavista teollisten hylly- ja varastointiratkaisujen valmistajista. Yli 800 työntekijää, 6 Euroopan tehdasta ja 80 % omaa valmistusta — Provost toimittaa laatua ja luotettavuutta yli 10 000 tuoteviitteellä.',
        'about_provost_stats': '800+ työntekijää | 6 tehdasta | 60+ vuotta | 80 000 asiakasta',
        'about_why_title': 'Miksi valita Baltscand?',
        'about_why_1': 'Paikallinen asiantuntemus — suomea ja englantia puhuva tiimi, jolla on syvä tuntemus pohjoismaisista teollisuusvaatimuksista.',
        'about_why_2': 'Alueellinen toimitusverkosto — suorat toimitukset Suomeen, Viroon, Latviaan ja Liettuaan.',
        'about_why_3': 'Ammattimainen asennus — koulutetut tiimit turvalliseen ja säädöstenmukaiseen asennukseen.',
        'about_why_4': 'Yksi yhteyshenkilö — konsultaatiosta jälkimyyntiin, yksi tiimi hoitaa kaiken.',
        'about_certs_title': 'Sertifioinnit ja standardit',
        'about_cert_1': 'Origine France Garantie — sertifioitu ranskalainen valmistus keskeisille tuotesarjoille',
        'about_cert_2': 'EN 15512 / EN 15620 — eurooppalaiset kuormahyllystandardit',
        'about_cert_3': 'EcoVadis-arvioitu — sitoutuminen yritysvastuuseen',
        # Industry pages
        'industries': 'Toimialat',
        'ind_warehousing': 'Varastointi ja logistiikka',
        'ind_warehousing_desc': 'Maksimoi varastokapasiteettisi kuormalavahyllyillä, pitkäjänteisillä hyllyillä ja monikerroksisilla tasoilla, jotka on suunniteltu suurten volyymien logistiikkatoimintoihin.',
        'ind_warehousing_challenge': 'Varastot tarvitsevat enemmän tilaa vähemmällä alalla, samalla säilyttäen nopean pääsyn keräilyyn ja lähetykseen. Oikea hyllyjärjestelmä voi kaksinkertaistaa tai kolminkertaistaa käyttökelpoisen varastotilasi.',
        'ind_retail': 'Vähittäiskauppa ja jakelu',
        'ind_retail_desc': 'Järjestä takavarasto ja jakelukeskus monipuolisilla hyllyillä erikokoisille tuotteille — pienistä osalaatikoista suuriin tavaroihin.',
        'ind_retail_challenge': 'Vähittäiskauppa vaatii joustavuutta: kausivaihtelut, vaihtelevat tuotekoot ja nopeat täydennysjaksot. Modulaariset hyllyt mukautuvat tarpeisiisi.',
        'ind_manufacturing': 'Teollisuus ja autoteollisuus',
        'ind_manufacturing_desc': 'Raskaiden kuormien hyllyt raaka-aineille, komponenteille ja valmiille tuotteille. Rengasvarastointi, osahyllyt ja työpajaorganisaatio tuotantoympäristöihin.',
        'ind_manufacturing_challenge': 'Teollisuuslaitokset käsittelevät raskaita kuormia, ylimitoitettuja osia ja arvokasta varastoa. Teollisuuslaatuiset hyllyt varmennettuine kantavuuksineen pitävät toiminnan turvallisena ja tehokkaana.',
        'ind_archive': 'Arkistot ja toimistot',
        'ind_archive_desc': 'Kompaktit arkistohyllyt ja asiakirjavarastointi toimistoihin, kirjastoihin ja tiedonhallintaan. Tilatehokkaat ratkaisut, jotka pitävät tiedostot järjestyksessä ja saavutettavissa.',
        'ind_archive_challenge': 'Asiakirja-arkistot kasvavat jatkuvasti, mutta lattiatila pysyy samana. Tarkoitukseen rakennetut arkistohyllyt maksimoivat pystytilan helpolla tiedostojen haulla.',
        'recommended_products': 'Suositellut tuotteet',
        'industry_challenge': 'Haaste',
        'explore_solutions': 'Tutustu ratkaisuihin',
        # Solutions by Need (homepage)
        'solutions_by_need': 'Ratkaisut tarpeittain',
        'sbn_heavy_title': 'Raskas varastointi',
        'sbn_heavy_desc': 'Kuormalavahyllyt ja pitkäjänteiset hyllyt varastoihin ja logistiikkakeskuksiin.',
        'sbn_light_title': 'Kevyet hyllyt',
        'sbn_light_desc': 'Monikäyttöiset teollisuushyllyt työpajoihin, varastohuoneisiin ja arkistoihin.',
        'sbn_bins_title': 'Laatikot ja pienet osat',
        'sbn_bins_desc': 'Modulaarinen laatikkovarastointi järjestelmälliseen pienten osien, työkalujen ja komponenttien säilytykseen.',
        'sbn_platforms_title': 'Tasot ja välikerrokset',
        'sbn_platforms_desc': 'Monikerroksiset tasot, jotka kaksinkertaistavat lattiatilasi ilman laajennusrakentamista.',
        # Enhanced form
        'industry_label': 'Toimiala *',
        'industry_ph': 'Valitse toimialasi',
        'ind_opt_warehousing': 'Varastointi ja logistiikka',
        'ind_opt_retail': 'Vähittäiskauppa ja jakelu',
        'ind_opt_manufacturing': 'Teollisuus ja autoteollisuus',
        'ind_opt_archive': 'Arkistot ja toimistot',
        'ind_opt_other': 'Muu',
        'project_type_label': 'Projektityyppi',
        'project_type_ph': 'Valitse projektityyppi',
        'pt_new': 'Uusi asennus',
        'pt_expansion': 'Laajennus / Lisäys',
        'pt_replacement': 'Vaihto / Päivitys',
        # Pricing
        'from_price': 'Alk.',
        'price_excl_tax': 'alv 0 %',
        'price_note': 'Aloitushinnat viitteellisiä. Lopullinen hinta riippuu kokoonpanosta, määrästä ja toimituspaikasta. Ota yhteyttä tarkkaa tarjousta varten.',
        'starting_from': 'Alkaen',
    }
}


# ─── Pricing Data (from provost.fr, EUR excl. tax) ────────────────────────
# Series-level "starting from" prices — matching provost.fr headline "à partir de"
# All prices double-checked from provost.fr product pages, EUR excl. tax (HT)
SERIES_PRICES = {
    'prospace-plus': 105,    # provost.fr/593 — "à partir de 105,01 €"
    'prorack-plus': 149,     # provost.fr/671 — "à partir de 148,98 €"
    'propal-3': 359,         # provost.fr/915 — "à partir de 359,41 €"
    'modul-plus': 460,       # provost.fr/3667 — "à partir de 459,86 €"
    # proplus-lp3: custom project-based, no standard starting price
}

# Product-level prices — matching provost.fr headline "à partir de" on each page
# Every price verified 2025-03-25 against the provost.fr URL in the comment
PRODUCT_PRICES = {
    # PROSPACE+
    'prospace-tubular': 105,          # provost.fr/593 — "à partir de 105,01 €"
    'prospace-metalsheet': 163,       # provost.fr/602 — "à partir de 163,27 €"
    'prospace-semitole': 174,         # provost.fr/1652 — "à partir de 173,99 €"
    'prospace-archive': 137,          # provost.fr/596 — "à partir de 136,84 €"
    'prospace-archive-semitole': 222, # provost.fr/608 — "à partir de 222,26 €"
    # PRORACK+
    'prorack-frames': 206,            # provost.fr/583 — "à partir de 205,65 €"
    'prorack-tire-rack': 150,         # provost.fr/584 — "à partir de 149,62 €"
    'prorack-garment-rack': 149,      # provost.fr/671 — "à partir de 148,98 €"
    'prorack-carton-storage': 231,    # provost.fr/581 — "à partir de 231,39 €"
    # PROPAL 3
    'propal3-static': 359,            # provost.fr/915 — "à partir de 359,41 €"
    # PROPLUS LP3 — component prices (platforms are custom/project)
    'proplus-staircases': 1464,       # provost.fr/1656 — "à partir de 1 464,44 €"
    'proplus-safety-gates': 1340,     # provost.fr/1218 — "à partir de 1 339,90 €"
    # MODUL+
    'modul-hinged-doors': 460,        # provost.fr/3667 — "à partir de 459,86 €"
    'modul-sliding-doors': 5790,      # provost.fr/3665 — "à partir de 5 789,71 €"
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

def hreflang_tags(lang, current_path):
    """Generate hreflang alternate links for EN↔FI cross-linking."""
    other = 'fi' if lang == 'en' else 'en'
    other_path = current_path.replace(f'/{lang}/', f'/{other}/', 1)
    return f"""<link rel="alternate" hreflang="en" href="{SITE_URL}{current_path if lang=='en' else other_path}">
<link rel="alternate" hreflang="fi" href="{SITE_URL}{other_path if lang=='en' else current_path}">
<link rel="alternate" hreflang="x-default" href="{SITE_URL}{current_path if lang=='en' else other_path}">"""

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

FAVICON = "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Crect width='100' height='100' rx='16' fill='%23072244'/%3E%3Ctext x='50' y='68' text-anchor='middle' font-family='sans-serif' font-size='60' font-weight='900' fill='%23ff6a00'%3EB%3C/text%3E%3C/svg%3E"

def favicon_link():
    return f'<link rel="icon" href="{FAVICON}">'

def jsonld_breadcrumb(crumbs, lang):
    """Generate BreadcrumbList JSON-LD. crumbs is list of (name, url) tuples."""
    items = []
    for i, (name, url) in enumerate(crumbs, 1):
        items.append(f'{{"@type":"ListItem","position":{i},"name":"{esc(name)}","item":"{SITE_URL}/{url}"}}')
    return f"""<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{",".join(items)}]}}
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
    base = f'/{lang}'
    return f"""
<header>
  <div class="nav-inner">
    <a class="logo" href="{base}/index.html">BALT<span>SCAND</span></a>
    <button class="hamburger" onclick="this.classList.toggle('open');document.getElementById('navLinks').classList.toggle('open')" aria-label="Toggle menu">
      <span></span><span></span><span></span>
    </button>
    <nav id="navLinks">
      <a href="{base}/index.html">{t(lang, 'products')}</a>
      <a href="{base}/services.html">{t(lang, 'services')}</a>
      <a href="{base}/industries/index.html">{t(lang, 'industries')}</a>
      <a href="{base}/about.html">{t(lang, 'about')}</a>
      {ls}
      <a class="mobile-call" href="tel:+358401234567">{t(lang, 'call_us')}</a>
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
    <div class="footer-distributor">{t(lang, 'distributor_line')}</div>
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
    <label for="formIndustry">{t(lang, 'industry_label')}</label>
    <select id="formIndustry" name="industry" style="width:100%;padding:13px 16px;border:2px solid #e8e8ee;border-radius:10px;font-size:15px;font-family:inherit;margin-bottom:16px;background:white;color:#333">
      <option value="">{t(lang, 'industry_ph')}</option>
      <option value="warehousing">{t(lang, 'ind_opt_warehousing')}</option>
      <option value="retail">{t(lang, 'ind_opt_retail')}</option>
      <option value="manufacturing">{t(lang, 'ind_opt_manufacturing')}</option>
      <option value="archive">{t(lang, 'ind_opt_archive')}</option>
      <option value="other">{t(lang, 'ind_opt_other')}</option>
    </select>
    <label for="formProjectType">{t(lang, 'project_type_label')}</label>
    <select id="formProjectType" name="project_type" style="width:100%;padding:13px 16px;border:2px solid #e8e8ee;border-radius:10px;font-size:15px;font-family:inherit;margin-bottom:16px;background:white;color:#333">
      <option value="">{t(lang, 'project_type_ph')}</option>
      <option value="new">{t(lang, 'pt_new')}</option>
      <option value="expansion">{t(lang, 'pt_expansion')}</option>
      <option value="replacement">{t(lang, 'pt_replacement')}</option>
    </select>
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
  if(!n){{document.getElementById('formName').focus();document.getElementById('formName').style.borderColor='#ff6a00';return}}
  if(!e||!/^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$/.test(e)){{document.getElementById('formEmail').focus();document.getElementById('formEmail').style.borderColor='#ff6a00';return}}
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
    css = """@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=DM+Serif+Display&display=swap');
/* Trust Strip */
.trust-strip{background:#072244;padding:16px 40px;position:relative;z-index:2}
.trust-strip-inner{max-width:1240px;margin:0 auto;display:flex;justify-content:center;gap:36px;flex-wrap:wrap;align-items:center}
.trust-badge{display:inline-flex;align-items:center;gap:8px;font-size:13px;font-weight:600;color:rgba(255,255,255,0.6);white-space:nowrap}
.trust-badge svg{width:18px;height:18px;color:#ff6a00;flex-shrink:0}
.trust-badge .accent{color:white;font-weight:700}
/* Why Baltscand */
.why-section{max-width:1240px;margin:0 auto;padding:48px 40px}
.why-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:20px;margin-top:20px}
.why-card{background:white;border:1px solid #e8e8ee;border-radius:14px;padding:28px;text-align:center;transition:all 0.2s}
.why-card:hover{border-color:#ff6a00;transform:translateY(-2px);box-shadow:0 8px 24px rgba(0,0,0,0.06)}
.why-card .why-icon{width:48px;height:48px;background:#fff3e6;border-radius:12px;display:flex;align-items:center;justify-content:center;margin:0 auto 16px}
.why-card .why-icon svg{width:24px;height:24px;color:#ff6a00}
.why-card h3{font-size:16px;font-weight:800;margin-bottom:6px}
.why-card p{font-size:13px;color:#666;line-height:1.5}
/* Sticky Quote Bar */
.sticky-quote{position:fixed;bottom:0;left:0;right:0;background:rgba(7,34,68,0.95);backdrop-filter:blur(12px);padding:12px 40px;z-index:99;transform:translateY(100%);transition:transform 0.3s ease;display:flex;align-items:center;justify-content:center;gap:16px}
.sticky-quote.show{transform:translateY(0)}
.sticky-quote span{color:rgba(255,255,255,0.7);font-size:14px;font-weight:500}
.sticky-quote .btn-primary{padding:10px 28px;font-size:14px;border-radius:8px}
/* Mobile Call */
.mobile-call{display:none!important}
/* Footer Distributor */
.footer-distributor{color:rgba(255,255,255,0.35);font-size:12px;text-align:center;width:100%;order:3;margin-top:4px}
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:'Inter',system-ui,-apple-system,sans-serif;color:#0f1729;background:#f8fafc;-webkit-font-smoothing:antialiased}
img{max-width:100%;display:block}
a{text-decoration:none;color:inherit}

/* Header */
header{background:#072244;color:white;position:sticky;top:0;z-index:100;backdrop-filter:blur(12px)}
.nav-inner{max-width:1320px;margin:0 auto;display:flex;align-items:center;justify-content:space-between;padding:18px 40px}
.logo{font-size:22px;font-weight:800;letter-spacing:3px}
.logo span{color:#ff6a00}
nav{display:flex;gap:32px;align-items:center}
nav a{color:rgba(255,255,255,0.8);font-size:13px;font-weight:600;text-transform:uppercase;letter-spacing:1.5px;padding:4px 0;border-bottom:2px solid transparent;transition:all 0.2s}
nav a:hover,nav a.active{color:white;border-bottom-color:#ff6a00}
.nav-cta{background:#ff6a00;color:white;padding:10px 24px;border-radius:8px;font-size:13px;font-weight:700;letter-spacing:0.5px;transition:background 0.2s}
.nav-cta:hover{background:#e85d04}
.lang-switch{background:rgba(255,255,255,0.1);padding:6px 14px;border-radius:6px;font-size:12px;font-weight:600;letter-spacing:0.5px;text-transform:none;border:1px solid rgba(255,255,255,0.15);transition:all 0.2s}
.lang-switch:hover{background:rgba(255,255,255,0.2);border-color:rgba(255,255,255,0.3);border-bottom-color:rgba(255,255,255,0.3)}

/* Hamburger */
.hamburger{display:none;background:none;border:none;cursor:pointer;padding:8px;flex-direction:column;gap:5px}
.hamburger span{display:block;width:24px;height:2px;background:white;transition:all 0.3s}
.hamburger.open span:nth-child(1){transform:rotate(45deg) translate(5px,5px)}
.hamburger.open span:nth-child(2){opacity:0}
.hamburger.open span:nth-child(3){transform:rotate(-45deg) translate(5px,-5px)}

/* Footer */
footer{background:#072244;color:rgba(255,255,255,0.5);padding:48px 40px 32px}
.footer-inner{max-width:1320px;margin:0 auto;display:flex;justify-content:space-between;align-items:center;font-size:13px;flex-wrap:wrap;gap:16px}
.footer-inner a{color:#ff6a00;transition:color 0.2s}
.footer-inner a:hover{color:#ff8c33}
.footer-sep{margin:0 8px;opacity:0.3}
.footer-links{display:flex;align-items:center}

/* Buttons */
.btn-primary{display:inline-flex;align-items:center;gap:10px;background:#ff6a00;color:white;padding:16px 36px;border-radius:12px;font-size:16px;font-weight:700;border:none;cursor:pointer;transition:all 0.25s;box-shadow:0 4px 16px rgba(255,106,0,0.3)}
.btn-primary:hover{background:#e85d04;transform:translateY(-1px);box-shadow:0 6px 24px rgba(255,106,0,0.4)}
.btn-ghost{display:inline-flex;align-items:center;gap:10px;background:transparent;color:#0f1729;padding:14px 32px;border-radius:12px;font-size:15px;font-weight:600;border:2px solid #d0d0d8;cursor:pointer;transition:all 0.2s}
.btn-ghost:hover{border-color:#0f1729;background:#072244;color:white}

/* Consultation banner */
.consult-banner{background:linear-gradient(135deg,#072244,#0a3260);border-radius:20px;padding:48px;display:flex;align-items:center;justify-content:space-between;gap:40px;margin:60px 40px;max-width:1240px;color:white}
.consult-banner h2{font-size:28px;font-weight:800;margin-bottom:8px}
.consult-banner p{color:rgba(255,255,255,0.65);font-size:15px;line-height:1.6;max-width:540px}
.consult-banner .btn-primary{background:white;color:#0f1729;box-shadow:0 4px 16px rgba(0,0,0,0.2)}
.consult-banner .btn-primary:hover{background:#f0f0f0;transform:translateY(-1px)}

/* Modal */
.modal-overlay{display:none;position:fixed;top:0;left:0;right:0;bottom:0;background:rgba(0,0,0,0.6);z-index:1000;align-items:center;justify-content:center;backdrop-filter:blur(4px)}
.modal-overlay.show{display:flex}
.modal{background:white;border-radius:20px;padding:44px;max-width:520px;width:92%;max-height:90vh;overflow-y:auto;position:relative;box-shadow:0 24px 64px rgba(0,0,0,0.2)}
.modal h2{font-size:24px;font-weight:800;margin-bottom:4px}
.modal .sub{color:#666;font-size:14px;margin-bottom:28px}
.modal .summary{background:#f8fafc;border-radius:12px;padding:16px 20px;margin-bottom:24px;font-size:14px;line-height:1.7;border-left:4px solid #ff6a00}
.modal label{display:block;font-size:12px;font-weight:700;color:#888;margin-bottom:6px;text-transform:uppercase;letter-spacing:1px}
.modal input,.modal textarea{width:100%;padding:13px 16px;border:2px solid #e8e8ee;border-radius:10px;font-size:15px;font-family:inherit;margin-bottom:16px;transition:border 0.2s}
.modal input:focus,.modal textarea:focus{outline:none;border-color:#ff6a00}
.modal textarea{height:80px;resize:vertical}
.modal .btn-submit{width:100%;background:#ff6a00;color:white;border:none;padding:16px;border-radius:12px;font-size:16px;font-weight:700;cursor:pointer;transition:all 0.2s}
.modal .btn-submit:hover{background:#e85d04}
.modal .btn-submit:disabled{cursor:not-allowed}
.modal .close{position:absolute;top:20px;right:20px;background:#f8fafc;border:none;width:36px;height:36px;border-radius:50%;font-size:18px;cursor:pointer;color:#666;display:flex;align-items:center;justify-content:center}

/* Back to top */
.btt{position:fixed;bottom:32px;right:32px;width:48px;height:48px;border-radius:50%;background:#072244;color:white;border:none;font-size:20px;cursor:pointer;opacity:0;transform:translateY(20px);transition:all 0.3s;z-index:90;box-shadow:0 4px 16px rgba(0,0,0,0.2)}
.btt.show{opacity:1;transform:translateY(0)}
.btt:hover{background:#ff6a00}

/* ===== INDEX PAGE ===== */

.hero{background:linear-gradient(135deg,#072244 0%,#0a3260 40%,#0d4a7a 100%);color:white;padding:100px 40px 80px;text-align:center;position:relative;overflow:hidden}
.hero::after{content:'';position:absolute;bottom:0;left:0;right:0;height:120px;background:linear-gradient(transparent,#f5f6f8)}
.hero h1{font-size:52px;font-weight:900;letter-spacing:-1px;margin-bottom:16px;position:relative;z-index:1}
.hero h1 span{color:#ff6a00}
.hero p{font-size:19px;color:rgba(255,255,255,0.6);max-width:640px;margin:0 auto 40px;line-height:1.6;position:relative;z-index:1}
.hero-cta{position:relative;z-index:1;display:flex;gap:16px;justify-content:center;flex-wrap:wrap}
.hero-stats{display:flex;justify-content:center;gap:64px;margin-top:56px;position:relative;z-index:1;flex-wrap:wrap}
.hero-stat{text-align:center}
.hero-stat .n{font-size:36px;font-weight:900;color:#ff6a00}
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
.series-title a:hover{color:#ff6a00}
.series-cat-badge{display:inline-block;background:#fff3e6;color:#ff6a00;padding:4px 14px;border-radius:6px;font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:1px}
.prod-count{font-size:13px;font-weight:500;color:#999}
.series-desc{color:#555;font-size:14px;line-height:1.6;margin:0;max-width:680px}
.series-header-right{display:flex;gap:10px;align-items:center;flex-shrink:0;padding-top:4px}
.standards-row{display:flex;flex-wrap:wrap;gap:6px;margin-bottom:16px}
.std-badge{display:inline-block;padding:4px 12px;background:#e8f5e9;color:#2d6a4f;border-radius:6px;font-size:11px;font-weight:700;letter-spacing:0.5px}
.btn-catalog{display:inline-flex;align-items:center;gap:8px;padding:10px 20px;background:#f8fafc;border:1px solid #d0d0d8;border-radius:10px;font-size:13px;font-weight:600;color:#555;transition:all 0.2s}
.btn-catalog:hover{background:#072244;color:white;border-color:#0f1729}
.btn-catalog svg{width:16px;height:16px}
.btn-view-all{display:inline-flex;align-items:center;gap:6px;padding:10px 22px;background:#ff6a00;color:white;border-radius:10px;font-size:13px;font-weight:700;transition:all 0.2s}
.btn-view-all:hover{background:#e85d04;transform:translateY(-1px)}

/* Product cards grid on homepage */
.series-products-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:16px}
.series-pcard{background:white;border-radius:14px;overflow:hidden;border:1px solid #e8e8ee;transition:all 0.25s;display:flex;flex-direction:column}
.series-section.odd .series-pcard{background:#fafafc}
.series-pcard:hover{transform:translateY(-4px);box-shadow:0 12px 32px rgba(0,0,0,0.08);border-color:#ff6a00}
.series-pcard img{width:100%;height:160px;object-fit:contain;padding:16px;background:#fafafc}
.series-section.odd .series-pcard img{background:white}
.series-pcard-body{padding:14px 16px;flex:1;display:flex;flex-direction:column}
.series-pcard-body h3{font-size:14px;font-weight:700;margin-bottom:4px;line-height:1.3;flex:1}
.series-pcard-body .card-link{display:inline-flex;align-items:center;gap:4px;color:#ff6a00;font-size:12px;font-weight:700;margin-top:6px}
/* Pricing */
.price-tag{display:inline-flex;align-items:baseline;gap:4px;margin-top:6px}
.price-tag .price-from{font-size:11px;color:#888;font-weight:500}
.price-tag .price-amount{font-size:16px;font-weight:800;color:#0f1729}
.price-tag .price-currency{font-size:12px;color:#888;font-weight:500}
.series-price{display:inline-flex;align-items:baseline;gap:6px;background:#fff3e6;padding:6px 14px;border-radius:8px;margin-left:auto}
.series-price .price-from{font-size:12px;color:#8a6530;font-weight:500}
.series-price .price-amount{font-size:20px;font-weight:900;color:#ff6a00}
.series-price .price-currency{font-size:13px;color:#8a6530;font-weight:600}
.product-price{background:#fff3e6;border:1px solid #f0d8b8;border-radius:12px;padding:16px 20px;margin-bottom:20px}
.product-price .price-from{font-size:13px;color:#8a6530;font-weight:500}
.product-price .price-amount{font-size:28px;font-weight:900;color:#ff6a00;margin:4px 0}
.product-price .price-note{font-size:12px;color:#8a6530;line-height:1.5}

/* ===== SERIES LANDING PAGE ===== */

.series-hero{background:linear-gradient(135deg,#072244 0%,#0a3260 40%,#0d4a7a 100%);color:white;padding:80px 40px 60px;position:relative}
.series-hero-inner{max-width:1240px;margin:0 auto;display:grid;grid-template-columns:1fr 1fr;gap:48px;align-items:center}
.series-hero-text .eyebrow{display:inline-block;background:rgba(255,106,0,0.2);color:#ff6a00;padding:5px 16px;border-radius:8px;font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:1.5px;margin-bottom:16px}
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
.product-card:hover{transform:translateY(-4px);box-shadow:0 12px 32px rgba(0,0,0,0.08);border-color:#ff6a00}
.product-card img{width:100%;height:220px;object-fit:contain;padding:20px;background:#fafafc}
.product-card-body{padding:20px}
.product-card-body h3{font-size:17px;font-weight:700;margin-bottom:6px}
.product-card-body p{font-size:13px;color:#666;line-height:1.5;margin-bottom:14px}
.product-card-body .card-link{display:inline-flex;align-items:center;gap:6px;color:#ff6a00;font-size:13px;font-weight:700}

/* ===== PRODUCT DETAIL PAGE ===== */

.breadcrumb{padding:14px 40px;font-size:13px;color:#888;max-width:1320px;margin:0 auto}
.breadcrumb a{color:#ff6a00;transition:color 0.2s}
.breadcrumb a:hover{color:#e85d04}

.product-hero{max-width:1320px;margin:0 auto;padding:40px;display:grid;grid-template-columns:1.1fr 0.9fr;gap:56px;align-items:start}
.gallery{position:sticky;top:100px}
.main-img{background:white;border-radius:16px;overflow:hidden;box-shadow:0 4px 24px rgba(0,0,0,0.06);margin-bottom:14px;cursor:zoom-in}
.main-img img{width:100%;height:460px;object-fit:contain;padding:28px}
.thumbs{display:flex;gap:10px;flex-wrap:wrap}
.thumb{width:80px;height:64px;border-radius:10px;overflow:hidden;cursor:pointer;border:2px solid transparent;background:white;box-shadow:0 1px 4px rgba(0,0,0,0.05);transition:border 0.2s}
.thumb:hover,.thumb.active{border-color:#ff6a00}
.thumb img{width:100%;height:100%;object-fit:contain;padding:4px}

.info{padding-top:4px}
.eyebrow{display:inline-block;background:#fff3e6;color:#ff6a00;padding:5px 16px;border-radius:8px;font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:1.5px;margin-bottom:14px}
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

.consult-box{background:linear-gradient(135deg,#072244,#0a3260);border-radius:16px;padding:32px;color:white;margin-top:28px}
.consult-box h3{font-size:20px;font-weight:800;margin-bottom:6px}
.consult-box p{font-size:14px;color:rgba(255,255,255,0.6);margin-bottom:20px;line-height:1.5}
.consult-box .btn-primary{width:100%;justify-content:center}

.detail-section{max-width:1320px;margin:0 auto;padding:0 40px 60px}
.section-block{margin-bottom:48px}
.section-heading{font-size:22px;font-weight:800;margin-bottom:20px;padding-bottom:12px;border-bottom:2px solid #e8e8ee;color:#0f1729}

.specs{width:100%;border-collapse:collapse}
.specs tr{border-bottom:1px solid #f0f0f5}
.specs td{padding:14px 18px;font-size:14px}
.specs td:first-child{font-weight:600;color:#555;width:260px;background:#fafafc;border-radius:4px 0 0 4px}

.lt{width:100%;border-collapse:collapse;font-size:13px;margin-top:8px}
.lt th{background:#072244;color:white;padding:11px 12px;text-align:center;font-size:11px;text-transform:uppercase;letter-spacing:0.5px}
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
.note-box strong{color:#0f1729}

.related-section{max-width:1320px;margin:0 auto;padding:0 40px 60px}
.related-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:16px}
.related-card{background:white;border-radius:14px;overflow:hidden;border:1px solid #e8e8ee;transition:all 0.25s;text-decoration:none;color:inherit}
.related-card:hover{transform:translateY(-3px);box-shadow:0 8px 24px rgba(0,0,0,0.08);border-color:#ff6a00}
.related-card img{width:100%;height:180px;object-fit:contain;padding:16px;background:#fafafc}
.related-card-info{padding:16px}
.related-card-info h4{font-size:15px;font-weight:700;margin-bottom:4px}
.related-card-info p{font-size:12px;color:#888;line-height:1.4}

.uprights-section{margin-bottom:24px;padding:20px 24px;background:white;border:1px solid #e0e0e8;border-radius:12px}
.uprights-section h4{font-size:14px;font-weight:700;color:#0f1729;margin-bottom:12px}
.upright-item{display:flex;justify-content:space-between;padding:8px 0;border-bottom:1px solid #f0f0f5;font-size:13px}
.upright-item:last-child{border-bottom:none}
.upright-name{font-weight:600}
.upright-load{color:#ff6a00;font-weight:600}

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
.catalog-dl:hover{background:#ff6a00;color:white;border-color:#ff6a00}

/* ===== RESPONSIVE ===== */

@media(max-width:900px){
  .nav-inner{padding:14px 20px}
  .hamburger{display:flex}
  nav{display:none;position:absolute;top:100%;left:0;right:0;background:#072244;flex-direction:column;padding:20px;gap:16px;border-top:1px solid rgba(255,255,255,0.1)}
  nav.open{display:flex}
  .nav-cta{display:none}
  .mobile-call{display:flex!important;background:#ff6a00;color:white!important;padding:12px 20px;border-radius:10px;text-align:center;justify-content:center;font-weight:700;border-bottom:none!important;min-height:44px}
  .hero{padding:60px 20px 50px}
  .hero h1{font-size:32px}
  .hero-stats{gap:32px}
  .trust-strip{padding:12px 20px}
  .trust-strip-inner{gap:16px 24px;justify-content:center}
  .trust-badge{font-size:11px}
  .why-grid{grid-template-columns:1fr}
  .why-section{padding:32px 20px}
  .series-section{padding:32px 20px}
  .series-header{flex-direction:column}
  .series-header-right{width:100%}
  .series-products-grid{grid-template-columns:repeat(auto-fill,minmax(150px,1fr));gap:12px;overflow-x:auto;-webkit-overflow-scrolling:touch}
  .series-pcard{min-height:44px}
  .consult-banner{flex-direction:column;text-align:center;margin:40px 20px;padding:32px 24px}
  .product-hero{grid-template-columns:1fr;padding:20px;gap:24px}
  .gallery{position:static}
  .main-img img{height:300px}
  .sticky-quote{padding:10px 20px;gap:12px}
  .sticky-quote span{font-size:12px}
  .info .feats{grid-template-columns:1fr}
  .detail-section{padding:0 20px 40px}
  .breadcrumb{padding:10px 20px}
  .series-hero-inner{grid-template-columns:1fr}
  .series-hero-img{display:none}
  .series-body{padding:40px 20px}
  .footer-inner{flex-direction:column;text-align:center}
  .services-grid{grid-template-columns:1fr;padding:32px 20px}
  .page-hero{padding:60px 20px 40px}
  .page-hero h1{font-size:32px}
  .about-content{padding:32px 20px}
  .industry-content{padding:32px 20px}
  .industry-cards{grid-template-columns:1fr}
  .sbn-grid{grid-template-columns:1fr 1fr}
  .sbn-section{padding:32px 20px}
}

@media(max-width:480px){
  .hero h1{font-size:26px}
  .hero p{font-size:16px}
  .hero-stats{gap:20px}
  .hero-stat .n{font-size:28px}
  .series-title{font-size:26px}
  .info h1{font-size:24px}
  .fins{flex-direction:column}
  .sbn-grid{grid-template-columns:1fr}
}

/* ===== SERVICES PAGE ===== */

.page-hero{background:linear-gradient(135deg,#072244 0%,#0a3260 40%,#0d4a7a 100%);color:white;padding:80px 40px 60px;text-align:center}
.page-hero h1{font-size:44px;font-weight:900;margin-bottom:12px}
.page-hero p{font-size:17px;color:rgba(255,255,255,0.6);max-width:640px;margin:0 auto;line-height:1.6}
.services-grid{max-width:1240px;margin:0 auto;padding:60px 40px;display:grid;grid-template-columns:repeat(2,1fr);gap:24px}
.service-card{background:white;border:1px solid #e8e8ee;border-radius:16px;padding:36px;transition:all 0.25s}
.service-card:hover{border-color:#ff6a00;transform:translateY(-3px);box-shadow:0 12px 32px rgba(0,0,0,0.06)}
.service-card .svc-icon{width:56px;height:56px;background:#fff3e6;border-radius:14px;display:flex;align-items:center;justify-content:center;margin-bottom:20px}
.service-card .svc-icon svg{width:28px;height:28px;color:#ff6a00}
.service-card h3{font-size:20px;font-weight:800;margin-bottom:8px}
.service-card p{font-size:14px;color:#666;line-height:1.7}

/* ===== ABOUT PAGE ===== */

.about-content{max-width:1240px;margin:0 auto;padding:60px 40px}
.about-intro{font-size:17px;color:#555;line-height:1.8;max-width:800px;margin:0 auto 48px;text-align:center}
.about-section{margin-bottom:48px}
.about-section h2{font-size:24px;font-weight:800;margin-bottom:16px;padding-bottom:10px;border-bottom:2px solid #e8e8ee}
.about-section p{font-size:15px;color:#555;line-height:1.7;margin-bottom:12px}
.about-stats{display:flex;justify-content:center;gap:40px;flex-wrap:wrap;padding:32px;background:#f8fafc;border-radius:16px;margin:20px 0 32px}
.about-stat{text-align:center}
.about-stat .n{font-size:32px;font-weight:900;color:#ff6a00}
.about-stat .l{font-size:12px;color:#888;text-transform:uppercase;letter-spacing:1.5px;margin-top:4px}
.cert-list{list-style:none;padding:0}
.cert-list li{display:flex;align-items:flex-start;gap:12px;padding:14px 18px;background:white;border-radius:10px;border:1px solid #e8e8ee;font-size:14px;color:#555;margin-bottom:8px}
.cert-list li::before{content:'\\2713';color:#2d6a4f;font-weight:800;font-size:16px;flex-shrink:0}
.about-why-list{list-style:none;padding:0}
.about-why-list li{display:flex;align-items:flex-start;gap:12px;padding:14px 18px;background:white;border-radius:10px;border:1px solid #e8e8ee;font-size:14px;color:#555;margin-bottom:8px}
.about-why-list li::before{content:'\\2713';color:#ff6a00;font-weight:800;font-size:16px;flex-shrink:0}

/* ===== INDUSTRY PAGES ===== */

.industry-content{max-width:1240px;margin:0 auto;padding:60px 40px}
.challenge-box{background:#fff8f0;border:1px solid #f0d8b8;border-radius:14px;padding:28px;margin-bottom:40px}
.challenge-box h2{font-size:18px;font-weight:800;color:#8a6530;margin-bottom:8px}
.challenge-box p{font-size:15px;color:#8a6530;line-height:1.7}
.industry-cards{display:grid;grid-template-columns:repeat(2,1fr);gap:20px;margin:40px 0}
.industry-card{background:white;border:1px solid #e8e8ee;border-radius:14px;padding:28px;display:flex;flex-direction:column;transition:all 0.25s}
.industry-card:hover{border-color:#ff6a00;transform:translateY(-3px);box-shadow:0 12px 32px rgba(0,0,0,0.06)}
.industry-card h3{font-size:18px;font-weight:800;margin-bottom:6px}
.industry-card p{font-size:14px;color:#666;line-height:1.6;margin-bottom:14px;flex:1}
.industry-card .card-link{color:#ff6a00;font-size:13px;font-weight:700}

/* ===== SOLUTIONS BY NEED ===== */

.sbn-section{max-width:1240px;margin:0 auto;padding:48px 40px}
.sbn-section h2{font-size:28px;font-weight:900;text-align:center;margin-bottom:28px}
.sbn-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:20px}
.sbn-card{background:white;border:1px solid #e8e8ee;border-radius:14px;padding:28px;text-align:center;transition:all 0.25s}
.sbn-card:hover{border-color:#ff6a00;transform:translateY(-3px);box-shadow:0 12px 32px rgba(0,0,0,0.06)}
.sbn-card .sbn-icon{width:56px;height:56px;background:#fff3e6;border-radius:14px;display:flex;align-items:center;justify-content:center;margin:0 auto 16px}
.sbn-card .sbn-icon svg{width:28px;height:28px;color:#ff6a00}
.sbn-card h3{font-size:16px;font-weight:800;margin-bottom:6px}
.sbn-card p{font-size:13px;color:#666;line-height:1.5}

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
<link rel="stylesheet" href="/styles.css?v=6">
<script>
// Auto-detect language from browser
var lang = (navigator.language || navigator.userLanguage || 'en').toLowerCase();
if (lang.startsWith('fi')) {
  window.location.replace('/fi/index.html');
} else {
  window.location.replace('/en/index.html');
}
</script>
</head>
<body style="background:#072244;color:white;display:flex;align-items:center;justify-content:center;min-height:100vh;text-align:center;font-family:Inter,sans-serif">
  <div>
    <h1 style="font-size:28px;font-weight:800;margin-bottom:24px">BALT<span style="color:#ff6a00">SCAND</span></h1>
    <p style="color:rgba(255,255,255,0.6);margin-bottom:32px">Choose your language / Valitse kieli</p>
    <div style="display:flex;gap:16px;justify-content:center">
      <a href="/en/index.html" style="background:#ff6a00;color:white;padding:16px 36px;border-radius:12px;font-weight:700;font-size:16px">🇬🇧 English</a>
      <a href="/fi/index.html" style="background:white;color:#0f1729;padding:16px 36px;border-radius:12px;font-weight:700;font-size:16px">🇫🇮 Suomi</a>
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
            brochure_btn = f'<a class="btn-catalog" href="/{s["brochure"]}" target="_blank" download><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>{t(lang, "catalog_pdf")}</a>'

        # Series starting price badge
        series_price_html = ''
        sp = SERIES_PRICES.get(s['slug'])
        if sp:
            series_price_html = f'<div class="series-price"><span class="price-from">{t(lang, "from_price")}</span> <span class="price-amount">{sp} &euro;</span> <span class="price-currency">{t(lang, "price_excl_tax")}</span></div>'

        # Product cards with images
        pcards = ''
        for p in s['products']:
            pname = esc(s_get(p, 'name', lang))
            pimg = p.get('gallery', [p.get('image', '')])[0]
            pp = PRODUCT_PRICES.get(p['id'])
            pprice = f'<div class="price-tag"><span class="price-from">{t(lang, "from_price")}</span> <span class="price-amount">{pp} &euro;</span></div>' if pp else ''
            pcards += f"""
          <a href="/{lang}/products/{s['slug']}/{p['id']}.html" class="series-pcard">
            <img src="/{pimg}" alt="{pname}" loading="lazy">
            <div class="series-pcard-body">
              <h3>{pname}</h3>
              {pprice}
              <span class="card-link">{t(lang, 'view_details')} &rarr;</span>
            </div>
          </a>"""

        cards += f"""
    <section class="series-section {alt}">
      <div class="series-inner">
        <div class="series-header">
          <div class="series-header-left">
            <div class="series-header-top">
              <h2 class="series-title"><a href="/{lang}/products/{s['slug']}/index.html">{sname_display}</a></h2>
              <span class="series-cat-badge">{category}</span>
              <span class="prod-count">{t(lang, 'n_products', n=len(s['products']))}</span>
              {series_price_html}
              {stds}
            </div>
            <p class="series-desc">{desc}</p>
          </div>
          <div class="series-header-right">
            <a class="btn-view-all" href="/{lang}/products/{s['slug']}/index.html">{t(lang, 'view_range', name=s['name'])} &rarr;</a>
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

    trust_strip = ''  # Removed — trust signals moved to hero stats

    html_out = f"""<!DOCTYPE html>
<html lang="{t(lang, 'html_lang')}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{t(lang, 'site_title')}</title>
<meta name="description" content="{esc(site_desc)}">
{og}
{hreflang_tags(lang, current_path)}
{jsonld_org(lang)}
{favicon_link()}
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="/styles.css?v=6">
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

<div class="sbn-section">
  <h2>{t(lang, 'solutions_by_need')}</h2>
  <div class="sbn-grid">
    <a href="/{lang}/industries/warehousing.html" class="sbn-card">
      <div class="sbn-icon"><svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="1" y="3" width="15" height="13"/><polygon points="16 8 20 8 23 11 23 16 16 16 16 8"/><circle cx="5.5" cy="18.5" r="2.5"/><circle cx="18.5" cy="18.5" r="2.5"/></svg></div>
      <h3>{t(lang, 'sbn_heavy_title')}</h3>
      <p>{t(lang, 'sbn_heavy_desc')}</p>
    </a>
    <a href="/{lang}/industries/retail.html" class="sbn-card">
      <div class="sbn-icon"><svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M6 2L3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4z"/><line x1="3" y1="6" x2="21" y2="6"/><path d="M16 10a4 4 0 0 1-8 0"/></svg></div>
      <h3>{t(lang, 'sbn_light_title')}</h3>
      <p>{t(lang, 'sbn_light_desc')}</p>
    </a>
    <a href="/{lang}/industries/manufacturing.html" class="sbn-card">
      <div class="sbn-icon"><svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="7" width="20" height="14" rx="2" ry="2"/><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/></svg></div>
      <h3>{t(lang, 'sbn_bins_title')}</h3>
      <p>{t(lang, 'sbn_bins_desc')}</p>
    </a>
    <a href="/{lang}/industries/archive.html" class="sbn-card">
      <div class="sbn-icon"><svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z"/></svg></div>
      <h3>{t(lang, 'sbn_platforms_title')}</h3>
      <p>{t(lang, 'sbn_platforms_desc')}</p>
    </a>
  </div>
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
    P = '/'  # absolute paths for Vercel cleanUrls compatibility
    current_path = f'/{lang}/products/{slug}/index.html'

    feats = ''.join(f'<div class="feat-item">{esc(f)}</div>' for f in s_list(series, 'features', lang))

    product_cards = ''
    for p in series['products']:
        img = P + p.get('gallery', [p.get('image', '')])[0]
        pname = esc(s_get(p, 'name', lang))
        pdesc = esc(s_get(p, 'description', lang)[:120])
        pp = PRODUCT_PRICES.get(p['id'])
        pprice = f'<div class="price-tag"><span class="price-from">{t(lang, "from_price")}</span> <span class="price-amount">{pp} &euro;</span></div>' if pp else ''
        product_cards += f"""
        <a href="/{lang}/products/{slug}/{p['id']}.html" class="product-card">
          <img src="{img}" alt="{pname}" loading="lazy">
          <div class="product-card-body">
            <h3>{pname}</h3>
            <p>{pdesc}...</p>
            {pprice}
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

    bc_ld = jsonld_breadcrumb([
        (t(lang, 'home'), f'{lang}/index.html'),
        (sname, f'{lang}/products/{slug}/index.html'),
    ], lang)

    page = f"""<!DOCTYPE html>
<html lang="{t(lang, 'html_lang')}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{sname} — Baltscand | Finland & Baltics</title>
<meta name="description" content="{esc(meta_desc)}">
{og}
{hreflang_tags(lang, current_path)}
{jsonld_org(lang)}
{bc_ld}
{favicon_link()}
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="/styles.css?v=6">
</head>
<body>
{nav(lang, '../../', current_path)}

<div class="series-hero">
  <div class="series-hero-inner">
    <div class="series-hero-text">
      <div class="eyebrow">{category}</div>
      <h1>{sname}</h1>
      <p>{esc(desc)}</p>
      {'<div class="series-price" style="margin:16px 0"><span class="price-from">' + t(lang, "starting_from") + '</span> <span class="price-amount">' + str(SERIES_PRICES[slug]) + ' &euro;</span> <span class="price-currency">' + t(lang, "price_excl_tax") + '</span></div>' if slug in SERIES_PRICES else ''}
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
    <a href="/{lang}/index.html">{t(lang, 'home')}</a> &rsaquo; {sname}
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
    P = '/'  # absolute paths for Vercel cleanUrls compatibility
    current_path = f'/{lang}/products/{slug}/{pid}.html'

    pname = esc(s_get(product, 'name', lang))
    sname = esc(series['name'])
    ptype = esc(s_get(product, 'type', lang))
    pdesc = esc(s_get(product, 'description', lang))

    # Price
    pprice = PRODUCT_PRICES.get(pid)
    price_html = ''
    if pprice:
        price_html = f'''<div class="product-price">
      <div class="price-from">{t(lang, 'starting_from')}</div>
      <div class="price-amount">{pprice} &euro; <span style="font-size:14px;font-weight:500;color:#8a6530">{t(lang, 'price_excl_tax')}</span></div>
      <div class="price-note">{t(lang, 'price_note')}</div>
    </div>'''

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
            lt_html += f'<h4 style="margin:20px 0 8px;font-size:14px;color:#0f1729">{sec.title()}</h4><table class="lt"><thead><tr>{cols}</tr></thead><tbody>{rows}</tbody></table>'

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
            cards += f'<a href="/{lang}/products/{slug}/{sib["id"]}.html" class="related-card"><img src="{sib_img}" alt="{sib_name}" loading="lazy"><div class="related-card-info"><h4>{sib_name}</h4><p>{sib_desc}...</p></div></a>'
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
    bc_ld = jsonld_breadcrumb([
        (t(lang, 'home'), f'{lang}/index.html'),
        (sname, f'{lang}/products/{slug}/index.html'),
        (pname, url),
    ], lang)

    # Why Baltscand section
    why_section = f"""
<div class="why-section">
  <h2 style="font-size:22px;font-weight:800;text-align:center">{t(lang, 'why_baltscand')}</h2>
  <div class="why-grid">
    <div class="why-card">
      <div class="why-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg></div>
      <h3>{t(lang, 'why_1_title')}</h3>
      <p>{t(lang, 'why_1_desc')}</p>
    </div>
    <div class="why-card">
      <div class="why-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="1" y="3" width="15" height="13"/><polygon points="16 8 20 8 23 11 23 16 16 16 16 8"/><circle cx="5.5" cy="18.5" r="2.5"/><circle cx="18.5" cy="18.5" r="2.5"/></svg></div>
      <h3>{t(lang, 'why_2_title')}</h3>
      <p>{t(lang, 'why_2_desc')}</p>
    </div>
    <div class="why-card">
      <div class="why-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/></svg></div>
      <h3>{t(lang, 'why_3_title')}</h3>
      <p>{t(lang, 'why_3_desc')}</p>
    </div>
  </div>
</div>"""

    page = f"""<!DOCTYPE html>
<html lang="{t(lang, 'html_lang')}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{pname} — Baltscand | Finland & Baltics</title>
<meta name="description" content="{esc(meta_desc)}">
{og}
{hreflang_tags(lang, current_path)}
{jld}
{bc_ld}
{favicon_link()}
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="/styles.css?v=6">
</head>
<body>
{nav(lang, '../../', current_path)}

<div class="breadcrumb">
  <a href="/{lang}/index.html">{t(lang, 'home')}</a> &rsaquo;
  <a href="/{lang}/products/{slug}/index.html">{sname}</a> &rsaquo;
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

    {price_html}

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

{why_section}

{consult(lang, P)}

<div class="sticky-quote" id="stickyQuote">
  <span>{t(lang, 'interested_in_product', name=pname)}</span>
  <a class="btn-primary" href="javascript:void(0)" onclick="openQuoteModal('{pname}')">{t(lang, 'sticky_quote')}</a>
</div>

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
// Sticky quote bar
(function(){{var sq=document.getElementById('stickyQuote');if(!sq)return;var cb=document.querySelector('.consult-box');window.addEventListener('scroll',function(){{var show=window.scrollY>600;if(cb){{var r=cb.getBoundingClientRect();if(r.top<window.innerHeight)show=false}}sq.classList.toggle('show',show)}});}})();
</script>
</body>
</html>"""

    path = os.path.join(out, f'{pid}.html')
    with open(path, 'w') as f:
        f.write(page)
    print(f'  {lang}/products/{slug}/{pid}.html')


# ═══════════════════════════════════════════════════════════════════════════
# SERVICES PAGE
# ═══════════════════════════════════════════════════════════════════════════

def gen_services(lang):
    lang_dir = os.path.join(BASE, lang)
    os.makedirs(lang_dir, exist_ok=True)
    current_path = f'/{lang}/services.html'
    gi = t(lang, 'general_inquiry')

    bc_ld = jsonld_breadcrumb([
        (t(lang, 'home'), f'{lang}/index.html'),
        (t(lang, 'services_title'), f'{lang}/services.html'),
    ], lang)

    page = f"""<!DOCTYPE html>
<html lang="{t(lang, 'html_lang')}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{t(lang, 'services_title')} — Baltscand</title>
<meta name="description" content="{esc(t(lang, 'services_subtitle'))}">
{meta_tags(t(lang, 'services_title') + ' — Baltscand', t(lang, 'services_subtitle'), data['series'][0]['heroImage'], f'{lang}/services.html')}
{hreflang_tags(lang, current_path)}
{jsonld_org(lang)}
{bc_ld}
{favicon_link()}
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="/styles.css?v=6">
</head>
<body>
{nav(lang, '', current_path)}

<div class="page-hero">
  <h1>{t(lang, 'services_title')}</h1>
  <p>{t(lang, 'services_subtitle')}</p>
</div>

<div class="services-grid">
  <div class="service-card">
    <div class="svc-icon"><svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg></div>
    <h3>{t(lang, 'svc_consult_title')}</h3>
    <p>{t(lang, 'svc_consult_desc')}</p>
  </div>
  <div class="service-card">
    <div class="svc-icon"><svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="1" y="3" width="15" height="13"/><polygon points="16 8 20 8 23 11 23 16 16 16 16 8"/><circle cx="5.5" cy="18.5" r="2.5"/><circle cx="18.5" cy="18.5" r="2.5"/></svg></div>
    <h3>{t(lang, 'svc_delivery_title')}</h3>
    <p>{t(lang, 'svc_delivery_desc')}</p>
  </div>
  <div class="service-card">
    <div class="svc-icon"><svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/></svg></div>
    <h3>{t(lang, 'svc_install_title')}</h3>
    <p>{t(lang, 'svc_install_desc')}</p>
  </div>
  <div class="service-card">
    <div class="svc-icon"><svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg></div>
    <h3>{t(lang, 'svc_support_title')}</h3>
    <p>{t(lang, 'svc_support_desc')}</p>
  </div>
</div>

{consult(lang)}
{modal(lang)}
{foot(lang)}
{back_to_top()}
</body>
</html>"""

    with open(os.path.join(lang_dir, 'services.html'), 'w') as f:
        f.write(page)
    print(f'  {lang}/services.html')


# ═══════════════════════════════════════════════════════════════════════════
# ABOUT PAGE
# ═══════════════════════════════════════════════════════════════════════════

def gen_about(lang):
    lang_dir = os.path.join(BASE, lang)
    os.makedirs(lang_dir, exist_ok=True)
    current_path = f'/{lang}/about.html'
    gi = t(lang, 'general_inquiry')

    bc_ld = jsonld_breadcrumb([
        (t(lang, 'home'), f'{lang}/index.html'),
        (t(lang, 'about_title'), f'{lang}/about.html'),
    ], lang)

    page = f"""<!DOCTYPE html>
<html lang="{t(lang, 'html_lang')}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{t(lang, 'about_title')} — Baltscand</title>
<meta name="description" content="{esc(t(lang, 'about_intro')[:155])}">
{meta_tags(t(lang, 'about_title') + ' — Baltscand', t(lang, 'about_intro')[:155], data['series'][0]['heroImage'], f'{lang}/about.html')}
{hreflang_tags(lang, current_path)}
{jsonld_org(lang)}
{bc_ld}
{favicon_link()}
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="/styles.css?v=6">
</head>
<body>
{nav(lang, '', current_path)}

<div class="page-hero">
  <h1>{t(lang, 'about_title')}</h1>
</div>

<div class="about-content">
  <p class="about-intro">{t(lang, 'about_intro')}</p>

  <div class="about-section">
    <h2>{t(lang, 'about_provost_title')}</h2>
    <p>{t(lang, 'about_provost_desc')}</p>
    <div class="about-stats">
      <div class="about-stat"><div class="n">800+</div><div class="l">{'Employees' if lang == 'en' else 'Työntekijää'}</div></div>
      <div class="about-stat"><div class="n">6</div><div class="l">{'Factories' if lang == 'en' else 'Tehdasta'}</div></div>
      <div class="about-stat"><div class="n">60+</div><div class="l">{'Years' if lang == 'en' else 'Vuotta'}</div></div>
      <div class="about-stat"><div class="n">80,000</div><div class="l">{'Customers' if lang == 'en' else 'Asiakasta'}</div></div>
    </div>
  </div>

  <div class="about-section">
    <h2>{t(lang, 'about_why_title')}</h2>
    <ul class="about-why-list">
      <li>{t(lang, 'about_why_1')}</li>
      <li>{t(lang, 'about_why_2')}</li>
      <li>{t(lang, 'about_why_3')}</li>
      <li>{t(lang, 'about_why_4')}</li>
    </ul>
  </div>

  <div class="about-section">
    <h2>{t(lang, 'about_certs_title')}</h2>
    <ul class="cert-list">
      <li>{t(lang, 'about_cert_1')}</li>
      <li>{t(lang, 'about_cert_2')}</li>
      <li>{t(lang, 'about_cert_3')}</li>
    </ul>
  </div>

  <div style="text-align:center;margin-top:40px">
    <a class="btn-primary" href="javascript:void(0)" onclick="openQuoteModal('{gi}')">{t(lang, 'start_project')}</a>
  </div>
</div>

{consult(lang)}
{modal(lang)}
{foot(lang)}
{back_to_top()}
</body>
</html>"""

    with open(os.path.join(lang_dir, 'about.html'), 'w') as f:
        f.write(page)
    print(f'  {lang}/about.html')


# ═══════════════════════════════════════════════════════════════════════════
# INDUSTRY PAGES
# ═══════════════════════════════════════════════════════════════════════════

INDUSTRIES = [
    {
        'slug': 'warehousing',
        'name_key': 'ind_warehousing',
        'desc_key': 'ind_warehousing_desc',
        'challenge_key': 'ind_warehousing_challenge',
        'series_slugs': ['prorack-plus', 'propal-3', 'proplus-lp3'],
    },
    {
        'slug': 'retail',
        'name_key': 'ind_retail',
        'desc_key': 'ind_retail_desc',
        'challenge_key': 'ind_retail_challenge',
        'series_slugs': ['prospace-plus', 'modul-plus'],
    },
    {
        'slug': 'manufacturing',
        'name_key': 'ind_manufacturing',
        'desc_key': 'ind_manufacturing_desc',
        'challenge_key': 'ind_manufacturing_challenge',
        'series_slugs': ['prorack-plus', 'prospace-plus', 'propal-3'],
    },
    {
        'slug': 'archive',
        'name_key': 'ind_archive',
        'desc_key': 'ind_archive_desc',
        'challenge_key': 'ind_archive_challenge',
        'series_slugs': ['prospace-plus', 'modul-plus'],
    },
]

def gen_industry_index(lang):
    """Generate the industries landing page listing all sectors."""
    lang_dir = os.path.join(BASE, lang, 'industries')
    os.makedirs(lang_dir, exist_ok=True)
    current_path = f'/{lang}/industries/index.html'
    gi = t(lang, 'general_inquiry')

    bc_ld = jsonld_breadcrumb([
        (t(lang, 'home'), f'{lang}/index.html'),
        (t(lang, 'industries'), f'{lang}/industries/index.html'),
    ], lang)

    cards = ''
    for ind in INDUSTRIES:
        cards += f"""
    <a href="{ind['slug']}.html" class="industry-card">
      <h3>{t(lang, ind['name_key'])}</h3>
      <p>{t(lang, ind['desc_key'])}</p>
      <span class="card-link">{t(lang, 'explore_solutions')} &rarr;</span>
    </a>"""

    page = f"""<!DOCTYPE html>
<html lang="{t(lang, 'html_lang')}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{t(lang, 'industries')} — Baltscand</title>
<meta name="description" content="{esc(t(lang, 'hero_desc'))}">
{meta_tags(t(lang, 'industries') + ' — Baltscand', t(lang, 'hero_desc'), data['series'][0]['heroImage'], f'{lang}/industries/index.html')}
{hreflang_tags(lang, current_path)}
{jsonld_org(lang)}
{bc_ld}
{favicon_link()}
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="/styles.css?v=6">
</head>
<body>
{nav(lang, '../', current_path)}

<div class="page-hero">
  <h1>{t(lang, 'industries')}</h1>
  <p>{t(lang, 'hero_desc')}</p>
</div>

<div class="industry-content">
  <div class="industry-cards">{cards}
  </div>
</div>

{consult(lang, '../')}
{modal(lang)}
{foot(lang)}
{back_to_top()}
</body>
</html>"""

    with open(os.path.join(lang_dir, 'index.html'), 'w') as f:
        f.write(page)
    print(f'  {lang}/industries/index.html')


def gen_industry_page(ind, lang):
    """Generate a single industry page."""
    lang_dir = os.path.join(BASE, lang, 'industries')
    os.makedirs(lang_dir, exist_ok=True)
    current_path = f'/{lang}/industries/{ind["slug"]}.html'
    gi = t(lang, 'general_inquiry')

    ind_name = t(lang, ind['name_key'])
    ind_desc = t(lang, ind['desc_key'])
    ind_challenge = t(lang, ind['challenge_key'])

    bc_ld = jsonld_breadcrumb([
        (t(lang, 'home'), f'{lang}/index.html'),
        (t(lang, 'industries'), f'{lang}/industries/index.html'),
        (ind_name, f'{lang}/industries/{ind["slug"]}.html'),
    ], lang)

    # Build series lookup
    series_map = {s['slug']: s for s in data['series']}

    # Recommended product cards
    rec_cards = ''
    for ss in ind['series_slugs']:
        s = series_map.get(ss)
        if not s:
            continue
        sname = esc(s['name'])
        sdesc = esc(s_get(s, 'description', lang)[:120])
        img = s.get('heroImage', '')
        rec_cards += f"""
      <a href="/{lang}/products/{ss}/index.html" class="product-card">
        <img src="/{img}" alt="{sname}" loading="lazy">
        <div class="product-card-body">
          <h3>{sname}</h3>
          <p>{sdesc}...</p>
          <span class="card-link">{t(lang, 'view_range', name=s['name'])} &rarr;</span>
        </div>
      </a>"""

    page = f"""<!DOCTYPE html>
<html lang="{t(lang, 'html_lang')}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(ind_name)} — Baltscand</title>
<meta name="description" content="{esc(ind_desc[:155])}">
{meta_tags(esc(ind_name) + ' — Baltscand', ind_desc[:155], data['series'][0]['heroImage'], f'{lang}/industries/{ind["slug"]}.html')}
{hreflang_tags(lang, current_path)}
{jsonld_org(lang)}
{bc_ld}
{favicon_link()}
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="/styles.css?v=6">
</head>
<body>
{nav(lang, '../', current_path)}

<div class="page-hero">
  <h1>{esc(ind_name)}</h1>
  <p>{esc(ind_desc)}</p>
</div>

<div class="industry-content">
  <div class="breadcrumb" style="padding:0 0 20px">
    <a href="/{lang}/index.html">{t(lang, 'home')}</a> &rsaquo;
    <a href="/{lang}/industries/index.html">{t(lang, 'industries')}</a> &rsaquo;
    {esc(ind_name)}
  </div>

  <div class="challenge-box">
    <h2>{t(lang, 'industry_challenge')}</h2>
    <p>{esc(ind_challenge)}</p>
  </div>

  <h2 style="font-size:24px;font-weight:800;margin-bottom:20px">{t(lang, 'recommended_products')}</h2>
  <div class="products-grid">{rec_cards}
  </div>

  <div style="text-align:center;margin-top:40px">
    <a class="btn-primary" href="javascript:void(0)" onclick="openQuoteModal('{esc(ind_name)}')">{t(lang, 'start_project')}</a>
  </div>
</div>

{consult(lang, '../')}
{modal(lang)}
{foot(lang)}
{back_to_top()}
</body>
</html>"""

    with open(os.path.join(lang_dir, f'{ind["slug"]}.html'), 'w') as f:
        f.write(page)
    print(f'  {lang}/industries/{ind["slug"]}.html')


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
    # Root page (no hreflang)
    entries = f'  <url><loc>{SITE_URL}/index.html</loc><priority>1.0</priority></url>\n'

    # Collect bilingual page pairs
    page_pairs = [('index.html', '1.0')]
    page_pairs.append(('services.html', '0.9'))
    page_pairs.append(('about.html', '0.8'))
    page_pairs.append(('industries/index.html', '0.9'))
    for ind in INDUSTRIES:
        page_pairs.append((f'industries/{ind["slug"]}.html', '0.8'))
    for s in data['series']:
        page_pairs.append((f'products/{s["slug"]}/index.html', '0.9'))
        for p in s['products']:
            page_pairs.append((f'products/{s["slug"]}/{p["id"]}.html', '0.8'))

    for path, priority in page_pairs:
        for lang in LANGS:
            url = f'{lang}/{path}'
            other = 'fi' if lang == 'en' else 'en'
            other_url = f'{other}/{path}'
            entries += f'  <url>\n    <loc>{SITE_URL}/{url}</loc>\n    <priority>{priority}</priority>\n'
            entries += f'    <xhtml:link rel="alternate" hreflang="{lang}" href="{SITE_URL}/{url}"/>\n'
            entries += f'    <xhtml:link rel="alternate" hreflang="{other}" href="{SITE_URL}/{other_url}"/>\n'
            entries += f'  </url>\n'

    content = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">
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
{favicon_link()}
<link rel="stylesheet" href="/styles.css?v=6">
</head>
<body>
{nav(lang, '', current_path)}
<div style="text-align:center;padding:120px 40px 80px;max-width:600px;margin:0 auto">
  <h1 style="font-size:72px;font-weight:900;color:#e8e8ee;margin-bottom:16px">404</h1>
  <h2 style="font-size:28px;font-weight:800;margin-bottom:12px">{t(lang, 'page_not_found')}</h2>
  <p style="color:#666;font-size:16px;line-height:1.6;margin-bottom:32px">{t(lang, '404_desc')}</p>
  <div style="display:flex;gap:16px;justify-content:center;flex-wrap:wrap">
    <a class="btn-primary" href="/{lang}/index.html">{t(lang, 'browse_products')}</a>
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
    print('Generating Baltscand site v5 (bilingual EN/FI + Services, About, Industries)...\n')

    gen_css()
    gen_robots()
    gen_sitemap()
    gen_root_index()

    for lang in LANGS:
        print(f'\n  [{lang.upper()}]')
        gen_index(lang)
        gen_services(lang)
        gen_about(lang)
        gen_industry_index(lang)
        for ind in INDUSTRIES:
            gen_industry_page(ind, lang)
        for s in data['series']:
            gen_series_page(s, lang)
            for p in s['products']:
                gen_product(s, p, lang)
        gen_404(lang)

    total = sum(len(s['products']) for s in data['series'])
    series_count = len(data['series'])
    ind_count = len(INDUSTRIES)
    per_lang = f'{series_count} series + {total} products + services + about + {ind_count} industries + 404'
    new_pages = 2 * (1 + 1 + 1 + 1 + ind_count + series_count + total + 1) + 4
    print(f'\nDone! root index + styles.css + robots.txt + sitemap.xml')
    print(f'  EN: {per_lang}')
    print(f'  FI: {per_lang}')
    print(f'  Total: {new_pages} files')
