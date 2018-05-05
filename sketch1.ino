//sketch
String in = "";

byte[] hexToByte(String coords){
  String newcoords = coords;
  byte[] bytes  = new byte[coords.length()/2]
  for(int i = 0; i < bytes.length; i++){
    bytes[i] = newcoords.substring(0, 2);
    newcoords = newcoords.substring(0, 2);
  }
}

void setup(){
  Serial.begin(9600);
  pinMode(a,OUTPUT);
  //...
}

void loop(){
  if(Serial.available()){
    //read bytes
  }
  else{
    //display previous char
  }
}
