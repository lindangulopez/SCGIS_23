838 vues  26 mai 2021  QGIS Plugin
It's a QGIS plugin to store some metadata for PostgreSQL layers inside a PostgreSQL database.


Documentation :

https://docs.3liz.org/qgis-pgmetadata...


Source code :
https://github.com/3liz/qgis-pgmetada...


Transifex for translation of the project :
https://www.transifex.com/3liz-1/pgme...



3Liz :
https://www.3liz.com Etienne Trimaille

{
PgMetadata

Store some metadata about layers which are stored in PostgreSQL. It's possible to define title, abstract, links, contacts etc. It also provides some search tool, in the QGIS Locator bar for instance.

Store some metadata about layers which are stored in PostgreSQL. It's possible to define title, abstract, links, contacts etc. It also provides some search tool, in the QGIS Locator bar for instance.

7 évaluation(s), 6564 téléchargements
Catégorie	Analysis
Étiquettes	metadata, postgresql, qgis, metadonnees, dcat, xml, csv
Plus d'infos	Page d'accueil   suivi des anomalies   dépôt du code
Auteur	3Liz
Version installée	1.2.2
Version disponible (stable)	1.2.2 mise à jour le lun. mai 15 05:03:59 2023
Changelog	Version 1.2.2:
* Fix "array exceeds maximum" for layers with many features (contribution from @effjot Florian Jenn)

Version 1.2.1:
* Fix a warning about invalid database
* Add the phone field to "Contacts" in the administration project

Version 1.2.0:
* License - Release PgMetadata under the GNU General Public License v2.0.
* Raise the QGIS minimum version to 3.16
* Add raster support (contribution from @effjot Florian Jenn)
* Fix handling of backslashes in file:// links to Windows files (contribution from @effjot Florian Jenn)
* Add phone number field (contribution from @effjot Florian Jenn)
* Email links are now clickable
* Connection names are now separated by `!!::!!` so that semicolons (former separator) can be used in connection names}
