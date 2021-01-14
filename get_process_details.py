import paramiko
import time
with open("devicelist.txt") as fp:
	lines=fp.readlines()
count=1
with open(out.txt) as ot:
	for host in lines:
		hostname=host.strip()
		print(hostname)
		ssh=paramiko.SSHClient()
		ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		ssh.connect(hostname,port=22,username="username",password="")
		ssh_stdin, ssh_stdout, ssh_stderr =ssh.exec_command("ps -A | grep 'process1\|process2\|process3",get_pty=True)
		opt=ssh_stdout.readlines()
		opt="".join(opt)
		print(opt+" "+str(count))
		ot.writelines(hostname+"\n\n")
		ot.writelines(opt+"$")
		ssh_stdin,ssh_stdout,ssh_stderr=ssh.exec_command(chr(26))
		ssh_stdin,ssh_stdout,ssh_stderr=ssh.exec_command("exit")
		ssh_stdin.flush()
		ssh_stdin.close()
		ssh.close()
with open("out.txt") as fp:
	data="".join(fp.readlines()).split('$')


