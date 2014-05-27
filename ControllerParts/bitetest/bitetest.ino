int lightIn = A3;
int b;

void setup(){
  Serial.begin(9600);
  pinMode(lightIn,INPUT);
}

void loop(){
  for(b=0;b<=255;b++){
    Serial.write(b);
  }
  
}
