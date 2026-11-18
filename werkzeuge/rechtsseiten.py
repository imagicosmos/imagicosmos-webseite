"""Erzeugt impressum.html, datenschutz.html, 404.html (Kopf und Fuß aus index.html) sowie robots.txt, sitemap.xml,
llms.txt und _config.yml. Aufruf im Ordner imagicosmos (über webseite/): python webseite/werkzeuge/rechtsseiten.py
Texte der Rechtsseiten hier ändern, nicht in den erzeugten Dateien. Vorbild: imagiclique/webseite/werkzeuge/."""
import io
src = io.open('webseite/index.html', encoding='utf-8').read()

def seite(titel, inhalt, wurzel=''):
    kopf = src[src.index('<header class="kopf">'):src.index('</header>') + 9]
    fuss = src[src.index('<footer class="fuss">'):src.index('</footer>') + 9]
    ix = wurzel + 'index.html'
    kopf = kopf.replace('href="#"', 'href="%s"' % ix).replace('href="#', 'href="%s#' % ix)
    fuss = (fuss.replace('href="#"', 'href="%s"' % ix)
                .replace('href="impressum.html"', 'href="%simpressum.html"' % wurzel)
                .replace('href="datenschutz.html"', 'href="%sdatenschutz.html"' % wurzel))
    return f'''<!DOCTYPE html>
<html lang="de" data-modus="hell">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta http-equiv="Content-Security-Policy" content="default-src 'self'; script-src 'self'; style-src 'self' 'unsafe-inline'; img-src 'self' data:; font-src 'self'; connect-src 'self'; object-src 'none'; base-uri 'self'; form-action 'self'">
<title>{titel} · Imagicosmos</title>
<meta name="robots" content="noindex">
<link rel="icon" href="{wurzel}bilder/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="{wurzel}bilder/apple-touch-icon.png">
<script src="{wurzel}modus.js"></script>
<link rel="stylesheet" href="{wurzel}style.css">
</head>
<body>
{kopf}
<main id="inhalt">
  <div class="leuchten" aria-hidden="true"></div>
  <article class="breite"><div class="rechtstext">
{inhalt.strip()}
  </div></article>
</main>
{fuss}
<script src="{wurzel}app.js"></script>
<script src="{wurzel}bausteine/zauberstab.js" data-stern="#8b5cf6" data-band="#c4b5fd" defer></script>
</body>
</html>
'''

ADR = '''<address>
Mario Glaser<br>
Gründelparkweg 5c<br>
08371 Glauchau%s
</address>'''
MAIL = '<a href="mailto:kontakt@imagicosmos.de">kontakt@imagicosmos.de</a>'

impressum = f'''
<h1>Impressum</h1>
<p><strong>Angaben gemäß § 5 Digitale-Dienste-Gesetz (DDG) und § 18 Abs. 1 Medienstaatsvertrag (MStV)</strong></p>
{ADR % ''}
<h2>Kontakt</h2>
<p>E-Mail: {MAIL}</p>
<h2>Über diese Seite</h2>
<p>Imagicosmos ist der gemeinsame Name für die privaten Software-Projekte Imagichron, Imagiclique, Imagicoll und Imagicruise. Diese Seite stellt die Projekte vor und führt zu ihren eigenen Seiten. Imagicosmos ist kein Unternehmen.</p>
<h2>Links zu anderen Seiten</h2>
<p>Diese Seite enthält Links zu anderen Webseiten (zum Beispiel zu den Seiten der einzelnen Programme). Für die Inhalte fremder Seiten sind die jeweiligen Anbieter verantwortlich. Bei Hinweisen auf rechtswidrige Inhalte entferne ich den Link umgehend.</p>
'''

datenschutz = f'''
<h1>Datenschutz</h1>
<p>Kurz gesagt: Diese Webseite setzt <strong>keine Cookies</strong>, nutzt <strong>keine Statistik- oder Werbedienste</strong> und lädt <strong>keine Inhalte von fremden Servern</strong> (auch keine Schriften). Es gibt kein Kontaktformular und kein Benutzerkonto.</p>
<p>Dieser Hinweis gilt für den Besuch dieser Webseite. Was die einzelnen Programme mit Daten machen, steht auf deren eigenen Seiten.</p>

<h2>Verantwortlich</h2>
{ADR % ('<br>' + chr(10) + 'E-Mail: ' + MAIL)}

<h2>Bereitstellung der Seite (Hosting)</h2>
<p>Diese Seite wird über <strong>GitHub Pages</strong> ausgeliefert. Anbieter ist die GitHub, Inc., 88 Colin P. Kelly Jr. Street, San Francisco, CA 94107, USA. Beim Aufruf der Seite verarbeitet GitHub technisch notwendige Daten, insbesondere deine <strong>IP-Adresse</strong>, Datum und Uhrzeit, die aufgerufene Seite und Angaben zu Browser und Betriebssystem. Das ist nötig, um die Seite auszuliefern und sie gegen Angriffe zu schützen.</p>
<p>Rechtsgrundlage ist Art. 6 Abs. 1 lit. f DSGVO (berechtigtes Interesse an einer sicheren und funktionierenden Webseite). Dabei können Daten in die USA übermittelt werden. GitHub ist nach dem EU-US Data Privacy Framework zertifiziert; dafür besteht ein Angemessenheitsbeschluss der EU-Kommission (Art. 45 DSGVO). Mehr dazu in der <a href="https://docs.github.com/de/site-policy/privacy-policies/github-general-privacy-statement" rel="noopener">Datenschutzerklärung von GitHub</a>.</p>

<h2>Hell oder dunkel</h2>
<p>Wenn du oben rechts auf ☀/☾ klickst, merkt sich dein Browser deine Wahl („hell“ oder „dunkel“) im lokalen Speicher deines Geräts. Diese Angabe wird nicht übertragen, und du kannst sie jederzeit über die Einstellungen deines Browsers löschen. Sie wird nur gespeichert, weil du die Funktion ausdrücklich nutzt (§ 25 Abs. 2 Nr. 2 TDDDG).</p>

<h2>Kontakt per E-Mail</h2>
<p>Wenn du mir eine E-Mail schreibst, verwende ich deine Angaben nur, um deine Anfrage zu beantworten (Art. 6 Abs. 1 lit. b bzw. f DSGVO). Ich lösche sie, sobald sie dafür nicht mehr nötig sind und keine gesetzlichen Aufbewahrungspflichten bestehen.</p>

<h2>Deine Rechte</h2>
<p>Du hast das Recht auf</p>
<ul>
  <li>Auskunft über die gespeicherten Daten (Art. 15 DSGVO),</li>
  <li>Berichtigung (Art. 16), Löschung (Art. 17) und Einschränkung der Verarbeitung (Art. 18),</li>
  <li>Datenübertragbarkeit (Art. 20) und Widerspruch gegen die Verarbeitung (Art. 21),</li>
  <li>Beschwerde bei einer Datenschutz-Aufsichtsbehörde (Art. 77), zum Beispiel der deines Wohnorts.</li>
</ul>
<p>Für Anfragen genügt eine E-Mail an die oben genannte Adresse.</p>

<p class="leise" style="margin-top:40px">Stand: November 2026</p>
'''

nf = '''
<h1>Seite nicht gefunden</h1>
<p>Diese Seite gibt es leider nicht (mehr). Vielleicht hilft der Weg zurück zur Startseite.</p>
<p style="margin-top:28px"><a class="knopf" href="/">Zur Startseite</a></p>
'''

def w(p, s):
    io.open('webseite/' + p, 'w', encoding='utf-8', newline='\n').write(s)

w('impressum.html', seite('Impressum', impressum))
w('datenschutz.html', seite('Datenschutz', datenschutz))
w('404.html', seite('Seite nicht gefunden', nf, '/'))
w('robots.txt', '''# imagicosmos.de - reine Informationsseite ohne private Inhalte.
# Alle Suchmaschinen und KI-Dienste duerfen lesen (wie bei imagichron.de, entschieden 11.11.2026).

User-agent: *
Allow: /

Sitemap: https://imagicosmos.de/sitemap.xml
''')
w('sitemap.xml', '''<?xml version="1.0" encoding="UTF-8"?>
<!-- Nur Seiten, die in Suchmaschinen erscheinen sollen (Rechtstexte haben „noindex“). Bei Änderungen lastmod anpassen. -->
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url><loc>https://imagicosmos.de/</loc><lastmod>2026-11-16</lastmod></url>
</urlset>
''')
w('llms.txt', '''# Imagicosmos

> Imagicosmos ist der gemeinsame Name für vier Programme, die Fotos gestalten und präsentieren. Private Software-Projekte aus Deutschland, Sprache: Deutsch.

Die Programme:

- **Imagichron** – Fotos erzählen: persönliche Bilder-Zeitreisen für Feste mit Geschichte. Programm für Windows. https://imagichron.de/
- **Imagiclique** – Fotos teilen: Status-Bilder für WhatsApp und Instagram aus eigenen Fotos, als App auf dem Android-Handy (Testphase). https://imagiclique.de/
- **Imagicoll** – Fotos sammeln und bewahren: Die Android-App „Fotos sichern“ bringt Handy-Fotos über das WLAN zu Hause auf den eigenen PC (Katalog für Windows), ohne Cloud und ohne Konto. Fotoalben für die Familie und Fotowand für Feiern sind in Arbeit. https://imagicoll.de/
- **Imagicruise** – Fotos von Reisen: Reiseberichte Tag für Tag mit Ereignissen, Fotos und Route auf der Karte; am Handy festhalten, am PC ausarbeiten, ohne Konto (Beta). https://imagicruise.de/

Grundsätze: einfach zu bedienen, keine Werbung, die Fotos bleiben bei ihren Besitzern.

## Seiten

- [Startseite](https://imagicosmos.de/): die vier Programme und die Grundsätze
''')
w('_config.yml', '''# GitHub Pages (Jekyll): Die Seite besteht aus fertigen Dateien, Jekyll kopiert sie nur.
# Interne Dateien werden nicht mit veröffentlicht.
exclude:
  - README.md
  - werkzeuge
''')
print('ok')
