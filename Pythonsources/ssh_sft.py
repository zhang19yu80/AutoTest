import paramiko

transport = paramiko.Transport(('10.1.1.1',8080))
transport.connect(username='zhangyu',password='123456')

sftp = paramiko.SFTPClient.from_transport(transport)

sftp.put('/zz/bb/cc','/rr/tt/yy')

sftp.get('/remote/path','/local/path')
