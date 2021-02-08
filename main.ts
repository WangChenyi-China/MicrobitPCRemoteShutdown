IrRemote.onPressEvent(remotebutton.Ok, function () {
    basic.pause(500)
    sensors.actuator_relay(DigitalPin.P1, on_off._on)
    ddon()
    basic.pause(100)
    sensors.actuator_relay(DigitalPin.P1, on_off._off)
})
IrRemote.onPressEvent(remotebutton.Down, function () {
    ddon()
    basic.pause(100)
    ddon()
    sensors.actuator_relay(DigitalPin.P1, on_off._on)
    basic.pause(5000)
    sensors.actuator_relay(DigitalPin.P1, on_off._off)
})
function ddon () {
    sensors.actuator_buzzer0(DigitalPin.P2, on_off._on)
    basic.pause(100)
    sensors.actuator_buzzer0(DigitalPin.P2, on_off._off)
}
IrRemote.IrRemote_init(Pins.P0)
pins.analogWritePin(AnalogPin.P8, 1023)
