# xorcrack
Use shift analysis and statistics to automatically decrypt xor ciphers.

##Run with help flag for explanation of inputs:
```
$ python xorcrack.py --help
usage: xorcrack.py [-h] key_min key_max common msg

xorcrack attempts to determine the

positional arguments:
  key_min     minimum key length to try
  key_max     maximum key length to try
  common      most common character in decoded message
  msg         file containing encrypted message

optional arguments:
  -h, --help  show this help message and exit

```

##Running on example message:
Specify that the key is between 2 and 20 characters and 'space' is the most common character
```
$ python xorcrack.py 2 20 " " example_message.dat
```
