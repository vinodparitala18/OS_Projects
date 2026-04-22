class Process:
    def __init__(self, pid, arrival, burst):
        self.pid = pid
        self.arrival = arrival
        self.burst = burst
        self.remaining = burst
        self.completion = 0
        self.waiting = 0
        self.turnaround = 0


# -------------------------------
# FCFS Scheduling
# -------------------------------
def fcfs(processes):
    processes.sort(key=lambda x: x.arrival)
    time = 0

    for p in processes:
        if time < p.arrival:
            time = p.arrival

        p.completion = time + p.burst
        p.turnaround = p.completion - p.arrival
        p.waiting = p.turnaround - p.burst

        time += p.burst

    return processes


# -------------------------------
# SJF Scheduling (Non-preemptive)
# -------------------------------
def sjf(processes):
    completed = []
    time = 0
    n = len(processes)
    ready = []

    processes.sort(key=lambda x: x.arrival)

    while len(completed) < n:
        for p in processes:
            if p.arrival <= time and p not in ready and p not in completed:
                ready.append(p)

        if ready:
            ready.sort(key=lambda x: x.burst)
            current = ready.pop(0)

            current.completion = time + current.burst
            current.turnaround = current.completion - current.arrival
            current.waiting = current.turnaround - current.burst

            time += current.burst
            completed.append(current)
        else:
            time += 1

    return completed


# -------------------------------
# Round Robin Scheduling
# -------------------------------
def round_robin(processes, quantum):
    queue = []
    time = 0
    completed = []
    processes.sort(key=lambda x: x.arrival)

    while True:
        for p in processes:
            if p.arrival <= time and p not in queue and p.remaining > 0:
                queue.append(p)

        if not queue:
            if all(p.remaining == 0 for p in processes):
                break
            time += 1
            continue

        current = queue.pop(0)

        exec_time = min(quantum, current.remaining)
        current.remaining -= exec_time
        time += exec_time

        for p in processes:
            if p.arrival <= time and p not in queue and p.remaining > 0 and p != current:
                queue.append(p)

        if current.remaining > 0:
            queue.append(current)
        else:
            current.completion = time
            current.turnaround = current.completion - current.arrival
            current.waiting = current.turnaround - current.burst
            completed.append(current)

    return completed


# -------------------------------
# Helper: Print Results
# -------------------------------
def print_results(processes):
    print("\nPID\tAT\tBT\tCT\tWT\tTAT")
    for p in processes:
        print(f"{p.pid}\t{p.arrival}\t{p.burst}\t{p.completion}\t{p.waiting}\t{p.turnaround}")

    avg_wt = sum(p.waiting for p in processes) / len(processes)
    avg_tat = sum(p.turnaround for p in processes) / len(processes)

    print(f"\nAverage Waiting Time: {avg_wt:.2f}")
    print(f"Average Turnaround Time: {avg_tat:.2f}")


# -------------------------------
# Main
# -------------------------------
if __name__ == "__main__":
    processes = [
        Process("P1", 0, 5),
        Process("P2", 1, 3),
        Process("P3", 2, 8),
    ]

    print("\n--- FCFS ---")
    fcfs_result = fcfs([Process(p.pid, p.arrival, p.burst) for p in processes])
    print_results(fcfs_result)

    print("\n--- SJF ---")
    sjf_result = sjf([Process(p.pid, p.arrival, p.burst) for p in processes])
    print_results(sjf_result)

    print("\n--- Round Robin (q=2) ---")
    rr_result = round_robin([Process(p.pid, p.arrival, p.burst) for p in processes], 2)
    print_results(rr_result)