import requests, json, urllib

class apiController:
    def __init__(self,studentsform, assigmentform):
        self.students_list = studentsform
        self.current_class_id = ''
        self.current_teacher_name=''
        self.mainurl = 'http://unityddl.azurewebsites.net'
    ###########################################

    def requestpost(self, url, post_data):
        rq_url = self.mainurl + url
        response = requests.post(rq_url, post_data)
        return response
    def requestget(self, url):
        rq_url = self.mainurl + url
        response = requests.get(rq_url)
        return response
    def login(self, code, password):
        data = {
            'key_code': code,
            'key_pass': password
        }
        response = self.requestpost('/login/admin',data)
        if response.status_code == 600:
            return 'error'
        else:
            return response.json()["school_id"]

    def getteachers_assingedtoclass(self,class_id,school_id):
        data =self.requestget('/school/teachers/'+school_id).json()
        contain_list = '['
        for teacher in data['teachers']:
            if class_id in teacher['classes']:
                contain_list= contain_list + '"'+ teacher['_id']+ '", '
        contain_list +=']'
        return contain_list

    #CLASSES#
    ###########################################
    def addclass(self,class_id, school_id):#done
        self.requestget('/class/create/'+class_id+'/'+school_id)
        return
    def deleteclass(self,class_id, school_id):
        teacher_list = self.getteachers_assingedtoclass(class_id,school_id)

        self.requestget('/class/remove/'+ teacher_list +'/'+ class_id +'/'+school_id)
        return
    def getclasses(self, school_id):#
        response = self.requestget('/school/classes/'+school_id)
        school_classes = list((object['class_name'] for object in response.json()['classes']))
        return school_classes
    def get_teacher_id(self, techer_name):
        return

    #TEACHERS#
    ############################################
    def addteacher(self,teacher,school_id):
        self.requestget('/school/teacher_generate/'+school_id+'/["'+teacher+'"]')
        return
    def deleteteacher(self,teacher,school_id):
        self.requestget ('/school/teacher/unregister/'+teacher+'/'+school_id)
        return
    def getteachers(self,school_id):
        teachers = self.requestget('/school/teachers/'+ school_id)
        names = list((object['name'] for object in teachers.json()['teachers']))
        ids = list((object['_id'] for object in teachers.json()['teachers']))
        return names
    def getunregistered_teachers(self,school_id):
        data = self.requestget('/school/teacher/unregistered/'+school_id).json()
        teachers_unregistered = list((object['name'] for object in data))
        return teachers_unregistered
    #STUDENTS
    ############################################

    def addtoformlist(self,element):
        self.students_list.append(element)
        return
    def deletefromformlist(self,element):
        self.students_list.remove(element)
        return
    def getformlist(self,class_id, school_id):
        data = self.requestget('/class/get/'+class_id+'/'+school_id).json()
        self.current_class_id = class_id
        self.students_list = data['students']
        return self.students_list
    def postformlist(self,school_id):
        data = {
            'class_name': self.current_class_id,
            'key_code': school_id,
            'students': self.students_list
        }
        self.requestpost('/class/changeStudents',data)
        return data

    #############################################

    def addassigmenttolist(self,element,school_id):
        self.requestget('/class/setTeacher/'+self.current_teacher_name+'/'+school_id+'/'+element)#addschool
        return
    def deletefromassigmentlist(self,element,school_id):
        self.requestget('/class/removeTeacher/'+self.current_teacher_name+'/'+school_id+'/'+element)#addschool
        return
    def getassigmentlist(self,teacher_id,school_id):
        data = self.requestget('/class/show/'+teacher_id+'/'+school_id).json()
        self.current_teacher_name = teacher_id
        assigmentlist = data['classes']
        return assigmentlist
    def getpossibleclasses(self,school_id):
        classes = self.getclasses(school_id)
        return classes
