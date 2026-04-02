#!/usr/bin/env python3
import paramiko

HOST = "api.openclawcn.net"
USER = "root"
PASS = "Wqx505@55071901"

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(HOST, 22, USER, PASS, timeout=15)

stdin, stdout, stderr = ssh.exec_command("systemctl status new-api --no-pager -l")
print(stdout.read().decode())
print(stderr.read().decode())

ssh.close()
