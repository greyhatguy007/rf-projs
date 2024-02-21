#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>

RF24 radio(9, 10); // CE, CSN

const int buttonPin = 2;
const int ledPin = 13;

boolean buttonState = LOW;
boolean isTransmitting = false;

void setup()
{
    pinMode(buttonPin, INPUT);
    pinMode(ledPin, OUTPUT);

    radio.begin();
    radio.openReadingPipe(1, 0xF0F0F0F0E1LL);
    radio.startListening();
}

void loop()
{
    buttonState = digitalRead(buttonPin);

    if (buttonState == HIGH && !isTransmitting)
    {
        digitalWrite(ledPin, HIGH);
        sendSignal();
        delay(500);
        isTransmitting = true;
    }
    else if (buttonState == LOW && isTransmitting)
    {
        digitalWrite(ledPin, LOW);
        isTransmitting = false;
    }

    if (radio.available())
    {
        receiveSignal();
        isTransmitting = false;
    }
}

void sendSignal()
{
    char text[] = "Button Pressed";
    radio.write(&text, sizeof(text));
}

void receiveSignal()
{
    char text[14] = "";
    radio.read(&text, sizeof(text));
    if (strcmp(text, "Button Pressed") == 0)
    {
        digitalWrite(ledPin, HIGH); // Toggle the LED on
    }
}
