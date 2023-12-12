from typing import Any

import bpy

from . import operators, ui

bl_info = {
    "name": "Quick Export",
    "version": (1, 0, 0),
    "author": "juso",
    "blender": (4, 0, 0),
    "category": "Import-Export",
    "location": "Outliner > Object",
    "description": "Quick export as OBJ with modifiers applied.",
}


def draw_menu(self: bpy.types.Menu, _context: bpy.types.Context) -> None:
    layout: bpy.types.UILayout = self.layout
    layout.separator()
    layout.menu(ui.QuickExportMenu.bl_idname)


def register() -> None:
    bpy.utils.register_class(ui.QuickExportMenu)
    for cls in operators.__all__:
        operator: type[bpy.types.Operator] | Any = getattr(operators, cls, None)
        if issubclass(operator, bpy.types.Operator):
            bpy.utils.register_class(operator)
    bpy.types.OUTLINER_MT_object.append(draw_menu)


def unregister() -> None:
    bpy.types.OUTLINER_MT_object.remove(draw_menu)
    bpy.utils.unregister_class(ui.QuickExportMenu)
    for cls in operators.__all__:
        operator: type[bpy.types.Operator] | Any = getattr(operators, cls, None)
        if issubclass(operator, bpy.types.Operator):
            bpy.utils.unregister_class(operator)


if __name__ == "__main__":
    register()
