class StudentNotFoundError(Exception):
    pass
def add_student(students,name,score):
    if name in students:
        return "学生已存在"
    if not isinstance(score,int) or score<0 or score>100 or score==True or score==False:
        return "成绩无效"
    students[name]=score
    return "添加成功"

def get_score(students,name):
    if name in students:
        return students[name]
    raise StudentNotFoundError("暂无学生信息")

def show_students(students):
    if not students:
        return "暂无学生信息"
    return students

def analyze_scores(students):
    if not students:
        return "暂无学生信息"
    total=0
    min_score=101
    max_score=0
    for name,score in students.items():
        if score<min_score:
            min_score=score
            min_name=name
        if score>max_score:
            max_score=score
            max_name=name
        total+=score
    average=total/len(students)
    return {
        "average":average,
        "max_name":max_name,
        "max_score":max_score,
        "min_name":min_name,
        "min_score":min_score
        }
def update_score(students,name,new_score):
    if name not in students:
        return "学生不存在"
    
    if not isinstance(new_score,int) or new_score<0 or new_score>100 or isinstance(new_score,bool):
        return "成绩无效"
    students[name]=new_score
    return "修改成功"
def delete_student(students,name):
    if name not in students:
        return "学生不存在"
    del students[name]
    return "删除成功"