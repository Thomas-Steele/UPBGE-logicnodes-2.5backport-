from ..node import node_type
from ..node import LogicNodeParameterType
from ...sockets import NodeSocketLogicObject
from ...sockets import NodeSocketLogicString
from ...sockets import NodeSocketLogicParameter
from ...sockets import NodeSocketLogicBrick


@node_type
class LogicNodeGetActuatorValue(LogicNodeParameterType):
    bl_idname = "NLGetActuatorValue"
    bl_label = "Get Actuator Value"
    nl_category = "Logic"
    nl_subcat = 'Bricks'
    nl_module = 'parameters'

    def init(self, context):
        LogicNodeParameterType.init(self, context)
        self.add_input(NodeSocketLogicObject, "Object")
        self.add_input(NodeSocketLogicBrick, "Actuator")
        self.inputs[-1].brick_type = 'actuators'
        self.add_input(NodeSocketLogicString, "Field")
        self.add_output(NodeSocketLogicParameter, "Value")

    def get_netlogic_class_name(self):
        return "ULGetActuatorValue"

    def get_input_names(self):
        return ["game_obj", "act_name", 'field']

    def get_output_names(self):
        return ['OUT']
