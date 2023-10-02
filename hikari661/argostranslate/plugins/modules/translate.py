#!/usr/bin/python

# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
import argostranslate.package
import argostranslate.translate
__metaclass__ = type

DOCUMENTATION = r'''
---
module: translate

short_description: A very simple module that translates text using the argos-translate software.

# If this is part of a collection, you need to use semantic versioning,
# i.e. the version is of the form "2.5.0" and not "2.4".
version_added: "1.0.1"

description: |
  A very simple module that translates text using the argos-translate software. 
  It requires the argos-translate engine be install on your system or execution environment. Usually something like:
     pip install argostranslate
  See https://github.com/argosopentech/argos-translate/ for other installation options.   

options:
    text:
        description: This is the block of text you wish to have translated.
        required: true
        type: str
    source:
        description: This is the source language the text is provided as. Language abbreviations should be used, eg:
            - 'en' = English
            - 'ja' = Japanese
            - 'ru' = Russian
            - 'ga' = Gaelic
        required: true
        type: string
    target:
        description: This is the target language you want the text translated to. Language abbreviations should be used, eg:
            - 'en' = English
            - 'ja' = Japanese
            - 'ru' = Russian
            - 'ga' = Gaelic
        required: true
        type: string

author:
    - Jonathan Bishop (@hikari661)
'''

EXAMPLES = r'''
# Pass in some text to translate
- name: Translate from English to Japanese
  hikari661.argostranslate.translate:
    text: 'My dog is very muddy.'
    source: 'en'
    target: 'ja'

# fail the module
hikari661.argostranslate.translate:
    text: 'fail me'
    source: 'en'
    target: 'ja'
'''

RETURN = r'''
# These are examples of possible return values, and in general should use other names for return values.
original_text:
    description: The text that was provided for translation.
    type: str
    returned: always
    sample: 'My dog is very muddy'
translated_text:
    description: The translated text.
    type: str
    returned: always
    sample: '私の犬は非常に泥だめです'
'''

from ansible.module_utils.basic import AnsibleModule

def run_module():
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        source=dict(type='str', required=True),
        target=dict(type='str', required=True),
        text=dict(type='str', required=True)
    )

    # seed the result dict in the object
    # we primarily care about changed and state
    # changed is if this module effectively modified the target
    # state will include any data that you want your module to pass back
    # for consumption, for example, in a subsequent task
    result = dict(
        changed=False,
        original_text='',
        translated_text=''
    )

    # the AnsibleModule object will be our abstraction working with Ansible
    # this includes instantiation, a couple of common attr would be the
    # args/params passed to the execution, as well as if the module
    # supports check mode
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False
    )

    # if the user is working with this module in only check mode we do not
    # want to make any changes to the environment, just return the current
    # state with no modifications
    if module.check_mode:
        module.exit_json(**result)

    # manipulate or modify the state as needed (this is going to be the
    # part where your module will do what it needs to do)
    # r = requests.post(module.params['server']"/translate", data={'q': module.params['text'], 'source': module.params['source'], 'target': module.params['target']})
    translatedText = argostranslate.translate.translate(module.params['text'], module.params['source'], module.params['target'])
    result['translated_text'] = translatedText
    result['original_text'] = module.params['text']
    # use whatever logic you need to determine whether or not this module
    # made any modifications to your target
    if module.params['text']:
        result['changed'] = True

    # during the execution of the module, if there is an exception or a
    # conditional state that effectively causes a failure, run
    # AnsibleModule.fail_json() to pass in the message and the result
    if module.params['text'] == 'fail me':
        module.fail_json(msg='You requested this to fail', **result)

    # in the event of a successful module execution, you will want to
    # simple AnsibleModule.exit_json(), passing the key/value results
    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()

