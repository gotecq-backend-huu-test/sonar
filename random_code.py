from HTTP_response_codes import responses, HttpResponse
import random



print(a)

@Error_Handler
def random_code(custom_note):
    print(f"This is a note: {custom_note}")
    code, description= random.choice(list(responses.items()))
    return HttpResponse(code, description)


result = random_code("Hello")
print(result)
