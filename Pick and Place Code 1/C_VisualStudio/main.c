#include <phidget22.h>
#include <stdio.h>
/* Determine if we are on Windows of Unix */
#ifdef WIN32
#include <windows.h>
#else
#include <unistd.h>
#define Sleep(x) usleep((x) * 1000)
#endif

//Declare any event handlers here. These will be called every time the associated event occurs.

static void CCONV onDCMotor0_Attach(PhidgetHandle ch, void* ctx) {
	printf("Attach!\n");
}

static void CCONV onDCMotor0_Detach(PhidgetHandle ch, void* ctx) {
	printf("Detach!\n");
}

int control(int serial, int velocity, int time) {
	//Declare your Phidget channels and other variables
	PhidgetDCMotorHandle dcMotor0;

	//Create your Phidget channels
	PhidgetDCMotor_create(&dcMotor0);

	//Set addressing parameters to specify which channel to open (if any)
	Phidget_setDeviceSerialNumber((PhidgetHandle)dcMotor0, serial);

	//Assign any event handlers you need before calling open so that no events are missed.
	Phidget_setOnAttachHandler((PhidgetHandle)dcMotor0, onDCMotor0_Attach, NULL);
	Phidget_setOnDetachHandler((PhidgetHandle)dcMotor0, onDCMotor0_Detach, NULL);

	//Open your Phidgets and wait for attachment
	Phidget_openWaitForAttachment((PhidgetHandle)dcMotor0, 100);

	//Do stuff with your Phidgets here or in your event handlers.
	PhidgetDCMotor_setTargetVelocity(dcMotor0, velocity);

	Sleep(time);

	//Close your Phidgets once the program is done.
	Phidget_close((PhidgetHandle)dcMotor0);

	PhidgetDCMotor_delete(&dcMotor0);

	return 0;
}

int main() {

	//control(146552, 1, 55 * 90);
	//control(146627, 1, 55 * 120);
	//control(146520, 1, 40 * 130);
	//control(146640, 1, 30 *130);
	//control(146491, -1, 3000);

	control(146627, -1, 55 * 88);
	control(146491, 1, 3000);
	control(146627, 1, 55 * 90);
	control(146552, -1, 55 * 90);
	control(146627, -1, 55 * 90);
	control(146491, -1, 3000);
	control(146627, 1, 55 * 120);
	control(146552, 1, 55 * 90);
}
