def maxmin():
    user_list = list(
        map(int, input("Please list the numbers separated by a space ").split()))
    min = user_list[0]
    max = user_list[0]
    for item in user_list:
        if item <= min:
            min = item
        if item >= max:
            max = item
    return (f"[{min},{max}]")


def main():
    a = maxmin()
    print(a)


main()
