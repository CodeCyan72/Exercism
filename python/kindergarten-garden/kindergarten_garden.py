meaning = {'V':"Violets", 'C':"Clover", 'R':"Radishes", 'G':"Grass"}

class Garden:
    diagram = []
    students = []
    def __init__(self, diagram, students = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Fred', 'Ginny', 'Harriet', 'Ileana', 'Joseph', 'Kincaid', 'Larry']):
        self.diagram = diagram.split('\n')
        self.students = sorted(students)

    def plants(self, query):
        myIndex = self.students.index(query)
        plants = ''
        for array in self.diagram:
            plants += array[2*myIndex:(2*myIndex + 2)]
        output = [meaning.get(letter) for letter in plants]
        return output
