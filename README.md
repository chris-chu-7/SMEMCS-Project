#SMEMCS - Smart Multi-Environmental Monitoring and Control System 

##Overview 

A lot of indoor environemnts suffer from inadequate ventilation, air quality high noise and pollution levels. However, a lot of places in cities, subhurbs and infrastructure lack real-time environemental monitoring and automated response systems in case there is an issue that needs to be addressed. 

SEMCS aims to provide a low cose portable environemntal monitoring solution that monistors key environmental parameters (lighting, air quality, sound, temperature, humidity), detecting unsafe levels for each of these conditions, respond to these conditions using fan, buzzer, visual display, and logging data for collection, analysis, and calibration. This can be utilized or the technology can be expanded to integrate into iOT platforms similar to NEST. 


The folders are as follows 
-> firmware -> Arduino code (.ino files) and files for testing (in the utils folder)
-> hardware -> photos, schematics, and parts list
-> logs -> raw and summarized sensor logs 
-> docs -> project notes, diagrams, and planning documents, schematics 
-> media -> photos/videos for demo and presentation. 


The hardware components used so far is the following
##Hardware Components 
    - KY-038 (Sound Sensor)
    - LDR (Light Detector)
    - Arduino Uno (Microcontroller)
    - DHT22 (Temperature/humidity sensor)
    - MQ135 (Gas Sensor)
    - Breadboard
    - LM358 Op - Amp
    - IRF540 N-Channel MOSFET 
    - Flyback Diode 
    - Buzzer 
    - LED
    - OLED
    - DC Fan 
    - Buck Converter (LM2596) 
    - TVS Diode 
    - Power Supply 
    - USB Cable 
    - Jumper Wires
    - Resistors 
    - Capacitors 

Initial sensor tests for the LDR and DHT22 showed stable results using Arduino’s .ino sketches. Further details and analysis will be included in the final report available in the /docs/ folder.
