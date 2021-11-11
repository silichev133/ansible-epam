import json
import vagrant
import os
vm = vagrant.Vagrant(os.path.dirname('/home/vagrant/cm/ansible/day-3/'))
status = vm.conf()
status.update({'ip_adresses': vm._run_vagrant_command(['ssh','slave', '-c', "hostname -I"]).split(' ')[0:-1]})
print(status)
json.dumps(status)
