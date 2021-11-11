
#!/usr/bin/python3
from ansible.module_utils.basic import *
 
def lastFirst(firstName, lastName):
    separator = ' Big Fat '
    result = lastName + separator + firstName
    return result
 
 
def main():
    fields = {
        "firstname": {"required": True, "type": "str"},
        "lastname": {
            "default": "davids",
            "choices": ['davids', 'alliston','wahi'],
            "type": 'str'
        }
    }
    module = AnsibleModule(argument_spec=fields)
    firstname = module.params['firstname']
    lastname = module.params['lastname']
    result = lastFirst(firstname,lastname)
    if result:
        module.exit_json(changed=True, meta=result)
    else:
        module.fail_json(changed=False, meta=result)
 
if __name__ == '__main__':
    main()
