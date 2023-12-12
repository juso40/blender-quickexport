import bpy

from . import operators


class QuickExportMenu(bpy.types.Menu):
    bl_idname: str = "QUICK_EXPORT_MT_menu"
    bl_label: str = "Quick Export"

    def draw(self, _context: bpy.types.Context) -> None:
        layout: bpy.types.UILayout = self.layout
        layout.operator(operators.QuickExportOperator.bl_idname)
        layout.operator(operators.OpenExportOperator.bl_idname)
