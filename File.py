def transcription1(dna):
    string = ''
    trans1 = []
    lcdna = dna.lower()
    transcription_map = {
        'c' : 'g',
        't' : 'a',
        'a' : 't',
        'g' : 'c',
    }
    for i in range(len(dna)):
        trans1.append(transcription_map[lcdna[i]])
    return string.join(trans1)

def transcription2(dna):
    string = ''
    trans2 = []
    lcdna = transcription1(dna)
    transcription_map = {
        'c' : 'g',
        't' : 'a',
        'a' : 'u',
        'g' : 'c',
    }
    for i in range(len(dna)):
        trans2.append(transcription_map[lcdna[i]])

    return string.join(trans2)

def frame_for_met(dna):
    n = 3
    dna_list = transcription2(dna)
    dna_split_list = [dna_list[i:i+n] for i in range(0, len(dna_list), n)]
    dna_split_list2 = [dna_list[i:i+n] for i in range(1, len(dna_list), n)]
    dna_split_list3 = [dna_list[i:i+n] for i in range(2, len(dna_list), n)]
    met_first = []
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
    n = 3
    dna_list = transcription2(dna)
    dna_split_list = frame_for_met(dna)
    met_first = []
    if dna_split_list[0] != "aug":
        for i in range(1, len(dna_split_list)):
            if dna_split_list[i] == "aug":
                met_first.append(dna_split_list[i])
                for j in range(i+1, len(dna_split_list)):
                    met_first.append(dna_split_list[j])
                return (met_first)
    else:
        return (dna_split_list)

def dna_to_amino_acid_chain(dna):
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
        'uuu': 'Phe'
    }

    trans3 = []
    trans4 = []
    n = 3
    dashlist = []
    dashlist2 = []
    dna_split_list = find_met(dna)

    for i in range(0, len(dna_split_list)):
        if rna_combos[dna_split_list[i]] != "STOP":
            trans3.append(rna_combos[dna_split_list[i]])
        else:
            break

    for i in range(0, len(trans3)):
        if i != len(trans3) - 1:
            dashlist.append(trans3[i])
            dashlist.append("-")
        else:
            dashlist.append(trans3[i])

    for i in range(len(trans3)+1, len(dna_split_list)):
        if dna_split_list[i] == "aug":
            trans4.append("Met")
            for j in range(i+1, len(dna_split_list)):
                trans4.append(rna_combos[dna_split_list[j]])

    for i in range(len(trans4)):
        if trans4[i] == "STOP":
            del trans4[i:]

    for i in range(0, len(trans4)):
        if i != len(trans4) - 1:
            dashlist2.append(trans4[i])
            dashlist2.append("-")
        else:
            dashlist2.append(trans4[i])

    if len(dashlist2) != 0:
        print("First Chain:","".join(dashlist))
        print("Second Chain:","".join(dashlist2))
    else:
        print("Chain:","".join(dashlist))

if __name__ == '__main__':
    dna = sys.argv[1]
    result = dna_to_amino_acid_chain(dna)
    print(result)
