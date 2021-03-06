#!/usr/bin/env python
# coding:utf-8
from __future__ import print_function, unicode_literals

import sys
import time
import traceback
from logging import StreamHandler
from ipymessenger.IpmsgServer import IpmsgServer

if __name__ == "__main__":

    dest_host = "192.168.26.189"
    # デバッグメッセージが必要な場合はloggingのHandlerを渡す
    #ip = IpmsgServer("sayamada", "ymsft_group", 2722, StreamHandler())
    ip = IpmsgServer("sayamada", "ymsft_group", 2722)
    try:
        ip.start()
        # wait initialize
        time.sleep(10)

        hello_no = ip.send_message(dest_host, "へろー")
        time.sleep(5)
        print("######send is success:" + str(ip.check_sended_message(hello_no)))

        test_no = ip.send_message_by_fuzzy_nickname("slope  太郎", "へろー by name")
        time.sleep(5)
        print("######send nickname is success:" + str(ip.check_sended_message(test_no)))

        # wait
        time.sleep(5)

        print(ip.get_message(dest_host, remove=True))

        time.sleep(100)

    except Exception as e:
        print("Exception occured")

        error_args = sys.exc_info()
        print(traceback.print_tb(error_args[2]))
        print(e)

    finally:
        ip.stop()
        ip.join()
