import json

subj = {}
with open('text_6.txt', 'r') as init_f:
    for line in init_f:
        subject, lecture, practice, lab = line.split()
        lecture = lecture[:-3]
        if lecture == '':
            lecture = 0
        practice = practice[:-4]
        if practice == '':
            practice = 0
        lab = lab[:-5]
        if lab == '':
            lab = 0
        subj[subject] = float(lecture) + float(practice) + float(lab)
print(f'Общее количество часов по предметам - {subj}')
