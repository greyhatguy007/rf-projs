# Intelligent Plant Monitoring and Watering System

## Overview

This project aims to create an intelligent plant monitoring and watering system using Arduino boards (node P), NRF24L01 modules, and a Raspberry Pi as a server (node S). The system enables bidirectional communication, allowing for seamless interaction and control between the devices.

## Components

### Arduino P (Plant Node)

- Equipped with sensors including Soil Moisture Meter, DHT11 Temperature and Humidity Sensor, etc.
- Communicates with Raspberry Pi (S) using NRF24L01 modules.
- Controls a servo motor for precise water dispensing based on instructions received.

### Raspberry Pi S (Control Center)

- Located at the control center.
- Runs a Django web server for data processing using a PyTorch-based deep learning model.
- NRF24L01 module facilitates bidirectional communication with Arduino P.
- Generates responses, including the recommended amount of water for the plant.

## Communication

- NRF24L01 modules enable wireless communication between Arduino P and Raspberry Pi S.
- Alternates between Transmit (TX) and Receive (RX) modes based on the communication.
- Web interface provides real-time visualization and customization options for monitoring settings.


## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- [Arduino](https://www.arduino.cc/)
- [Raspberry Pi](https://www.raspberrypi.org/)
- [NRF24L01 Library](https://github.com/nRF24/RF24)
- [Django](https://www.djangoproject.com/)
- [PyTorch](https://pytorch.org/)

