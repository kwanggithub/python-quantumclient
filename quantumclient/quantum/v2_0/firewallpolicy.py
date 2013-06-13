# Copyright 2013 Big Switch Networks
# All Rights Reserved
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
#
# @author: KC Wang, Big Switch Networks
#
# vim: tabstop=4 shiftwidth=4 softtabstop=4

import logging

from quantumclient.quantum import v2_0 as quantumv20


class ListFirewallPolicy(quantumv20.ListCommand):
    """List firewall policies that belong to a given tenant."""

    resource = 'firewall_policy'
    log = logging.getLogger(__name__ + '.ListFirewallPolicy')
    list_columns = ['id', 'name', 'description', 'shared',
                    'firewall_rules_list', 'firewalls_list',
                    'audited']
    _formatters = {}
    pagination_support = True
    sorting_support = True


class ShowFirewallPolicy(quantumv20.ShowCommand):
    """Show information of a given firewall policy."""

    resource = 'firewall_policy'
    log = logging.getLogger(__name__ + '.ShowFirewallPolicy')


class CreateFirewallPolicy(quantumv20.CreateCommand):
    """Create a firewall policy."""

    resource = 'firewall_policy'
    log = logging.getLogger(__name__ + '.CreateFirewallPolicy')

    def add_known_arguments(self, parser):
        parser.add_argument(
            '--name',
            help='name for the firewall policy')
        parser.add_argument(
            '--description',
            help='description for the firewall policy')
        parser.add_argument(
            '--shared',
            action='store_true',
            help='shared (default True)'
        parser.add_argument(
            '--firewall_rules_list',
            help='ordered list of firewall rules for the policy')
        parser.add_argument(
            '--audited',
            action='store_false',
            help='audited (default False)')

    def args2body(self, parsed_args):
        body = {
            self.resource: {},
        }
        quantumv20.update_dict(parsed_args, body[self.resource],
                               ['name', 'description', 'shared',
                                'firewall_rules_list', 'audited',
                                'tenant_id'])
        return body


class UpdateFirewallPolicy(quantumv20.UpdateCommand):
    """Update a given firewall policy."""

    resource = 'firewall_policy'
    log = logging.getLogger(__name__ + '.UpdateFirewallPolicy')


class DeleteFirewallPolicy(quantumv20.DeleteCommand):
    """Delete a given firewall policy."""

    resource = 'firewall_policy'
    log = logging.getLogger(__name__ + '.DeleteFirewallPolicy')
