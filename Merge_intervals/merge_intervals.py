"""
Merge Intervals
EN
Given a list of intervals, merge all overlapping intervals into one combined list.

ES
Dada una lista de intervalos, combina todos los intervalos superpuestos en una lista unificada.

Example:
merge_intervals([[1,3],[2,6],[8,10],[15,18]]) → [[1,6],[8,10],[15,18]]
"""
def merge_intervals(intervals):
    if not intervals:
        return []
    ivs = sorted(intervals, key=lambda x: x[0])
    merged = [ivs[0][:]]
    for start, end in ivs[1:]:
        if start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    return merged

print(merge_intervals([[1,3],[2,6],[8,10],[15,18]]))
