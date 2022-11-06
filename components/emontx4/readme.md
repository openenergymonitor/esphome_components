# ESPHome Component for EmonTX4

## Basic Configuration

This is not complete, you will need to add the other standard ESPHome components such as `esphome:`, `api:` etc. This is the additional sections to make the emoncms component work.

```
external_components:
  - source:
      type: git
      url: https://github.com/openenergymonitor/esphome_components
      # you can use the dvelopment repo from borpin
      # url: https://github.com/borpin/esphome_components
      # ref: bpo-dev # for the very latest version but that might break things (I'm working in this repo)!
    components: [ emontx4 ]
    refresh: 0s # ensure a fresh pull from GitHub - only required if you think things will have changed.

mqtt:
  broker: xxx.xxx.xxx.xxx
  username: xxxxx
  password: xxxxx
  discovery: false

# Enable logging
logger:
  level: VERBOSE #makes uart stream available in esphome logstream
  baud_rate: 0 #disable logging over uart

uart:
  id: emontx4_uart
  rx_pin: RX
  tx_pin: TX
  baud_rate: 115200

sensor:
  - platform: emontx4
    vrms:
      id: iv
      name: Vrms
      retain: false
    message_number:
      id: msg
      name: Message Number
      retain: false
    p1:
      id: p1
      name: Kitchen Power
      retain: false
    e1:
      id:e1
      name: Kitchen Energy
      retain: false
    on_data: # send a JSON by MQTT if required
      then:
        - mqtt.publish_json:
            topic: emon
            payload: |-
              root["P3"] = id(p3).state;
              root["E3"] = id(e3).state;

```

### MQTT

As setup above, ESPHome by default creates a state topic for each sensor with a base topic name the same as the ESPHome device name.

Adding the `on_data` section means that a single JSON string can be sent to Emoncms (or any other system) and this can be configured independently of the sensors generated for HomeAssistant.

If a sensor is required for Emoncms and not ESPHome, omit the `name` for the sensor such that it is an internal sensor only.

Currently there is no way to *not* send the standard sensor data to MQTT. I have an open issue with ESPHome to enable that.

### Sensors Available

The following sensors are currently available to be configured:

```
message_number
vrms
pN -- where N is 1-12
eN -- where N is 1-12
pulse_count
pulse_energy
tN -- where N is 1-3
```

### TODO

1. Investigate sending via HTTP
2. Test Temperature sensors
3. Test Pulse sensor
4. Scale Pulse sensor (currently assumes 1 flash per Wh)