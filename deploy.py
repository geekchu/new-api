#!/usr/bin/env python3
import paramiko

HOST = "api.openclawcn.net"
USER = "root"
PASS = "Wqx505@55071901"
DEPLOY_DIR = "/opt/new-api"
SERVICE = "new-api"

print("· 连接服务器...")
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(HOST, 22, USER, PASS, timeout=15)

print("· 上传二进制...")
sftp = ssh.open_sftp()
sftp.put("new-api-linux", f"{DEPLOY_DIR}/{SERVICE}-new")
sftp.close()

print("· 部署...")
cmd = f"""
cd {DEPLOY_DIR}
[ -f {SERVICE} ] && cp {SERVICE} {SERVICE}.bak
chmod +x {SERVICE}-new
mv {SERVICE}-new {SERVICE}
systemctl restart {SERVICE}
sleep 5
systemctl is-active {SERVICE}
"""
stdin, stdout, stderr = ssh.exec_command(cmd)
result = stdout.read().decode()
error = stderr.read().decode()
ssh.close()

if "active" in result:
    print("✓ 部署成功")
else:
    print("✗ 失败:")
    print("stdout:", result)
    print("stderr:", error)
