# ESPHome Component for EmonTX4

## Basic Configuration

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
    p1:
      id: p1
      name: Kitchen Power
    e1:
      id:e1
      name: Kitchen Energy
```

The following sensors are currently available

```
message_number
vrms
pN -- where N is 1-12
eN -- where N is 1-12
pulse_count
pulse_energy
tN -- where N is 1-3
```
