import subprocess 
from subprocess import Popen, PIPE


status = subprocess.call(["ssh", "-i", "pass.pem", "root@IP", "hostname && uptime"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE);
ret = subprocess.Popen(["ssh", "-i", "keypass.pem", "root@IP", "hostname && upptime"], stdout=subprocess.PIPE, stderr=subprocess.PIPE);
print ret.stdout.read()
print ret.stderr.read()
