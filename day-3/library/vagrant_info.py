#!/usr/bin/python
import argparse
import os
import re
import vagrant
import json
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--list", default=False, action="store_true")
    parser.add_argument("--host", default="", action="store")
    args = parser.parse_args()
    stack = vagrant.Vagrant(os.getcwd())
    current = stack.conf()
    if stack.status()[0].state == "running":
        if (args.host):
            if (args.host == current["Host"]):
                print
                json.dumps({
                    "ansible_host": current["HostName"],
                    "ansible_port": current["Port"],
                    "ansible_user": current["User"],
                    "ansible_ssh_private_key_file": current["IdentityFile"]
                }, indent=4)
            else:
                print
                {}
        if (args.list):
            print
            json.dumps({
                "vagrant": {
                    "hosts": [
                        current["Host"]
                    ],
                    "vars": {
                        "ansible_user": current["User"],
                        "ansible_ssh_private_key_file": current["IdentityFile"]
                    }
                },
                "_meta": {
                    "hostvars": {
                        current["Host"]: {
                            "ansible_host": current["HostName"],
                            "ansible_port": current["Port"]
                        }
                    }
                }
            }, indent=4)
    else:
        print
        {}
if name == '__main__':
    main()
