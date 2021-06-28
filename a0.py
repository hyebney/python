""" CSCA08 Assignment 0, Fall 2017
 I hereby agree that the work contained herein is solely my work and that I
 have not received any external help from my peers, nor have I used any
 resources not directly supplied by the course in order to complete this
 assignment. I have not looked at anyone else's solution, and no one has
 looked at mine. I understand that by adding my name to this file, I am
 making a formal declaration, and any subsequent discovery of plagiarism
 or other academic misconduct could result in a charge of perjury in
 addition to other charges under the academic code of conduct of the
 University of Toronto Scarborough Campus
 Name: Hyebeen Jung
 UtorID: junghyeb
 Student Number: 1004346512
 Date: October, 7, 2017
"""


def split_input(dna):
    ''' (str) -> list
    Takes in a DNA sequence and returns a list with three elements:
    the upstream data, the gene, and the downstream data.
    REQ: dna must be consisted of letters {A, G, C, T}
    >>> split_input("ACTATGAACATGA")
    ['ACT', 'ATGAAC', 'ATGA']
    >>> split_input("ACTATGAAC")
    ['ACT', 'ATGAAC', '']
    '''

    # creates an empty list
    sequence = ["", "", ""]

    # assigns a starting codon
    spliter = "ATG"

    # splits the DNA sequence in three elements
    if dna.find(spliter) == -1:
        sequence[0] = dna
        return sequence

    sequence = dna.split(spliter, 2)
    if (len(sequence) == 2):
        sequence[1] = spliter + sequence[1]
        sequence.append("")
    else:
        sequence[1] = spliter + sequence[1]
        sequence[2] = spliter + sequence[2]

    # returns the list
    return sequence


def get_gene(dna):
    ''' (str) -> str
    Takes in a DNA sequence and returns a string
    representation of the gene.
    REQ: dna must be consisted of letters {A, G, C, T}
    >>> get_gene("ACTATGAACATGA")
    'ATGAAC'
    >>> get_gene("")
    'ERROR'
    '''

    # creates a list of DNA sequence in three elements
    sequence = split_input(dna)

    # returns the string representation of the gene
    if (sequence[1] == ""):
        return "ERROR"
    else:
        return str(sequence[1])


def validate_gene(gene):
    ''' (str) -> bool
    Takes in a string representation of gene and
    returns a boolean that indicates the validity of the gene.
    >>> validate_gene("ATGAAC")
    True
    >>> validate_gene("ATG")
    False
    >>> validate_gene("ATGAA")
    False
    >>> validate_gene("ATGCCCC")
    False
    '''
    # set valid to true
    validity = True

    # check if the gene starts with ATG
    req1 = gene.startswith("ATG")

    # check if it contains at least one more codon after
    req2 = (len(gene) >= 6)

    # check if it only contains full codons
    req3 = (len(gene) % 3 == 0)

    # check if it does not contain four consecutive identical nucleotides
    req4 = (gene.count('A') <= 3)
    req4 = (gene.count('G') <= 3)
    req4 = (gene.count('C') <= 3)
    req4 = (gene.count('T') <= 3)

    # returns the validity in boolean
    validity = req1 and req2 and req3 and req4
    return validity


def is_palindromic(gene):
    ''' (str) -> bool
    Checks if the given gene is palindromic.
    >>> is_palindromic("ATGAAAGTA")
    True
    >>> is_palindromic("ATGACATTG")
    False
    '''
    # returns a boolean that indiciates whether it is palindromic or not
    return gene == gene[::-1]


def evaluate_sequence(dna):
    ''' (str) -> str
    Evalautes a DNA sequence and returns an appropriate message.
    >>> evaluate_sequence("")
    'No Gene Found'
    >>> evaluate_sequence("ATG")
    'Invalid Gene'
    >>> evaluate_sequence("ATGAAC")
    'Valid Gene Found'
    >>> evaluate_sequence("ATGAAAGTA")
    'Valid Palindromic Gene Found'
    '''

    if (get_gene(dna) == "ERROR"):
        return "No Gene Found"
    elif (validate_gene(dna)):
        if (is_palindromic(dna)):
            return "Valid Palindromic Gene Found"
        else:
            return "Valid Gene Found"
    else:
        return "Invalid Gene"
