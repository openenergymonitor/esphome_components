#include "emontx4.h"
#include "esphome/core/log.h"

namespace esphome {
namespace emontx4 {

static const char *TAG = "emontx4";

bool first_run = false;

void Emontx4Component::dump_config() {
  ESP_LOGCONFIG(TAG, "Emontx4:");
  LOG_SENSOR("  ", "Message Number", message_number_sensor_);
  LOG_SENSOR("  ", "Vrms", vrms_sensor_);
  LOG_SENSOR("  ", "P1", p1_sensor_);
  LOG_SENSOR("  ", "P2", p2_sensor_);
  LOG_SENSOR("  ", "P3", p3_sensor_);
  LOG_SENSOR("  ", "P4", p4_sensor_);
  LOG_SENSOR("  ", "P5", p5_sensor_);
  LOG_SENSOR("  ", "P6", p6_sensor_);
  LOG_SENSOR("  ", "P7", p7_sensor_);
  LOG_SENSOR("  ", "P8", p8_sensor_);
  LOG_SENSOR("  ", "P9", p9_sensor_);
  LOG_SENSOR("  ", "P10", p10_sensor_);
  LOG_SENSOR("  ", "P11", p11_sensor_);
  LOG_SENSOR("  ", "P12", p12_sensor_);
  LOG_SENSOR("  ", "E1", e1_sensor_);
  LOG_SENSOR("  ", "E2", e2_sensor_);
  LOG_SENSOR("  ", "E3", e3_sensor_);
  LOG_SENSOR("  ", "E4", e4_sensor_);
  LOG_SENSOR("  ", "E5", e5_sensor_);
  LOG_SENSOR("  ", "E6", e6_sensor_);
  LOG_SENSOR("  ", "E7", e7_sensor_);
  LOG_SENSOR("  ", "E8", e8_sensor_);
  LOG_SENSOR("  ", "E9", e9_sensor_);
  LOG_SENSOR("  ", "E10", e10_sensor_);
  LOG_SENSOR("  ", "E11", e11_sensor_);
  LOG_SENSOR("  ", "E12", e12_sensor_);
  LOG_SENSOR("  ", "Pulse Count", pulse_count_sensor_);
  LOG_SENSOR("  ", "Pulse Energy", pulse_energy_sensor_);
  LOG_SENSOR("  ", "T1", t1_sensor_);
  LOG_SENSOR("  ", "T2", t2_sensor_);
  LOG_SENSOR("  ", "T3", t3_sensor_);
}

void Emontx4Component::setup() {
  do { } while ( !(this->available()) );
//   if (this->available()) {
    this->write_str("l");
    ESP_LOGD(TAG, "Write list command");
//   }
}

void Emontx4Component::loop() {
    this->write_str("l");
    ESP_LOGD(TAG, "Write list command");

    while (this->available()) {
        uint8_t c;
        this->read_byte(&c);
        this->handle_char_(c);
    }
}

void Emontx4Component::handle_char_(uint8_t c) {
  if (c == '\r')
    return;
  if (c == '\n') {
    std::string s(this->rx_message_.begin(), this->rx_message_.end());
    std::char x = s[0];
    if (x == "{")
    {
        ESP_LOGD(TAG, "JSON string received: %s", s.c_str());
        this->json_string_ = s;
        parse_json_data_();
    } else
    {
        ESP_LOGI(TAG, "%s", s.c_str());
    }

    this->rx_message_.clear();
    return;
  }
  this->rx_message_.push_back(c);
}

void Emontx4Component::parse_json_data_(){
// TODO - add code in to check for exisence of the Data. Possible to specify the sensor
// without the JSON being available
    json::parse_json(this->json_string_, [this](JsonObject json_data) {
        if (message_number_sensor_ != nullptr) {
            message_number_sensor_->publish_state(json_data["MSG"]);
        }
        if (vrms_sensor_ != nullptr) {
            vrms_sensor_->publish_state(json_data["Vrms"]);
        }
        if (p1_sensor_ != nullptr) {
            p1_sensor_->publish_state(json_data["P1"]);
        }
        if (p2_sensor_ != nullptr) {
            p2_sensor_->publish_state(json_data["P2"]);
        }
        if (p3_sensor_ != nullptr) {
            p3_sensor_->publish_state(json_data["P3"]);
        }
        if (p4_sensor_ != nullptr) {
            p4_sensor_->publish_state(json_data["P4"]);
        }
        if (p5_sensor_ != nullptr) {
            p5_sensor_->publish_state(json_data["P5"]);
        }
        if (p6_sensor_ != nullptr) {
            p6_sensor_->publish_state(json_data["P6"]);
        }
        if (p7_sensor_ != nullptr) {
            p7_sensor_->publish_state(json_data["P7"]);
        }
        if (p8_sensor_ != nullptr) {
            p8_sensor_->publish_state(json_data["P8"]);
        }
        if (p9_sensor_ != nullptr) {
            p9_sensor_->publish_state(json_data["P9"]);
        }
        if (p10_sensor_ != nullptr) {
            p10_sensor_->publish_state(json_data["P10"]);
        }
        if (p11_sensor_ != nullptr) {
            p11_sensor_->publish_state(json_data["P11"]);
        }
        if (p12_sensor_ != nullptr) {
            p12_sensor_->publish_state(json_data["P12"]);
        }
        if (e1_sensor_ != nullptr) {
            e1_sensor_->publish_state(json_data["E1"]);
        }
        if (e2_sensor_ != nullptr) {
            e2_sensor_->publish_state(json_data["E2"]);
        }
        if (e3_sensor_ != nullptr) {
            e3_sensor_->publish_state(json_data["E3"]);
        }
        if (e4_sensor_ != nullptr) {
            e4_sensor_->publish_state(json_data["E4"]);
        }
        if (e5_sensor_ != nullptr) {
            e5_sensor_->publish_state(json_data["E5"]);
        }
        if (e6_sensor_ != nullptr) {
            e6_sensor_->publish_state(json_data["E6"]);
        }
        if (e7_sensor_ != nullptr) {
            e7_sensor_->publish_state(json_data["E7"]);
        }
        if (e8_sensor_ != nullptr) {
            e8_sensor_->publish_state(json_data["E8"]);
        }
        if (e9_sensor_ != nullptr) {
            e9_sensor_->publish_state(json_data["E9"]);
        }
        if (e10_sensor_ != nullptr) {
            e10_sensor_->publish_state(json_data["E10"]);
        }
        if (e11_sensor_ != nullptr) {
            e11_sensor_->publish_state(json_data["E11"]);
        }
        if (e12_sensor_ != nullptr) {
            e12_sensor_->publish_state(json_data["E12"]);
        }
        if (pulse_count_sensor_ != nullptr) {
            pulse_count_sensor_->publish_state(json_data["pulse"]);
        }
        if (pulse_energy_sensor_ != nullptr) {
            pulse_energy_sensor_->publish_state(json_data["pulse"]);
        }
        if (t1_sensor_ != nullptr) {
            t1_sensor_->publish_state(float(json_data["T1"])*0.1);
        }
        if (t2_sensor_ != nullptr) {
            t2_sensor_->publish_state(float(json_data["T2"])*0.1);
        }
        if (t3_sensor_ != nullptr) {
            t3_sensor_->publish_state(float(json_data["T3"])*0.1);
        }
        // Emontx4OnDataTrigger::Emontx4OnDataProcess(Emontx4OnDataTrigger);
        // Emontx4OnDataTrigger::Emontx4OnDataProcess();
        // TODO Trigger ON_DATA
    });
}

}  // namespace emontx4
}  // namespace esphome