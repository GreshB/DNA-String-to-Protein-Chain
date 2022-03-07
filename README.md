# DNA-String-to-Protein-Chain
Program takes in a sequence of DNA and converts it to up to two protein chains. This program accounts for frame shifts as well. 
If a dna strand that won't be able to create a protein chain is inputted, a message is printed to inform the user.


Note: The DNA strand must be 5' to 3', i.e. the coding strand

To start run `python File.py`

<img width="647" alt="Screen Shot 2022-03-06 at 5 44 32 PM" src="https://user-images.githubusercontent.com/100721569/156947470-999d8a7f-bd10-423c-b8ef-3bca271afe52.png">

<img width="540" alt="Screen Shot 2022-03-06 at 5 48 34 PM" src="https://user-images.githubusercontent.com/100721569/156947622-e77be805-6c2d-4a65-b261-91fe125a3e02.png">

All updates since the initial posting of this program:
- removed all if statements used to convert the DNA sequence, RNA sequence, and codons, and replaced them with dictionaries
- added the ability for two chains to be outputted
- added aesthetic formating to the outputted chain(s)
- added descriptions to each function
- added comments to if statements and loops to describe what their purposes are
- formatted the code to be read more easily
