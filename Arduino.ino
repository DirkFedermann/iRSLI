
#include <Adafruit_NeoPixel.h>
#ifdef __AVR__
  #include <avr/power.h>
#endif

// Which pin on the Arduino is connected to the NeoPixels?
// On a Trinket or Gemma we suggest changing this to 1
#define PIN            6

// How many NeoPixels are attached to the Arduino?
#define NUMPIXELS      12
#define MAXBRIGHTNESS 1

Adafruit_NeoPixel pixels = Adafruit_NeoPixel(NUMPIXELS, PIN, NEO_GRB);

void setup() {
  Serial.begin(9600);
  pixels.begin();
}

int red, green, blue;
String data;
void loop() {
  if(Serial.available() > 0) {
    data = Serial.readStringUntil('#');
    for(int i=0; i<= NUMPIXELS; i++) {
      charToLED(i,data[i]);
    }
  }
}

// c = Color; i = number of the LED
void charToLED (int i, int c) {
  // Red
  if(c == 'r') {
    red = MAXBRIGHTNESS;
    green = 0;
    blue = 0;
  }
  // green
  if(c == 'g') {
    red = 0;
    green = MAXBRIGHTNESS;
    blue = 0;
  }
  // blue
  if(c == 'b') {
    red = 0;
    green = 0;
    blue = MAXBRIGHTNESS;
  }
  // yellow
  if(c == 'y') {
    red = MAXBRIGHTNESS;
    green = MAXBRIGHTNESS;
    blue = 0;
  }
  // magenta
  if(c == 'm') {
    red = MAXBRIGHTNESS;
    green = 0;
    blue = MAXBRIGHTNESS;
  }
  // cyan
  if(c == 'c') {
    red = 0;
    green = MAXBRIGHTNESS;
    blue = MAXBRIGHTNESS;
  }
  // white
  if(c == 'w') {
    red = MAXBRIGHTNESS;
    green = MAXBRIGHTNESS;
    blue = MAXBRIGHTNESS;
  }
  // black/out
  if(c == 'k') {
    red = 0;
    green = 0;
    blue = 0;
  }
  pixels.setPixelColor(i, pixels.Color(red,green,blue));
  pixels.show();
}
