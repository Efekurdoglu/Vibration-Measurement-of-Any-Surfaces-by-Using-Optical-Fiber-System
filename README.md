# Vibration-Measurement-of-Any-Surfaces-by-Using-Optical-Fiber-System

## Introduction
- The measurement of vibrations is a crucial topic. Some vibrations are necessary for the proper operation of devices (e.g., shakers, ultrasonic cleaning baths, rock drills), while others are merely undesirable side effects of manufacturing tolerances or the structure's response to external forces. As a result, we looked into the literature and found that there are a variety of methods for detecting the frequency and amplitude of vibrations using mechanical, electrical, and optical sensors [1, 4]. Regardless of the operating principle, these systems can be divided into two groups depending on whether physical contact with the vibrating item is required. As a result, we chose the option that does not require physical contact with the vibrating item.
## SolidWorks
- In order to illustrate our design in real world, we have been used SolidWorks to visualize the real system. The used components in the system, IR (Infrared Led), Op-Amp, concave lens, fiber optic cable, mirror, photodiode (BPW41N) and ESP32. The software used for the system, Matlab, Arduino IDE, Proteus 8 Professional, Spyder(anoconda3) and SolidWorks2021
![11.png](SolidWorks/11.png)
- We collected the dispersed IR Led with the help of thin-sided lens, our light source from infrared led. We collect our led light with the fiber optic cable that we place at the focal point of our thin-sided lens. Our light, which we carry with a fiber optic cable, is transmitted to the mirror. It is transmitted to our other fiber optic cable with the vibration angle of the mirror. The output of this fiber optic cable falls on our photo diode. Thus, we take measurements depending on the amount of light falling on our photodiode.
![3.png](SolidWorks/3.png)
- It is the d1 length between our IR Led and our Lens. Here, we detect the rays emitted to the environment so that they come onto our Lens. With the thin-edged lens, the rays that will come out of our lens are transferred to our fiber optic cable when they come to the d2 focal point. Our light coming out of our fiber optic cable hits our mirror in the distance d3 and is refracted depending on the amount of vibration and comes to our other fiber optic cable. Our light, which we receive with our other fiber cable in the distance d4, drops a certain amount of light on the photodiode at a distance of d5. Thus, in line with the results from our equations, we measure the amount of vibration in the system as a result of the voltages created by the falling light on our photodiode.
## Circuit
- Small signal amplifier is designed for this task. Current generated by photodiode is fed into base of bjt and bjt operates as an amplifier. Output of BJT is then gets read by ESP32.
![led_circuit.png](Proteus/led_circuit.png)
- Proteus is not able to simulate photodiodes. So a sinusoidal current source is used for each electrical component. 
![led_circuit_2.png](Proteus/led_circuit_2.png)
## Spyder (Python)
- All matrix multiplication has been done in Spyder by using Python3. The purpose of using this program is to enhance our ability to work a wide range in software.
## Proteus 8 Professional
- The electrical circuit model was built in order to implement the exact real-life scenario. Hence, the infrared (IR) LED was used to have more consistent and least confliction with other light waves in the experimental environment. The circuit simulate the capturing light by using photodiode, in this circuit. The light was directed to photodiode without any component but the project was aimed to move the light from the source and reflected from the vibrated surface with the help of optical fiber, then the reflected light delivered to photodiode. While capturing the data by the photodiode, the necessary parameters can be found and implemented into real world application.
## Arduino
- When we get the output from the circuit, we need to analyze the data and comment about the frequency as well as amplitude. Thus, the output of the circuit is implemented into Arduino as an analog input and then transfer the data into Matlab throughout Rx and Tx communication protocol. Code:
void setup() {
Serial.begin(115200);
}
void loop() {
float recieved_signal = analogRead(A0)*5/1023;
Serial.println(recieved_signal);
}
## MATLAB 2021b
- While getting our data from Arduino, we need to apply some methods to get meaning of the data.Data recieved is a vector array which includes numerical voltages starting from zero to N number of index.  We applied FFT (Fast Fourier Transform) to recieved vector array to separate all the signals which are acquiring from the surface. And then, we will have several spectral components so that the frequency of the surface could be obtained. Due to constaints of our physical model, we are only be able to define our own signal and process it for simulation. Amplitudes of ac components of the signals are given randomly.
![matlab1.png](Matlab/matlab1.png)
![matlab2.png](Matlab/matlab2.png)
## Mathematical Background
- We used a simple construction in Fig. 9 to get the result of the vibration frequency of the surface, which is the mathematical foundation of this project. In this scenario, the fiber optic specifications play an important part in transporting data from one location to another without losing any data.
- The optic fibers typically have a 0.98-mm core made of Poly-Methyl-Methacrylate (PMMA) [3] and surrounded by a thin (about 20-m) fluorinated polymer cladding (which is much larger than the 9-m core of glass single mode fibers used for high-performance optical communications and the 62.5-m core of multimode glass fibers). As a result, the Ray Optics computation is basically depicted below.
![Simple_Design.JPG](Simple_Design.JPG)
![math1.JPG](Mathematical_background/math1.JPG)




















