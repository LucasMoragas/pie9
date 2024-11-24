#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>

// Configuração dos pinos CE e CSN
#define CE_PIN 9
#define CSN_PIN 10

RF24 radio(CE_PIN, CSN_PIN);

// Endereço do canal de comunicação
const byte address[6] = "00001";

void setup() {
  Serial.begin(9600);
  radio.begin();
  radio.openReadingPipe(0, address);
  radio.setPALevel(RF24_PA_LOW);
  radio.startListening();
}

void loop() {
  if (radio.available()) {
    int receivedValue = 0;
    
    // Recebe o valor
    radio.read(&receivedValue, sizeof(receivedValue));
    // Mostra no monitor serial
    Serial.println(receivedValue);
  }
  
  delay(100); // Pequeno atraso para evitar sobrecarga
}
