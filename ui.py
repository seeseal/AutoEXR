import bpy
from . import auto_exr_pass_setup

class AutoEXRPassSetupPanel(bpy.types.Panel):
    bl_label = "Auto EXR Pass Setup"
    bl_idname = "RENDER_PT_auto_exr_pass_setup"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Tool'

    def draw(self, context):
        layout = self.layout
        layout.operator("render.auto_exr_pass_setup", text="Setup EXR Passes")

class AutoEXRPassSetupErrorOperator(bpy.types.Operator):
    bl_idname = "render.auto_exr_pass_setup_error"
    bl_label = "Auto EXR Pass Setup Error"

    def execute(self, context):
        self.report({'ERROR'}, "Access is denied: Please save the file in a different location.")
        return {'FINISHED'}

    def invoke(self, context, event):
        self.execute(context)
        return {'FINISHED'}

class RENDER_OT_auto_exr_pass_setup(bpy.types.Operator):
    bl_idname = "render.auto_exr_pass_setup"
    bl_label = "Auto EXR Pass Setup"

    def execute(self, context):
        auto_exr_pass_setup.auto_exr_pass_setup()
        return {'FINISHED'}
