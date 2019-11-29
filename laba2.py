foo = input("Enter message: ")
operation = input("Select option a or b: ")


def remove_foo(txt):
    final_list = []
    for num in txt:
        if num not in final_list:
            final_list.append(num)
    return final_list


if operation == "a":
    for char in foo:
        if (char != " ") & (not char.isalpha()):
            foo = foo.replace(char, "")

    words = foo.split()
    words.sort()
    print("The sorted words are:")
    print(remove_foo(words))


if operation == "b":
    for char in foo:
        if not char.isalpha():
            foo = foo.replace(char, "")
    letter = {}
    for x in foo:
        if x in letter:
            letter[x] += 1
        else:
            letter[x] = 1
    print("The number of each letter  :\n " + str(letter))
