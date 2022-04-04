# DNA-String-to-Protein-Chain
Program takes in a sequence of DNA and converts it to up to two protein chains. This program accounts for frame shifts as well. 
If a dna strand that won't be able to create a protein chain is inputted, a message is printed to inform the user.


Note: The DNA strand must be 5' to 3', i.e. the coding strand

To start run `python File.py`

Success Example:
```
$ python3 File.py gatgactgtaccaggattacatggtggtcgctaaaggatgcacaatatgcgctaaagtcg
First Chain: Met-Thr-Val-Pro-Gly-Leu-His-Gly-Gly-Arg
Second Chain: Met-His-Asn-Met-Arg
None
```

Failure Example:
```
$ python3 File.py atcgcgcgcgcgcgctcgctgctgctcgtgcgtgcg

*******************************************
* This sequence will not create a protein *
*******************************************

Please try another DNA sequence
```

All updates since the initial posting of this program:
- removed all if statements used to convert the DNA sequence, RNA sequence, and codons, and replaced them with dictionaries
- added the ability for two chains to be outputted
- added aesthetic formating to the outputted chain(s)
- added descriptions to each function
- added comments to if statements and loops to describe what their purposes are
- formatted the code to be read more easily
