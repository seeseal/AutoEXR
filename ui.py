import bpy

class OBJECT_OT_add_cube(bpy.types.Operator):
    bl_idname = "mesh.add_cube"
    bl_label = "Add Cube"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.mesh.primitive_cube_add(size=2, enter_editmode=False, align='WORLD', location=(0, 0, 0))
        return {'FINISHED'}

class UpdateNotifierPanel(bpy.types.Panel):
    bl_label = "Update Notifier"
    bl_idname = "VIEW3D_PT_update_notifier"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Tool'

    def draw(self, context):
        layout = self.layout
        layout.operator("mesh.add_cube", text="Add Cube")
