# COMPE-361 Project 2
## Background
### Toeplitz Matrix
A Toeplitz matrix (diagonal-constant matrix) is a matrix where each diagonal from left to right is constant. For example, the following n x n matrix is a Toeplitz matrix:
<img width="521" alt="Screenshot 2024-04-14 at 11 15 51 PM" src="https://github.com/aarontartz/Solo-Python-Projects/assets/166546889/7344a6ab-4014-4497-8372-8605be54831f">

## Matrices
### Matrix K<sub>3</sub>
<img width="266" alt="Screenshot 2024-04-14 at 11 15 20 PM" src="https://github.com/aarontartz/Solo-Python-Projects/assets/166546889/5353d993-f694-47bb-a975-9f9c092fb0f1">

### Matrix K<sub>4</sub>
<img width="341" alt="Screenshot 2024-04-14 at 11 21 06 PM" src="https://github.com/aarontartz/Solo-Python-Projects/assets/166546889/5351cf4b-ae30-4e3b-a92b-35686bbbba1f">

## Description
This project accomplishes the following (in order):
* From K<sub>3</sub>, instantiate T<sub>3</sub> so that the cell at a<sub>0</sub> is 1
* From T<sub>3</sub>, define U<sub>3</sub> by performing the following row operations:
  - R<sub>2</sub> <- R<sub>2</sub> + R<sub>1</sub>
  - R<sub>3</sub> <- R<sub>3</sub> + R<sub>2</sub>
*Note U<sub>3</sub> is an upper-triangular Toeplitz matrix
* To see how T<sup>-1</sup> can be calculated with U, perform the following:
  - Verify T<sub>3</sub> = U<sub>3</sub><sup>T</sup>U<sub>3</sub>
  - Verify U<sub>3</sub>U<sub>3</sub><sup>-1</sup> = I<sub>3</sub>
  - Verify (U<sub>3</sub><sup>T</sup>U<sub>3</sub>)<sup>-1</sup> = T<sub>3</sub><sup>-1</sup>
* Then, repeat the following using K<sub>4</sub>
