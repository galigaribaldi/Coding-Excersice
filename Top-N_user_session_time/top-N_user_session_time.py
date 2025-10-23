"""
Top N Users by Total Session Time
EN
Given a list of session logs (user, duration), aggregate total duration per user 
and return the top N users by total time. Ignore malformed entries.

ES
Dada una lista de registros de sesión (usuario, duración), calcula la duración total por usuario 
y devuelve los N usuarios con mayor tiempo total. Ignora entradas mal formadas.

Example:
logs = [{"user": "u1", "duration": 30}, {"user": "u2", "duration": 10}, {"user": "u1", "duration": 15}]
top_n_users_by_time(logs, 2) → [("u1", 45), ("u2", 10)]
"""
def top_n_users_by_time(logs, n):
    totals = {}
    for row in logs:
        try:
            user = row["user"]
            dur = int(row["duration"])
            if dur < 0:
                continue
            totals[user] = totals.get(user, 0) + dur
        except (KeyError, ValueError, TypeError):
            continue
    return sorted(totals.items(), key=lambda x: x[1], reverse=True)[:n]

print(top_n_users_by_time(
    [{"user": "u1", "duration": 30}, {"user": "u2", "duration": 10}, {"user": "u1", "duration": 15}], 2))
