""" 
QUESTION: You’re given a list of meeting intervals, where each interval is defined by a start time and an end time (intervals[i] = [startᵢ, endᵢ]). Determine whether it’s possible for one person to attend every meeting without any overlaps.

Example 1:

Input: intervals = [[0,30],[5,10],[15,20]]
Output: false
Example 2:

Input: intervals = [[7,10],[2,4]]
Output: true
Constraints:

0 <= intervals.length <= 10^4
Each interval has exactly two elements (intervals[i].length == 2)
0 <= startᵢ < endᵢ <= 10^6

"""
# Solution one -  O(n^2)
def can_attend_meetings(intervals):
    for i in range(len(intervals)):
        for j in range(i + 1, len(intervals)):
            interval_1_start = intervals[i][0]  
            interval_1_end = intervals[i][1]  
            interval_2_start = intervals[j][0]  
            interval_2_end = intervals[j][1]  

            if (
                interval_1_start >= interval_2_start
                and interval_1_start < interval_2_end
                or interval_2_start >= interval_1_start
                and interval_2_start < interval_1_end
            ):
                return False

    return True


# print(can_attend_meetings([[0, 30], [5, 10], [15, 20]]))  # False
# print(can_attend_meetings([[7, 10], [2, 4]]))  # True

# -------------------------------


# Solution two - sorted array -  O(n log n)
def can_attend_meetings_2(intervals):
    intervals.sort()  # Python runs a variation of quick sort which is O(n log n)
    print(intervals)
    for i in range(len(intervals) - 1):  # O(n)
        if intervals[i][1] > intervals[i + 1][0]:
            return False

    return True


print(can_attend_meetings_2([[0, 30], [5, 10], [15, 20]]))  # False
print(can_attend_meetings_2([[7, 10], [2, 4]]))  # True