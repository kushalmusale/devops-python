# Mini Project — DevOps Server Info Generator
server_report = {
    "server_name": "App-Server-1",
    "server_ip": "172.31.45.12",
    "services": ["nginx", "ssh", "docker"],
    "status": "healthy"
}
print("==== SERVER REPORT ====")
for k, v in server_report.items():
    print(f"{k}: {v}")
