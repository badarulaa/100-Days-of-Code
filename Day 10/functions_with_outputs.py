def format_name(f_name, l_name):
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"{formatted_f_name} {formatted_l_name}"

print(format_name("rOgER","LalER"))



def function_1(text):
    return text + text

def function_2(text):
    return text.title()

print(function_2(function_1("halo")))