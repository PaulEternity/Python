def process_student_info(info):
    try:
        student_info = info.split()
        if len(student_info) != 5:
            raise ValueError()
        student_id = student_info[0]
        if len(student_id) != 4 or not student_id.isdigit():
            raise ValueError()
        name = student_info[1]
        if not name.isalpha() or len(name) > 10:
            raise ValueError()
        scores = [int(score) for score in student_info[2:]]
        for score in scores:
            if score < 0:
                raise ValueError()
        avg_score = sum(scores) / len(scores)
        return (student_id, name, scores, avg_score)
    except ValueError:
        raise ValueError("学生信息格式有误")

def sort_students(students):
    students.sort(key=lambda x: (x[3], x[2][0]), reverse=True)
    return students

try:
    n = input()
    if not n.isdigit() or int(n) <= 1 or int(n) > 100:
        raise ValueError("输入的人数必须是数字，大于1并且小于等于100")
    n = int(n)

    student_list = []
    for _ in range(n):
        student_info = input("请输入学生信息：")
        student = process_student_info(student_info)
        student_list.append(student)

    sorted_students = sort_students(student_list)

    for student in sorted_students:
        student_id, name, scores, avg_score = student
        score_str = ' '.join(str(score) for score in scores)
        print(f"{student_id} {name} {score_str} {avg_score:.2f}")

except ValueError as e:
    print(str(e))