import paramiko
import os

hostname = '192.168.0.58'
username = 'root'
password = os.environ.get('password')

key = paramiko.RSAKey.generate(2048)
private_key_path = os.path.expanduser('~/.ssh/id_rsa')
public_key_path = os.path.expanduser('~/.ssh/id_rsa.pub')

key.write_private_key_file(private_key_path)
with open(public_key_path, 'w') as f:
    f.write(f'ssh-rsa {key.get_name()} {key.get_base64()}')
print(f"SSH密钥对已生成并保存到 {private_key_path} 和 {public_key_path}")
try:
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname, username=username, password=password)
    with open(public_key_path, 'r') as f:
        public_key = f.read().strip()
    ssh.exec_command(f'mkdir -p ~/.ssh && echo "{public_key}" >> ~/.ssh/authorized_keys && chmod 600 ~/.ssh/authorized_keys && chmod 700 ~/.ssh')
    print("公钥已成功添加到目标服务器的 ~/.ssh/authorized_keys 文件中")
except Exception as e:
    print(f"发生错误: {e}")
finally:
    ssh.close()