# DetectX-AI Day 9: Final Data Science Dashboard
# Install: pip install matplotlib

import matplotlib.pyplot as plt

# Sample data from your hacker_logs.txt
# In real project, this will read from file
threat_data = {
    'SAFE Logins': 12,
    'SQL Injection Attempts': 7,
    'XSS Attacks': 4,
    'Weak Passwords': 5
}

risk_levels = {
    'LOW': 12,
    'MEDIUM': 5,
    'HIGH (Blocked)': 11
}

# --- Graph 1: Types of Attacks ---
plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.bar(threat_data.keys(), threat_data.values(), color=['green', 'red', 'orange', 'yellow'])
plt.title('🛡️ DetectX-AI: Threat Analysis')
plt.xticks(rotation=15)
plt.ylabel('Number of Attempts')

# --- Graph 2: Risk Level Pie Chart ---
plt.subplot(1, 2, 2)
colors = ['#2ecc71', '#f1c40f', '#e74c3c']
plt.pie(risk_levels.values(), labels=risk_levels.keys(), autopct='%1.1f%%', colors=colors)
plt.title('Risk Distribution')

plt.tight_layout()
plt.savefig('attack_report.png')
print("✅ Graph Saved: attack_report.png")
plt.show()

print("\n--- 📊 Day 9 Final Report ---")
print(f"Total Logins Checked: {sum(threat_data.values())}")
print(f"Threats Blocked: {risk_levels['HIGH (Blocked)']}")
print(f"System Safety: 95.8%")
print("\n👩‍💻 Project by Anjana | AEGYTHON 2026 | 9 Days Streak COMPLETED! 🔥")
