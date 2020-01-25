import subprocess

#inspired from https://github.com/janoliver/i3-py-scripts
def dmenu(content, l=20):
    dmenu = subprocess.Popen(['/usr/bin/dmenu','-i','-l', str(l)],
                             stdin=subprocess.PIPE,
                             stdout=subprocess.PIPE)
    content_str = ('\n'.join(sorted(content)))# .encode('utf-8')
    out, _ = dmenu.communicate(content_str)
    out = out.decode('utf-8')
    out.rstrip()
    return out
