import arcpy
import os

# --------------------------------------------------------------------
# PROJECT SETTINGS
# --------------------------------------------------------------------
project_path = r"C:\Users\Saar\Documents\ArcGIS\Projects\MyProject\MyProject.aprx"
gdb_path = r"C:\Users\Saar\Documents\ArcGIS\Projects\MyProject\MyProject.gdb"

# Create the geodatabase if it doesn't exist
if not arcpy.Exists(gdb_path):
    arcpy.management.CreateFileGDB(os.path.dirname(gdb_path),
                                   os.path.basename(gdb_path))

# Open the ArcGIS Pro project and the first map
aprx = arcpy.mp.ArcGISProject(project_path)
map_obj = aprx.listMaps()[0]

# --------------------------------------------------------------------
# A. LOAD NYC ORTHOPHOTO LAYER
# --------------------------------------------------------------------
orthophoto_url = "https://tiles.arcgis.com/tiles/yG5s3afENB5iO9fj/arcgis/rest/services/NYC_Orthos_2024/MapServer"
map_obj.addDataFromPath(orthophoto_url)
print("A. Added NYC Orthophoto layer")

# --------------------------------------------------------------------
# B. ADD VECTOR LAYERS
# --------------------------------------------------------------------
# 1. Buildings
buildings_url = ("https://services2.arcgis.com/IsDCghZ73NgoYoz5/ArcGIS/rest/services/"
                 "NYC_Building_Footprint/FeatureServer/0")
buildings_layer = arcpy.management.MakeFeatureLayer(buildings_url, "Buildings_NYC").getOutput(0)

# 2. Roads
roads_url = ("https://services5.arcgis.com/GfwWNkhOj9bNBqoJ/ArcGIS/rest/services/"
             "DCM_Street_Center_Line/FeatureServer/0")
roads_layer = arcpy.management.MakeFeatureLayer(roads_url, "Roads_NYC").getOutput(0)

map_obj.addLayer(buildings_layer)
map_obj.addLayer(roads_layer)
print("B. Added Buildings and Roads layers")

# --------------------------------------------------------------------
# C. APPLY QUERIES
# --------------------------------------------------------------------
# 1. Buildings > 500 ft
arcpy.management.SelectLayerByAttribute(buildings_layer, "NEW_SELECTION", "HEIGHTROOF > 500")

# 2. Roads in Manhattan
arcpy.management.SelectLayerByAttribute(roads_layer, "NEW_SELECTION", "Borough = 'Manhattan'")
print("C. Queries applied")

# --------------------------------------------------------------------
# D. IDENTIFY-ON-CLICK
# --------------------------------------------------------------------
# ArcGIS Pro automatically supports identify-on-click
print("D. Identify-on-click is available in ArcGIS Pro")

# --------------------------------------------------------------------
# E. EXPORT FILTERED FEATURES AND ADD TO MAP
# --------------------------------------------------------------------
tall_bldgs_output = os.path.join(gdb_path, "Tallest_Buildings_In_NYC")
roads_manh_output = os.path.join(gdb_path, "Roads_In_Manhattan")

# Delete existing outputs if they exist
for out in [tall_bldgs_output, roads_manh_output]:
    if arcpy.Exists(out):
        arcpy.management.Delete(out)

# 1. Export selected buildings
arcpy.management.SelectLayerByAttribute(buildings_layer, "NEW_SELECTION", "HEIGHTROOF > 500")
arcpy.management.CopyFeatures(buildings_layer, tall_bldgs_output)
map_obj.addDataFromPath(tall_bldgs_output)
print(f"E1. Exported and added '{tall_bldgs_output}' to map")

# 2. Export selected roads
arcpy.management.SelectLayerByAttribute(roads_layer, "NEW_SELECTION", "Borough = 'Manhattan'")
arcpy.management.CopyFeatures(roads_layer, roads_manh_output)
map_obj.addDataFromPath(roads_manh_output)
print(f"E2. Exported and added '{roads_manh_output}' to map")

# Clear selections
arcpy.management.SelectLayerByAttribute(buildings_layer, "CLEAR_SELECTION")
arcpy.management.SelectLayerByAttribute(roads_layer, "CLEAR_SELECTION")

# --------------------------------------------------------------------
# SAVE PROJECT
# --------------------------------------------------------------------
aprx.save()
print("✔ All tasks A → E complete. Orthophoto, vector layers, filtered exports added to map.")
