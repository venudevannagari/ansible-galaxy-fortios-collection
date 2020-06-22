#!/usr/bin/python
from __future__ import (absolute_import, division, print_function)
# Copyright 2019-2020 Fortinet, Inc.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

__metaclass__ = type

ANSIBLE_METADATA = {'status': ['preview'],
                    'supported_by': 'community',
                    'metadata_version': '1.1'}

DOCUMENTATION = '''
---
module: fortios_log_fortianalyzer_cloud_override_filter
short_description: Override filters for FortiAnalyzer Cloud in Fortinet's FortiOS and FortiGate.
description:
    - This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the
      user to set and modify log_fortianalyzer_cloud feature and override_filter category.
      Examples include all parameters and values need to be adjusted to datasources before usage.
      Tested with FOS v6.2.0
version_added: "2.9"
author:
    - Link Zheng (@chillancezen)
    - Hongbin Lu (@fgtdev-hblu)
    - Frank Shen (@frankshen01)
    - Jie Xue (@JieX19)
    - Miguel Angel Munoz (@mamunozgonzalez)
    - Nicolas Thomas (@thomnico)
notes:
    - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks
requirements:
    - ansible>=2.9.0
options:
    host:
        description:
            - FortiOS or FortiGate IP address.
        type: str
        required: false
    username:
        description:
            - FortiOS or FortiGate username.
        type: str
        required: false
    password:
        description:
            - FortiOS or FortiGate password.
        type: str
        default: ""
    vdom:
        description:
            - Virtual domain, among those defined previously. A vdom is a
              virtual instance of the FortiGate that can be configured and
              used as a different unit.
        type: str
        default: root
    https:
        description:
            - Indicates if the requests towards FortiGate must use HTTPS protocol.
        type: bool
        default: true
    ssl_verify:
        description:
            - Ensures FortiGate certificate must be verified by a proper CA.
        type: bool
        default: true
    log_fortianalyzer_cloud_override_filter:
        description:
            - Override filters for FortiAnalyzer Cloud.
        default: null
        type: dict
        suboptions:
            anomaly:
                description:
                    - Enable/disable anomaly logging.
                type: str
                choices:
                    - enable
                    - disable
            cifs:
                description:
                    - Enable/disable CIFS logging.
                type: str
                choices:
                    - enable
                    - disable
            dlp_archive:
                description:
                    - Enable/disable DLP archive logging.
                type: str
                choices:
                    - enable
                    - disable
            dns:
                description:
                    - Enable/disable detailed DNS event logging.
                type: str
                choices:
                    - enable
                    - disable
            filter:
                description:
                    - FortiAnalyzer Cloud log filter.
                type: str
            filter_type:
                description:
                    - Include/exclude logs that match the filter.
                type: str
                choices:
                    - include
                    - exclude
            forward_traffic:
                description:
                    - Enable/disable forward traffic logging.
                type: str
                choices:
                    - enable
                    - disable
            gtp:
                description:
                    - Enable/disable GTP messages logging.
                type: str
                choices:
                    - enable
                    - disable
            local_traffic:
                description:
                    - Enable/disable local in or out traffic logging.
                type: str
                choices:
                    - enable
                    - disable
            multicast_traffic:
                description:
                    - Enable/disable multicast traffic logging.
                type: str
                choices:
                    - enable
                    - disable
            severity:
                description:
                    - Lowest severity level to log.
                type: str
                choices:
                    - emergency
                    - alert
                    - critical
                    - error
                    - warning
                    - notification
                    - information
                    - debug
            sniffer_traffic:
                description:
                    - Enable/disable sniffer traffic logging.
                type: str
                choices:
                    - enable
                    - disable
            ssh:
                description:
                    - Enable/disable SSH logging.
                type: str
                choices:
                    - enable
                    - disable
            ssl:
                description:
                    - Enable/disable SSL logging.
                type: str
                choices:
                    - enable
                    - disable
            voip:
                description:
                    - Enable/disable VoIP logging.
                type: str
                choices:
                    - enable
                    - disable
'''

EXAMPLES = '''
- hosts: fortigates
  collections:
    - fortinet.fortios
  connection: httpapi
  vars:
   vdom: "root"
   ansible_httpapi_use_ssl: yes
   ansible_httpapi_validate_certs: no
   ansible_httpapi_port: 443
  tasks:
  - name: Override filters for FortiAnalyzer Cloud.
    fortios_log_fortianalyzer_cloud_override_filter:
      vdom:  "{{ vdom }}"
      log_fortianalyzer_cloud_override_filter:
        anomaly: "enable"
        cifs: "enable"
        dlp_archive: "enable"
        dns: "enable"
        filter: "<your_own_value>"
        filter_type: "include"
        forward_traffic: "enable"
        gtp: "enable"
        local_traffic: "enable"
        multicast_traffic: "enable"
        severity: "emergency"
        sniffer_traffic: "enable"
        ssh: "enable"
        ssl: "enable"
        voip: "enable"
'''

RETURN = '''
build:
  description: Build number of the fortigate image
  returned: always
  type: str
  sample: '1547'
http_method:
  description: Last method used to provision the content into FortiGate
  returned: always
  type: str
  sample: 'PUT'
http_status:
  description: Last result given by FortiGate on last operation applied
  returned: always
  type: str
  sample: "200"
mkey:
  description: Master key (id) used in the last call to FortiGate
  returned: success
  type: str
  sample: "id"
name:
  description: Name of the table used to fulfill the request
  returned: always
  type: str
  sample: "urlfilter"
path:
  description: Path of the table used to fulfill the request
  returned: always
  type: str
  sample: "webfilter"
revision:
  description: Internal revision number
  returned: always
  type: str
  sample: "17.0.2.10658"
serial:
  description: Serial number of the unit
  returned: always
  type: str
  sample: "FGVMEVYYQT3AB5352"
status:
  description: Indication of the operation's result
  returned: always
  type: str
  sample: "success"
vdom:
  description: Virtual domain used
  returned: always
  type: str
  sample: "root"
version:
  description: Version of the FortiGate
  returned: always
  type: str
  sample: "v5.6.3"

'''

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.connection import Connection
from ansible_collections.fortinet.fortios.plugins.module_utils.fortios.fortios import FortiOSHandler
from ansible_collections.fortinet.fortios.plugins.module_utils.fortimanager.common import FAIL_SOCKET_MSG


def login(data, fos):
    host = data['host']
    username = data['username']
    password = data['password']
    ssl_verify = data['ssl_verify']

    fos.debug('on')
    if 'https' in data and not data['https']:
        fos.https('off')
    else:
        fos.https('on')

    fos.login(host, username, password, verify=ssl_verify)


def filter_log_fortianalyzer_cloud_override_filter_data(json):
    option_list = ['anomaly', 'cifs', 'dlp_archive',
                   'dns', 'filter', 'filter_type',
                   'forward_traffic', 'gtp', 'local_traffic',
                   'multicast_traffic', 'severity', 'sniffer_traffic',
                   'ssh', 'ssl', 'voip']
    dictionary = {}

    for attribute in option_list:
        if attribute in json and json[attribute] is not None:
            dictionary[attribute] = json[attribute]

    return dictionary


def underscore_to_hyphen(data):
    if isinstance(data, list):
        for i, elem in enumerate(data):
            data[i] = underscore_to_hyphen(elem)
    elif isinstance(data, dict):
        new_data = {}
        for k, v in data.items():
            new_data[k.replace('_', '-')] = underscore_to_hyphen(v)
        data = new_data

    return data


def log_fortianalyzer_cloud_override_filter(data, fos):
    vdom = data['vdom']
    log_fortianalyzer_cloud_override_filter_data = data['log_fortianalyzer_cloud_override_filter']
    filtered_data = underscore_to_hyphen(filter_log_fortianalyzer_cloud_override_filter_data(log_fortianalyzer_cloud_override_filter_data))

    return fos.set('log.fortianalyzer-cloud',
                   'override-filter',
                   data=filtered_data,
                   vdom=vdom)


def is_successful_status(status):
    return status['status'] == "success" or \
        status['http_method'] == "DELETE" and status['http_status'] == 404


def fortios_log_fortianalyzer_cloud(data, fos):

    if data['log_fortianalyzer_cloud_override_filter']:
        resp = log_fortianalyzer_cloud_override_filter(data, fos)

    return not is_successful_status(resp), \
        resp['status'] == "success" and \
        (resp['revision_changed'] if 'revision_changed' in resp else True), \
        resp


def main():
    fields = {
        "host": {"required": False, "type": "str"},
        "username": {"required": False, "type": "str"},
        "password": {"required": False, "type": "str", "default": "", "no_log": True},
        "vdom": {"required": False, "type": "str", "default": "root"},
        "https": {"required": False, "type": "bool", "default": True},
        "ssl_verify": {"required": False, "type": "bool", "default": True},
        "log_fortianalyzer_cloud_override_filter": {
            "required": False, "type": "dict", "default": None,
            "options": {
                "anomaly": {"required": False, "type": "str",
                            "choices": ["enable",
                                        "disable"]},
                "cifs": {"required": False, "type": "str",
                         "choices": ["enable",
                                     "disable"]},
                "dlp_archive": {"required": False, "type": "str",
                                "choices": ["enable",
                                            "disable"]},
                "dns": {"required": False, "type": "str",
                        "choices": ["enable",
                                    "disable"]},
                "filter": {"required": False, "type": "str"},
                "filter_type": {"required": False, "type": "str",
                                "choices": ["include",
                                            "exclude"]},
                "forward_traffic": {"required": False, "type": "str",
                                    "choices": ["enable",
                                                "disable"]},
                "gtp": {"required": False, "type": "str",
                        "choices": ["enable",
                                    "disable"]},
                "local_traffic": {"required": False, "type": "str",
                                  "choices": ["enable",
                                              "disable"]},
                "multicast_traffic": {"required": False, "type": "str",
                                      "choices": ["enable",
                                                  "disable"]},
                "severity": {"required": False, "type": "str",
                             "choices": ["emergency",
                                         "alert",
                                         "critical",
                                         "error",
                                         "warning",
                                         "notification",
                                         "information",
                                         "debug"]},
                "sniffer_traffic": {"required": False, "type": "str",
                                    "choices": ["enable",
                                                "disable"]},
                "ssh": {"required": False, "type": "str",
                        "choices": ["enable",
                                    "disable"]},
                "ssl": {"required": False, "type": "str",
                        "choices": ["enable",
                                    "disable"]},
                "voip": {"required": False, "type": "str",
                         "choices": ["enable",
                                     "disable"]}

            }
        }
    }

    module = AnsibleModule(argument_spec=fields,
                           supports_check_mode=False)

    # legacy_mode refers to using fortiosapi instead of HTTPAPI
    legacy_mode = 'host' in module.params and module.params['host'] is not None and \
                  'username' in module.params and module.params['username'] is not None and \
                  'password' in module.params and module.params['password'] is not None

    versions_check_result = None
    if not legacy_mode:
        if module._socket_path:
            connection = Connection(module._socket_path)
            fos = FortiOSHandler(connection)

            is_error, has_changed, result = fortios_log_fortianalyzer_cloud(module.params, fos)
            versions_check_result = connection.get_system_version()
        else:
            module.fail_json(**FAIL_SOCKET_MSG)
    else:
        try:
            from fortiosapi import FortiOSAPI
        except ImportError:
            module.fail_json(msg="fortiosapi module is required")

        fos = FortiOSAPI()

        login(module.params, fos)
        is_error, has_changed, result = fortios_log_fortianalyzer_cloud(module.params, fos)
        fos.logout()

    if versions_check_result and versions_check_result['matched'] is False:
        module.warn("Ansible has detected version mismatch between FortOS system and galaxy, see more details by specifying option -vvv")

    if not is_error:
        if versions_check_result and versions_check_result['matched'] is False:
            module.exit_json(changed=has_changed, version_check_warning=versions_check_result, meta=result)
        else:
            module.exit_json(changed=has_changed, meta=result)
    else:
        if versions_check_result and versions_check_result['matched'] is False:
            module.fail_json(msg="Error in repo", version_check_warning=versions_check_result, meta=result)
        else:
            module.fail_json(msg="Error in repo", meta=result)


if __name__ == '__main__':
    main()
