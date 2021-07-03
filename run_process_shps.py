import arcpy

def remove_field(fields, to_remove):
    for field in to_remove:
        fields.remove(field)

shape_filename = "C:\Users\julia\Documents\input\Pontos_super.shp"
fields_to_remove = ["FID", "Shape", "OBJECTID"]
output_surf_root = "C:\Users\julia\Documents\output\out_surface_raster"
kriging_model = "Spherical"
cell_size = 5
search_radius = "Variable 12"

with arcpy.da.SearchCursor(shape_filename, "*") as cursor:
    fields = list(cursor.fields)
    remove_field(fields, fields_to_remove)
    for field in fields:
        output_surf_path = output_surf_root + "\\" + field
        arcpy.Kriging_3d(shape_filename, field, output_surf_path, kriging_model, cell_size, search_radius)