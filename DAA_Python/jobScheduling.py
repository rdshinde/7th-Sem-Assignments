#Job Scheduling alogrithm

def jobScheduling(jobs, n):
    # Sort the jobs according to their finish time
    jobs.sort(key = lambda x: x[1])

    # To store the selected jobs
    selectedJobs = []

    # Select the first job
    selectedJobs.append(jobs[0])

    # Iterate through the remaining jobs
    for i in range(1, n):
        # If the start time of the current job is greater than or equal to the finish time of the previously selected job, then select the current job
        if jobs[i][0] >= selectedJobs[-1][1]:
            selectedJobs.append(jobs[i])

    # Print the selected jobs
    for job in selectedJobs:
        print(job[2], end = " ")

# Driver code
jobs = [[1, 2, 'a'], [3, 5, 'b'], [0, 6, 'c'], [5, 7, 'd'], [5, 9, 'e'], [7, 8, 'f']]
n = len(jobs)
jobScheduling(jobs, n)