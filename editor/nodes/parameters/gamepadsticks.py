from ..node import node_type
from ..node import LogicNodeParameterType
from ...sockets import NodeSocketLogicBoolean
from ...sockets import NodeSocketLogicIntegerPositiveCent
from ...sockets import NodeSocketLogicFloatPositive
from ...sockets import NodeSocketLogicVectorXYZ
from ...sockets import NodeSocketLogicFloat
from ...enum_types import _enum_controller_stick_operators
from bpy.props import EnumProperty


@node_type
class LogicNodeGamepadSticks(LogicNodeParameterType):
    bl_idname = "NLGamepadSticksCondition"
    bl_label = "Gamepad Sticks"
    nl_module = 'parameters'

    axis: EnumProperty(
        name='Axis',
        items=_enum_controller_stick_operators,
        description="Gamepad Sticks"
    )

    def init(self, context):
        self.add_input(NodeSocketLogicBoolean, 'Inverted')
        self.add_input(NodeSocketLogicIntegerPositiveCent, 'Index')
        self.add_input(NodeSocketLogicFloatPositive, 'Sensitivity', {'value': 1.0})
        self.add_input(NodeSocketLogicFloatPositive, 'Threshold', {'value': 0.05})
        self.add_output(NodeSocketLogicFloat, "X", {'enabled': False})
        self.add_output(NodeSocketLogicFloat, "Y", {'enabled': False})
        self.add_output(NodeSocketLogicVectorXYZ, "Vector")
        LogicNodeParameterType.init(self, context)

    def draw_buttons(self, context, layout):
        layout.prop(self, "axis", text='')

    nl_class = "ULGamepadSticks"

    def get_input_names(self):
        return ['inverted', "index", 'sensitivity', 'threshold']

    def get_output_names(self):
        return ["X", "Y", "VEC"]

    def get_attributes(self):
        return [
            ("axis", f'{self.axis}')
        ]
