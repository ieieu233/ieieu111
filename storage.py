import json
def save_students(students,filename):
    with open(filename,"w",encoding="utf-8") as f:
        json.dump(students,f,ensure_ascii=False,indent=4)
def load_students(filename):
    try:
        with open(filename,"r",encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}