def main():

    original_str = 'Python Programming'
    ##################################################
    # Comlete your code here
    ##################################################
    sub1 = str(original_str.split(' ')[0])
    sub2 = str(original_str.split(' ')[1])
    merged_str = f'{sub2} {sub1}'
    print(sub2)
    print(sub1)
    print(merged_str)

    #########################################
    # Do not delete the return statement
    return sub1, sub2, merged_str


if __name__ == '__main__':
    main()
