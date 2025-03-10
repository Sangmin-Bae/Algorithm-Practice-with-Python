'''
[문제 설명]
    - 배열을 입력받아 합으로 0을 만들 수 있는 3개의 엘리먼트를 출력하라.

[입출력 예제]
    - 입력
        - nums = [-1, 0, 1, 2, -1, -4]

    - 출력
        - [
        -   [-1, 0, 1],
        -   [-1, -1, 2]
        - ]
'''

from typing import List

class Solutions:
    # Solution 00
    def three_sum_00(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums.sort()

        for i in range(len(nums) - 2):
            first = nums[i]
            if nums[i] == nums[i - 1]:
                continue
            for j in range(len(nums[i + 1:]) - 1):
                second = nums[i + j + 1]
                for k in range(len(nums[i + j + 2:])):
                    third = nums[i + j + k + 2]

                    if first + second + third == 0:
                        results.append([first, second, third])

        return results

    # Solution 01 - 브루트 포스로 계산
    def three_sum_01(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums.sort()

        # 브루트 포스 n^3 반복
        for i in range(len(nums) - 2):
            # 중복된 값 건너뛰기
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums) - 1):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                for k in range(j + 1, len(nums)):
                    if k > j + 1 and nums[k] == nums[k - 1]:
                        continue
                    if nums[i] + nums[j] + nums[k] == 0:
                        results.append([nums[i], nums[j], nums[k]])

        return results

    # Solution 02 - 투 포인터로 합 계산
    def three_sum_02(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums.sort()

        for i in range(len(nums) - 2):
            # 중복된 값 건너뛰기
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # 간격을 좁혀가며 합 sum 계산
            left, right = i + 1, len(nums) - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
                else:
                    # sum = 0인 경우이므로 정답 및 스킵 처리
                    results.append([nums[i], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

        return results

if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, -4]

    sol = Solutions()

    print(f"Solution 00 Output : {sol.three_sum_00(nums)}")
    print(f"Solution 01 Output : {sol.three_sum_01(nums)}")
    print(f"Solution 02 Output : {sol.three_sum_02(nums)}")