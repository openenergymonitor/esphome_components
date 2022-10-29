# ESPHome Component for EmonTX4

## Basic Configuration

```
external_components:
  - source:
      type: git
      url: https://github.com/borpin/esphome_components
      # ref: bpo-dev # for the latest version but that might break things!
    components: [ emontx4 ]
    refresh: 0s # ensure a fresh pull from GitHub

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
    message_number:
      id: msg
      name: Message Number
    p1_power:
      id: p1
      name: Kitchen Power
    e1_energy:
      id:e1
      name: Kitchen Energy
```

The following sensors are currently available

```
message_number
vrms
p1_power
p2_power
p3_power
e1_energy
e2_energy
e3_energy
```
