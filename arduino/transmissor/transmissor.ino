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
  radio.openWritingPipe(address);
  radio.setPALevel(RF24_PA_LOW);
  radio.stopListening();
}

void loop() {
  // Gera um valor aleatório entre 20 e 30
  int randomValue = random(20, 31);
  
  // Envia o valor
  bool success = radio.write(&randomValue, sizeof(randomValue));
  
  if (success) {
    Serial.print("Enviado: ");
    Serial.println(randomValue);
  } else {
    Serial.println("Falha ao enviar");
  }
  
  delay(100); // Aguarda 1 segundo
}
