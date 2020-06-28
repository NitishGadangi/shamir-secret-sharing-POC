# cypherock_challenge
My solutions to the cypherock challenge. ```Figure Out SSS Problem Code: CTS1```

> Question will be added here later

Refer [sss_with_gf256.py](https://github.com/NitishGadangi/cypherock_challenge/blob/master/sss_with_gf256.py) for the code

Used [GF256 library](https://gf256.readthedocs.io/en/stable/) for making operations over Galois Field(256).

The applet forms 4 shares where the secret can be reconstructed from any 2 shares. [Shamir secret sharing scheme](https://en.wikipedia.org/wiki/Shamir%27s_Secret_Sharing) is applied to each byte separately and used Galois Field(256) as the underlying finite field.

By default a secret key is already defiled in the code.
And reconstruction can be done by using any two shares. By default reconstruction is done using share3 & share4.
Refer comments within the code for more explanation.<br>
![main_code](https://github.com/NitishGadangi/cypherock_challenge/blob/master/main_code.jpg?raw=true)

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
![Output](https://github.com/NitishGadangi/cypherock_challenge/blob/master/output.jpg?raw=true)
