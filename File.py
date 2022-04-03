#!/usr/bin/env python3

import sys

def transcription1(dna):
    '''
    Purpose: To reinact the first stage of DNA transcription with an inputted DNA sequence
    Parameter(s): DNA: the inputted DNA sequence
    Return Values: string.join(trans1) a string of the new DNA sequence
    '''

    string = ''
    trans1 = []
    lcdna = dna.lower()
    transcription_map = {
        'c' : 'g',
        't' : 'a',
        'a' : 't',
        'g' : 'c',
    }

    # creates a string that converts the DNA sequenence
    for i in range(len(dna)):
        trans1.append(transcription_map[lcdna[i]])
    return string.join(trans1)

def transcription2(dna):
    '''
    Purpose: To reinact the second stage of DNA transcription with an inputted DNA sequence
    Parameter(s): DNA: the inputted DNA sequence
    Return Values: trans2_stirng: a string of RNA based on the initial DNA sequence
    '''

    string = ''
    trans2 = []
    lcdna = transcription1(dna)
    transcription_map = {
        'c' : 'g',
        't' : 'a',
        'a' : 'u',
        'g' : 'c',
    }

    # creates a string that converted the DNA sequence into RNA
    for i in range(len(dna)):
        trans2.append(transcription_map[lcdna[i]])

    trans2_string = string.join(trans2)

    # makes sure the length of the string is divisible by 3 due to later neccessities
    while len(trans2_string) % 3 != 0:
        trans2_string = trans2_string[:-1]

    return trans2_string

def frame_for_met(dna):
    '''
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
    '''

    n = 3
    dna_list = transcription2(dna)
    dna_split_list = [dna_list[i:i+n] for i in range(0, len(dna_list), n)]
    dna_split_list2 = [dna_list[i:i+n] for i in range(1, len(dna_list), n)]
    dna_split_list3 = [dna_list[i:i+n] for i in range(2, len(dna_list), n)]
    met_first = []

    # rearranging the codon list to find an element "aug", if it cannot be found,
    # a message informing the user that a protein will not be produced
    # as it is not possbile to make "aug" the first codon in the list
    if "aug" not in dna_split_list:
        if "aug" not in dna_split_list2:
            if "aug" not in dna_split_list3:
                print("\n*******************************************")
                print("* This sequence will not create a protein *")
                print("*******************************************\n")
            else:
                return dna_split_list3
        else:
            return dna_split_list2
    else:
        return dna_split_list

def find_met(dna):
    '''
    Purpose: To limit a list of RNA codons in such a way that "aug" is the first element
    Parameter(s): DNA: the inputted DNA sequence
    Return Values: dna_split_list: a list consisting of RNA codons that contain "aug"
                   "None": returned if "aug" was not in the list
                   met_first: a list in which "aug" is the first element
    '''

    n = 3
    dna_list = transcription2(dna)
    dna_split_list = frame_for_met(dna)
    met_first = []

    # checking to make sure "aug" was in dna_split_list
    if dna_split_list == None:
        return "None"

    # if the first codon in the codon list is not "aug", it will attempt to produce
    # a list in which it is
    if dna_split_list[0] != "aug":
        for i in range(1, len(dna_split_list)):
            if dna_split_list[i] == "aug":
                met_first.append(dna_split_list[i])
                for j in range(i+1, len(dna_split_list)):
                    met_first.append(dna_split_list[j])
    else:
        return dna_split_list

    # a message informing the user that a protein will not be produced
    # as it is not possbile to make "aug" the first codon in the list
    if met_first == []:
        print(dna_split_list)
        print("\n*******************************************")
        print("* This sequence will not create a protein *")
        print("*******************************************\n")
        return "None"

    return met_first

def dna_to_amino_acid_chain(dna):
    '''
    Purpose: To convert a sequence of DNA into a chain of amino acids forming a protein
    Parameter(s): DNA: the inputted DNA sequence
    Return Values: "Please try another DNA sequence": returned if the DNA sequence can not form a protein
    '''

    rna_combos = {
        'aaa': 'Lys',
        'aac': 'Asn',
        'aag': 'Lys',
        'aau': 'Asn',
        'aca': 'Thr',
        'acc': 'Thr',
        'acg': 'Thr',
        'acu': 'Thr',
        'aga': 'Arg',
        'agc': 'Ser',
        'agg': 'Arg',
        'agu': 'Ser',
        'ucu': 'Ser',
        'ucg': 'Ser',
        'uca': 'Ser',
        'ucc': 'Ser',
        'aua': 'Ile',
        'auc': 'Ile',
        'aug': 'Met',
        'auu': 'Ile',
        'caa': 'Gln',
        'cac': 'His',
        'cag': 'Gln',
        'cau': 'His',
        'cca': 'Pro',
        'ccc': 'Pro',
        'ccg': 'Pro',
        'ccu': 'Pro',
        'cga': 'Arg',
        'cgc': 'Arg',
        'cgg': 'Arg',
        'cgu': 'Arg',
        'cua': 'Leu',
        'cuc': 'Leu',
        'cug': 'Leu',
        'cuu': 'Leu',
        'gaa': 'Glu',
        'gac': 'Asp',
        'gag': 'Glu',
        'gau': 'Asp',
        'gca': 'Ala',
        'gcc': 'Ala',
        'gcg': 'Ala',
        'gcu': 'Ala',
        'gga': 'Gly',
        'ggc': 'Gly',
        'ggg': 'Gly',
        'ggu': 'Gly',
        'gua': 'Val',
        'guc': 'Val',
        'gug': 'Val',
        'guu': 'Val',
        'uaa': 'STOP',
        'uac': 'Tyr',
        'uag': 'STOP',
        'uau': 'Tyr',
        'uga': 'STOP',
        'ugc': 'Cys',
        'ugg': 'Trp',
        'ugu': 'Cys',
        'uuc': 'Phe',
        'uug': 'Leu',
        'uuu': 'Phe',
        'uua': 'Leu'
    }

    trans3 = []
    trans4 = []
    n = 3
    dashlist = []
    dashlist2 = []
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
        if rna_combos[dna_split_list[i]] != "STOP":
            trans3.append(rna_combos[dna_split_list[i]])
        else:
            break

    # formating the chain to have dashes between the amino acids
    for i in range(0, len(trans3)):
        if i != len(trans3) - 1:
            dashlist.append(trans3[i])
            dashlist.append("-")
        else:
            dashlist.append(trans3[i])

    # checking to see if there is another possible chain in dna_split_list,
    # and if there is, creating a new list to produce it
    for i in range(len(trans3)+1, len(dna_split_list)):
        if dna_split_list[i] == "aug":
            trans4.append("Met")
            for j in range(i+1, len(dna_split_list)):
                trans4.append(rna_combos[dna_split_list[j]])

    # checking to see if there is a STOP codon in the second list, and if so,
    # deleted it and everything afterwards
    if "STOP" in trans4:
        stop = trans4.index("STOP")
        del trans4[stop:]

    # formating the second chain to have dashes between the amino acids
    for i in range(0, len(trans4)):
        if i != len(trans4) - 1:
            dashlist2.append(trans4[i])
            dashlist2.append("-")
        else:
            dashlist2.append(trans4[i])

    # checking to see if there was a second chain produced, and if so
    # printing an additional line for it
    if len(dashlist2) != 0:
        print("First Chain:","".join(dashlist))
        print("Second Chain:","".join(dashlist2))
    else:
        print("Chain:","".join(dashlist))



if __name__ == '__main__':
    dna = sys.argv[1]
    result = dna_to_amino_acid_chain(dna)
    print(result)
