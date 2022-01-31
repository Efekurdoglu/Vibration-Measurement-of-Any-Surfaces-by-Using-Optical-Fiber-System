void setup() {
Serial.begin(115200);

}

void loop() {
int recieved_signal = analogRead(A0)*5/1023;
Serial.println(recieved_signal);

}
