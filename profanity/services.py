from profanity_service.profanity import profanity_array, profanity


def get_profanity_matrix(request):
    text_array = extract_array_from_article_body_json(request.data['data'])
    result, profane = profanity_array(text_array)

    # call the profanity service
    return {"result": result, "profane": profane}


def extract_array_from_article_body_json(article_body):
    text_array = []
    for text in article_body:
        if text['type'] == 'header':
            text_array.append(text['data']['text'])
        if text['type'] == 'list':
            text_array.append(text['data']['items'][0])
        if text['type'] == 'paragraph':
            text_array.append(text['data']['text'])
    return text_array


def check_string_profanity(request):
    a = profanity(request.data['string'])
    return a
