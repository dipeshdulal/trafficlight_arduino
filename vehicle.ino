void turnOn(char);
// traffic lights
enum LEDS {
	R1 = 2, G1, Y1,
	R2,	G2,	Y2,
	R3,	G3,	Y3,
	R4,	G4,	Y4
};

char incomingByte;
char incoming[12];

// to turn on as per the given ascii character
void turnOn(char c){
	if(c == 'A'){
		digitalWrite(R1, HIGH);
	}else if(c == 'B'){
		digitalWrite(G1, HIGH);
	}else if(c == 'C'){
		digitalWrite(Y1, HIGH);
	}else if(c == 'D'){
		digitalWrite(R2, HIGH);
	}else if(c == 'E'){
		digitalWrite(G2, HIGH);
	}else if(c == 'F'){
		digitalWrite(Y2, HIGH);
	}else if(c == 'G'){
		digitalWrite(R3, HIGH);
	}else if(c == 'H'){
		digitalWrite(G3, HIGH);
	}else if(c == 'I'){
		digitalWrite(Y3, HIGH);
	}else if(c == 'J'){
		digitalWrite(R4, HIGH);
	}else if(c == 'K'){
		digitalWrite(G4, HIGH);
	}else if(c == 'L'){
		digitalWrite(Y4, HIGH);
	}
}

// to turn off as per the given ascii character
void turnOff(char c){
	if(c == 'a'){
		digitalWrite(R1, LOW);
	}else if(c == 'b'){
		digitalWrite(G1, LOW);
	}else if(c == 'c'){
		digitalWrite(Y1, LOW);
	}else if(c == 'd'){
		digitalWrite(R2, LOW);
	}else if(c == 'e'){
		digitalWrite(G2, LOW);
	}else if(c == 'f'){
		digitalWrite(Y2, LOW);
	}else if(c == 'g'){
		digitalWrite(R3, LOW);
	}else if(c == 'h'){
		digitalWrite(G3, LOW);
	}else if(c == 'i'){
		digitalWrite(Y3, LOW);
	}else if(c == 'j'){
		digitalWrite(R4, LOW);
	}else if(c == 'k'){
		digitalWrite(G4, LOW);
	}else if(c == 'l'){
		digitalWrite(Y4, LOW);
	}
}

void setup()
{

	// initialize serial communication:
	Serial.begin(9600);
	
	// initializing all 2-13 pins as output
	for(int i = 2; i <= 13; i++){
		pinMode(i, OUTPUT);
	}

}

void loop()
{
	//digitalWrite(Y4, HIGH);
	
	// see if there's incoming serial data:
     if (Serial.available() >= 12) {
		// read the oldest byte in the serial buffer:
		for(int i = 0; i <= 12; i++){
			incoming[i] = Serial.read();
		}
		
		// incomingByte = Serial.read();
		for(int i = 0; i <= 12; i++){
			incomingByte = incoming[i];
			if(incomingByte > 97){
				turnOff(incomingByte);
	     	}else{
				turnOn(incomingByte);
		    }
    	}
		
	}
}

