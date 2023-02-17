from random import choices

class pcfg:
    def __init__(self, N : set, T : set, S, R : dict) -> None:
        '''
        N, T - sets of nonterminal and terminl symbols rescppectivily

        S - start symbol

        R - dictionary of type (A, alpha) : p, where A -> alpha = (X1, ..., Xn) is a production rule and p its probability
        '''
        self.N = N
        self.T = T
        self.S = S
        self.R = R 
        # rules, ordered by N 
        self.rulebook = {A : set() for A in N}
        for rule, probability in self.R.items():
            # sybol we are rewritting
            A = rule[0]
            self.rulebook[A].add((rule[1], probability))
    
    def generate(self, start=None) -> tuple:
        '''
        Generates a random string following the probability distribution, starting on start (default= self.S). 
        
        Return a generated string
        '''
        if start is None:
            start = self.S
        
        string = [start]

        nonterminals_left = True
        while nonterminals_left:
            nonterminals_left = False
            for index, A in enumerate(string):
                # skips terminals
                if A in self.T:
                    continue 
                nonterminals_left = True
                #  chose a string,
                rules = self.rulebook[A]
                tmp_string = choices(population=[list(r[0]) for r in rules], weights=[r[1] for r in rules])[0]
                new_string = string[:index] + list(tmp_string) + string[index:]
                string = new_string
            if len(string) < 20:
                print(string)
        
        return string




S = 'S'
x = 'x'
N = set(S)
T = set(x)
R = {
    (S, (S, x)) : 0.1, 
    (S, (x,)) : 0.9
}
g = pcfg(N, T, S, R)
