def counting(word):
    my_dict = {}
    for letter in word:
        if letter not in my_dict:
            my_dict[letter] = 1
        else:
            my_dict[letter] += 1
    return my_dict


def shortcuts(k_s_c):
    k_s_c = {"copy":"ctrl+c"
             }




def main():
    print(counting("aba"))


if __name__ == '__main__':
    main()