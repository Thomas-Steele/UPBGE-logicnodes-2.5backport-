from ..node import node_type
from ..node import LogicNodeParameterType
from ...sockets import NodeSocketLogicParameter
from ...sockets import NodeSocketLogicNodeGroupNode
from ...sockets import NodeSocketLogicGeometryNodeTree
from ...sockets import NodeSocketLogicString


@node_type
class LogicNodeGetGeoNodeAttr(LogicNodeParameterType):
    bl_idname = "NLGetGeometryNodeAttribute"
    bl_label = "Get Node Value"
    bl_icon = 'DRIVER_TRANSFORM'
    nl_category = 'Nodes'
    nl_subcat = 'Geometry'
    nl_module = 'parameters'

    def init(self, context):
        LogicNodeParameterType.init(self, context)
        self.add_input(NodeSocketLogicGeometryNodeTree, 'Tree')
        self.add_input(NodeSocketLogicNodeGroupNode, 'Node Name')
        self.add_input(NodeSocketLogicString, "Internal")
        self.add_input(NodeSocketLogicString, "Attribute")
        self.add_output(NodeSocketLogicParameter, "Value")
        self.update_draw()

    def update_draw(self):
        if len(self.inputs) < 4:
            return
        tree = self.inputs[0]
        nde = self.inputs[1]
        itl = self.inputs[2]
        att = self.inputs[3]
        if (tree.value or tree.is_linked) and (nde.value or nde.is_linked):
            itl.enabled = att.enabled = True
        else:
            itl.enabled = att.enabled = False

    def get_netlogic_class_name(self):
        return "ULGetNodeAttribute"

    def get_input_names(self):
        return ["tree_name", 'node_name', "internal", 'attribute']

    def get_output_names(self):
        return ['OUT']
