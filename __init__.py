bl_info = {
    "name": "My Custom Addon",
    "blender": (2, 80, 0),
    "category": "Object",
    "version": (1, 0, 0),
    "location": "3D View > Tool Shelf",
    "description": "An addon that creates a cube and auto-updates",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "support": "COMMUNITY",
}

import bpy
from .updater import check_for_update
from .ui import UpdateNotifierPanel, OBJECT_OT_add_cube

classes = (UpdateNotifierPanel, OBJECT_OT_add_cube)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.app.timers.register(check_for_update, first_interval=86400, persistent=True)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
    bpy.app.timers.unregister(check_for_update)

if __name__ == "__main__":
    register()
