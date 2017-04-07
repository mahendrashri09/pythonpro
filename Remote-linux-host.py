import subprocess 
from subprocess import Popen, PIPE


#ret = subprocess.call(["ssh", "-i", "pass.pem", "root@75.101.199.181", "hostname && uptime"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE);
ret = subprocess.Popen(["ssh", "-i", "pass.pem", "root@75.101.199.181", "hostname && upptime"], stdout=subprocess.PIPE, stderr=subprocess.PIPE);
print ret.stdout.read()
print ret.stderr.read()
