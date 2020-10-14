class School:
    everyone = {}
    def __init__(self):
        self.everyone = {}

    def add_student(self, name, grade):
        if self.everyone.get(grade) == None:
            self.everyone[grade] = [name]
        else:
            self.everyone[grade].append(name)

    def roster(self):
        output = []
        for grade in range(13):
            output.extend(sorted(self.everyone[grade] if self.everyone.get(grade) != None else []))
        return output

    def grade(self, grade_number):
        return sorted(self.everyone[grade_number] if self.everyone.get(grade_number) != None else [])
