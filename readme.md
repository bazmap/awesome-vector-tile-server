<div align="center">
<h1>A curated list of vector tile servers</h1>
  <p>
    An awesome list of vector tile servers
    <img src="https://img.shields.io/badge/awesome-grey?logo=awesomelists&logoColor=fff&labelColor=0099FF" alt="contributors" />
  </p>
</div>
 
[![Button Icon]][Link] 

[Button Icon]: https://img.shields.io/badge/👉_The_curated_list-EF2D5E?style=for-the-badge
[Link]: #the-curated-list 'The curated list'



# 📔 Table of Contents

- [📔 Table of Contents](#-table-of-contents)
- [🌟 About the project](#-about-the-project)
- [🗺️ Introduction to vector tiles](#️-introduction-to-vector-tiles)
  - [✏️ Format](#️-format)
  - [🗃️ Schema](#️-schema)
  - [🖌️ Style](#️-style)
  - [🧰 Tools](#-tools)
- [👋 How to contribute](#-how-to-contribute)
- [📝The curated list](#the-curated-list)



# 🌟 About the project
It is not really easy to find vector tile servers despite the increasing popularity of this format in webGIS.
You will find here a curated list of open‑source and commercial vector tile servers.

This list aims to help developers, GIS professionals, and map enthusiasts discover, compare, and evaluate available solutions for serving vector data.

Contributions are welcome — if you have a favorite vector tile server that isn’t listed, feel free to open an issue or a pull request!



# 🗺️ Introduction to vector tiles
## ✏️ Format
Vector tiles can be found with different formats :
- [Mapbox Vector Tiles (.mvt)](https://github.com/mapbox/vector-tile-spec) : oftently used with the Protocolbuffer Binary Format (.pbf) extension
- MBTiles : a SQLight container storing tiled map data encoded in the Mapbox Vector Tiles (MVT) format
- PMTiles : a single-file archive format for storing tiled map data encoded in the Mapbox Vector Tiles (MVT) format
- [TileJSON](https://github.com/mapbox/tilejson-spec)
- [Versatiles](https://docs.versatiles.org/)
- GeoJSON
- TopoJSON


## 🗃️ Schema
Tiles data are structured using a specific schema (which layers, which attributes...). It is possible to use it's own schema but some have been standardized (for Open Street Map data sources) :
- [OpenMapTiles schema](https://openmaptiles.org/schema/)
- [Shortbread vector schema](https://shortbread-tiles.org)
- [Protomap schema](https://docs.protomaps.com/basemaps/layers)
- [Tilezen schema](https://tilezen.readthedocs.io/en/latest/layers/)


## 🖌️ Style
Using vector tiles into web maps requires to define how to style the data. This is a JSON file that contain the tile layers sources and their visual appearances. Depending on the map rendering technology, different style specifications exists :
- [Mapbox Style Specification](https://docs.mapbox.com/style-spec/guides/) for Mapbox GL JS
- [MapLibre Style Specification](https://maplibre.org/maplibre-style-spec/) for Maplibre GL JS


## 🧰 Tools
Here is some tools that can be used with verctor tiles :
- To diplay what your tiles contain : [vector-inspector by Stevage](https://stevage.github.io/vector-inspector/#?url=&loc=0.8/0/0)
- To generate MapLibre Styles : [Maputnik](https://maputnik.github.io/editor/#1.07/0/0)
- To generate Mapbox styles : 
  - [Mapbox](https://www.mapbox.com/mapbox-studio)
  - [MapTiler](https://cloud.maptiler.com/maps/editor)
  - [Fresco](https://fresco.go-spatial.org/)
- [Mapbox awesome-vector-tile](https://github.com/mapbox/awesome-vector-tiles)
- [Awesome-maplibre](https://github.com/maplibre/awesome-maplibre)



# 👋 How to contribute
You have found new servers ? You spotted a mistake ? Feel free to contribute by forking this repo and submitting your PR.
The curated list is generated upon the vector-tile-server-list.json file. It is structurated this way :  
An array of objects containing these properties :
- `name` (text) : common name of the ressource
- `description` (text) : description of the content
- `server-url` (object) :
  - `url` (text) : url to use the ressource
  - `active` (boolean) : is the provided url active ?
- `metadata-url` (object) :
  - `url` (text) : url to find additionnal ressources or where the tilset have been found 
  - `active` (boolean) : is the provided url active ?
- `schema` (text) : if provided
- `styles` (array of objects) : array of available styles
  - `name` (text) : style's name
  - `style-url` (object) : 
    - `url` (text) : url to use the defining style 
    - `active` (boolean) : is the provided url active ?
  - `metadata-url` (object) : 
    - `url` (text) : url where to find any additionnal informations for the style
    - `active` (boolean) : is the provided url active ?
- `coverage` (text) : the coverage of the tileset (can be "world" or a country name, not a bounding box)
- `provider` (text) : the provider's name
- `attribution` (text) : the attribution in HTML format. Pay attention that some tileset need multiples attributions, others include their own attributions. Double quotes need to be escaped ;-)

Here is an exemple :
```json
[
  {
    "name":"My tileset",
    "description":"The tileset contain very specific data",
    "server-url":{
      "url":"https://www.tileset.xyz/tileset.mvt",
      "active":true
    },
    "metadata-url":{
      "url":"https://www.tileset.xyz/metadata",
      "active":true
    },
    "schema":"Specific",
    "styles":[
      {
        "name":"Style 1", 
        "style-url":{
          "url":"https://www.tileset.xyz/style1.json",
          "active":true
        }
      },
      {
        "name":"Style 2", 
        "style-url":{
          "url":"https://www.tileset.xyz/style2.json",
          "active":true
        }, 
        "metadata-url":{
          "url":"https://www.tileset.xyz/metadata-style",
          "active":true
        }
      }
    ],
    "coverage":"World",
    "provider":"My tileset corporation",
    "attribution":"<a href=\"https://www.tileset.xyz/about/\">Tileset</a>"
  }
]
```



# 📝The curated list
For each link provided, a simple test is done every 24h to check if the link is active :
- 🟢 : the link coul be reached
- 🔴 : the link could not be reached




<!--START of the curated list-->
<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Description</th>
            <th>URL</th>
            <th>Styles</th>
            <th>Coverage</th>
            <th>Provider</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Admin Express</td>
            <td>Tuiles vectorielles administratives de l'IGN<br /><a href='https://geoservices.ign.fr/documentation/services/api-et-services-ogc/tuiles-vectorielles-tmswmts/styles' title='https://geoservices.ign.fr/documentation/services/api-et-services-ogc/tuiles-vectorielles-tmswmts/styles (url is active)' target='_blank'>Metadata 🟢</a><br />Attribution : <code>IGN-F/Geoportail<code></td>
            <td><a href='https://data.geopf.fr/tms/1.0.0/ADMIN_EXPRESS/{z}/{x}/{y}.pbf' title='Tile server url (url is active)' target='_blank'>https://data.geopf.fr/tms/1.0.0/ADMIN_EXPRESS/{z}/{x}/{y}.pbf🟢</a></td>
            <td><ul><li><a href='https://data.geopf.fr/annexes/ressources/vectorTiles/styles/ADMIN_EXPRESS/adminexpress.json' title='Tile server url (url is active)' target='_blank'>Thème par défaut🟢</a></li></ul></td>
            <td>France métropolitaine et DOM</td>
            <td>IGN</td>
        </tr>
        <tr>
            <td>BD TOPO®</td>
            <td>Tuiles vectorielles de la Base de données Topographiques (BD TOPO®) de l'IGN<br /><a href='https://geoservices.ign.fr/documentation/services/api-et-services-ogc/tuiles-vectorielles-tmswmts/styles' title='https://geoservices.ign.fr/documentation/services/api-et-services-ogc/tuiles-vectorielles-tmswmts/styles (url is active)' target='_blank'>Metadata 🟢</a><br />Attribution : <code>IGN-F/Geoportail<code></td>
            <td><a href='https://data.geopf.fr/tms/1.0.0/BDTOPO/{z}/{x}/{y}.pbf' title='Tile server url (url is active)' target='_blank'>https://data.geopf.fr/tms/1.0.0/BDTOPO/{z}/{x}/{y}.pbf🟢</a></td>
            <td><ul><li><a href='https://data.geopf.fr/annexes/ressources/vectorTiles/styles/BDTOPO/classique.json' title='Tile server url (url is active)' target='_blank'>Classique🟢</a></li><li><a href='https://data.geopf.fr/annexes/ressources/vectorTiles/styles/BDTOPO/bati.json' title='Tile server url (url is active)' target='_blank'>Bâtiments🟢</a></li><li><a href='https://data.geopf.fr/annexes/ressources/vectorTiles/styles/BDTOPO/hydrographie.json' title='Tile server url (url is active)' target='_blank'>Hydrographie🟢</a></li><li><a href='https://data.geopf.fr/annexes/ressources/vectorTiles/styles/BDTOPO/routier.json' title='Tile server url (url is active)' target='_blank'>Réseau routier🟢</a></li><li><a href='https://data.geopf.fr/annexes/ressources/vectorTiles/styles/BDTOPO/bati_date.json' title='Tile server url (url is active)' target='_blank'>Age du bâti🟢</a></li><li><a href='https://data.geopf.fr/annexes/ressources/vectorTiles/styles/BDTOPO/bati_etages.json' title='Tile server url (url is active)' target='_blank'>Bâtiments étages🟢</a></li></ul></td>
            <td>France métropolitaine et DOM</td>
            <td>IGN</td>
        </tr>
        <tr>
            <td>Courbes de niveau</td>
            <td>Tuiles vectorielles des courbes de niveau de l'IGN<br /><a href='https://geoservices.ign.fr/documentation/services/api-et-services-ogc/tuiles-vectorielles-tmswmts/styles' title='https://geoservices.ign.fr/documentation/services/api-et-services-ogc/tuiles-vectorielles-tmswmts/styles (url is active)' target='_blank'>Metadata 🟢</a><br />Attribution : <code>IGN-F/Geoportail<code></td>
            <td><a href='https://data.geopf.fr/tms/1.0.0/ISOHYPSE/{z}/{x}/{y}.pbf' title='Tile server url (url is active)' target='_blank'>https://data.geopf.fr/tms/1.0.0/ISOHYPSE/{z}/{x}/{y}.pbf🟢</a></td>
            <td><ul><li><a href='https://data.geopf.fr/annexes/ressources/vectorTiles/styles/ISOHYPSE/isohypse_multicolore.json' title='Tile server url (url is active)' target='_blank'>Multicolor🟢</a></li><li><a href='https://data.geopf.fr/annexes/ressources/vectorTiles/styles/ISOHYPSE/isohypse_monochrome_marron.json' title='Tile server url (url is active)' target='_blank'>Marron🟢</a></li><li><a href='https://data.geopf.fr/annexes/ressources/vectorTiles/styles/ISOHYPSE/isohypse_monochrome_orange.json' title='Tile server url (url is active)' target='_blank'>Orange🟢</a></li></ul></td>
            <td>France métropolitaine et DOM</td>
            <td>IGN</td>
        </tr>
        <tr>
            <td>OCS GE</td>
            <td>Tuiles vectorielles de l'OCS GE (Occupation du Sol)<br /><a href='https://geoservices.ign.fr/documentation/services/api-et-services-ogc/tuiles-vectorielles-tmswmts/styles' title='https://geoservices.ign.fr/documentation/services/api-et-services-ogc/tuiles-vectorielles-tmswmts/styles (url is active)' target='_blank'>Metadata 🟢</a><br />Attribution : <code>IGN-F/Geoportail<code></td>
            <td><a href='https://data.geopf.fr/tms/1.0.0/OCSGE_2016/{z}/{x}/{y}.pbf' title='Tile server url (url is active)' target='_blank'>https://data.geopf.fr/tms/1.0.0/OCSGE_2016/{z}/{x}/{y}.pbf🟢</a></td>
            <td><ul><li><a href='https://data.geopf.fr/annexes/ressources/vectorTiles/styles/OCSGE/ocsge_couverture.json' title='Tile server url (url is active)' target='_blank'>Couverture🟢</a></li><li><a href='https://data.geopf.fr/annexes/ressources/vectorTiles/styles/OCSGE/ocsge_usage.json' title='Tile server url (url is active)' target='_blank'>Usage🟢</a></li></ul></td>
            <td>France métropolitaine et DOM</td>
            <td>IGN</td>
        </tr>
        <tr>
            <td>Parcellaire Express (PCI)</td>
            <td>Tuiles vectorielles du parcellaire cadastral de l'IGN<br /><a href='https://geoservices.ign.fr/documentation/services/api-et-services-ogc/tuiles-vectorielles-tmswmts/styles' title='https://geoservices.ign.fr/documentation/services/api-et-services-ogc/tuiles-vectorielles-tmswmts/styles (url is active)' target='_blank'>Metadata 🟢</a><br />Attribution : <code>IGN-F/Geoportail<code></td>
            <td><a href='https://data.geopf.fr/tms/1.0.0/PCI/{z}/{x}/{y}.pbf' title='Tile server url (url is active)' target='_blank'>https://data.geopf.fr/tms/1.0.0/PCI/{z}/{x}/{y}.pbf🟢</a></td>
            <td><ul><li><a href='https://data.geopf.fr/annexes/ressources/vectorTiles/styles/PCI/noir_et_blanc.json' title='Tile server url (url is active)' target='_blank'>Noir et blanc🟢</a></li><li><a href='https://data.geopf.fr/annexes/ressources/vectorTiles/styles/PCI/pci.json' title='Tile server url (url is active)' target='_blank'>Thème par défaut🟢</a></li></ul></td>
            <td>France métropolitaine et DOM</td>
            <td>IGN</td>
        </tr>
        <tr>
            <td>Plan IGN</td>
            <td>Tuiles vectorielles du plan IGN<br /><a href='https://geoservices.ign.fr/documentation/services/api-et-services-ogc/tuiles-vectorielles-tmswmts/styles' title='https://geoservices.ign.fr/documentation/services/api-et-services-ogc/tuiles-vectorielles-tmswmts/styles (url is active)' target='_blank'>Metadata 🟢</a><br />Attribution : <code>IGN-F/Geoportail<code></td>
            <td><a href='https://data.geopf.fr/tms/1.0.0/PLAN.IGN/{z}/{x}/{y}.pbf' title='Tile server url (url is active)' target='_blank'>https://data.geopf.fr/tms/1.0.0/PLAN.IGN/{z}/{x}/{y}.pbf🟢</a></td>
            <td><ul><li><a href='https://data.geopf.fr/annexes/ressources/vectorTiles/styles/PLAN.IGN/standard.json' title='Tile server url (url is active)' target='_blank'>Standard🟢</a></li><li><a href='https://data.geopf.fr/annexes/ressources/vectorTiles/styles/PLAN.IGN/attenue.json' title='Tile server url (url is active)' target='_blank'>Atténué🟢</a></li><li><a href='https://data.geopf.fr/annexes/ressources/vectorTiles/styles/PLAN.IGN/gris.json' title='Tile server url (url is active)' target='_blank'>Gris🟢</a></li><li><a href='https://data.geopf.fr/annexes/ressources/vectorTiles/styles/PLAN.IGN/sans_toponymes.json' title='Tile server url (url is active)' target='_blank'>Sans toponymes🟢</a></li><li><a href='https://data.geopf.fr/annexes/ressources/vectorTiles/styles/PLAN.IGN/toponymes.json' title='Tile server url (url is active)' target='_blank'>Toponymes🟢</a></li><li><a href='https://data.geopf.fr/annexes/ressources/vectorTiles/styles/PLAN.IGN/accentue.json' title='Tile server url (url is active)' target='_blank'>Accentué🟢</a></li><li><a href='https://data.geopf.fr/annexes/ressources/vectorTiles/styles/PLAN.IGN/classique.json' title='Tile server url (url is active)' target='_blank'>Classique🟢</a></li><li><a href='https://data.geopf.fr/annexes/ressources/vectorTiles/styles/PLAN.IGN/epure.json' title='Tile server url (url is active)' target='_blank'>Epuré🟢</a></li><li><a href='https://viglino.github.io/geoservice-style/mono/mono_red.json' title='Tile server url (url is active)' target='_blank'>Mono red🟢</a></li><li><a href='https://viglino.github.io/geoservice-style/mono/mono_green.json' title='Tile server url (url is active)' target='_blank'>Mono green🟢</a></li><li><a href='https://viglino.github.io/geoservice-style/mono/mono_blue.json' title='Tile server url (url is active)' target='_blank'>Mono blue🟢</a></li><li><a href='https://viglino.github.io/geoservice-style/mono/mono_purple.json' title='Tile server url (url is active)' target='_blank'>Mono purple🟢</a></li><li><a href='https://viglino.github.io/geoservice-style/mono/mono_orange.json' title='Tile server url (url is active)' target='_blank'>Mono orange🟢</a></li><li><a href='https://viglino.github.io/geoservice-style/mono/mono_yellow.json' title='Tile server url (url is active)' target='_blank'>Mono yellow🟢</a></li><li><a href='https://viglino.github.io/geoservice-style/mono/mono_black.json' title='Tile server url (url is active)' target='_blank'>Mono black🟢</a></li><li><a href='https://viglino.github.io/geoservice-style/mono/mono_gray.json' title='Tile server url (url is active)' target='_blank'>Mono gray🟢</a></li><li><a href='https://viglino.github.io/geoservice-style/erp/erp.json' title='Tile server url (url is active)' target='_blank'>ERP🟢</a></li><li><a href='https://viglino.github.io/geoservice-style/mapart/mapart.json' title='Tile server url (url is active)' target='_blank'>MapArt🟢</a></li><li><a href='https://viglino.github.io/geoservice-style/cyanotype/cyanotype.json' title='Tile server url (url is active)' target='_blank'>Cyanotype🟢</a></li><li><a href='https://viglino.github.io/geoservice-style/cassini/cassini.json' title='Tile server url (url is active)' target='_blank'>Cassini map🟢</a></li><li><a href='https://viglino.github.io/geoservice-style/retro/retro.json' title='Tile server url (url is active)' target='_blank'>Retro map🟢</a></li><li><a href='https://viglino.github.io/geoservice-style/guidebook/guidebook.json' title='Tile server url (url is active)' target='_blank'>Guide book🟢</a></li><li><a href='https://viglino.github.io/geoservice-style/coffee/coffee.json' title='Tile server url (url is active)' target='_blank'>Coffee🟢</a></li><li><a href='https://viglino.github.io/geoservice-style/mondrian/mondrian.json' title='Tile server url (url is active)' target='_blank'>Mondrian🟢</a></li><li><a href='https://viglino.github.io/geoservice-style/roads/roads.json' title='Tile server url (url is active)' target='_blank'>Roads🟢</a></li><li><a href='https://viglino.github.io/geoservice-style/halloween/halloween.json' title='Tile server url (url is active)' target='_blank'>Halloween🟢</a></li><li><a href='https://viglino.github.io/geoservice-style/christmas/christmas.json' title='Tile server url (url is active)' target='_blank'>Christmas🟢</a></li></ul></td>
            <td>France métropolitaine et DOM</td>
            <td>IGN</td>
        </tr>
        <tr>
            <td>OpenFreeMap</td>
            <td>OpenFreeMap lets you display custom maps on your website and apps for free<br /><a href='https://openfreemap.org/' title='https://openfreemap.org/ (url is active)' target='_blank'>Metadata 🟢</a><br />Attribution : <code><a href="https://openfreemap.org" target="_blank">OpenFreeMap</a> <a href="https://www.openmaptiles.org/" target="_blank">© OpenMapTiles</a> Data from <a href="https://www.openstreetmap.org/copyright" target="_blank">OpenStreetMap</a><code></td>
            <td><a href='https://tiles.openfreemap.org/planet' title='Tile server url (url is active)' target='_blank'>https://tiles.openfreemap.org/planet🟢</a></td>
            <td><ul><li><a href='https://tiles.openfreemap.org/styles/positron' title='Tile server url (url is active)' target='_blank'>Positron🟢</a></li><li><a href='https://tiles.openfreemap.org/styles/bright' title='Tile server url (url is active)' target='_blank'>Bright🟢</a></li><li><a href='https://tiles.openfreemap.org/styles/liberty' title='Tile server url (url is active)' target='_blank'>Liberty🟢</a></li><li><a href='https://tiles.openfreemap.org/styles/liberty' title='Tile server url (url is active)' target='_blank'>3D🟢</a></li><li><a href='https://viglino.github.io/geoservice-style/openfreecassini/openfreecassini.json' title='Tile server url (url is active)' target='_blank'>Cassini🟢</a></li></ul></td>
            <td>World</td>
            <td>OpenFreeMap</td>
        </tr>
        <tr>
            <td>Cadastre France</td>
            <td><br /><a href='https://openmaptiles.data.gouv.fr/' title='https://openmaptiles.data.gouv.fr/ (url is active)' target='_blank'>Metadata 🟢</a><br />Attribution : <code><a href="https://cadastre.data.gouv.fr/">&copy; DINUM (data.gouv.fr)</a><code></td>
            <td><a href='https://openmaptiles.data.gouv.fr/data/cadastre/{z}/{x}/{y}.pbf' title='Tile server url (url is active)' target='_blank'>https://openmaptiles.data.gouv.fr/data/cadastre/{z}/{x}/{y}.pbf🟢</a></td>
            <td><ul></ul></td>
            <td>France métropolitaine et DOM</td>
            <td>DINUM (data.gouv.fr)</td>
        </tr>
        <tr>
            <td>Découpage administratif - France</td>
            <td><br /><a href='https://openmaptiles.data.gouv.fr/' title='https://openmaptiles.data.gouv.fr/ (url is active)' target='_blank'>Metadata 🟢</a><br />Attribution : <code>© DINUM (data.gouv.fr)<code></td>
            <td><a href='https://openmaptiles.data.gouv.fr/data/decoupage-administratif/{z}/{x}/{y}.pbf' title='Tile server url (url is active)' target='_blank'>https://openmaptiles.data.gouv.fr/data/decoupage-administratif/{z}/{x}/{y}.pbf🟢</a></td>
            <td><ul></ul></td>
            <td>France métropolitaine et DOM</td>
            <td>DINUM (data.gouv.fr)</td>
        </tr>
        <tr>
            <td>Cadastre DVF France</td>
            <td><br /><a href='https://openmaptiles.data.gouv.fr/' title='https://openmaptiles.data.gouv.fr/ (url is active)' target='_blank'>Metadata 🟢</a><br />Attribution : <code><a href="https://cadastre.data.gouv.fr/">&copy; DINUM (data.gouv.fr)</a><code></td>
            <td><a href='https://openmaptiles.data.gouv.fr/data/cadastre-dvf/{z}/{x}/{y}.pbf' title='Tile server url (url is active)' target='_blank'>https://openmaptiles.data.gouv.fr/data/cadastre-dvf/{z}/{x}/{y}.pbf🟢</a></td>
            <td><ul></ul></td>
            <td>France métropolitaine et DOM</td>
            <td>DINUM (data.gouv.fr)</td>
        </tr>
        <tr>
            <td>ifremer-atlasdce</td>
            <td><br /><a href='https://openmaptiles.data.gouv.fr/' title='https://openmaptiles.data.gouv.fr/ (url is active)' target='_blank'>Metadata 🟢</a><br />Attribution : <code>data.gouv.fr<code></td>
            <td><a href='https://openmaptiles.data.gouv.fr/data/ifremer-atlasdce/{z}/{x}/{y}.pbf' title='Tile server url (url is active)' target='_blank'>https://openmaptiles.data.gouv.fr/data/ifremer-atlasdce/{z}/{x}/{y}.pbf🟢</a></td>
            <td><ul></ul></td>
            <td>France métropolitaine et DOM</td>
            <td>data.gouv.fr</td>
        </tr>
        <tr>
            <td>Decoupage administratif 2024 France</td>
            <td><br /><a href='https://openmaptiles.data.gouv.fr/' title='https://openmaptiles.data.gouv.fr/ (url is active)' target='_blank'>Metadata 🟢</a><br />Attribution : <code>© DINUM (data.gouv.fr)<code></td>
            <td><a href='https://openmaptiles.data.gouv.fr/data/decoupage-administratif-2024/{z}/{x}/{y}.pbf' title='Tile server url (url is active)' target='_blank'>https://openmaptiles.data.gouv.fr/data/decoupage-administratif-2024/{z}/{x}/{y}.pbf🟢</a></td>
            <td><ul></ul></td>
            <td>France métropolitaine et DOM</td>
            <td>© DINUM (data.gouv.fr)</td>
        </tr>
        <tr>
            <td>Tuiles vectorielles Monde par data.gouv.fr</td>
            <td><br /><a href='https://openmaptiles.data.gouv.fr/' title='https://openmaptiles.data.gouv.fr/ (url is active)' target='_blank'>Metadata 🟢</a><br />Attribution : <code><a href=https://www.data.gouv.fr/ target=_blank>&copy; DINUM (data.gouv.fr)</a> <a href=https://www.openmaptiles.org/ target=_blank>&copy; OpenMapTiles</a> <a href=https://www.openstreetmap.org/copyright target=_blank>&copy; Contributeurs OpenStreetMap</a><code></td>
            <td><a href='https://openmaptiles.data.gouv.fr/data/planet-vector/{z}/{x}/{y}.pbf' title='Tile server url (url is active)' target='_blank'>https://openmaptiles.data.gouv.fr/data/planet-vector/{z}/{x}/{y}.pbf🟢</a></td>
            <td><ul><li><a href='https://openmaptiles.data.gouv.fr/styles/osm-bright/style.json' title='Tile server url (url is active)' target='_blank'>Bright🟢</a></li><li><a href='https://openmaptiles.data.gouv.fr/styles/osm-openmaptiles/style.json' title='Tile server url (url is active)' target='_blank'>OSM OpenMapTiles🟢</a></li><li><a href='https://openmaptiles.data.gouv.fr/styles/positron/style.json' title='Tile server url (url is active)' target='_blank'>Positron🟢</a></li><li><a href='https://openmaptiles.data.gouv.fr/styles/dark-matter/style.json' title='Tile server url (url is active)' target='_blank'>Dark Matter🟢</a></li><li><a href='https://openmaptiles.data.gouv.fr/styles/maptiler-toner/style.json' title='Tile server url (url is active)' target='_blank'>Toner🟢</a></li><li><a href='https://openmaptiles.data.gouv.fr/styles/fiord-color/style.json' title='Tile server url (url is active)' target='_blank'>Fiord Color🟢</a></li></ul></td>
            <td>World</td>
            <td>DINUM (data.gouv.fr)</td>
        </tr>
        <tr>
            <td>Tuiles vectorielles France par DINUM (data.gouv.fr)</td>
            <td><br /><a href='https://openmaptiles.data.gouv.fr/' title='https://openmaptiles.data.gouv.fr/ (url is active)' target='_blank'>Metadata 🟢</a><br />Attribution : <code><a href="https://www.data.gouv.fr/" target="_blank">&copy; DINUM (data.gouv.fr)</a> <a href="https://www.openmaptiles.org/" target="_blank">&copy; OpenMapTiles</a> <a href="https://www.openstreetmap.org/copyright" target="_blank">&copy; Contributeurs OpenStreetMap</a><code></td>
            <td><a href='https://openmaptiles.data.gouv.fr/data/france-vector/{z}/{x}/{y}.pbf' title='Tile server url (url is active)' target='_blank'>https://openmaptiles.data.gouv.fr/data/france-vector/{z}/{x}/{y}.pbf🟢</a></td>
            <td><ul></ul></td>
            <td>France métropolitaine et DOM</td>
            <td>DINUM (data.gouv.fr)</td>
        </tr>
        <tr>
            <td>Base - Switzerland</td>
            <td>Points d'intérêt sur différents thèmes<br /><a href='https://www.geo.admin.ch/en/vector-tiles-service-available-services-and-data' title='https://www.geo.admin.ch/en/vector-tiles-service-available-services-and-data (url is active)' target='_blank'>Metadata 🟢</a><br />Attribution : <code>© swisstopo, © FDFA, © FOEN, © FOCP, © SAC, © Naturefriends Switzerland, © opentransportdata.swiss, © MapTiler, © OpenStreetMap contributors<code></td>
            <td><a href='https://vectortiles.geo.admin.ch/tiles/ch.swisstopo.base.vt/v1.0.0/tiles.json' title='Tile server url (url is active)' target='_blank'>https://vectortiles.geo.admin.ch/tiles/ch.swisstopo.base.vt/v1.0.0/tiles.json🟢</a></td>
            <td><ul><li><a href='https://vectortiles.geo.admin.ch/styles/ch.swisstopo.basemap.vt/style.json' title='Tile server url (url is active)' target='_blank'>Base Map🟢</a></li><li><a href='https://vectortiles.geo.admin.ch/styles/ch.swisstopo.lightbasemap.vt/style.json' title='Tile server url (url is active)' target='_blank'>Light Base Map🟢</a></li><li><a href='https://vectortiles.geo.admin.ch/styles/ch.swisstopo.imagerybasemap.vt/style.json' title='Tile server url (url is active)' target='_blank'>Imagery Base Map🟢</a></li><li><a href='https://vectortiles.geo.admin.ch/styles/ch.swisstopo.basemap-winter.vt/style.json' title='Tile server url (url is active)' target='_blank'>Base Map Winter🟢</a></li></ul></td>
            <td>Switzerland and Liechtenstein</td>
            <td>Swisstopo</td>
        </tr>
        <tr>
            <td>Relief - Switzerland</td>
            <td>Eléments de terrain tirés des cartes nationales<br /><a href='https://www.geo.admin.ch/en/vector-tiles-service-available-services-and-data' title='https://www.geo.admin.ch/en/vector-tiles-service-available-services-and-data (url is active)' target='_blank'>Metadata 🟢</a><br />Attribution : <code>© swisstopo, © FDFA, © FOEN, © FOCP, © SAC, © Naturefriends Switzerland, © opentransportdata.swiss, © MapTiler, © OpenStreetMap contributors<code></td>
            <td><a href='https://vectortiles.geo.admin.ch/tiles/ch.swisstopo.relief.vt/v1.0.0/tiles.json' title='Tile server url (url is active)' target='_blank'>https://vectortiles.geo.admin.ch/tiles/ch.swisstopo.relief.vt/v1.0.0/tiles.json🟢</a></td>
            <td><ul><li><a href='https://vectortiles.geo.admin.ch/styles/ch.swisstopo.basemap.vt/style.json' title='Tile server url (url is active)' target='_blank'>Base Map🟢</a></li><li><a href='https://vectortiles.geo.admin.ch/styles/ch.swisstopo.lightbasemap.vt/style.json' title='Tile server url (url is active)' target='_blank'>Light Base Map🟢</a></li><li><a href='https://vectortiles.geo.admin.ch/styles/ch.swisstopo.imagerybasemap.vt/style.json' title='Tile server url (url is active)' target='_blank'>Imagery Base Map🟢</a></li><li><a href='https://vectortiles.geo.admin.ch/styles/ch.swisstopo.basemap-winter.vt/style.json' title='Tile server url (url is active)' target='_blank'>Base Map Winter🟢</a></li></ul></td>
            <td>Switzerland and Liechtenstein</td>
            <td>Swisstopo</td>
        </tr>
        <tr>
            <td>OpenStreetMap</td>
            <td>Des tuiles OpenStreetMap vectorielles libres, gratuites, sans inscription et anonymes<br /><a href='https://tuiles.enliberte.fr/' title='https://tuiles.enliberte.fr/ (url is not active)' target='_blank'>Metadata 🔴</a><br />Attribution : <code>© <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors<code></td>
            <td><a href='https://osm.nbg1.your-objectstorage.com/planet.pmtiles' title='Tile server url (url is active)' target='_blank'>https://osm.nbg1.your-objectstorage.com/planet.pmtiles🟢</a></td>
            <td><ul><li><a href='https://tuiles.enliberte.fr/styles/bright.json' title='Tile server url (url is not active)' target='_blank'>Bright🔴</a></li><li><a href='https://tuiles.enliberte.fr/styles/basic.json' title='Tile server url (url is not active)' target='_blank'>Basic🔴</a></li><li><a href='https://tuiles.enliberte.fr/styles/positron.json' title='Tile server url (url is not active)' target='_blank'>Positron🔴</a></li><li><a href='https://tuiles.enliberte.fr/styles/liberty.json' title='Tile server url (url is not active)' target='_blank'>Liberty🔴</a></li><li><a href='https://tuiles.enliberte.fr/styles/dark-matter.json' title='Tile server url (url is not active)' target='_blank'>Dark Matter🔴</a></li><li><a href='https://tuiles.enliberte.fr/styles/maptiler-3d.json' title='Tile server url (url is not active)' target='_blank'>Maptiler 3D🔴</a></li><li><a href='https://tuiles.enliberte.fr/styles/toner.json' title='Tile server url (url is not active)' target='_blank'>Toner🔴</a></li><li><a href='https://tuiles.enliberte.fr/styles/fiord-color.json' title='Tile server url (url is not active)' target='_blank'>Fiord color🔴</a></li></ul></td>
            <td>World</td>
            <td>Tuiles en Liberté</td>
        </tr>
        <tr>
            <td>OpenStreetMap</td>
            <td>Free vector tiles server open for public use<br /><a href='https://docs.versatiles.org/guides/use_tiles.versatiles.org.html' title='https://docs.versatiles.org/guides/use_tiles.versatiles.org.html (url is active)' target='_blank'>Metadata 🟢</a><br />Attribution : <code>© <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors<code></td>
            <td><a href='https://tiles.versatiles.org/tiles/osm/{z}/{x}/{y}' title='Tile server url (url is active)' target='_blank'>https://tiles.versatiles.org/tiles/osm/{z}/{x}/{y}🟢</a></td>
            <td><ul><li><a href='https://tiles.versatiles.org/assets/styles/colorful/style.json' title='Tile server url (url is active)' target='_blank'>Colorful🟢</a></li><li><a href='https://tiles.versatiles.org/assets/styles/eclipse/style.json' title='Tile server url (url is active)' target='_blank'>Eclipse🟢</a></li><li><a href='https://tiles.versatiles.org/assets/styles/greybeard/style.json' title='Tile server url (url is active)' target='_blank'>Greybeard🟢</a></li><li><a href='https://tiles.versatiles.org/assets/styles/neutrino/style.json' title='Tile server url (url is active)' target='_blank'>Neutrino🟢</a></li></ul></td>
            <td>World</td>
            <td>Versatiles</td>
        </tr>
    </tbody>
</table>
<!--END of the curated list-->

