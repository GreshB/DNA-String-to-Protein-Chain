#!/usr/bin/env python3

import sys

from constants import RNA_COMBOS, STAGE_ONE_TRANSCRIPTION_MAP, STAGE_TWO_TRANSCRIPTION_MAP


def transcription1(dna):
    """
    Purpose: To reinact the first stage of DNA transcription with an inputted DNA sequence
    Parameter(s): DNA: the inputted DNA sequence
    Return Values: string.join(trans1) a string of the new DNA sequence
    """

    string = ""
    trans1 = []
    lcdna = dna.lower()

    # creates a string that converts the DNA sequenence
    for i in range(len(dna)):
        trans1.append(STAGE_ONE_TRANSCRIPTION_MAP[lcdna[i]])
    return string.join(trans1)


def transcription2(dna):
    """
    Purpose: To reinact the second stage of DNA transcription with an inputted DNA sequence
    Parameter(s): DNA: the inputted DNA sequence
    Return Values: trans2_stirng: a string of RNA based on the initial DNA sequence
    """

    string = ""
    trans2 = []
    lcdna = transcription1(dna)

    # creates a string that converted the DNA sequence into RNA
    for i in range(len(dna)):
        trans2.append(STAGE_TWO_TRANSCRIPTION_MAP[lcdna[i]])

    trans2_string = string.join(trans2)

    # makes sure the length of the string is divisible by 3 due to later neccessities
    while len(trans2_string) % 3 != 0:
        trans2_string = trans2_string[:-1]

    return trans2_string


def split_codons(dna_string, codon_length, start_pos):
    return [
        dna_string[i : i + codon_length]
        for i in range(start_pos, len(dna_string), codon_length)
    ]


def frame_for_met(dna):
    """
    Purpose: To frame the RNA sequence created from the DNA sequence in such a way
             that if "aug" is in the string, then a created list that has organized
             the RNA sequence into codons, ensures that "aug" will be one of its elements
             will be returned. (Example: "caug" would become ["cau","g"] without framing,
             so this function will instead alter it to ["c","aug"])
    Parameter(s): DNA: the inputted DNA sequence
    Return Values: dna_split_list: The RNA sequence in list form in which "aug" is an element,
                                   if "aug" was present in the RNA string, without ever being missaligned
                   dna_split_list2: The RNA sequence in list form in which "aug" is an element,
                                  if "aug" was present in the RNA string, but was not in the initial
                                  list format, due to being missaligned by 1 nucleotide
                    dna_split_list3: The RNA sequence in list form in which "aug" is an element,
                                   if "aug" was present in the RNA string, but was not in the initial
                                   list format, due to being misalligned by 2 nucleotides
    """

    dna_list = transcription2(dna)
    dna_splits = [split_codons(dna_list, 3, x) for x in range(3)]

    met_first = []

    for split in dna_splits:
        if "aug" in split:
            return split

    print("\n*******************************************")
    print("* This sequence will not create a protein *")
    print("*******************************************\n")

    return None


def find_met(dna):
    """
    Purpose: To limit a list of RNA codons in such a way that "aug" is the first element
    Parameter(s): DNA: the inputted DNA sequence
    Return Values: dna_split_list: a list consisting of RNA codons that contain "aug"
                   "None": returned if "aug" was not in the list
                   met_first: a list in which "aug" is the first element
    """

    n = 3
    dna_list = transcription2(dna)
    dna_split_list = frame_for_met(dna)
    met_first = []

    # checking to make sure "aug" was in dna_split_list
    if not dna_split_list:
        return "None"

    # if the first codon in the codon list is not "aug", it will attempt to produce
    # a list in which it is
    if dna_split_list[0] != "aug":
        for i in range(1, len(dna_split_list)):
            if dna_split_list[i] == "aug":
                met_first.append(dna_split_list[i])
                for j in range(i + 1, len(dna_split_list)):
                    met_first.append(dna_split_list[j])
    else:
        return dna_split_list

    # a message informing the user that a protein will not be produced
    # as it is not possbile to make "aug" the first codon in the list
    if not met_first:
        print(dna_split_list)
        print("\n*******************************************")
        print("* This sequence will not create a protein *")
        print("*******************************************\n")
        return "None"

    return met_first


def dna_to_amino_acid_chain(dna):
    """
    Purpose: To convert a sequence of DNA into a chain of amino acids forming a protein
    Parameter(s): DNA: the inputted DNA sequence
    Return Values: "Please try another DNA sequence": returned if the DNA sequence can not form a protein
    """

    trans3 = []
    trans4 = []
    dna_split_list = find_met(dna)

    # checking to make sure "aug" was in dna_split_list
    if dna_split_list == "None":
        return "Please try another DNA sequence"

    # checking to see if the last element contains 3 nucleotides, if not,
    # it will be deleted, since it not only wouldn't contribute to the chain
    # it wouldn't be a key in the rna_combos dictionary
    if len(dna_split_list[-1]) % 3 != 0:
        dna_split_list = dna_split_list[:-1]

    # checking to see if a codon is not a STOP codon
    for i in range(0, len(dna_split_list)):
        if RNA_COMBOS[dna_split_list[i]] != "STOP":
            trans3.append(RNA_COMBOS[dna_split_list[i]])
        else:
            break

    # checking to see if there is another possible chain in dna_split_list,
    # and if there is, creating a new list to produce it
    for i in range(len(trans3) + 1, len(dna_split_list)):
        if dna_split_list[i] == "aug":
            trans4.append("Met")
            for j in range(i + 1, len(dna_split_list)):
                trans4.append(RNA_COMBOS[dna_split_list[j]])

    # checking to see if there is a STOP codon in the second list, and if so,
    # deleted it and everything afterwards
    if "STOP" in trans4:
        stop = trans4.index("STOP")
        del trans4[stop:]

    # checking to see if there was a second chain produced, and if so
    # printing an additional line for it
    if len(trans4) != 0:
        print("First Chain:", format_dash_list(trans3))
        print("Second Chain:", format_dash_list(trans4))
    else:
        print("Chain:", format_dash_list(trans3))


def format_dash_list(amino_acids):
    return "-".join(amino_acids)


def main():
    if len(sys.argv) != 2:
        print("Requires one and only one command line argument")
        print("Please provide a DNA sequence as a single string containing only g, t, c, and a")
        print("Example:")
        print(f"{sys.argv[0]} gatgactgtaccaggattacatggtggtcgctaaaggatgcacaatatgcgctaaagtcg")
        exit(-1)
    dna = sys.argv[1]
    result = dna_to_amino_acid_chain(dna)
    print(result)


if __name__ == "__main__":
    main()
