from ..node import node_type
from ..node import LogicNodeActionType
from ...sockets import NodeSocketLogicCondition
from ...sockets import NodeSocketLogicObject
from ...sockets import NodeSocketLogicIntegerPositive
from ...sockets import NodeSocketLogicBoolean
from ...sockets import NodeSocketLogicFloat
from ...enum_types import _enum_vehicle_axis
from bpy.props import EnumProperty


@node_type
class LoigcNodeVehicleSetAttributes(LogicNodeActionType):
    bl_idname = "NLVehicleSetAttributes"
    bl_label = "Set Attributes"
    nl_category = "Physics"
    nl_subcat = 'Vehicle'
    nl_module = 'actions'
    nl_class = "ULVehicleSetAttributes"

    search_tags = [
        ['Set Vehicle Attributes', {}]
    ]

    def update_draw(self, context=None):
        self.inputs[2].enabled = self.value_type != 'ALL'
        ipts = self.inputs
        ipts[4].enabled = ipts[3].value
        ipts[6].enabled = ipts[5].value
        ipts[8].enabled = ipts[7].value
        ipts[10].enabled = ipts[9].value

    value_type: EnumProperty(
        name='Axis',
        items=_enum_vehicle_axis,
        update=update_draw
    )

    def init(self, context):
        self.add_input(NodeSocketLogicCondition, "Condition")
        self.add_input(NodeSocketLogicObject, "Collider")
        self.add_input(NodeSocketLogicIntegerPositive, "Wheels", {'value': 2})
        self.add_input(NodeSocketLogicBoolean, "Suspension")
        self.add_input(NodeSocketLogicFloat, "")
        self.add_input(NodeSocketLogicBoolean, "Stiffness")
        self.add_input(NodeSocketLogicFloat, "")
        self.add_input(NodeSocketLogicBoolean, "Damping")
        self.add_input(NodeSocketLogicFloat, "")
        self.add_input(NodeSocketLogicBoolean, "Friction")
        self.add_input(NodeSocketLogicFloat, "")
        self.add_output(NodeSocketLogicCondition, 'Done')
        LogicNodeActionType.init(self, context)

    def get_output_names(self):
        return ["OUT"]

    def draw_buttons(self, context, layout):
        layout.prop(self, "value_type", text='')

    def get_input_names(self):
        return [
            "condition",
            "vehicle",
            "wheelcount",
            'set_suspension_compression',
            'suspension_compression',
            'set_suspension_stiffness',
            'suspension_stiffness',
            'set_suspension_damping',
            'suspension_damping',
            'set_tyre_friction',
            'tyre_friction'
        ]

    def get_attributes(self):
        return [
            ("value_type", f'"{self.value_type}"'),
        ]
