from heapq import *
'''
Solution Review: Problem Challenge 1 - Minimum Meeting Rooms (hard) 
Given a list of intervals representing the start and end time of ‘N’ meetings, 
find the minimum number of rooms required to hold all the meetings.
Example 1:
Meetings: [[1,4], [2,5], [7,9]]
Output: 2
Explanation: Since [1,4] and [2,5] overlap, we need two rooms to hold these two meetings. [7,9] can 
occur in any of the two rooms later.
Example 2:
Meetings: [[6,7], [2,4], [8,12]]
Output: 1
Explanation: None of the meetings overlap, therefore we only need one room to hold all meetings.
Example 3:
Meetings: [[1,4], [2,3], [3,6]]
Output:2
Explanation: Since [1,4] overlaps with the other two meetings [2,3] and [3,6], we need two rooms to 
hold all the meetings.
 
Example 4:
Meetings: [[4,5], [2,3], [2,4], [3,5]]
Output: 2
Explanation: We will need one room for [2,3] and [3,5], and another room for [2,4] and [4,5].
 
Here is a visual representation of Example 4:
'''

def minMeetingRooms(appts):
	roomsNeeded = 1
	# sort the arrays
	appts.sort()

	# check if any overlapping
	for i in range(len(appts)-1):
		if appts[i][1] > appts[i+1][0]:
			roomsNeeded += 1
	return roomsNeeded

print(minMeetingRooms([[6,7], [2,4], [8,12]]))

# optimize
class Meeting:
  def __init__(self, start, end):
    self.start = start
    self.end = end

  def __lt__(self, other):
    # min heap based on meeting.end
    return self.end < other.end

def minMeetingRoomsFast(appts):
	# sort the arrays
	appts.sort()

	# initialize
	minRooms = 0
	minHeap = []

	# check if any overlapping
	for appt in appts:
		while (len(minHeap) > 0 and appt[0] >= minHeap[0][1]):
			heappop(minHeap)
		heappush(minHeap, appt)
		minRooms = max(minRooms, len(minHeap))
	return minRooms

print(minMeetingRoomsFast([[6,7], [2,4], [8,12]]))
