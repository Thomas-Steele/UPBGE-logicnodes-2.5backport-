from .socket import NodeSocketLogic
from .socket import PARAMETER_SOCKET_COLOR
from .socket import socket_type
from .socket import update_draw
from bpy.types import NodeSocket
from bpy.props import BoolProperty
import bpy


@socket_type
class NodeSocketLogicXYZ(NodeSocket, NodeSocketLogic):
    bl_idname = "NLXYZSocket"
    bl_label = "Boolean"

    x: BoolProperty(update=update_draw, default=True)
    y: BoolProperty(update=update_draw, default=True)
    z: BoolProperty(update=update_draw, default=True)

    color = PARAMETER_SOCKET_COLOR

    def draw(self, context, layout, node, text):
        if self.is_linked or self.is_output:
            layout.label(text=text)
        else:
            row = layout.row()
            row.prop(self, 'x', text="X")
            row.prop(self, 'y', text="Y")
            row.prop(self, 'z', text="Z")

    def get_unlinked_value(self):
        return "dict(x={}, y={}, z={})".format(self.x, self.y, self.z)
