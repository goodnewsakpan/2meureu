from kivy.factory import Factory

register = Factory.register


def register_factory():
    register("CoverImage", module="Components.frame")
    register("RealRecycleView", module="Components.scrollview")
    register("TextField", module="Components.textfield")
    register("TagTextField", module="Components.textfield")
    register("TabsBar", module="Components.tab")
    register("TabsItem", module="Components.tab")
    register("TabsItemText", module="Components.tab")
    register("TrailingPressedIconButton", module="Components.list")
    register("PieChart", module="Components.charts")
    register("LineChart", module="Components.charts")
    register("BarChart", module="Components.charts")
    register("DrawTools", module="Components.drawtools")
    register("GridMagnifier", module="Components.canvas")
    register("GridCanvas", module="Components.canvas")
