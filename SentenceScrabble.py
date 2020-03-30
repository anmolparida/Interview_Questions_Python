
input_str = "xsx the dog abc is cba barking at the god idol asd dsa an i na i xsx "
input_str = " i am going to eat, ma will u also go?"

input_str = input_str.lower()

rev_input_str = input_str[::-1]
out_list = []

for word in input_str.split(" "):
    for rev_word in rev_input_str.split(" "):
        if len(word) > 1:
            if word == rev_word:
                if word[::-1] not in out_list:
                    out_list.append(word)
print(out_list)


