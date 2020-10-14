class Matrix:
    myMatrix = []
    def __init__(self, matrix_string):
        self.myMatrix = []
        state1 = matrix_string.split('\n')
        for x in state1:
            state2 = x.split()              # Because I couldn't find a simpler way :(
            state3 = []
            state3.extend(map(int, state2)) # apparently you can't use the assignment operator with map?
            self.myMatrix.append(state3)    #
        

    def row(self, index):
        return self.myMatrix[index - 1]

    def column(self, index):
        temp = []
        for x in self.myMatrix:
            temp.append(x[index-1])
        return temp
