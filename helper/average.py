def get_average(questions):
    total = 0
    try:
        for i in questions:
            if i['user_answer'] == i['right_answer']:
                total += 1
    except Exception as e:
        print(e)
        return 0
    return total / len(questions) * 100