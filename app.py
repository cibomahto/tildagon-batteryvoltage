import app

import machine
import bq25895
from events.input import Buttons, BUTTON_TYPES

class BatteryVoltage(app.App):
    def __init__(self):
        self.button_states = Buttons(self)

    def update(self, delta):
        if self.button_states.get(BUTTON_TYPES["CANCEL"]):
            # The button_states do not update while you are in the background.
            # Calling clear() ensures the next time you open the app, it stays open.
            # Without it the app would close again immediately.
            self.button_states.clear()
            self.minimise()

    def draw(self, ctx):
        voltage = bq25895.bq25895(machine.I2C(7)).get_Vbat()

        ctx.save()
        ctx.rgb(0.2,0,0).rectangle(-120,-120,240,240).fill()
        ctx.rgb(1,0,0).move_to(-80,0).text(f"voltage:{voltage:.2f}V")
        ctx.restore()

__app_export__ = BatteryVoltage
