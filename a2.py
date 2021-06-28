"""CSCA08 Assignment 2, Fall 2017
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
 Date: December 1, 2017
"""


class GeneticSequence():
    ''' This class represents a genetic sequence. '''

    def __init__(self):
        ''' (GeneticSequence) -> NoneType
        Creates a new DNA genetic sequence for a client and
        initializes new dictionaries of chromosomes and markers
        into the genetic sequence.
        '''

        # Initializing new dictionaries for chromosomes and markers
        self._chromes = {}
        self._marks = {}

    def set_by_pos(self, num_pair, num_pos, chromo_pair):
        ''' (GeneticSequence, int, int, str) -> NoneType
        This function sets individual pairs of nucleotides
        into a dictionary of chromosomes with designated pair number,
        position number, and the chromosome pair that can be retrieved
        in the future.
        REQ: chromo_pair should consist of {'A', 'T', 'C', 'G'}
        '''

        # Initializes new key to the dictionary of chromosomes inside
        # the GeneticSequence object and refer to the method in
        # Chromosome to initialize another key to the dictionary of
        # nucleotide pairs.
        self._chromes[num_pair] = set_by_pos(num_pos, chromo_pair)

    def set_marker(self, marker, num_pair, num_pos):
        ''' (GeneticSequence, str, int, int) -> NoneType
        This function sets a marker of user's choice to a
        designated pair number, position number of a chromosome
        inside chromosomes dictionary.
        REQ: None
        '''

        # Set marker to a tuple of pair number and position number
        marker = (num_pair, num_pos)

    def set_by_marker(self, marker, chromo_pair):
        ''' (GeneticSequence, str, str) -> NoneType
        This function sets a marker of user's choice to a specific
        chromosome pair inside chromosomes dictionary.
        REQ: chromo_pair should consist of {'A', 'T', 'C', 'G'}
        '''

        # Set marker refer to the specific chromosome pair
        # inside dictionary of markers
        self._marks[marker] = chromo_pair

    def get_by_pos(self, num_pair, num_pos):
        ''' (GeneticSequence, int, int) -> str
        This functions finds and returns the chromosome of user's choice
        at a designated pair number and position number inside
        chromosomes dictionary.
        REQ: num_pair and num_pos should be greater than or equal to 0
        '''

        # Find the chromosome by pair number and position number
        find_chromo = self._chromes[num_pair]
        find_chromo.get_by_pos(num_pos)

        # Return the chromosome pair that has been found
        return find_chromo

    def get_by_marker(self, marker):
        ''' (GeneticSequence, str) -> str
        This function finds and returns the chromosome of user's choice
        that is paired with a specific marker inside the marker dictionary.
        REQ: None
        '''

        # Find the chromosome by marker
        find_chromo = marks[marker]

        # Return the chromosome pair that has been found
        return find_chromo

    def get_chromosome(self, num_pair):
        ''' (GeneticSequence, int) -> Chromosome
        This functions finds and returns the whole Chromosome object
        of user's choice at a designated pair number inside
        chromosomes dictionary.
        REQ: num_pos should be valid number; i.e. positive integer
        '''

        # Return the chromosome
        return self._chromes[num_pair]

    def set_chromose(self, num_pair, chromo):
        ''' (GeneticSequence, int, Chromosome) -> NoneType
        This function mutates the chromose of chromosome inside the
        chromosomes dictionary at a given pair number.
        REQ: chromo should consist of {'A', 'T', 'C', 'G'}
        '''

        # Mutate the chromose inside a chromosome at a given pair number
        self._chromes[num_pair] = set_by_pos(Chromosome)


class Chromosome():
    ''' This class represents a chromosome. '''

    def __init__(self):
        ''' (Chromosome) -> NoneType
        Initializes new Chromosome object.
        '''

        # Creates new dictionary that holds nucleotides
        self._nucleotides = {}

    def set_by_pos(self, num_pos, chromo_pair):
        ''' (Chromosome, int, str) -> NoneType
        This function sets and maps a chromosome pair
        at a given position number.
        REQ: chromo_pair should consist of {'A', 'T', 'C', 'G'}
        '''

        # Adds new key of chromosome pair to the nucleotides dictionary
        self._nucleotides[num_pair] = chromo_pair

    def set_by_pos(self, chromo):
        ''' (Chromosome, Chromosome) -> NoneType
        This fuction sets and maps a Chromosome object to the
        nucleotides dictionary of Chromosome.
        REQ: None
        '''

        # Adds new Chromosome object to the nucleotides dictionary
        self._nucleotides.update(Chromosome)

    def get_by_pos(self, num_pos):
        ''' (Chromosome, int) -> str
        This function finds and returns the chromosome pair at
        a given position number inside the nucleotides dictionary.
        REQ: num_pos should be valid number; i.e. positive integer
        '''

        # Returns the nucleotides at a specific position number
        return self._nucleotides[num_pos]


class Client(GeneticSequence):
    ''' This class represents a client, created by inheritence
    inheriting attributes/methods from GeneticSequence. '''

    def __init__(self, identification):
        ''' (Client, str) -> NoneType
        Creates a client with an identification number.
        REQ: None
        '''

        # Use inheriting method from GeneticSequence class to create Client
        GeneticSequence.__init__(self)

        # Store identification number inside Client
        self._id = identification

    def test(self, query):
        ''' (Client, query) -> bool
        This function query an individual's genetic sequence.
        Query is a way of asking whether a certain pattern exists
        within the client's genetic sequence. Using the special query
        sequence created from the Query class, this function tests
        whether the given query sequence exists within the client's
        DNA. This function either returns True, False, or may get
        rejected depending on several occasions.
        REQ: query must be valid
        '''


class Male(Client):
    ''' This class represents a male client, created by inheritence
    inheriting attributes/methods from Client.
    '''


class Female(Client):
    ''' This class represents a female client, created by inheritence
    inheriting attributes/methods from Client and only extending
    the ones we need.
    '''

    def procreate(self, father, binder):
        ''' (Female, Male, Binder) -> Client
        Creates an offspring with a Male and a Binder.
        REQ: binder must have at least one attribute inside
        '''

        # Creates an offspring genetic sequence with corresponding sex
        if (binder._sex == "F"):
            offspring = Female()
        else:
            offspring = Male()

        # For every key of binder
        for i in binder.keys():
            # For every key of key of binder
            for j in binder[i].keys():
                # For every value of key of key of binder
                for k in binder[i][j].keys():
                    # Give temporary variable names
                    # to show what each represents
                    num_pair = i
                    num_pos = j
                    maternal = k

                    # If binder has left-maternal chromosome pair
                    if (maternal == "LM"):
                        # Get mother's chromosome pair
                        mother_chrome = self._chromes.get_by_pos(num_pair,
                                                                 num_pos)
                        # The child gets the left nucleotide of the
                        # mother's chromosome
                        left_maternal = mother_chrome[0]
                        # Get father's chromosome pair
                        father_chrome = father._chromes.get_by_pos(num_pair,
                                                                   num_pos)
                        # The child gets the right nucleotide of the
                        # father's chromosome
                        right_paternal = father_chrome[1]

                        # Child gets the chromosome of the parents'
                        # nucleotides inside its genetic sequence
                        # with corresponding pair number and position number
                        child_chrome = left_maternal + right_paternal
                        offspring.set_by_pos(num_pair, num_pos, child_chrome)
                    # If binder has right-maternal chromosome pair
                    elif (maternal == "RM"):
                        # Get mother's chromosome pair
                        mother_chrome = self._chromes.get_by_pos(num_pair,
                                                                 num_pos)
                        # The child gets the right nucleotide of the
                        # mother's chromosome
                        right_maternal = mother_chrome[1]
                        # Get father's chromosome pair
                        father_chrome = father._chromes.get_by_pos(num_pair,
                                                                   num_pos)
                        # The child gets the left nucleotide of the
                        # father's chromosome
                        left_paternal = father_chrome[0]

                        # Child gets the chromosome of the parents'
                        # nucleotides inside its genetic sequence
                        # with corresponding pair number and position number
                        child_chrome = right_maternal + left_paternal
                        offspring.set_by_pos(num_pair, num_pos, child_chrome)
                    # If the binder does not have item at the current key,
                    # nothing happens to the offspring's genetic sequence
                    else:
                        pass

        # Return the offspring that has been created
        return offspring


class Binder(GeneticSequence):
    ''' This class represents a binder, which is a genetic sequence
    where each nucleotides comes from each parent by building binding
    chromosomes that can set a given position or marker to be either
    left-maternal, the child gets the mother's left nucleotide and
    father's right, or right-maternal, the child gets the fathers
    left nucleotide and the mother's rightcreated by inheritence
    inheriting attributes/methods from GeneticSequence and only
    extending the ones we need. '''

    def set_sex(self, sex):
        ''' (Binder, str) -> NoneType
        Assign a sex for offspring.
        REQ: sex belongs to: {"F" or "M"}
        '''

        # Create and sex attribute inside the object itself
        # which determines the sex of the offspring created by this binder
        self._sex = sex

    def set_by_pos(self, num_pair, num_pos, maternal):
        ''' (Binder, int, int, str) -> NoneType
        Set a chromosome at a given pair number and a position number
        to be either left maternal or right maternal.
        REQ: num_pair and num_pos must be greater than or equal to 0
        REQ: maternal belongs to: {"LM" or "RM"}
        '''

        # Initializes new key to the dictionary of chromosomes inside
        # the Binder object and refer to the method in Chromosome to
        # initialize another key to the dictionary of nucleotide pairs.
        self._chromes[num_pair] = set_by_pos(num_pos, maternal)


class Query(GeneticSequence):
    ''' This class represents a query, created by inheritence
    inheriting attributes/methods from GeneticSequence. '''
