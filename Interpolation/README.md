# COMPE-361 Project 9
## Background
### Gaussian Function
<img width="236" alt="Screenshot 2024-05-14 at 11 39 01 AM" src="https://github.com/aarontartz/Advanced-Programming-Projects/assets/166546889/72256463-e186-42b2-8f67-4cec1b2cc2b8">

### Chebyshev Nodes
<img width="399" alt="Screenshot 2024-05-14 at 11 41 10 AM" src="https://github.com/aarontartz/Advanced-Programming-Projects/assets/166546889/3e77c218-2613-4c25-97cc-2747fcb47bb9">

## Description
Part 1:
* Plots g(x) over the interval x = [2.0, 2.0], with σ<sup>2</sup> = 0.2 and µ = 0.0 in RED.
* Using 6 equidistant points over the interval, scatter plots the points on the x-axis as BLUE dots.
* Constructs and plots a fifth order Lagrange polynomial interpolation L(x).
* Using 10 equidistant points over the interval, scatter plots the points on the x-axis as GREEN dots.
* Constructs and plots a ninth order Lagrange polynomial interpolation L(x).

Part 2:
* Defines Python function l(j, x, nodes), that generates Lagrange basis polynomials using Chebyshev points on the interval [-2,2].
* Plots the function l(j, x, nodes) for 0 ≤ j ≤ k.
* Using 6 Chebyshev points over the interval, scatter plots the points on the x-axis as CYAN dots.
* Constructs and plots a fifth order Lagrange polynomial interpolation L(x).
* Quantizes the discrepancy between g(x) and L(x) using equally spaced interpolating points and Chebyshev interpolating points by computing ||g(x) - L(x)|| for all three sets of points (6 equidistant, 10 equidistant, 6 Chebyshev).

## Output graph
<img width="736" alt="Screenshot 2024-05-14 at 11 54 43 AM" src="https://github.com/aarontartz/Advanced-Programming-Projects/assets/166546889/05dbd409-ace4-41f2-960f-a78c21847ef4">

