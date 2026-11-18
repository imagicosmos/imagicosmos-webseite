# Webseite von Imagicosmos

Eine einzelne Seite, die die vier Programme (Imagichron, Imagiclique, Imagicoll, Imagicruise) vorstellt und zu
ihren eigenen Seiten führt. Erstellt am 16.11.2026. Gerüst, Schrift und Logo-Animation stammen aus
`../../imagiclique/webseite` (dort wiederum aus `../../imagichron-webseite`); Grund und Akzent sind neutral, die
Farbe kommt von den vier Projekten (`../marke`).

Grundsätze wie bei den anderen Seiten: einfaches HTML/CSS/JavaScript, **nichts von fremden Servern**, strenge
Content-Security-Policy, keine Cookies, keine Statistik.

## Dateien

| Datei | Inhalt |
|---|---|
| `index.html` | Startseite: Einstieg, Programme (vier Karten), Grundsätze |
| `style.css` | Gestaltung; Abschnitt 1 Farben, Abschnitt 15 Eigenes (Marken-Feld, Projektkarten) |
| `app.js`, `modus.js` | Hell/Dunkel, Laufband, wechselnde Wörter, Einblenden |
| `bausteine/zauberstab.js` | Logo-Animation, „cosmos“ in Nachtviolett (wie in `../marke/zauber/`); gemeinsamer Baustein „zauberstab“ aus `../bausteine` (seit 18.11.2026; nicht von Hand ändern, neu einbauen mit `node ../bausteine/werkzeuge/einbauen.js zauberstab webseite/bausteine`). Wort und Farben liest er aus dem Logo und `style.css`, die Leuchtfarben stehen als `data-stern`/`data-band` in der Einbindung |
| `bilder/` | Zeichen der vier Projekte (unveränderte Kopien aus `../marke/*.svg`), `favicon.svg`, `apple-touch-icon.png`, `teilen.png` (Vorschaubild 1200 × 630) |
| `schriften/` | Josefin Sans 700 mit Lizenz (aus `../marke/schrift/`) |
| `impressum.html`, `datenschutz.html`, `404.html`, `robots.txt`, `sitemap.xml`, `llms.txt`, `_config.yml` | **erzeugt** von `werkzeuge/rechtsseiten.py` – Texte dort ändern, dann im Ordner `imagicosmos` aufrufen: `python webseite/werkzeuge/rechtsseiten.py` |

Nach Änderungen an Kopf oder Fuß in `index.html` das Werkzeug neu laufen lassen, damit die Rechtsseiten gleich
aussehen.

## Veröffentlichen

Wie bei Imagiclique: `webseite-veroeffentlichen.cmd` (im Ordner `imagicosmos`) lädt den **committeten** Stand von
`webseite/` als einzelnen Commit mit neutralem Autor per Force-Push in das öffentliche Repository
`imagicosmos/imagicosmos-webseite`; GitHub Pages liefert dessen Zweig `main` aus
(https://imagicosmos.de/, seit 18.11.2026; die alte Adresse https://imagicosmos.github.io/imagicosmos-webseite/ leitet weiter). Nichts außerhalb von `webseite/` und keine private
E-Mail-Adresse gelangt dorthin. Nichts direkt im öffentlichen Repository ändern.

## Domain imagicosmos.de

Verbunden am 18.11.2026 (DNS bei IONOS von Mario, für die Organisation bestätigt; TXT-Eintrag bei IONOS nicht löschen).
Die Datei `CNAME` (eine Zeile `imagicosmos.de`) muss hier in `webseite/` bleiben: Das Veröffentlichungs-Skript ersetzt
das öffentliche Repository jedes Mal ganz, ohne `CNAME` wäre die Adresse danach weg.

## Noch offen

1. **Zeichen von Imagicosmos:** entschieden am 16.11.2026 (vier Menschen unter ihrem Sternbild, Nachtviolett).
   `bilder/favicon.svg` = `../marke/imagicosmos.svg`, `bilder/apple-touch-icon.png` = `../marke/png/imagicosmos-180.png`.
   „cosmos“ ist im Logo und im Vorschaubild `teilen.png` violett wie in der Marke (Mario, 16.11.2026).
2. **Links zu den Programmen** (17.11.2026): Imagichron → https://imagichron.de/, Imagiclique →
   https://imagiclique.de/ (verbunden seit 17.11.2026), Imagicoll →
   https://imagicoll.de/ (App „Fotos sichern“, verbunden seit 18.11.2026), Imagicruise →
   https://imagicruise.de/ (Beta, verbunden seit 17.11.2026). Je zwei Stellen in `index.html` (Karte und Fußzeile)
   und eine in `llms.txt`. Ändert sich eine Adresse (eigene Domain), in `index.html` und in
   `werkzeuge/rechtsseiten.py` (Text von `llms.txt`) ändern, dann `python webseite/werkzeuge/rechtsseiten.py`.
3. **Stand der Programme:** Imagicoll zeigt die App „Fotos sichern“, Alben und Fotowand stehen als „in Arbeit“ im
   Text. Texte und Stand anpassen, wenn die Projekte weiter sind.
4. **Grundsätze prüfen:** Die drei Aussagen (Fotos gehören dir, einfach, keine Werbung) müssen für jedes Programm
   stimmen, das hier erscheint.
5. **Rechtstexte:** nach dem Muster der anderen Seiten geschrieben, nicht juristisch geprüft.
6. **Rückverweise:** Fußzeilen von imagichron.de und der Imagiclique-Seite auf Imagicosmos umstellen, sobald
   diese Seite online ist.
