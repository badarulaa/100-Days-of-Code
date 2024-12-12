def calculate_love_score(name1, name2):
    combined_string = name1 + name2
    lower_case = combined_string.lower()

    t = lower_case.count("t")
    r = lower_case.count("r")
    u = lower_case.count("u")
    e = lower_case.count("e")

    true = t + r + u + e

    l = lower_case.count("l")
    o = lower_case.count("o")
    v = lower_case.count("v")
    e = lower_case.count("e")

    love = l + o + v + e

    score = int(str(true) + str(love))
    print(score)

calculate_love_score("Kanye West", "Kim Kardashian")