def twoSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                result = [i, j]
                return result

def check_int_number():
    """
    Проверяем является ли символ целым числом.
    :return:
    """
    pass

def get_numbers(string):
    """
    Из строки получаем числа
    -10^9 <= number <= 10^9
    -10^9 <= target <= 10^9
    :return: List[int]
    """
    numbers = string.split(', ')
    for num in numbers:
        print(num)
    return  numbers

def check_exit(string):
    """
    Функция выхода из программы
    :param string:
    :return:
    """
    if string == 'Q' or string == 'q':
        return False
    else:
        return True


if __name__ == '__main__':
    run = True

    while run:
        print('Enter numbers, segregate with , ')
        numbers = input()
        print('Enter the target number')
        target = int(input())

        nums = get_numbers(numbers)

        print('Press Q to exit, and any to continue')
        state = input()
        run = check_exit(state)

