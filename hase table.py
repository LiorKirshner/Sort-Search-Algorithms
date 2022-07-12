def main():
    table = [[] for i in range(9)]

    my_input = [5,28,19,15,20,33,12,17,10]

    for i in my_input:
        table[i%9].append(i)

    for element in table:
        for sub_element in element:
            print(sub_element)

    #print(table)



if __name__ == '__main__':
    main()