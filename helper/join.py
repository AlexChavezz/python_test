def join(questions, data):
    for i in range(len(data)):
        for j in questions:
            # verificar si el id de la pregunta existe en el id de la respuesta
                if data[i][0] == str(j['_id']):
                    j['user_answer'] = data[i][1]
                else:
                    if 'user_answer' not in j:
                        j['user_answer'] = None
    return questions

