from arm.logicnode.arm_nodes import *

class PickObjectNode(ArmLogicTreeNode):
    """Picks the rigid body in the given location using the screen
    coordinates (2D).
    
    @seeNode Mask
    
    @input Screen Coords: the location at which to pick, in screen 
        coordinates
    @input Mask: a bit mask value to specify which
        objects are considered
    
    @output RB: the object that was hit
    @output Hit: the hit position in world coordinates
    """
    bl_idname = 'LNPickObjectNode'
    bl_label = 'Pick RB'
    arm_section = 'ray'
    arm_version = 1

    def init(self, context):
        super(PickObjectNode, self).init(context)
        self.add_input('NodeSocketVector', 'Screen Coords')
        self.add_input('NodeSocketInt', 'Mask', default_value=1)

        self.add_output('ArmNodeSocketObject', 'RB')
        self.add_output('NodeSocketVector', 'Hit')
