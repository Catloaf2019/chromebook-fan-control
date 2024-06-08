# chromebook-fan-control
A python3 script to create fan curves on chromebooks running Linux

To test:
\# python3 tempctrl.py

To install (systemd):

\# chmod +x tempctrl.py
\# cp tempctrl.py /usr/local/bin
\# cp chromebook-fanctrl.service /etc/systemd/system
\# systemctl enable --now chromebook-fanctrl

You must also have python3 installed at /usr/bin/python3 and ectool at /usr/local/bin/python3, you must modify the script if you have these files at other locations
You can download ectool at https://tree123.org/files/utils/ectool
