class apiController:
    def __init__(self,studentsform):
        self.students_list = studentsform
    #CLASSES#
    ###########################################
    def addclass(self,class_id, school_id):

        return
    def deleteclass(self,class_id, school_id):

        return
    def getclasses(self, school_id):
        classes = ['2F', '3B', '4C', '4A', '5M']
        return classes

    #TEACHERS#
    ############################################
    def addteacher(self,school_id):

        return
    def deleteteacher(self,school_id):

        return
    def getteachers(self,school_id):
        teachers = ['Tomek Marek', 'Adam Stańczuk', 'Piotr Karolak']
        return teachers
    #STUDENTS
    ############################################

    def addtoformlist(self,element):
        self.students_list.append(element)
        return
    def deletefromformlist(self,element):
        self.students_list.remove(element)
        return self.students_list
    def getformlist(self,class_id):
        self.students_list = ['Tomek Marek', 'Adam Stańczuk', 'Piotr Karolak', 'Piotr Karolak', 'Piotr Karol']
        return self.students_list
    def postformlist(self):
        return self.students_list

    
