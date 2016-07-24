# [Shapefile]

The world borders ZIP file contains a set of data files collectively known as an ESRI Shapefile, one of the most popular geospatial data formats. When unzipped, the world borders dataset includes files with the following extensions:

* .shp: Holds the vector data for the world borders geometries.
* .shx: Spatial index file for geometries stored in the .shp.
* .dbf: Database file for holding non-geometric attribute data (e.g., integer and character fields).
* .prj: Contains the spatial reference information for the geographic data stored in the shapefile.

## Convert for DWG (Autocad) to DXF

Download [TeighaFileConverter]. Works for Ubuntu, Windows and other platforms.

## Convert from DXF to Shapefile

Since shape files can only have one feature type we will create one for points, one for lines and one for polygons:

```sh
ogr2ogr gaston14_points.shp gaston14.dxf -where "ogr_geometry = 'POINT'"
ogr2ogr gaston14_lines.shp gaston14.dxf -where "ogr_geometry = 'LINESTRING'"
ogr2ogr gaston14_polygons.shp gaston14.dxf -where "ogr_geometry = 'POLYGON'" 
```

## Other links about converting between DWG and Shapefile and other formats

* Web app-converter: http://www.gisconvert.com. Can convert AutoCAD DXF, AutoCAD DWG, SHP, or KML to ESRI Shapefile, Google KML, or DXF.
* http://gis.stackexchange.com/questions/27007/transforming-from-dwg-dxf-to-gis/27020
* https://danielbrannstrom.wordpress.com/2010/11/01/converting-autocad-dwg-files-to-esri-shapefiles/

[TeighaFileConverter]: <https://www.opendesign.com/guestfiles/TeighaFileConverter>
[Shapefile]: <https://en.wikipedia.org/wiki/Shapefile>
