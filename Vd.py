import re
import hashlib
from datetime import datetime

# --- DetectX-AI Day 8: Advanced Guardian with Logs ---

def check_threats(username, password):
    risk_score = 0
    reasons = []

    # SQL Injection Patterns
    sql_patterns = ["' OR '1'='1", "' OR 1=1", "admin'--", "'--", "' OR", "DROP TABLE"]
    for pattern in sql_patterns:
        if pattern.lower() in password.lower() or pattern.lower() in username.lower():
            risk_score += 80
            reasons.append(f"SQL Injection Detected: {pattern}")

    # XSS Patterns
    xss_patterns = ["<script>", "</script>", "<img", "onerror=", "alert("]
    for pattern in xss_patterns:
        if pattern.lower() in password.lower() or pattern.lower() in username.lower():
            risk_score += 70
            reasons.append(f"XSS Attack Detected: {pattern}")

    # Weak Password Check
    if len(password) < 8:
        risk_score += 20
        reasons.append("Weak Password: Less than 8 chars")

    # Final Risk Level
    if risk_score >= 70:
        level = "HIGH 🔴 - BLOCKED"
    elif risk_score >= 20:
        level = "MEDIUM 🟡 - SUSPICIOUS"
    else:
        level = "LOW 🟢 - SAFE"
    
    return risk_score, level, reasons

def save_log(username, level, score):
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{time}] User: {username} | Risk: {level} | Score: {score}\n"
    with open("hacker_logs.txt", "a") as f:
        f.write(log_entry)
    print(f"Log saved -> {log_entry}")

# --- MAIN DEMO ---
print("--- 🛡️ DetectX-AI Day 8 Dashboard ---")
user = input("Enter Username: ")
pwd = input("Enter Password: ")

score, level, reasons = check_threats(user, pwd)

print(f"\nRisk Score: {score}")
print(f"Status: {level}")
if reasons:
    print("Reasons:")
    for r in reasons:
        print(f" - {r}")

# Save to logs (This is Data Science part!)
save_log(user, level, score)

if "BLOCKED" in level:
    print("\n🚫 ACCESS DENIED - Threat Logged!")
else:
    print("\n✅ ACCESS GRANTED")
