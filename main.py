from student import(
    add_student,
    get_score,
    show_students,
    analyze_scores,
    update_score,
    delete_student
)
from storage import(
    save_students,
    load_students
)
from pathlib import Path


def main():
    BASE_DIR = Path(__file__).resolve().parent
    filename = BASE_DIR / "students.json"
    students = load_students(filename)
    while True:
        print("====学生管理系统====")
        print("1. 添加学生")
        print("2. 查询成绩")
        print("3. 显示所有学生")
        print("4. 分析成绩")
        print("5. 修改成绩")
        print("6. 删除学生")
        print("0. 退出系统")
        choice=input("请输入你的选择：")
        if choice=="1":
            name=input("请输入学生姓名：")
            try:
                score=int(input("请输入学生成绩："))
            except ValueError:
                print("请输入有效的整数")
                continue 
            result=add_student(students,name,score)
            print(result)
            if result=="添加成功":
                save_students(students,filename)
        elif choice=="2":
            print(get_score(students,input("请输入学生姓名：")))
        elif choice=="3":
            print(show_students(students))  
        elif choice=="4":
            print(analyze_scores(students))
        elif choice=="5":
            name=input("请输入要修改成绩的学生姓名：")
            try:
                new_score=int(input("请输入成绩："))
            except ValueError:
                print("请输入有效的整数")
                continue    
            result=update_score(students,name,new_score)
            print(result)
            if result=="修改成功":
                save_students(students,filename)
        elif choice=="6":
            name=input("请输入要删除的学生姓名：")
            result=delete_student(students,name)
            print(result)
            if result=="删除成功":
                save_students(students,filename)
        elif choice=="0":
            print("退出系统")
            break
        else:
<<<<<<< HEAD
            print("功能开发中(master)")        
=======
            print("功能开发中(feature-menu)")        
>>>>>>> feature-menu
if __name__=="__main__":
    main()

# feature-sort 分支：开发成绩排序功能