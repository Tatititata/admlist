def admission_list(applicant_list:list=[], major_dict:dict={}):
    """
    This function gets a dictionary of majors: keys are major names (str type) and values are number of vacancies (int type)
    dictionary sample: {'major_01': 4, 'major_02': 20}
    The applicant list consists of lists with applicant name (str type), applicant score for the major (int type), 
    applicant's preferency for this major (int type) and major name (str type) from the dictionary of majors.
    """
    if len(applicant_list) == 0 or len(major_dict) == 0:
        print('This function requires a dictionary of majors and a list of applicants')
        print('such as:')
        print('\nmajors with number of vacancies\n')
        majors = {
            'dom_01': 3,
            'dom_02': 1,
            'dom_03': 2
            }
        print(majors)
        abiturient_list = [
            ['Barbie', 200, 1, 'dom_01'],
            ['Barbie', 288, 2, 'dom_03'],
            
            ['35397934', 234, 2, 'dom_02'],
            ['35397934', 254, 4, 'dom_01'],

            ['Boris', 277, 6, 'dom_03'],
            ['Boris', 245, 2, 'dom_02'],
            ['Boris', 277, 1, 'dom_01'],
            
            ['Alex', 248, 1, 'dom_02'],
            ['Alex', 285, 3, 'dom_01'],
            ['Alex', 255, 2, 'dom_03'],

            ['Ken', 248, 1, 'dom_01'],
            ['Ken', 255, 2, 'dom_03'],
            ['Ken', 276, 3, 'dom_02'],

            ['XXX', 246, 1, 'dom_01'],
            ['XXX', 246, 2, 'dom_03'],

            ['15931546', 244, 10, 'dom_02']
            ]

        print('\napplicants with score and preferency for every major\n')
        for abiturient in abiturient_list:
            print(abiturient)
        
    else:
        majors = major_dict
        abiturient_list = applicant_list
        

    print('\nBefore filling up the majors are empty:\n')
    for dom in majors:
        majors[dom] = {i: [0, 0, 0, ''] for i in range(majors[dom])}#preparing a dict of all majors with vacanses ready to be filled
        print(dom, len(majors[dom]), majors[dom])


    abiturient_ID_unique = list()#list of unique IDs
    for abitur in abiturient_list:
        abiturient_ID_unique.append(abitur[0])
    abiturient_ID_unique = list(set(abiturient_ID_unique))

    unsuccessfull_list = list()

    def check_place(student):

        dom = student[3]
        for i in range(len(majors[dom])): # all vacant places in major
            if student[1] >= majors[dom][i][1]: # comparing student scores
                if student[1] == majors[dom][i][1] and i == len(majors[dom])-1:
                    print('Warning!')
                    print(majors[dom][len(majors[dom])-1], 'and', student)
                    print('both have the same score and claim last vacancy in', student[3])
                    print(majors[dom][len(majors[dom])-1], 'is set to another priority')
                pop = majors[dom][len(majors[dom])-1] # securing last in the que

                for j in range(len(majors[dom])-1, i, -1):
                    majors[dom][j] = majors[dom][j-1] # moving students to the tail
                majors[dom][i] = student#insert the student into major
                return(pop) # last in the que
        return(student) # the student does not fit the major


    def first_priority(student_id):
        person_priorities = list()
        for abiturient in abiturient_list:
            if abiturient[0] == student_id:
                person_priorities.append(abiturient) # list of all person priorities, may be unsorted
        person_priorities = sorted(person_priorities, key = lambda x: x[2])#sorted
        return person_priorities[0]


    for abit in abiturient_ID_unique:
        success = check_place(first_priority(abit))
        while success != [0, 0, 0, '']: # if the applicant have not filled the major
            person_priorities = list()
            for abiturient in abiturient_list:
                if abiturient[0] == success[0]:
                    person_priorities.append(abiturient) # list of all applicant's priorities, may be unsorted
            priorities = sorted(person_priorities, key = lambda x: x[2]) # sorted
            for item in priorities:#checking new priority for the applicant
                if item[2] == success[2]:
                    priority_index = (priorities.index(item)) + 1
                    if priority_index == len(priorities): # if there is no priority left the applicant goes to unsuccessfull list
                        unsuccessfull_list.append(item[0])
                        success = [0, 0, 0, '']
                    else:
                        success = check_place(priorities[priority_index]) # checking vacancy in major of next priority
                        break

    print('\nMajors are filled up with applicants:\n')
    for dom in majors:
        print('\n')
        print(dom, len(majors[dom]))
        for d in majors[dom]:
            print(majors[dom][d])

           
    print('\nTotal number of applicants:', len(abiturient_ID_unique), '\n\n')
    print('List of unsucsessful applicants:')
    print(unsuccessfull_list)
