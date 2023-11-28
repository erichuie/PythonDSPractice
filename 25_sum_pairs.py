import math
def sum_pairs(nums, goal):
    """Return tuple of first pair of nums that sum to goal.

    For example:

        >>> sum_pairs([1, 2, 2, 10], 4)
        (2, 2)

    (4, 2) sum to 6, and come before (5, 1):

        >>> sum_pairs([4, 2, 10, 5, 1], 6) # (4, 2)
        (4, 2)

    (4, 3) sum to 7, and finish before (5, 2):

        >>> sum_pairs([5, 1, 4, 8, 3, 2], 7)
        (4, 3)

    No pairs sum to 100, so return empty tuple:

        >>> sum_pairs([11, 20, 4, 2, 1, 5], 100)
        ()
    """
    # for i in range(0,len(nums)-1):
    #     for j in range(i+1, len(nums)):
    #         if nums[i] + nums[j] == goal:
    #             return (nums[i], nums[j])
    # return ()
    curr_index_pair = []
    curr_index_difference = math.inf
    for i in range(0,len(nums)-1):
        diff_of_goal_nums = goal - nums[i]
        if diff_of_goal_nums in nums:
            if curr_index_difference > (nums.index(diff_of_goal_nums)
                                         - nums.index(nums[i])):
                curr_index_difference = (nums.index(diff_of_goal_nums)
                                         - nums.index(nums[i]))
                curr_index_pair = [diff_of_goal_nums, nums[i]]
    return tuple(curr_index_pair)



