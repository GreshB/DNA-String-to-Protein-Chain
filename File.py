def transcription1(dna):
    string = ''
    trans1 = []
    lcdna = dna.lower()
    for i in range(len(dna)):
        if lcdna[i] == 'c':
            trans1.append('g')
        if lcdna[i] == 't':
            trans1.append('a')
        if lcdna[i] == 'a':
            trans1.append('t')
        if lcdna[i] == 'g':
            trans1.append('c')

    return string.join(trans1)

def transcription2(dna):
    string = ''
    trans2 = []
    lcdna = transcription1(dna)
    for i in range(len(lcdna)):
        if lcdna[i] == 'c':
            trans2.append('c')
        if lcdna[i] == 't':
            trans2.append('u')
        if lcdna[i] == 'a':
            trans2.append('a')
        if lcdna[i] == 'g':
            trans2.append('g')

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
    trans3 = []
    n = 3
    dna_split_list = find_met(dna)
    dashlist = []

    for i in range(len(dna_split_list)):
        if dna_split_list[i] == "uuc" or dna_split_list[i] == "uuu":
            trans3.append("Phe")
        if dna_split_list[i] == "uua" or dna_split_list[i] == "uug" or dna_split_list[i] == "cuu" or dna_split_list[i] == "cuc" or dna_split_list[i] == "cua" or dna_split_list[i] == "cug":
            trans3.append("Leu")
        if dna_split_list[i] == "auu" or dna_split_list[i] == "auc" or dna_split_list[i] == "aua":
            trans3.append("Ile")
        if dna_split_list[i] == "aug":
            trans3.append("Met")
        if dna_split_list[i] == "guu" or dna_split_list[i] == "guc" or dna_split_list[i] == "gua" or dna_split_list[i] == "gug":
            trans3.append("Val")
        if dna_split_list[i] == "ucu" or dna_split_list[i] == "ucc" or dna_split_list[i] == "uca" or dna_split_list[i] == "ucg":
            trans3.append("Ser")
        if dna_split_list[i] == "ccu" or dna_split_list[i] == "ccc" or dna_split_list[i] == "cca" or dna_split_list[i] == "ccg":
            trans3.append("Pro")
        if dna_split_list[i] == "acu" or dna_split_list[i] == "acc" or dna_split_list[i] == "aca" or dna_split_list[i] == "acg":
            trans3.append("Thr")
        if dna_split_list[i] == "gcu" or dna_split_list[i] == "gcc" or dna_split_list[i] == "gca" or dna_split_list[i] == "gcg":
            trans3.append("Ala")
        if dna_split_list[i] == "uau" or dna_split_list[i] == "uac":
            trans3.append("Tyr")
        if dna_split_list[i] == "uaa" or dna_split_list[i] == "uag" or dna_split_list[i] == "uga":
            break
        if dna_split_list[i] == "cau" or dna_split_list[i] == "cac":
            trans3.append("His")
        if dna_split_list[i] == "caa" or dna_split_list[i] == "cag":
            trans3.append("Gln")
        if dna_split_list[i] == "aau" or dna_split_list[i] == "aac":
            trans3.append("Asn")
        if dna_split_list[i] == "aaa" or dna_split_list[i] == "aag":
            trans3.append("Lys")
        if dna_split_list[i] == "gau" or dna_split_list[i] == "gac":
            trans3.append("Asp")
        if dna_split_list[i] == "gaa" or dna_split_list[i] == "gag":
            trans3.append("Glu")
        if dna_split_list[i] == "ugu" or dna_split_list[i] == "ugc":
            trans3.append("Cys")
        if dna_split_list[i] == "ugg":
            trans3.append("Trp")
        if dna_split_list[i] == "cgu" or dna_split_list[i] == "cgc" or dna_split_list[i] == "cga" or dna_split_list[i] == "cgg" or dna_split_list[i] == "aga" or dna_split_list[i] == "agg":
            trans3.append("Arg")
        if dna_split_list[i] == "agu" or dna_split_list[i] == "agc":
            trans3.append("Ser")
        if dna_split_list[i] == "ggu" or dna_split_list[i] == "ggc" or dna_split_list[i] == "gga" or dna_split_list[i] == "ggg":
            trans3.append("Gly")

    for i in range(0, len(trans3)):
        if trans3[i] != trans3[-1]:
            dashlist.append(trans3[i])
            dashlist.append("-")
        else:
            dashlist.append(trans3[i])

    return "".join(dashlist)
