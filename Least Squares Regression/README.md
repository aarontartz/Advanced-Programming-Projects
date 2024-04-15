# COMPE-361 Project 8
## Description
Using file "2N2222.csv" which contains laboratory measurements of voltage across the collector-emitter (VCE) region of a NPN bipolar junction transistor (BJT) as the base current IB is varied from approximately 3 to 18 mA the following is completed (in order):
* Download and load the measurement data into a NumPy array
* Use the SciPy curve_fit function to find an accurate equation to model the relationship between VCE and IB
* Scatter plot the data
* From scatter of the raw data, propose model function, and use SciPy curve_fit to compute optimal parameters of this model
* Compute the one standard deviation errors on your parameters using the parameter covariance matrix returned by curve_fit to evaluate parameter estimates
* Use model function to estimate VCE for IB = 3.1mA.
