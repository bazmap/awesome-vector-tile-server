# A curated list of vector tile servers

## Introduction to vector tiles
### Format
Vector tiles can be found with different formats :
- [Mapbox Vector Tiles (.mvt)](https://github.com/mapbox/vector-tile-spec) : oftently used with the Protocolbuffer Binary Format (.pbf) extension
- MBTiles : a SQLight container storing tiled map data encoded in the Mapbox Vector Tiles (MVT) format
- PMTiles : a single-file archive format for storing tiled map data encoded in the Mapbox Vector Tiles (MVT) format
- [TileJSON](https://github.com/mapbox/tilejson-spec)
- [Versatiles](https://docs.versatiles.org/)
- GeoJSON
- TopoJSON

### Schema
Tiles data are structured using a specific schema (which layers, which attributes...). It is possible to use it's own schema but some have been standardized (for Open Street Map data sources) :
- [OpenMapTiles schema](https://openmaptiles.org/schema/)
- [Shortbread vector schema](https://shortbread-tiles.org)
- [Protomap schema](https://docs.protomaps.com/basemaps/layers)
- [Tilezen schema](https://tilezen.readthedocs.io/en/latest/layers/)

### Style
Using vector tiles into web maps requires to define how to style the data. This is a JSON file that contain the tile layers sources and their visual appearances. Depending on the map rendering technology, different style specifications exists :
- [Mapbox Style Specification](https://docs.mapbox.com/style-spec/guides/) for Mapbox GL JS
- [MapLibre Style Specification](https://maplibre.org/maplibre-style-spec/) for Maplibre GL JS


### Tools
Here is some tools that can be used with verctor tiles :
- To diplay what your tiles contain : [vector-inspector by Stevage](https://stevage.github.io/vector-inspector/#?url=&loc=0.8/0/0)
- To generate MapLibre Styles : [Maputnik](https://maputnik.github.io/editor/#1.07/0/0)
- To generate Mapbox styles : 
  - [Mapbox](https://www.mapbox.com/mapbox-studio)
  - [MapTiler](https://cloud.maptiler.com/maps/editor)
  - [Fresco](https://fresco.go-spatial.org/)
- [Mapbox awesome-vector-tile](https://github.com/mapbox/awesome-vector-tiles)
- [Awesome-maplibre](https://github.com/maplibre/awesome-maplibre)

## How to contribute
You have found new servers ? You spotted a mistake ? Feel free to contribute by forking this repo and submitting your PR.
The curated list is generated upon the vector-tile-server-list.json file. It is structurated this way :  
An array of objects containing these properties :
- `name` (text) : common name of the ressource
- `description` (text) : description of the content
- `url` (text) : url to use the ressource
- `metadata-url` (text) : url to find additionnal ressources or where the tilset have been found 
- `schema` (text) : if provided
- `flavors` (array of objects) : array of available styles
  - `style` (text) : style's name
  - `style-url` (text) : url to use the defining style
  - `metadata-url` (text) : url where to find any additionnal informations for the style
- `coverage` (text) : the coverage of the tileset (can be "world" or a country name, not a bounding box)
- `provider` (text) : the provider's name
- `attribution` (text) : the attribution in HTML format. Pay attention that some tileset need multiples attributions. Some tileset includes their own attributions.

Here is an exemple :
```json
[
  {
    "name":"My tileset",
    "description":"The tileset contain very specific data",
    "url":"https://www.tileset.xyz/tileset.mvt",
    "metadata-url":"https://www.tileset.xyz/metadata",
    "schema":"Specific",
    "flavors":[
      {"style":"Style 1", "url":"https://www.tileset.xyz/style1.json"},
      {
        "style":"Style 2", 
        "url":"https://www.tileset.xyz/style2.json", 
        "metadata-url":"https://www.tileset.xyz/metadata-style"
      }
    ],
    "coverage":"World",
    "provider":"My tileset corporation",
    "attribution":"<a href="https://www.tileset.xyz/about/">Tileset</a>"
  }
]
```

## The curated list
You will find here the curated list of vector tile servers.


