class course_info:
    def __init__(self, course_number='none'):
        self.course_number = course_number
        self.current_room_number = ''
        self.current_instructor = ''
        self.current_meeting_time = ''
    def get_course_info(self):
        dic_courses = {
            'CSC101': {
                'Room Number': 3004,
                'Instructor': 'Haynes',
                'Meeting Time': '8:00 a.m.'
            },
            'CSC102': {
                'Room Number': 4501,
                'Instructor': 'Alvarado',
                'Meeting Time': '9:00 a.m.'
            },
            'CSC103': {
                'Room Number': 6755,
                'Instructor': 'Rich',
                'Meeting Time': '10:00 a.m.'
            },
            'NET110': {
                'Room Number': 1244,
                'Instructor': 'Burke',
                'Meeting Time': '11:00 a.m.'
            },
            'COM241': {
                'Room Number': 1411,
                'Instructor': 'Lee',
                'Meeting Time': '1:00 p.m.'
            },
        }
        self.current_room_number = dic_courses[self.course_number]["Room Number"]
        self.current_instructor = dic_courses[self.course_number]["Instructor"]
        self.current_meeting_time = dic_courses[self.course_number]["Meeting Time"]
    def print_course_info(self):
        print('Current Room Number: ',self.current_room_number)
        print('Current Instructor: ',self.current_instructor)
        print('Current Meeting Time: ',self.current_meeting_time)
if __name__ == "__main__":
    #Create an instance of the Course info class
    #This will prompt the use to enter a course number
    c1 = course_info(input("Enter course number: "))
    c1.get_course_info()
    c1.print_course_info()