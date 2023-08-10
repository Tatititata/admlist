# admlist
Gale–Shapley algorithm for admission list

admission_list(applicant_list:list=[], major_dict:dict={})

This programme performs a propose-and-reject algorithm for applicants and university majors.

The programme requires a list of applicants and a dictionary of majors. 


List of applicants sample:

[['Barbie', 200, 1, 'dom_01'],
['Barbie', 288, 2, 'dom_03'],
 
['35397934', 234, 2, 'dom_02'],
['35397934', 254, 4, 'dom_01'],

['Boris', 277, 6, 'dom_03'],
['Boris', 245, 2, 'dom_02'],
['Boris', 277, 1, 'dom_01'],
            
['Alex', 248, 1, 'dom_02'],
['Alex', 285, 3, 'dom_01'],
['Alex', 255, 2, 'dom_03'],

['Ken', 248, 1, 'dom_02'],
['Ken', 255, 2, 'dom_03'],
['Ken', 276, 3, 'dom_02'],

['XXX', 246, 1, 'dom_01'],
['XXX', 246, 2, 'dom_03'],

['15931546', 244, 10, 'dom_02']]

Every applicant is a list with applicant's unique name, scores he got for a major, his preference to enter the major and the major name. 


Major dictionary sample:

{
'dom_01': 3, 
'dom_02': 1, 
'dom_03': 2
}

Major's name is 'dom_01', it has 3 vacancies to fill, etc.



This programme fills major vacancies with applicants according to their scores and desires.
The applicant with maximum score goes to his desire no1 and the applicant with minimum score and only one desire could go to unfortunate unseccessful list.

The programme with no arguments shows it's work with dict and list above.

Have fun playing with number of majors and applicants.
