from pathlib import Path

import bpy

__all__: list[str] = [
    "QuickExportOperator",
    "OpenExportOperator",
]


class QuickExportOperator(bpy.types.Operator):
    bl_idname: str = "outliner.obj_export"
    bl_label: str = "Batch export OBJ"
    bl_description: str = "Export selected as OBJ with modifiers applied and without materials, skips non meshes."

    @classmethod
    def poll(cls: type["QuickExportOperator"], context: bpy.types.Context) -> bool:
        return bool(context.selected_objects)

    def execute(self, context: bpy.types.Context) -> set[str]:
        if bpy.data.filepath == "":
            self.report({"ERROR"}, "Save the file first!")
            return {"FINISHED"}

        directory: Path = Path(bpy.data.filepath).parent / "export" / "obj"
        directory.mkdir(exist_ok=True, parents=True)

        obj_active: bpy.types.Object = context.active_object
        selected_objects: list[bpy.types.Object] = list(context.selected_objects)
        # Deselect all objects and export them one by one
        bpy.ops.object.select_all(action="DESELECT")
        for obj in selected_objects:
            if obj.type != "MESH":
                self.report({"WARNING"}, f"Skipping {obj.name}, not a mesh.")
                continue

            obj.select_set(True)
            self.report({"INFO"}, f"Exporting {obj.name}")
            file_path: str = str(directory / f"{context.active_object.name}.obj")
            bpy.ops.wm.obj_export(
                filepath=file_path,
                apply_modifiers=True,
                export_selected_objects=True,
                export_materials=False,
            )
            self.report({"INFO"}, f"Exported to {file_path}")
            obj.select_set(False)

        context.view_layer.objects.active = obj_active
        for obj in selected_objects:
            obj.select_set(True)

        return {"FINISHED"}


class OpenExportOperator(bpy.types.Operator):
    bl_idname: str = "outliner.open_export_dir"
    bl_label: str = "Reveal in File Explorer"
    bl_description: str = "Opens the export directory in the file explorer, if it exists."

    @classmethod
    def poll(cls: type["OpenExportOperator"], context: bpy.types.Context) -> bool:
        return context.active_object is not None and context.active_object.type == "MESH"

    def execute(self, _context: bpy.types.Context) -> set[str]:
        if bpy.data.filepath == "":
            self.report({"ERROR"}, "Save the file first!")
            return {"FINISHED"}

        directory: Path = Path(bpy.data.filepath).parent / "export" / "obj"
        if directory.exists():
            bpy.ops.wm.path_open(filepath=str(directory))
        else:
            self.report({"ERROR"}, f"Directory {directory} does not exist.")

        return {"FINISHED"}
