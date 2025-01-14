import os

import bpy
from bpy.props import StringProperty, IntProperty, BoolProperty, IntVectorProperty, EnumProperty, CollectionProperty
from bpy.types import AddonPreferences
from ..config import __addon_name__
from ..properties import ResourcePlan, ResourcePlansInfo, Material, ClassificationBasisl


class CrafterAddonPreferences(AddonPreferences):
    # this must match the add-on name (the folder name of the unzipped file)
    bl_idname = __addon_name__

    # https://docs.blender.org/api/current/bpy.props.html
    # The name can't be dynamically translated during blender programming running as they are defined
    # when the class is registered, i.e. we need to restart blender for the property name to be correctly translated.
#====================希望用户再次打开还能保留的属性【要开自动保存】====================
#==========功能显示属性==========
    Plans: BoolProperty(name="Plans",
                        default=True,)# type: ignore
    Import_World: BoolProperty(name="Import World",
                               default=True,)# type: ignore
    Import_Resources: BoolProperty(name="Import Resources",
                                   default=True,)# type: ignore
    Load_Materials: BoolProperty(name="Load Materials",
                                 default=True,)# type: ignore
#==========导入世界属性==========
    World_Path: StringProperty(name="World path",
                               default="World path",
                               subtype="DIR_PATH",) # type: ignore
    XYZ_1: IntVectorProperty(name="XYZ-1",
                             default=(0,0,0),
                             description="Starting coordinates")# type: ignore
    XYZ_2: IntVectorProperty(name="XYZ-2",
                             default=(0,0,0),
                             description="Ending coordinates")# type: ignore
    solid: IntProperty(name="Solid",
                       default=0,)# type: ignore
#==========导入纹理属性==========
    Texture_Interpolation: EnumProperty(name="Texture Interpolation",
                                        items=[("Linear","Linear","Linear interpolation"),
                                               ("Closest","Closest","No interpolation (sample closest texel)"),
                                               ("Cubic","Cubic","Cubic interpolation"),
                                               ("Smart","Smart","Bicubic when magnifying, else bilinear (OSL only)")],
                                        default="Closest",
                                        description="Texture interpolation method",
                                        update=lambda self, context: self.update_texture_interpolation(context))# type: ignore
    Resources_Plans_List: CollectionProperty(name="Resources Plans",type=ResourcePlan)#type: ignore
    Resources_Plans_List_index: IntProperty(name="Resources Plans index",default=0)# type: ignore
    Resources_Plans_Info_List: CollectionProperty(name="Resources Plans Info",type=ResourcePlansInfo)# type: ignore
    Resources_Plans_Info_List_index: IntProperty(name="Resources Plans Info index",default=0)# type: ignore
#==========加载材质属性==========
    Materials_List: CollectionProperty(name="Materials",type=Material)#type: ignore
    Materials_List_index: IntProperty(name="Materials index",default=0)# type: ignore
    Classification_Basis_List: CollectionProperty(name="Classification Basis",type=ClassificationBasisl)# type: ignore
    Classification_Basis_List_index: IntProperty(name="Classification Basis index",default=0)# type: ignore
#==========偏好设置面板==========
    def draw(self, context: bpy.types.Context):
        layout = self.layout
        layout.prop(self, "Plans")
        layout.prop(self, "Import_World")
        layout.prop(self, "Import_Resources")
        layout.prop(self, "Load_Materials")
#==========修改变量操作==========
    def update_texture_interpolation(self, context):
        bpy.ops.crafter.set_texture_interpolation()
        return None
