#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>

RF24 radio(9, 10); // CE, CSN

const int buttonPin = 2; // Connect button to digital pin 2
const int ledPin = 13;   // Connect LED to digital pin 13

boolean buttonState = LOW;

void setup()
{
    pinMode(buttonPin, INPUT);
    pinMode(ledPin, OUTPUT);

    radio.begin();
    radio.openWritingPipe(0xF0F0F0F0E1LL);
}

void loop()
{
    buttonState = digitalRead(buttonPin);

    if (buttonState == HIGH)
    {
        digitalWrite(ledPin, HIGH); // Toggle the LED on
        sendSignal();
        delay(500); // Debouncing delay
    }
    else
    {
        digitalWrite(ledPin, LOW); // Toggle the LED off
    }

    if (radio.available())
    {
        receiveSignal();
        delay(500); // Debouncing delay
        radio.stopListening();
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
        digitalWrite(ledPin, LOW); // Toggle the LED off
    }
    radio.startListening();
}
