# Shamir Secret Sharing Script (Basic Implementation)

Aim: To create a program implementing Shamir Secret Sharing Algorithm with the following features:
```
The applet should accept a byte array of size 32. 
For eg - private byte[] secret = new byte[32]; 
The applet should form 4 shares where the secret could be reconstructed from any 2 shares. 
Apply Shamir secret sharing scheme to each byte separately and use Galois Field(256) as the underlying finite field. 
Y coordinate corresponding to the same X coordinates shall be stored in the same byte array for each share. 
The applet should accept M number of byte array and reconstruct the original secret using Shamir’s Algorithm. 
Notes: No external library (accept for generating random numbers) shall be used.
```


Refer [sss_with_gf256.py](/sss_with_gf256.py) for the code

Used [GF256 library](https://gf256.readthedocs.io/en/stable/) for making operations over Galois Field(256).

The applet forms 4 shares where the secret can be reconstructed from any 2 shares. [Shamir secret sharing scheme](https://en.wikipedia.org/wiki/Shamir%27s_Secret_Sharing) is applied to each byte separately and used Galois Field(256) as the underlying finite field.

By default a secret key is already defiled in the code.
And reconstruction can be done by using any two shares. By default reconstruction is done using share3 & share4.
Refer comments within the code for more explanation.<br>
![main_code](/main_code.jpg)

## Instructions
- Clone or download the repository
- For first time, run this in Powershell
```
pip install gf256
```
- Next do this to execute
```
python sss_with_gf256.py
```
- make changes in the basecode based on the requirements
## Output
Here is a snippet for output for the default input.<br>
you can customise the input by editing the inputs within the code.<br>
Refer comments in the code for more info<br>
![Output]/output.jpg)
