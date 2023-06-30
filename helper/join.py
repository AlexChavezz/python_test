def join(questions, data):
    for i in range(len(data)):
        for j in questions:
            if data[i][0] == str(j['_id']):
                j['user_answer'] = data[i][1]
    return questions

