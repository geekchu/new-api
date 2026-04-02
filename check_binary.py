#!/usr/bin/env python3
import paramiko

HOST = "api.openclawcn.net"
USER = "root"
PASS = "Wqx505@55071901"

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(HOST, 22, USER, PASS, timeout=15)

stdin, stdout, stderr = ssh.exec_command("ls -lh /opt/new-api/new-api && file /opt/new-api/new-api && /opt/new-api/new-api --version 2>&1 | head -5")
print(stdout.read().decode())
print(stderr.read().decode())

ssh.close()
