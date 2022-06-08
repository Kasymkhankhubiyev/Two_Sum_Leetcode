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

def get_numbers():
    """
    Из строки получаем числа
    -10^9 <= number <= 10^9
    -10^9 <= target <= 10^9
    :return: List[int]
    """
    pass


if __name__ == '__main__':

    print('Enter numbers, segregate with , ')
    numbers = input()
    print('Enter the target number')
    target = int(input())
