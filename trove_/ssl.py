# -*- coding: utf-8 -*-

import os

from subprocess import Popen, call

ca_conf = "/home/aghadge/ssl/ca/sub-ca/sub-ca.conf"
password = "amitg.b91"
openssl_command = "openssl ca -config {} -days {} -in {}.csr -out {}.crt -passin pass:{} -batch -extensions server_ext"


class SSL:

    def __init__(self):
        pass
    
    def get(self, csr_text):
        duration = 365
        return request_ssl_certificate(csr_text, duration)

    def request_ssl_certificate(self, csr_text, duration):
        cmds = openssl_command.format(ca_conf, duration*365, csr_text, csr_text, password)
        print("Command: {}".format(cmds))
        ps = Popen(cmds,  shell=True)
        status = ps.wait()
        output = ps.communicate()
        if status == 0:
            return True
        else:
            print(output[-1])
        return False
