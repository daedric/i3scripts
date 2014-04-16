import time
import tempfile
import os
import stat
import i3


# This has been inspired from i3minator
def i3exec(cmd, sleep=0.1, root=None):
  print "Execute: {}".format(cmd)
  with tempfile.NamedTemporaryFile("w") as temp:
    if root:
      temp.file.write("cd {}\n".format(root))
    temp.file.write(cmd + "\n")
    temp.file.close()
    current_stats = os.stat(temp.name)
    os.chmod(temp.name, current_stats.st_mode | stat.S_IEXEC)
    i3.command("exec", temp.name)
    time.sleep(sleep)


