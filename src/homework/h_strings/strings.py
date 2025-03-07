def get_hamming_distance(dna1, dna2): 
    "Calculates the Hamming distance between two DNA strands."
    if len(dna1) != len(dna2): 
        raise ValueError("DNA strands must be of equal length") 
    
    distance = 0 
    for i in range(len(dna1)):
        if dna1[i] != dna2[i]:
            distance += 1
        return distance 
    
def get_dna_complement(dna):
    "Return the complement of a DNA strand."
    complement = " "
    for nucleotide in dna:
        if nucleotide == 'A':
            complement += 'T'
        elif nucleotide == 'T':
            complement += 'A'
        elif nucleotide == 'C':
            complement += 'G'
        elif nucleotide == 'G':
            complement += 'C'
    return complement[::-1] #Reverse the sequence
    