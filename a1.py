"""CSCA08 Assignment 1, Fall 2017
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
 Date: November 12, 2017
"""


def pair_genes(first_gene, second_gene):
    ''' (str, str) -> bool
    Genes can be paired together by allowing the nucleotides from
    the first gene to pair-bond with the nucleotides from the second gene.
    Guanine will pair with cytosine, and adenine will pair with thymine.
    Genes can also pair in either direction. This function takes in two
    string representations of genes and returns a boolean that indicates
    whether the two genes can pair or not.
    REQ: genes must be consisted of letters {A, G, C, T}
    >>> pair_genes("TCAG", "AGTC")
    True
    >>> pair_genes("TCAG", "CTGA")
    True
    >>> pair_genes("TCAG", "CCAG")
    False
    '''

    # declare a boolean that indicates whether the two genes are pairable
    can_pair = False

    # create a sample of gene that can pair
    sample_gene = ""
    for nucleotide in first_gene:
        if (nucleotide == "A"):
            sample_gene += "T"
        elif (nucleotide == "T"):
            sample_gene += "A"
        elif (nucleotide == "G"):
            sample_gene += "C"
        else:
            sample_gene += "G"

    # check if the sample gene matches the second gene
    if (second_gene == sample_gene):
        can_pair = True

    # genes can also pair either direction
    if (second_gene[::-1] == sample_gene):
        can_pair = True

    # returns the boolean that indicates whether the two genes can pair
    return can_pair


def zip_length(gene):
    ''' (str) -> int
    Genes can partially pair with itself in a process called zipping.
    Zipping occurs when at either end of a gene can form a pair bond,
    and continues until the pair of nucleotides can no longer form a bond.
    Guanines pair with cytosines, and adenines pair with thymines.
    This function returns an integer value that indicates the maximum
    number of nucleotides pairs that the gene can zip.
    REQ: genes must be consisted of letters {A, G, C, T}
    >>> zip_length("AGTCTCGCT")
    2
    >>> zip_length("AGTCTCGAG")
    0
    '''

    # declare a variable that counts the zip length
    zip_length_count = 0

    # for loop that is in charge of each nucleotides from the left
    for left_index in range(len(gene)):
        # declare a variable that is in charge of the indices of
        # each nucleotides from the right
        right_index = len(gene) - 1 - left_index
        # checks if either end of the gene can form a bond
        if (gene[left_index] == "A" and gene[right_index] == "T"):
            zip_length_count += 1
        elif (gene[left_index] == "C" and gene[right_index] == "G"):
            zip_length_count += 1
        elif (gene[left_index] == "G" and gene[right_index] == "C"):
            zip_length_count += 1
        elif (gene[left_index] == "T" and gene[right_index] == "A"):
            zip_length_count += 1
        # once the gene can no longer zip,
        # returns the zip length right away
        else:
            return zip_length_count


def splice_gene(source, destination, start_anchor, end_anchor):
    ''' (list, list, str, str) -> None
    This function performs splicing of gene sequences.
    Splicing of genes can be done by taking a nucleotide sequence
    from one gene and replace it with a nucleotide sequence from another.
    First, find the anchor sequences, which are the sequences found
    within the starting and end anchor given by the user (anchors can be
    found from either end of the gene). Then, if the starting anchor and
    the end anchor is found in both genes, the anchor sequence extracted
    from the source (the first gene) replaces the anchor sequence from
    the destination (the second gene). If the anchor is not found in
    both genes, the splice or the mutation does not occur.
    REQ: the anchors must be consisted of letters {A, G, C, T}
    '''

    # convert the source gene into a string
    source_gene = ""
    for i in range(len(source)):
        source_gene += source[i]

    # convert the destination gene into a string
    destination_gene = ""
    for j in range(len(destination)):
        destination_gene += destination[j]

    # find the index of start and end anchor from the source
    source_start_anchor = source_gene.find(start_anchor)
    source_end_anchor = source_gene.find(end_anchor, source_start_anchor)

    # start and end anchor can be found in reverse order
    if (source_start_anchor == -1 and source_end_anchor == -1):
        source_start_anchor = source_gene.rfind(start_anchor)
        source_end_anchor = source_gene.rfind(end_anchor,
                                              source_start_anchor)

    # find the index of start and end anchor from the destination
    destination_start_anchor = destination_gene.find(start_anchor)
    destination_end_anchor = destination_gene.find(end_anchor,
                                                   destination_start_anchor)

    # start and end anchor can be found in reverse order
    if (destination_start_anchor == -1 and destination_end_anchor == -1):
        destination_start_anchor = destination_gene.rfind(start_anchor)
        destination_end_anchor = destination_gene.rfind(
            end_anchor, destination_start_anchor)

    # check if the indices are found in source gene
    if (source_start_anchor != -1 and source_end_anchor != -1):
        # check if the indices are found in destination gene
        if (destination_start_anchor != -1 and destination_end_anchor != -1):
            # for loop to find the anchor sequence from the source
            source_anchor_sequence = ""
            for i in range(source_start_anchor,
                           source_end_anchor + len(end_anchor)):
                source_anchor_sequence += source[i]
            # remove the nucleotides of anchor sequence from the source
            count = 0
            while (count < len(source_anchor_sequence)):
                del source[source_start_anchor]
                count += 1
            # for loop to find the anchor sequence from the destination
            destination_anchor_sequence = ""
            for i in range(destination_start_anchor,
                           destination_end_anchor + len(end_anchor)):
                destination_anchor_sequence += destination[i]
            # remove the nucleotides from start and end anchor from
            # the destination
            count = 0
            while (count < len(destination_anchor_sequence)):
                del destination[destination_start_anchor]
                count += 1
            # splice the anchor sequence into the destination
            for l in range(len(source_anchor_sequence) - 1, -1, -1):
                destination.insert(destination_start_anchor,
                                   source_anchor_sequence[l])
        # if not found, splice does not occur
        else:
            pass
    # if not found, splice does not occur
    else:
        pass


def match_mask(gene, mask):
    ''' (str, str) -> int
    This function creates a mask to find a specific pattern in the gene.
    Masks can pair with parts of genes, but does not necessarily pair
    with the entire gene. Masks can be consisted of multis which are
    the special nucleotides, represented inside square brackets,
    that can mimic the bonding behaviour of multiple nucleotides.
    It can also create a nucleotide that is capapble of pairing with
    any other nucleotide, called stars. In addition, if there are
    repeated sequences of nucleotides in masks, it can be denoted
    by using numbers. An example of a mask would be [AG]C3*, which
    can be paired with any gene sequences that starts with T or C,
    followed by three G, followed by any other nucleotides.
    This function will take in a string representation of a gene,
    and a mask, and returns the index of the first nucleotide in
    the sequence that is matched by the given mask. If it is not
    found anywhere in the sequence, it returns -1.
    REQ: masks are strings consisted of '[', ']', numbers, and '*'
    REQ: the letters inside the square brackets, should be
    consisted of letters {A, G, C, T}
    REQ: masks cannot start with integers
    >>> match_mask("CCCAGGGGTT", "[TC]G")
    3
    >>> match_mask("CCCAGGGGTT", "*")
    0
    >>> match_mask("CCCCGGGG", "A")
    -1
    '''

    # declare a variable for set of nucleotides and integers
    nucleotides = "AGCT"
    numbers = "123456789"

    # declare a variable that is in charge of keeping the index
    # of the first nucleotide in gene that matches mask
    match_index = -1

    # declare variables that make a gene sequence from the mask
    # four mask off gene sequences since there are four types of nucleotides
    mask_off = []

    # for loop to read through the mask
    for index in range(len(mask)):
        # star is a special character that can pair with any nucleotides
        if (mask[index] == "*"):
            mask_off.append(nucleotides)
        # nucleotides pair with specific nucleotides
        elif (mask[index] in nucleotides):
            # adenine pairs with thymine
            if (mask[index] == "A"):
                mask_off.append("T")
            # thymine pairs with adenine
            elif (mask[index] == "T"):
                mask_off.append("A")
            # cytosine pairs with guanine
            elif (mask[index] == "C"):
                mask_off.append("G")
            # guanine pairs with cytosine
            else:
                mask_off.append("C")
        # repeated sequences of nucleotides can be denoted using numbers
        elif (mask[index] in numbers):
            # multiple adenines
            if (mask[index - 1] == "A"):
                mask_off.extend("A" * int(mask[index]))
            # multiple thymines
            elif (mask[index - 1] == "T"):
                mask_off.extend("T" * int(mask[index]))
            # multiple cytosine
            elif (mask[index - 1] == "C"):
                mask_off.extend("C" * int(mask[index]))
            # multiple guanine
            else:
                mask_off.extend("G" * int(mask[index]))
        # masks can have special nucleotides called multis
        else:
            mask_start = mask.find("[")
            mask_end = mask.rfind("]")
            # for loop to get the multis inside the bracket
            multis = ""
            # get the multi from the mask
            for m in range(index + 1, mask_end):
                multis += mask[m]
            # convert multis into pairable nucleotides
            multi_pair = ""
            # for loop to go through the multis
            for multi in range(len(multis)):
                # adenine pairs with thymine
                if (multis[multi] == "A"):
                    multi_pair += "T"
                # thymine pairs with adenine
                elif (multis[multi] == "T"):
                    multi_pair += "A"
                # cytosine pairs with guanine
                elif (multis[multi] == "C"):
                    multi_pair += "G"
                # guanine pairs with cytosine
                else:
                    multi_pair += "C"

            # add multi_pair to the mask off list
            mask_off.append(multi_pair)

    # remove multis from the mask
    for i in range(mask_end + 1):
        del mask_off[mask_start+1]

    # declare a boolean that indicates whether the gene matches the mask
    match = False

    # temporary counter
    g = 0
    # while loop to go through the gene while matching index is not found
    while(not match and g < len(gene)):
            # if the element in mask off gene is a single letter
            if (len(mask_off[g]) == 1):
                # check if the nucleotide is the same as the elemnet
                # in mask off gene
                if (mask_off[g] == gene[g]):
                    match_index = g
                    match = True
            # if the element in mask off gene is not a single letter
            else:
                if (gene[g] in mask_off[g]):
                    match_index = g
                    match = True
            g += 1

    # return the the first matching index of the gene
    return match_index


def process_gene_file(file_handle, gene, mask):
    ''' (io.TextIOWrapper, str, str) -> tuple
    Takes in a file handle for a file containing one gene per line,
    a string representing a gene and a string representing a mask.
    Then, it returns a tuple (p, m, z) where p is the first gene that can
    pair with the input gene string, m is the first gene that matches
    the mask, and z is the longest gene zip found up in any gene up to
    and including the point where both p and m were found. If no genes
    match the given gene or mask, -1 is returned in place of p or m.
    REQ: file should not be empty
    REQ: genes must be consisted of letters {A, G, C, T}
    REQ: masks are strings consisted of '[', ']', numbers, and '*'
    REQ: the letters inside the square brackets, should be
    consisted of letters {A, G, C, T}
    REQ: masks cannot start with integers
    '''
