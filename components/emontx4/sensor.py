import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import sensor, uart, json
from esphome import automation
from esphome.const import (
    CONF_ID,
    UNIT_VOLT,
    UNIT_WATT,
    UNIT_CELSIUS,
    UNIT_EMPTY,
    UNIT_WATT_HOURS,
    UNIT_PULSES,
    ICON_CURRENT_AC,
    ICON_FLASH,
    ICON_THERMOMETER,
    ICON_PERCENT,
    ICON_EMPTY,
    ICON_PULSE,
    DEVICE_CLASS_VOLTAGE,
    DEVICE_CLASS_POWER,
    DEVICE_CLASS_ENERGY,
    DEVICE_CLASS_TEMPERATURE,
    DEVICE_CLASS_EMPTY,
    STATE_CLASS_MEASUREMENT,
    STATE_CLASS_TOTAL_INCREASING,
    CONF_TRIGGER_ID,
)

    # UNIT_PULSES,


DEPENDENCIES = ["uart"]
AUTO_LOAD = ["json"]

emontx4_ns = cg.esphome_ns.namespace("emontx4")
Emontx4Component = emontx4_ns.class_("Emontx4Component", uart.UARTDevice, cg.Component)

# Emontx4OnDataTrigger = emontx4_ns.class_(
#     "Emontx4OnDataTrigger", automation.Trigger.template()
# )

CONF_MSG_NUMBER = "message_number"
CONF_VRMS = "vrms"
CONF_P1 = "p1"
CONF_P2 = "p2"
CONF_P3 = "p3"
CONF_P4 = "p4"
CONF_P5 = "p5"
CONF_P6 = "p6"
CONF_P7 = "p7"
CONF_P8 = "p8"
CONF_P9 = "p9"
CONF_P10 = "p10"
CONF_P11 = "p11"
CONF_P12 = "p12"
CONF_E1 = "e1"
CONF_E2 = "e2"
CONF_E3 = "e3"
CONF_E4 = "e4"
CONF_E5 = "e5"
CONF_E6 = "e6"
CONF_E7 = "e7"
CONF_E8 = "e8"
CONF_E9 = "e9"
CONF_E10 = "e10"
CONF_E11 = "e11"
CONF_E12 = "e12"
CONF_PULSE_COUNT = "pulse count"
CONF_PULSE_ENERGY = "pulse energy"
CONF_T1 = "t1"
CONF_T2 = "t2"
CONF_T3 = "t3"
CONF_ON_DATA = "on_data"

CONFIG_SCHEMA = (
    cv.Schema(
        {
            cv.GenerateID(): cv.declare_id(Emontx4Component),
            cv.Optional(CONF_ON_DATA): automation.validate_automation(single=True),
            # cv.Optional(CONF_ON_DATA): automation.validate_automation(
            #         {
            #             cv.GenerateID(CONF_TRIGGER_ID): cv.declare_id(Emontx4OnDataTrigger),
            #         }
            # ),
            cv.Optional(CONF_MSG_NUMBER): sensor.sensor_schema(
                unit_of_measurement=UNIT_EMPTY,
                # icon=ICON_EMPTY,
                accuracy_decimals=0,
            ),
            cv.Optional(CONF_VRMS): sensor.sensor_schema(
                unit_of_measurement=UNIT_VOLT,
                device_class=DEVICE_CLASS_VOLTAGE,
                state_class=STATE_CLASS_MEASUREMENT,
                accuracy_decimals=1,
            ),
            cv.Optional(CONF_P1): sensor.sensor_schema(
                unit_of_measurement=UNIT_WATT,
                device_class=DEVICE_CLASS_POWER,
                state_class=STATE_CLASS_MEASUREMENT,
                accuracy_decimals=0,
            ),
            cv.Optional(CONF_P2): sensor.sensor_schema(
                unit_of_measurement=UNIT_WATT,
                device_class=DEVICE_CLASS_POWER,
                state_class=STATE_CLASS_MEASUREMENT,
                accuracy_decimals=0,
            ),
            cv.Optional(CONF_P3): sensor.sensor_schema(
                unit_of_measurement=UNIT_WATT,
                device_class=DEVICE_CLASS_POWER,
                state_class=STATE_CLASS_MEASUREMENT,
                accuracy_decimals=0,
            ),
            cv.Optional(CONF_P4): sensor.sensor_schema(
                unit_of_measurement=UNIT_WATT,
                device_class=DEVICE_CLASS_POWER,
                state_class=STATE_CLASS_MEASUREMENT,
                accuracy_decimals=0,
            ),
            cv.Optional(CONF_P5): sensor.sensor_schema(
                unit_of_measurement=UNIT_WATT,
                device_class=DEVICE_CLASS_POWER,
                state_class=STATE_CLASS_MEASUREMENT,
                accuracy_decimals=0,
            ),
            cv.Optional(CONF_P6): sensor.sensor_schema(
                unit_of_measurement=UNIT_WATT,
                device_class=DEVICE_CLASS_POWER,
                state_class=STATE_CLASS_MEASUREMENT,
                accuracy_decimals=0,
            ),
            cv.Optional(CONF_P7): sensor.sensor_schema(
                unit_of_measurement=UNIT_WATT,
                device_class=DEVICE_CLASS_POWER,
                state_class=STATE_CLASS_MEASUREMENT,
                accuracy_decimals=0,
            ),
            cv.Optional(CONF_P8): sensor.sensor_schema(
                unit_of_measurement=UNIT_WATT,
                device_class=DEVICE_CLASS_POWER,
                state_class=STATE_CLASS_MEASUREMENT,
                accuracy_decimals=0,
            ),
            cv.Optional(CONF_P9): sensor.sensor_schema(
                unit_of_measurement=UNIT_WATT,
                device_class=DEVICE_CLASS_POWER,
                state_class=STATE_CLASS_MEASUREMENT,
                accuracy_decimals=0,
            ),
            cv.Optional(CONF_P10): sensor.sensor_schema(
                unit_of_measurement=UNIT_WATT,
                device_class=DEVICE_CLASS_POWER,
                state_class=STATE_CLASS_MEASUREMENT,
                accuracy_decimals=0,
            ),
            cv.Optional(CONF_P11): sensor.sensor_schema(
                unit_of_measurement=UNIT_WATT,
                device_class=DEVICE_CLASS_POWER,
                state_class=STATE_CLASS_MEASUREMENT,
                accuracy_decimals=0,
            ),
            cv.Optional(CONF_P12): sensor.sensor_schema(
                unit_of_measurement=UNIT_WATT,
                device_class=DEVICE_CLASS_POWER,
                state_class=STATE_CLASS_MEASUREMENT,
                accuracy_decimals=0,
            ),
            cv.Optional(CONF_E1): sensor.sensor_schema(
                unit_of_measurement=UNIT_WATT_HOURS,
                device_class=DEVICE_CLASS_ENERGY,
                state_class=STATE_CLASS_TOTAL_INCREASING,
                accuracy_decimals=0,
            ),
            cv.Optional(CONF_E2): sensor.sensor_schema(
                unit_of_measurement=UNIT_WATT_HOURS,
                device_class=DEVICE_CLASS_ENERGY,
                state_class=STATE_CLASS_TOTAL_INCREASING,
                accuracy_decimals=0,
            ),
            cv.Optional(CONF_E3): sensor.sensor_schema(
                unit_of_measurement=UNIT_WATT_HOURS,
                device_class=DEVICE_CLASS_ENERGY,
                state_class=STATE_CLASS_TOTAL_INCREASING,
                accuracy_decimals=0,
            ),
            cv.Optional(CONF_E4): sensor.sensor_schema(
                unit_of_measurement=UNIT_WATT_HOURS,
                device_class=DEVICE_CLASS_ENERGY,
                state_class=STATE_CLASS_TOTAL_INCREASING,
                accuracy_decimals=0,
            ),
            cv.Optional(CONF_E5): sensor.sensor_schema(
                unit_of_measurement=UNIT_WATT_HOURS,
                device_class=DEVICE_CLASS_ENERGY,
                state_class=STATE_CLASS_TOTAL_INCREASING,
                accuracy_decimals=0,
            ),
            cv.Optional(CONF_E6): sensor.sensor_schema(
                unit_of_measurement=UNIT_WATT_HOURS,
                device_class=DEVICE_CLASS_ENERGY,
                state_class=STATE_CLASS_TOTAL_INCREASING,
                accuracy_decimals=0,
            ),
            cv.Optional(CONF_E7): sensor.sensor_schema(
                unit_of_measurement=UNIT_WATT_HOURS,
                device_class=DEVICE_CLASS_ENERGY,
                state_class=STATE_CLASS_TOTAL_INCREASING,
                accuracy_decimals=0,
            ),
            cv.Optional(CONF_E8): sensor.sensor_schema(
                unit_of_measurement=UNIT_WATT_HOURS,
                device_class=DEVICE_CLASS_ENERGY,
                state_class=STATE_CLASS_TOTAL_INCREASING,
                accuracy_decimals=0,
            ),
            cv.Optional(CONF_E9): sensor.sensor_schema(
                unit_of_measurement=UNIT_WATT_HOURS,
                device_class=DEVICE_CLASS_ENERGY,
                state_class=STATE_CLASS_TOTAL_INCREASING,
                accuracy_decimals=0,
            ),
            cv.Optional(CONF_E10): sensor.sensor_schema(
                unit_of_measurement=UNIT_WATT_HOURS,
                device_class=DEVICE_CLASS_ENERGY,
                state_class=STATE_CLASS_TOTAL_INCREASING,
                accuracy_decimals=0,
            ),
            cv.Optional(CONF_E11): sensor.sensor_schema(
                unit_of_measurement=UNIT_WATT_HOURS,
                device_class=DEVICE_CLASS_ENERGY,
                state_class=STATE_CLASS_TOTAL_INCREASING,
                accuracy_decimals=0,
            ),
            cv.Optional(CONF_E12): sensor.sensor_schema(
                unit_of_measurement=UNIT_WATT_HOURS,
                device_class=DEVICE_CLASS_ENERGY,
                state_class=STATE_CLASS_TOTAL_INCREASING,
                accuracy_decimals=0,
            ),
            cv.Optional(CONF_PULSE_COUNT): sensor.sensor_schema(
                unit_of_measurement=UNIT_PULSES,
                # ICON_PULSE,
                device_class=DEVICE_CLASS_EMPTY,
                state_class=STATE_CLASS_TOTAL_INCREASING,
                accuracy_decimals=0,
            ),
            cv.Optional(CONF_PULSE_ENERGY): sensor.sensor_schema(
                unit_of_measurement=UNIT_WATT_HOURS,
                device_class=DEVICE_CLASS_ENERGY,
                state_class=STATE_CLASS_TOTAL_INCREASING,
                accuracy_decimals=0,
            ),
            cv.Optional(CONF_T1): sensor.sensor_schema(
                unit_of_measurement=UNIT_CELSIUS,
                device_class=DEVICE_CLASS_TEMPERATURE,
                state_class=STATE_CLASS_MEASUREMENT,
                accuracy_decimals=1,
            ),
            cv.Optional(CONF_T2): sensor.sensor_schema(
                unit_of_measurement=UNIT_CELSIUS,
                device_class=DEVICE_CLASS_TEMPERATURE,
                state_class=STATE_CLASS_MEASUREMENT,
                accuracy_decimals=1,
            ),
            cv.Optional(CONF_T3): sensor.sensor_schema(
                unit_of_measurement=UNIT_CELSIUS,
                device_class=DEVICE_CLASS_TEMPERATURE,
                state_class=STATE_CLASS_MEASUREMENT,
                accuracy_decimals=1,
            ),
        }
    )
    .extend(cv.COMPONENT_SCHEMA)
    .extend(uart.UART_DEVICE_SCHEMA)
)

# FINAL_VALIDATE_SCHEMA = uart.final_validate_device_schema(
#     "cse7766", baud_rate=4800, require_rx=True
# )

async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
    await uart.register_uart_device(var, config)

    if CONF_MSG_NUMBER in config:
        sens = await sensor.new_sensor(config[CONF_MSG_NUMBER])
        cg.add(var.set_message_number_sensor(sens))

    if CONF_VRMS in config:
        sens = await sensor.new_sensor(config[CONF_VRMS])
        cg.add(var.set_vrms_sensor(sens))

    if CONF_P1 in config:
        sens = await sensor.new_sensor(config[CONF_P1])
        cg.add(var.set_p1_sensor(sens))

    if CONF_P2 in config:
        sens = await sensor.new_sensor(config[CONF_P2])
        cg.add(var.set_p2_sensor(sens))

    if CONF_P3 in config:
        sens = await sensor.new_sensor(config[CONF_P3])
        cg.add(var.set_p3_sensor(sens))

    if CONF_P4 in config:
        sens = await sensor.new_sensor(config[CONF_P4])
        cg.add(var.set_p4_sensor(sens))

    if CONF_P5 in config:
        sens = await sensor.new_sensor(config[CONF_P5])
        cg.add(var.set_p5_sensor(sens))

    if CONF_P6 in config:
        sens = await sensor.new_sensor(config[CONF_P6])
        cg.add(var.set_p6_sensor(sens))

    if CONF_P7 in config:
        sens = await sensor.new_sensor(config[CONF_P7])
        cg.add(var.set_p7_sensor(sens))

    if CONF_P8 in config:
        sens = await sensor.new_sensor(config[CONF_P8])
        cg.add(var.set_p8_sensor(sens))

    if CONF_P9 in config:
        sens = await sensor.new_sensor(config[CONF_P9])
        cg.add(var.set_p9_sensor(sens))

    if CONF_P10 in config:
        sens = await sensor.new_sensor(config[CONF_P10])
        cg.add(var.set_p10_sensor(sens))

    if CONF_P11 in config:
        sens = await sensor.new_sensor(config[CONF_P11])
        cg.add(var.set_p11_sensor(sens))

    if CONF_P12 in config:
        sens = await sensor.new_sensor(config[CONF_P12])
        cg.add(var.set_p12_sensor(sens))

    if CONF_E1 in config:
        sens = await sensor.new_sensor(config[CONF_E1])
        cg.add(var.set_e1_sensor(sens))

    if CONF_E2 in config:
        sens = await sensor.new_sensor(config[CONF_E2])
        cg.add(var.set_e2_sensor(sens))

    if CONF_E3 in config:
        sens = await sensor.new_sensor(config[CONF_E3])
        cg.add(var.set_e3_sensor(sens))

    if CONF_E4 in config:
        sens = await sensor.new_sensor(config[CONF_E4])
        cg.add(var.set_e4_sensor(sens))

    if CONF_E5 in config:
        sens = await sensor.new_sensor(config[CONF_E5])
        cg.add(var.set_e5_sensor(sens))

    if CONF_E6 in config:
        sens = await sensor.new_sensor(config[CONF_E6])
        cg.add(var.set_e6_sensor(sens))

    if CONF_E7 in config:
        sens = await sensor.new_sensor(config[CONF_E7])
        cg.add(var.set_e7_sensor(sens))

    if CONF_E8 in config:
        sens = await sensor.new_sensor(config[CONF_E8])
        cg.add(var.set_e8_sensor(sens))

    if CONF_E9 in config:
        sens = await sensor.new_sensor(config[CONF_E9])
        cg.add(var.set_e9_sensor(sens))

    if CONF_E10 in config:
        sens = await sensor.new_sensor(config[CONF_E10])
        cg.add(var.set_e10_sensor(sens))

    if CONF_E11 in config:
        sens = await sensor.new_sensor(config[CONF_E11])
        cg.add(var.set_e11_sensor(sens))

    if CONF_E12 in config:
        sens = await sensor.new_sensor(config[CONF_E12])
        cg.add(var.set_e12_sensor(sens))

    if CONF_PULSE_COUNT in config:
        sens = await sensor.new_sensor(config[CONF_PULSE_COUNT])
        cg.add(var.set_pulse_count_sensor(sens))

    if CONF_PULSE_ENERGY in config:
        sens = await sensor.new_sensor(config[CONF_PULSE_ENERGY])
        cg.add(var.set_pulse_energy_sensor(sens))

    if CONF_T1 in config:
        sens = await sensor.new_sensor(config[CONF_T1])
        cg.add(var.set_t1_sensor(sens))

    if CONF_T2 in config:
        sens = await sensor.new_sensor(config[CONF_T2])
        cg.add(var.set_t2_sensor(sens))

    if CONF_T3 in config:
        sens = await sensor.new_sensor(config[CONF_T3])
        cg.add(var.set_t3_sensor(sens))
    
    # Trigger definition, must be at the end of 'to_code'
    if CONF_ON_DATA in config:
        await automation.build_automation(
            var.get_done_trigger(), [], config[CONF_ON_DATA]
        )


