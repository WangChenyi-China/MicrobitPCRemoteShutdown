def on_press_ok():
    basic.pause(500)
    sensors.actuator_relay(DigitalPin.P1, on_off._ON)
    ddon()
    basic.pause(100)
    sensors.actuator_relay(DigitalPin.P1, on_off._OFF)
IrRemote.on_press_event(remotebutton.OK, on_press_ok)

def on_press_down():
    ddon()
    basic.pause(100)
    ddon()
    sensors.actuator_relay(DigitalPin.P1, on_off._ON)
    basic.pause(5000)
    sensors.actuator_relay(DigitalPin.P1, on_off._OFF)
IrRemote.on_press_event(remotebutton.DOWN, on_press_down)

def ddon():
    sensors.actuator_buzzer0(DigitalPin.P2, on_off._ON)
    basic.pause(100)
    sensors.actuator_buzzer0(DigitalPin.P2, on_off._OFF)
IrRemote.IrRemote_init(Pins.P0)
pins.analog_write_pin(AnalogPin.P8, 1023)