# SchoolBell-Keygen

This repository contains a proof of concept for a key generator targeting the SchoolBell application by ktims.com. SchoolBell is designed to manage school bell systems, and this key generator is an educational tool to test my skills on key generation.

The purpose of this project is to provide insights into the mechanisms of software licensing and security. It is intended strictly for educational use and not for circumventing the purchase of legitimately licensed software. Users are encouraged to respect the software’s licensing agreement and to purchase a license if they choose to use the product.

A valid activation code alongside the username is found in the validuserkey.txt file to immediately activate without brute-forcing.

# How it works

Schoolbell transforms the key and username inputted and compares the two with a few parameters.

```
f(k) == f(n)
```

Valid keys are 16 characters long and are taken to a transformative part of the code which iteratively indexes the character in the string with a map string array.

```
SQLFTMKZHJYDVCWP
XPQDHZFSRYCKWGJV
CBFNWDQPJZVLKXGS
ZSMXNLYTBFRCGVPD
BPXWQHSLFTKZDYJV
LJGNWKMTQRPXVBDH
KZHTMPFLWDGNRJBY
MDWJNYCLXZRKGQFP
VDBYJRLSTHFNGMWK
TLXJFMRSVNCYHGZW
BCRKLJXDVWZSMQHG
CNWFQGRTHSZDMXJK
WZTXDNKSYCBMGHRF
YMWBCVJDFZNPXSQH
CXTHPYZSWNBGFKLJ
WRGSVKXLNCMZDPJB
```

Taken an input key, the program goes through the above codes for each character to see where in the index they fall on.

With an example key of "MPSRQMYKKJQCMZPL", the first character "M" is compared to the first array string which is "SQLFTMKZHJYDVCWP".
The code finds where "M" lies on the array string which in this case is index of 5, so the transformed M is now 5.
Then goes to the next code "XPQDHZFSRYCKWGJV" of the character "P", which is now index of 1. If the index is 10 it then goes to the letter A as in hex and so on till F which is index 15.
Continue for all the rest and the transformed key is now "51FA46FBF3D0B947".

The transformed key is sliced and gets 4 parameters taken out of it p1, p2, p3, p4.
These are then compared against the username parameters named np1, np2, np3 and np4.

![keycheck](assets/image.png "keycheck")

For the software to activate, 2 checks must be made.
The last 2 characters of the transformed key are taken as a checksum for the rest of the key and the checksum should match the last 2 hex values of the ascii sum of the first 14 characters of the transformed key. And the second condition is for the np1-4 values to match the p1-4 values.

The username is transformed to the below np1-4 values, with np3 always being 10.

```
np1 = (10 + strlen(username)) & 0xF
np2 = (ascii_sum(username)) & 0xFF
np3 = strlen("Schoolbell")
np4 = np2 + 39
```

```
p1 = transformed_keyinput[0]

p2 = transformed_keyinput[1]
p2 = transformed_keyinput[2]

p3 = transformed_keyinput[3]

p4 = transformed_keyinput[4]
p4 = transformed_keyinput[5]
```

Since p1-4 are key values this makes it pretty simple to brute force a key, since we only need to match the np3 and np4 values, this gives us a big window for key generation.
With the bruteforce script, it finds keys that have the np3 as 10 and np4 as whatever np2 is, + 39.
We use checksumfix to fix the checksum at the end by iterating ascii values and we have a valid key.
Now we produce a bunch of keys and try to find a key that matches a username. This can be automated as well but i chose not to do it.
We can use usernametokey to check our valid key list to match any usernames we put in. 
If there's no output, that means it couldn't find a correct key for it.

### An example would be:

```
Enter name: GuardianN06
Code found for username: MPSRQMYKKJQCMZPL

Transformed key: 51FA46FBF3D0B947
Checksum: 47

key: 208.03.4031

p1=5 np1=5
p2=31 np2=31
p3=10 np3=10
p4=70 np4=70
```

Or with the username "CRACKED" in validuserkey.txt

Feel free to make the scripts better performing!
