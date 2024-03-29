'''
Problem Statement 
Given a list of non-overlapping intervals sorted by their start time, insert a given interval at the correct position and merge all necessary intervals to produce a list that has only mutually exclusive intervals.
Example 1:
Input: Intervals=[[1,3], [5,7], [8,12]], New Interval=[4,6]
Output: [[1,3], [4,7], [8,12]]
Explanation: After insertion, since [4,6] overlaps with [5,7], we merged them into one [4,7].
Example 2:
Input: Intervals=[[1,3], [5,7], [8,12]], New Interval=[4,10]
Output: [[1,3], [4,12]]
Explanation: After insertion, since [4,10] overlaps with [5,7] & [8,12], we merged them into [4,12].
Example 3:
Input: Intervals=[[2,3],[5,7]], New Interval=[1,4]
Output: [[1,4], [5,7]]
Explanation: After insertion, since [1,4] overlaps with [2,3], we merged them into one [1,4].
'''

def insertInterval(appts, newAppt):
	finalIntervals = []
	# insert
	for i in range(len(appts)):
		firstInNew = newAppt[0]
		if appts[i][0] < firstInNew and appts[i+1][0] > firstInNew:
			print("add")
			appts.insert(i+1, newAppt)
			break;
	print(appts)

	# merge intervals
	for i in range(len(appts)-1):
		if appts[i][1] > appts[i+1][0]:
			finalIntervals.append([appts[i][0], appts[i+1][1]])
		else:
			finalIntervals.append(appts[i])

	return finalIntervals

print(insertInterval([[1,3], [5,7], [8,12]], [4,6]))

