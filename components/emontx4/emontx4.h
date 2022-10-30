#pragma once

#include "esphome/core/component.h"
#include "esphome/components/sensor/sensor.h"
#include "esphome/components/uart/uart.h"
#include "esphome/components/json/json_util.h"
#include "esphome/core/automation.h"

namespace esphome {
namespace emontx4 {

class Emontx4Component : public Component, public uart::UARTDevice {
  public:
    void set_message_number_sensor(sensor::Sensor *message_number_sensor) { message_number_sensor_ = message_number_sensor; }
    void set_vrms_sensor(sensor::Sensor *vrms_sensor) { vrms_sensor_ = vrms_sensor; }
    void set_p1_sensor(sensor::Sensor *p1_sensor) { p1_sensor_ = p1_sensor; }
    void set_p2_sensor(sensor::Sensor *p2_sensor) { p2_sensor_ = p2_sensor; }
    void set_p3_sensor(sensor::Sensor *p3_sensor) { p3_sensor_ = p3_sensor; }
    void set_p4_sensor(sensor::Sensor *p4_sensor) { p4_sensor_ = p4_sensor; }
    void set_p5_sensor(sensor::Sensor *p5_sensor) { p5_sensor_ = p5_sensor; }
    void set_p6_sensor(sensor::Sensor *p6_sensor) { p6_sensor_ = p6_sensor; }
    void set_p7_sensor(sensor::Sensor *p7_sensor) { p7_sensor_ = p7_sensor; }
    void set_p8_sensor(sensor::Sensor *p8_sensor) { p8_sensor_ = p8_sensor; }
    void set_p9_sensor(sensor::Sensor *p9_sensor) { p9_sensor_ = p9_sensor; }
    void set_p10_sensor(sensor::Sensor *p10_sensor) { p10_sensor_ = p10_sensor; }
    void set_p11_sensor(sensor::Sensor *p11_sensor) { p11_sensor_ = p11_sensor; }
    void set_p12_sensor(sensor::Sensor *p12_sensor) { p12_sensor_ = p12_sensor; }
    void set_e1_sensor(sensor::Sensor *e1_sensor) { e1_sensor_ = e1_sensor; }
    void set_e2_sensor(sensor::Sensor *e2_sensor) { e2_sensor_ = e2_sensor; }
    void set_e3_sensor(sensor::Sensor *e3_sensor) { e3_sensor_ = e3_sensor; }
    void set_e4_sensor(sensor::Sensor *e4_sensor) { e4_sensor_ = e4_sensor; }
    void set_e5_sensor(sensor::Sensor *e5_sensor) { e5_sensor_ = e5_sensor; }
    void set_e6_sensor(sensor::Sensor *e6_sensor) { e6_sensor_ = e6_sensor; }
    void set_e7_sensor(sensor::Sensor *e7_sensor) { e7_sensor_ = e7_sensor; }
    void set_e8_sensor(sensor::Sensor *e8_sensor) { e8_sensor_ = e8_sensor; }
    void set_e9_sensor(sensor::Sensor *e9_sensor) { e9_sensor_ = e9_sensor; }
    void set_e10_sensor(sensor::Sensor *e10_sensor) { e10_sensor_ = e10_sensor; }
    void set_e11_sensor(sensor::Sensor *e11_sensor) { e11_sensor_ = e11_sensor; }
    void set_e12_sensor(sensor::Sensor *e12_sensor) { e12_sensor_ = e12_sensor; }
    void set_pulse_count_sensor(sensor::Sensor *pulse_count_sensor) { pulse_count_sensor_ = pulse_count_sensor; }
    void set_pulse_energy_sensor(sensor::Sensor *pulse_energy_sensor) { pulse_energy_sensor_ = pulse_energy_sensor; }
    void set_t1_sensor(sensor::Sensor *t1_sensor) { t1_sensor_ = t1_sensor; }
    void set_t2_sensor(sensor::Sensor *t2_sensor) { t2_sensor_ = t2_sensor; }
    void set_t3_sensor(sensor::Sensor *t3_sensor) { t3_sensor_ = t3_sensor; }

    Trigger<> *get_done_trigger() const;
    // Trigger<> *get_done_trigger() const { return done_trigger_; }

    void dump_config() override;
    // void setup() override;
    void loop() override;

    float get_setup_priority() const { return setup_priority::DATA; }

  protected:
    void parse_json_data_();

    void handle_char_(uint8_t c);
    Trigger<> *done_trigger_;
    // Trigger<> *done_trigger_ = new Trigger<>();

    std::vector<uint8_t> rx_message_;
    std::string json_string_;

    sensor::Sensor *message_number_sensor_{nullptr};
    sensor::Sensor *vrms_sensor_{nullptr};
    sensor::Sensor *p1_sensor_{nullptr};
    sensor::Sensor *p2_sensor_{nullptr};
    sensor::Sensor *p3_sensor_{nullptr};
    sensor::Sensor *p4_sensor_{nullptr};
    sensor::Sensor *p5_sensor_{nullptr};
    sensor::Sensor *p6_sensor_{nullptr};
    sensor::Sensor *p7_sensor_{nullptr};
    sensor::Sensor *p8_sensor_{nullptr};
    sensor::Sensor *p9_sensor_{nullptr};
    sensor::Sensor *p10_sensor_{nullptr};
    sensor::Sensor *p11_sensor_{nullptr};
    sensor::Sensor *p12_sensor_{nullptr};
    sensor::Sensor *e1_sensor_{nullptr};
    sensor::Sensor *e2_sensor_{nullptr};
    sensor::Sensor *e3_sensor_{nullptr};
    sensor::Sensor *e4_sensor_{nullptr};
    sensor::Sensor *e5_sensor_{nullptr};
    sensor::Sensor *e6_sensor_{nullptr};
    sensor::Sensor *e7_sensor_{nullptr};
    sensor::Sensor *e8_sensor_{nullptr};
    sensor::Sensor *e9_sensor_{nullptr};
    sensor::Sensor *e10_sensor_{nullptr};
    sensor::Sensor *e11_sensor_{nullptr};
    sensor::Sensor *e12_sensor_{nullptr};
    sensor::Sensor *pulse_count_sensor_{nullptr};
    sensor::Sensor *pulse_energy_sensor_{nullptr};
    sensor::Sensor *t1_sensor_{nullptr};
    sensor::Sensor *t2_sensor_{nullptr};
    sensor::Sensor *t3_sensor_{nullptr};
};

// class Emontx4OnDataTrigger : public Trigger<float> {
//  public:
//   explicit Emontx4OnDataProcess(Number *parent) {
//     parent->add_on_state_callback([this](float value) { this->trigger(value); });
//   }
  // public:
  //   void Emontx4OnDataProcess() { this->trigger();}
  // };
}  // namespace emontx4
}  // namespace esphome