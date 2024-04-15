// Pin tanımları
const int joystick1XPin = A0;
const int joystick1YPin = A1;
const int joystick1ButtonPin = 4;

const int joystick2XPin = A2;
const int joystick2YPin = A3;
const int joystick2ButtonPin = 5;

// Değişkenler
int joystick1XValue = 0;
int joystick1YValue = 0;
int joystick1ButtonState = 0;

int joystick2XValue = 0;
int joystick2YValue = 0;
int joystick2ButtonState = 0;

void setup() {
  // Joystick pinlerini giriş olarak ayarla
  pinMode(joystick1XPin, INPUT);
  pinMode(joystick1YPin, INPUT);
  pinMode(joystick1ButtonPin, INPUT_PULLUP);

  pinMode(joystick2XPin, INPUT);
  pinMode(joystick2YPin, INPUT);
  pinMode(joystick2ButtonPin, INPUT_PULLUP);

  // Seri bağlantıyı başlat
  Serial.begin(9600);
}

void loop() {
  // Joystick 1 değerlerini oku
  joystick1XValue = analogRead(joystick1XPin);
  joystick1YValue = analogRead(joystick1YPin);
  joystick1ButtonState = digitalRead(joystick1ButtonPin);

  // Joystick 2 değerlerini oku
  joystick2XValue = analogRead(joystick2XPin);
  joystick2YValue = analogRead(joystick2YPin);
  joystick2ButtonState = digitalRead(joystick2ButtonPin);

  // Veriyi seri port üzerinden gönder
  Serial.print(joystick1XValue);
  Serial.print(joystick1YValue);
  Serial.print(joystick1ButtonState);
  Serial.print(joystick2XValue);
  Serial.print(joystick2YValue);
  Serial.println(joystick2ButtonState);

  // Kısa bir bekleme
  delay(50);
}
