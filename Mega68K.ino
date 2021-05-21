#include "Mega68K.h"

void setup()
{
    Serial.begin(115200);
    Serial.println("[M68K]: BEGIN_READ");
    for (size_t i = 0; i < szPins; ++i)
    {
        pinMode(pins[i], INPUT);
        Serial.print("[INFO]: ");
        Serial.print(names[i]);
        Serial.print(":    \t");
        Serial.println(digitalRead(pins[i]));
    }
    Serial.println("[M68K]: END_READ");
}

void loop()
{
    delay(1);
}
