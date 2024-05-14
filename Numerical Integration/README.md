# COMPE-361 Project 12
## Background
### Fresnel Sine Integral
The Fresnel sine integral is commonly used to calculate electromagnetic field intensity:<br />
<img width="122" alt="Screenshot 2024-05-14 at 11 13 02 AM" src="https://github.com/aarontartz/Advanced-Programming-Projects/assets/166546889/a5a3e15f-f593-4e4a-89b5-4a2de9072f8b"><br />
The exact solution of this integral over the interval [0, 2π] is:<br />
<img width="131" alt="Screenshot 2024-05-14 at 11 17 12 AM" src="https://github.com/aarontartz/Advanced-Programming-Projects/assets/166546889/0a7b3eac-8c6e-45a5-b1eb-669050759517">

## Description
This project:
* Plots the Fresnel sine integral over the interval x = [0, 2π].
* Implements a serial version of Simpson’s Method to integrate the Fresnel sine integral, and reports the error in normalized scientific format.
* Implements a parallel version of Simpson’s Method to integrate the Fresnel sine integral, and reports the error in normalized scientific format.
* For different magnitudes of h, stores h and the error in a suitable data structure.
* On a log-scale 3D plot, plots h vs error vs elapsed multithreaded time and discusses the findings.

## Output Graphs
<img width="599" alt="Screenshot 2024-05-14 at 11 23 42 AM" src="https://github.com/aarontartz/Advanced-Programming-Projects/assets/166546889/ad1ee101-ec17-46c1-85d3-141e0bdca56f"><br />
<img width="505" alt="Screenshot 2024-05-14 at 11 22 26 AM" src="https://github.com/aarontartz/Advanced-Programming-Projects/assets/166546889/ae0ed41c-d36a-4a00-bf39-98d5728c63f0"><br />
<img width="319" alt="Screenshot 2024-05-14 at 11 22 45 AM" src="https://github.com/aarontartz/Advanced-Programming-Projects/assets/166546889/75eb463a-08b2-4d99-b5d9-539d43990717"><br />
<img width="364" alt="Screenshot 2024-05-14 at 11 22 56 AM" src="https://github.com/aarontartz/Advanced-Programming-Projects/assets/166546889/ef6f5c11-7401-48f3-8b61-79b75a9e2f7e"><br />
<img width="318" alt="Screenshot 2024-05-14 at 11 23 22 AM" src="https://github.com/aarontartz/Advanced-Programming-Projects/assets/166546889/33e21985-ea91-478c-b9b9-4ef73d54b7bc">
