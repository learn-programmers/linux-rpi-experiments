#include<stdio.h>
#include<wiringPi.h>

int main(){

	if(wiringPiSetup() == -1) 
		return -1; 

	pinMode(2, OUTPUT); 

	for(;;) 
	{
		digitalWrite(2,0); 
		delay(1000); 
		digitalWrite(2,1); 
		delay(1000); 
	}

	return 0;
}
