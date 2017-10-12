import requests, json
class apiController:
    def __init__(self,studentsform, assigmentform):
        self.students_list = studentsform
        self.assigment_list = assigmentform
        self.mainurl = 'http://unityddl.azurewebsites.net'
    ###########################################

    def requestpost(self, url, post_data):
        rq_url = self.mainurl + url
        response = requests.post(rq_url, post_data)
        return response.json()
    def requestget(self, url, data):

        return
    def login(self, code, password):
        data = {
            'key_code': code,
            'key_pass': password
        }
        response = self.requestpost('/login/admin',data)
        return response
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
        return
    def getformlist(self,class_id):
        self.students_list = ['Tomek Marek', 'Adam Stańczuk', 'Piotr Karolak', 'Piotr Karolak', 'Piotr Karol']
        return self.students_list
    def postformlist(self):
        return

    #############################################

    def addassigmenttolist(self):
        self.assigment_list.append('')
        return
    def deletefromassigmentlist(self):
        self.assigment_list = self.assigment_list[:-1]
        return
    def getassigmentlist(self,class_id):
        self.assigment_list = ['2C', '3A', '4D']
        return self.assigment_list
    def postassigmentlist(self, editedlist):
        return self.assigment_list
    def getpossibleclasses(self):
        classes = ['2F', '3B', '4C', '4A', '5M']
        return classes

    
