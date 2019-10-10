const int pinoLED_0 = 6;
const int pinoLED_1 = 8;
const int pinoLED_2 = 7;
const int pinoLED_3 = 11;



void setup() {
  // put your setup code here, to run once:
  pinMode(pinoLED_0, OUTPUT);  // Definindo o pino como OUTPUT
  pinMode(pinoLED_1, OUTPUT);  // Definindo o pino como OUTPUT
  pinMode(pinoLED_2, OUTPUT);  // Definindo o pino como OUTPUT
  pinMode(pinoLED_3, OUTPUT);  // Definindo o pino como OUTPUT

  Serial.begin(9600);          // Velocidade padrão da porta de conexão

  digitalWrite(pinoLED_0,HIGH);
  digitalWrite(pinoLED_1,HIGH);
  digitalWrite(pinoLED_2,HIGH);
  digitalWrite(pinoLED_3,HIGH);
}

void loop() {
  // put your main code here, to run repeatedly:
  char leitura = Serial.read();

  if(leitura == '0'){
    digitalWrite(pinoLED_0,HIGH);
    digitalWrite(pinoLED_1,LOW);
    digitalWrite(pinoLED_2,LOW);
    digitalWrite(pinoLED_3,LOW);
  }else if(leitura == '1'){
    digitalWrite(pinoLED_0,LOW);
    digitalWrite(pinoLED_1,HIGH);
    digitalWrite(pinoLED_2,LOW);
    digitalWrite(pinoLED_3,LOW);
  }else if(leitura == '2'){
    digitalWrite(pinoLED_0,LOW);
    digitalWrite(pinoLED_1,LOW);
    digitalWrite(pinoLED_2,HIGH);
    digitalWrite(pinoLED_3,LOW);
  }else if(leitura == '3'){
    digitalWrite(pinoLED_0,LOW);
    digitalWrite(pinoLED_1,LOW);
    digitalWrite(pinoLED_2,LOW);
    digitalWrite(pinoLED_3,HIGH);
  }
  
}
