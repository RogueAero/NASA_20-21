//connect 3.3v to AREF


const int ap1 = A5; 
const int ap2 = A4;
const int ap3 = A3;

int sv1 = 0;        
int ov1 = 0;    
int sv2 = 0;      
int ov2= 0;      
int sv3 = 0;       
int ov3= 0;      

void setup() {
  // initialize serial communications at 9600 bps:
  Serial.begin(9600);

}

void loop() {
  analogReference(EXTERNAL);    //connect 3.3v to AREF
  // read the analog in value:
  sv1 = analogRead(ap1);            
  // map it to the range of the analog out:
  ov1 = map(sv1, 0, 1023, 0, 255);  
  // change the analog out value:
  delay(2);                     
  //
  sv2 = analogRead(ap2);            

  ov2 = map(sv2, 0, 1023, 0, 255); 
 // 
  delay(2);                 
  //
  sv3 = analogRead(ap3);            

  ov3 = map(sv3, 0, 1023, 0, 255);  

  //float mv = analogRead(0) / 1023.0 * 5000.0; 
  //float g = mv / 300.0;

  // print the results to the serial monitor:
  Serial.print("Xsensor1 = " );                       
  Serial.print(sv1);      
  Serial.print("\t output1 = ");      
  Serial.println(ov1);   

  Serial.print("Ysensor2 = " );                       
  Serial.print(sv2);      
  Serial.print("\t output2 = ");      
  Serial.println(ov2);   

  Serial.print("Zsensor3 = " );                       
  Serial.print(sv3);      
  Serial.print("\t output3 = ");      
  Serial.println(ov3);   
  
  float gforce=0.0108*analogRead(A3) - 5.5;
  
  delay(3000);                     
  //two different values for one analog value read
  //first value is the ADC converted value in 10-bit resolution(0 to 1023)
  //second one is mapped for PWM and it is in 8-bit resolution(0 to 255)
  //Three values for X, Y & Z axes are displayed together are repeated after an interval of 3 seconds.
}
