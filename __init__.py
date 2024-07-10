bl_info = {
    "name": "Auto EXR Pass Setup",
    "blender": (3, 6, 0),
    "category": "Render",
    "version": (1, 2, 0),
    "author": "SeeSeal & Bhavish",
}

import bpy
import os
from .updater import check_for_update
from .ui import AutoEXRPassSetupPanel, AutoEXRPassSetupErrorOperator, RENDER_OT_auto_exr_pass_setup

def render_filepath_set(scene):
    try:
        blend_file_dir = bpy.path.abspath('//')
        renders_folder = os.path.join(blend_file_dir, "Renders")
        os.makedirs(renders_folder, exist_ok=True)

        blend_file_name = bpy.path.display_name_from_filepath(bpy.data.filepath)
        blend_file_path = os.path.join(renders_folder, blend_file_name)
        os.makedirs(blend_file_path, exist_ok=True)

        scene_name = scene.name
        scene_path = os.path.join(blend_file_path, scene_name)
        os.makedirs(scene_path, exist_ok=True)

        # Set render output filepath to scene directory with "####" for frame numbering
        scene.render.filepath = os.path.join(scene_path, "####")

        # Set render output file format to EXR
        scene.render.image_settings.file_format = 'OPEN_EXR_MULTILAYER'
        scene.render.image_settings.exr_codec = 'DWAA'
    except PermissionError:
        bpy.ops.render.auto_exr_pass_setup_error('INVOKE_DEFAULT')

def auto_exr_pass_setup():
    # Get the current scene
    scene = bpy.context.scene

    # Ensure nodes are used in the compositor
    scene.use_nodes = True
    tree = scene.node_tree

    # Clear existing nodes
    tree.nodes.clear()

    # Enable Denoising Data Pass
    bpy.context.view_layer.cycles.denoising_store_passes = True

    # Add Render Layers node
    render_layers_node = tree.nodes.new(type='CompositorNodeRLayers')
    render_layers_node.location = (0, 0)

    # Add Composite node
    composite_node = tree.nodes.new(type='CompositorNodeComposite')
    composite_node.location = (400, 0)

    # Link nodes
    tree.links.new(render_layers_node.outputs['Image'], composite_node.inputs['Image'])

classes = (AutoEXRPassSetupPanel, AutoEXRPassSetupErrorOperator, RENDER_OT_auto_exr_pass_setup)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.app.handlers.render_init.append(render_filepath_set)
    bpy.app.timers.register(check_for_update, first_interval=86400, persistent=True)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
    bpy.app.handlers.render_init.remove(render_filepath_set)
    bpy.app.timers.unregister(check_for_update)

if __name__ == "__main__":
    register()
