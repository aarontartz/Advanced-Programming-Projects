# COMPE-361 Project 13

## Description
This project:
* Loads the discrete time domain signal x from the pickle file and plots the signal with respect to time (signal was sampled at 256 Hz for 6s).
* Knowing that each second of the signal encodes a single ASCII character, performs a DFT on each second of x and plots the "one-side" spectrum for each symbol.
* Normalizes the "DFT Amplitude" so each represented frequency has amplitude = 1.
* Verifying each frequency with an amplitude near 1 is a power of 2 and therefore represents the presence of an enabled bit in an 8-bit byte, adds up the frequency values for each separate second (i.e. byte) of the spectrum of x and prints these values in hexadecimal.
* Converts the sequence of hexadecimal values into a string.
* Assuming each hexadecimal value represents an ASCII character, displays the secret word.

## Output graphs
<img width="766" alt="Screenshot 2024-05-14 at 11 29 03 AM" src="https://github.com/aarontartz/Advanced-Programming-Projects/assets/166546889/42cd0b66-c6dc-4c68-b118-c581adf1154d"><br />
<img width="1338" alt="Screenshot 2024-05-14 at 11 29 59 AM" src="https://github.com/aarontartz/Advanced-Programming-Projects/assets/166546889/c3abbcfa-991e-43d8-9cb0-68c150aa05e3">
