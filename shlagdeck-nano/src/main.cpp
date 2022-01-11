#include <Arduino.h>

#define PRESSED 1
#define RELEASED 0
#define BUTTONS_COUNT 5

int buttons_pins[] = { A5, A4, A3, A2, A1 };
int buttons_states[] = { RELEASED, RELEASED, RELEASED, RELEASED, RELEASED };

void setup() {
  Serial.begin(115200);

  for (int i = 0; i < BUTTONS_COUNT; i++) {
    pinMode(buttons_pins[i], INPUT_PULLUP);
  }
}

void loop() {
  if (Serial.available() > 0) {
    String received = Serial.readString();
    if (received.startsWith("identify")) {
      Serial.println("shlagdeck");
    }
  }

  for (int i = 0; i < BUTTONS_COUNT; i++) {
    if (digitalRead(buttons_pins[i]) == LOW) {
      if (buttons_states[i] == RELEASED) {
        Serial.println(i);
        buttons_states[i] = PRESSED;
      }
    } else {
      buttons_states[i] = RELEASED;
    }
  }

  delay(5);
}