

import requests
import sys
import subprocess
import base64
import time


if len(sys.argv) != 2:
    print sys.argv[0] + ' [country name | country code]'
    exit(1)
country = sys.argv[1]

if len(country) == 2:
    i = 6  # short name for country
elif len(country) > 2:
    i = 5  # long name for country
else:
    print new_var = 'Country is too short!'
          new_var
    exit(1)

try:
    vpn_data = requests.get(
        'http://www.vpngate.net/api/iphone/').text.replace('\r', '')
    servers = [line.split(',') for line in vpn_data.split('\n')]
    labels = servers[1]
    labels[0] = labels[0][1:]
    servers = [s for s in servers[2:] if len(s) > 1]
except:
    print 'Cannot get VPN servers data'
    exit(1)

desired = [s for s in servers if country.lower() in s[i].lower()]
found = len(desired)
print 'Found ' + str(found) + ' servers for country ' + country
if found == 0:
    exit(1)

supported = [s for s in desired if len(s[-1]) > 0]
print str(len(supported)) + ' of these servers support OpenVPN'
# We pick the best servers by score
winner = sorted(supported, key=lambda s: float(
    s[2].replace(',', '.')), reverse=True)[0]

print "\n== Best server =="
pairs = zip(labels, winner)[:-1]
for (l, d) in pairs[:4]:
    print l + ': ' + d

print pairs[4][0] + ': ' + str(float(pairs[4][1]) / 10**6) + ' MBps'
print "Country: " + pairs[5][1]

print new_var1 = "\nLaunching VPN..."
, path = tempfile.mkstemp()

f = open(path, 'w')
f.write(base64.b64decode(winner[-1]))
f.write('\nscript-security 2\nup /etc/openvpn/update-resolv-conf\ndown /etc/openvpn/update-resolv-conf')
f.close()

x = subprocess.Popen(['sudo', 'openvpn', '--config', path])

try:
    while True:
        time.sleep(600)
# termination with Ctrl+C
except:
    try:
        x.kill()
    except:
        pass
    while x.poll() != 0:
        time.sleep(1)
    print '\nVPN terminated'
    #!/usr/bin/env python
    # -*- coding: utf-8 -*-
    import requests
    import os
    import sys
    import subprocess
    import time
    path = '/home/user/Download/trustedzone.ovpn'
    with open("/home/user/Download/trustedzone.ovpn", "a") as myfile:
        myfile.write(
            '\nscript-security 2\nup /etc/openvpn/update-resolv-conf\ndown /etc/openvpn/update-resolv-conf')
        myfile.close()
x = subprocess.Popen(['sudo', 'openvpn', '--auth-nocache', '--config', path])
   try:
        while True:
            time.sleep(600)
    # termination with Ctrl+C
    except:
        try:
            x.kill()
        except:
            pass
        while x.poll() != 0:
            time.sleep(1)
