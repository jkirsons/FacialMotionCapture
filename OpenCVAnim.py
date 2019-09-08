import bpy


class OBJECT_MT_OpenCVPanel(bpy.types.WorkSpaceTool):
    """Creates a Panel in the Object properties window"""
    bl_label = "OpenCV Animation"
    bl_space_type = 'VIEW_3D'
    bl_context_mode='OBJECT'
        
    #bl_region_type = 'TOOLS'
    bl_idname = "ui_plus.opencv"
    #bl_context = "object"
    bl_options = {'REGISTER'}

    bl_icon = "ops.generic.select_circle"

        
    def draw_settings(context, layout, tool):

        row = layout.row()
        op = row.operator("wm.opencv_operator", text="Capture", icon="OUTLINER_OB_CAMERA")
        
        #props = tool.operator_properties("wm.opencv_operator")
        #layout.prop(props, "stop", text="Stop Capture")
        #layout.prop(tool.op, "stop", text="Stop Capture")

def register():
    #bpy.utils.register_class(OBJECfT_MT_OpenCVPanel)
    #bpy.types.VIEW3D_PT_tools_active.prepend(OBJECT_MT_OpenCVPanel.draw)  # << add menu above
    bpy.utils.register_tool(OBJECT_MT_OpenCVPanel, separator=True, group=True)

def unregister():
    #bpy.types.VIEW3D_PT_tools_active.remove(OBJECT_MT_OpenCVPanel.draw)
    #bpy.utils.unregister_class(OBJECT_MT_OpenCVPanel)
    bpy.utils.unregister_tool(OBJECT_MT_OpenCVPanel)

if __name__ == "__main__":
    register()
