import paramiko

ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect(hostname='10.1.1..1',port=8080,username='zhangyu',password='123456')

stdin,stdout,stderr = ssh.exec_command('cd')

out, err = stdout.read(), stderr.read()

result = out if out else err
print(result.decode())
