import wiringpi
import time

def ActivateADC ():
    wiringpi.digitalWrite(pin_CS_adc, 0)       # Actived ADC using CS
    time.sleep(0.000005)

def DeactivateADC():
    wiringpi.digitalWrite(pin_CS_adc, 1)       # Deactived ADC using CS
    time.sleep(0.000005)

def readadc(adcnum): 
    if ((adcnum > 7) or (adcnum < 0)): 
        return -1 
    revlen, recvData = wiringpi.wiringPiSPIDataRW(1, bytes([1,(8+adcnum)<<4,0]))
    time.sleep(0.000005)
    adcout = ((recvData[1]&3) << 8) + recvData[2] 
    
    return adcout  

#Setup
pin_CS_adc = 16                                 #We will use w16 as CE, not the default pin w15!
led1 = 1
led2 = 2
wiringpi.wiringPiSetup() 
wiringpi.pinMode(led1,1)
wiringpi.pinMode(led2,1)
wiringpi.pinMode(pin_CS_adc, 1)                 # Set ce to mode 1 ( OUTPUT )
wiringpi.wiringPiSPISetupMode(1, 0, 500000, 0)  #(channel, port, speed, mode)




#ledfunction
def changeLED():
   
    if tmp0 > tmp1:
        wiringpi.digitalWrite(led1,1)
        wiringpi.digitalWrite(led2,0)
    else:
        wiringpi.digitalWrite(led1,0)
        wiringpi.digitalWrite(led2,1)


#Main
try:
    while True:
        ActivateADC()
        tmp0 = readadc(0) # read channel 0
        DeactivateADC()
    
        ActivateADC()
        tmp1 = readadc(1) # read channel 0
        DeactivateADC()

        print ("input0:",tmp0)
        print ("input1:",tmp1)
        time.sleep(0.2)
        changeLED()

except KeyboardInterrupt:
    DeactivateADC()
    print("\nProgram terminated")

