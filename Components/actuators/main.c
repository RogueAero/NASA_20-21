#include "mbed.h"
#include "math.h"


#define SPI1_MOSI PA_7
#define SPI1_MISO PA_6
#define SPI1_SCK PA_5
#define CS PA_4


/**** Motor drive ******/
#define M1_PWM PA_12
#define M1_DIR PB_0

#define M2_PWM PB_6
#define M2_DIR PB_1

#define M3_PWM PA_8
#define M3_DIR PA_11

DigitalOut m1_pwm(M1_PWM);
DigitalOut m1_dir(M1_DIR);

DigitalOut m2_pwm(M2_PWM);
DigitalOut m2_dir(M2_DIR);

DigitalOut m3_pwm(M3_PWM);
DigitalOut m3_dir(M3_DIR);


// Serial pc(USBTX, USBRX);
typedef struct {
	float x;
	float y;
	float z;
} vec;


SPI spi(PA_7, PA_6, PA_5); // mosi, miso, sclk
DigitalOut cs(PA_4);

uint8_t lis3dh_readReg(uint8_t addr) {
	uint8_t returnVal = 0x00;
    cs = 0;
 
    spi.write(0x80 | addr);
    returnVal = spi.write(0x00);

    cs = 1;
	return returnVal;
}

void lis3dh_writeReg(uint8_t addr, uint8_t val) {
    cs = 0;

    spi.write(addr);
    spi.write(val);
    
    cs = 1;
}


void wait_s(float seconds) {
	wait_us(int(seconds*1000000));
}




int main() {
	float x,y,z;
	int16_t int_x, int_y, int_z;
	int avg_x, avg_y, avg_z;

	uint8_t N = 5;
	int16_t ringbuf_x[N];
	int16_t ringbuf_y[N];
	int16_t ringbuf_z[N];

	uint8_t buf_index_x = 0;
	uint8_t buf_index_y = 0;
	uint8_t buf_index_z = 0;

	// set reference vectors
	vec m1_ref = {1, 0, 0.0};
	vec m2_ref = {-0.5, -0.866, 0.0};
	vec m3_ref = {-0.5, 0.866, 0.0};

	// for some reason we need to do this multiple times to get it working
	lis3dh_readReg(0x0F);
	lis3dh_readReg(0x0F);
	lis3dh_readReg(0x0F);
	lis3dh_readReg(0x0F);

	// setup accelerometer
	lis3dh_writeReg(0x20, 0x27);

	int count  = 0;
	while (1) {
		
		int_x = (lis3dh_readReg(0x28) | (lis3dh_readReg(0x29) << 8));
		int_y = (lis3dh_readReg(0x2A) | (lis3dh_readReg(0x2B) << 8));
		int_z = (lis3dh_readReg(0x2C) | (lis3dh_readReg(0x2D) << 8));

		ringbuf_x[buf_index_x++] = int_x;
		ringbuf_y[buf_index_y++] = int_y;
		ringbuf_z[buf_index_z++] = int_z;

		if (buf_index_x >= N) buf_index_x = 0;
		if (buf_index_y >= N) buf_index_y = 0;
		if (buf_index_z >= N) buf_index_z = 0;

		// compute the average of samples in the ring buffer
		avg_x = 0, avg_y = 0, avg_z = 0;
		for (uint8_t i = 0; i < N; i++) {
			avg_x += ringbuf_x[i];
		}
		for (uint8_t i = 0; i < N; i++) {
			avg_y += ringbuf_y[i];
		}
		for (uint8_t i = 0; i < N; i++) {
			avg_z += ringbuf_z[i];
		}
		avg_x /= N;
		avg_y /= N;
		avg_z /= N;
		
		x = float(avg_x)/16 * 0.0001 * 9.807;
		y = float(avg_y)/16 * 0.0001 * 9.807;
		z = float(avg_z)/16 * 0.0001 * 9.807;

		float err_m1 = m1_ref.x*x + m1_ref.y * y + m1_ref.z * z;
		float err_m2 = m2_ref.x*x + m2_ref.y * y + m2_ref.z * z;
		float err_m3 = m3_ref.x*x + m3_ref.y * y + m3_ref.z * z;
		
		if (count % 10 == 0){
			printf("Accel: %d x  %d y  %d z   err_m1: %d  err_m2: %d  err_m3: %d\n\r", 
				int(x*1000), int(y*1000), int(z*1000), int(err_m1*1000), int(err_m2*1000), int(err_m3*1000));
		}

		m1_pwm = (abs(err_m1) > 0.03 ? 1 : 0);
		m2_pwm = (abs(err_m2) > 0.03 ? 1 : 0);
		m3_pwm = (abs(err_m3) > 0.03 ? 1 : 0);

		m1_dir = (err_m1 > 0 ? 0 : 1);
		m2_dir = (err_m2 > 0 ? 0 : 1);
		m3_dir = (err_m3 > 0 ? 0 : 1);

		wait_s(0.05);
		count++;
	}
	

}
