#!"C:/Python/python.exe"
import win32file
import distutils.dir_util
import distutils.file_util
import cgi
import cgitb
import pr
import sys

print("Content-type: text/html\n")
print("<html><header><link rel='stylesheet' href='\\theme.css'></header><body>\n")
print("<ul class='shell-body'>\n")
sys.stdout.flush()

# find the letter of USB
drive_list = []
drivebits = win32file.GetLogicalDrives()
for drive in range(1, 26):
    mask = 1 << drive
    if drivebits & mask:
        # here if the drive is at least there
        drname = '%c:\\' % chr(ord('A') + drive)
        t = win32file.GetDriveType(drname)
        if t == win32file.DRIVE_REMOVABLE:
            drive_list.append(drname)

# convert USB letter to string and use it as a destination for copy
pre_dst = ''.join(drive_list)

form = cgi.FieldStorage()

if form.getvalue("terminal"):
    print('Preparing to copy Terminal part ... <br>', flush=True)
    # install script
    pr.install()
    # terminal
    pr.pr_platform_silverball()
    pr.pr_platform_blade()
    pr.pr_platform_lara()
    pr.pr_terminal_product()
    pr.pr_terminal_configuration()
    pr.pr_content()
    pr.pr_banners()
    print("<br><br> Finished")
if form.getvalue("cashier"):
    print('Preparing to copy Cashier part ... <br>', flush=True)
    # install script
    pr.install()
    # cashier
    pr.pr_cashier_platform()
    pr.pr_cashier_product()
    pr.pr_cashier_configuration()
    print("<br><br> Finished")
if form.getvalue("mediastation"):
    print('Preparing to copy Mediastation files ... <br>', flush=True)
    # install script
    pr.install()
    # mediastation
    pr.pr_mediastation_product()
    pr.pr_mediastation_configuration()
    pr.pr_mediastation_platform()
    pr.pr_mediastation_cert_fix()
    print("<br><br> Finished")
if form.getvalue("everything"):
    print('Preparing to copy EVERYTHING ... <br>', flush=True )
    # install script
    pr.install()
    # terminal
    pr.pr_platform_silverball()
    pr.pr_platform_blade()
    pr.pr_platform_lara()
    pr.pr_terminal_product()
    pr.pr_terminal_configuration()
    pr.pr_content()
    pr.pr_banners()
    # cashier
    pr.pr_cashier_platform()
    pr.pr_cashier_product()
    pr.pr_cashier_configuration()
    # mediastation
    pr.pr_mediastation_product()
    pr.pr_mediastation_configuration()
    pr.pr_mediastation_platform()
    pr.pr_mediastation_cert_fix()
    print("<br><br> Finished")
if form.getvalue("test"):
    print('Preparing to copy Terminal part ... <br>', flush=True)
    # install script
    pr.install()
    print("<br><br> Finished")


print("</ul></body></html>\n")
