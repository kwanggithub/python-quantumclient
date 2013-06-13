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


class ListFirewallRule(quantumv20.ListCommand):
    """List firewall rules that belong to a given tenant."""

    resource = 'firewall_rule'
    log = logging.getLogger(__name__ + '.ListFirewallRule')
    list_columns = ['id', 'name', 'description', 'firewall_policy_id',
                    'shared', 'protocol', 'source_ip_address',
                    'destination_ip_address', 'source_port',
                    'destination_port', 'action', 'enabled']
    _formatters = {}
    pagination_support = True
    sorting_support = True


class ShowFirewallRule(quantumv20.ShowCommand):
    """Show information of a given firewall rule."""

    resource = 'firewall_rule'
    log = logging.getLogger(__name__ + '.ShowFirewallRule')


class CreateFirewallRule(quantumv20.CreateCommand):
    """Create a firewall rule."""

    resource = 'firewall_rule'
    log = logging.getLogger(__name__ + '.CreateFirewallRule')

    def add_known_arguments(self, parser):
        parser.add_argument(
            '--name',
            help='name for the firewall rule')
        parser.add_argument(
            '--description',
            help='description for the firewall rule')
        parser.add_argument(
            '--shared',
            action='store_true',
            help='shared (default True)')
        parser.add_argument(
            '--protcol',
            help='protocol for the firewall rule: {tcp, udp, icmp}')
        parser.add_argument(
            '--source-ip-address',
            help='source ip address')
        parser.add_argument(
            '--destination-ip-address',
            help='destination ip address')
        parser.add_argument(
            '--source-port',
            help='source port')
        parser.add_argument(
            '--destination-port',
            help='destination port')
        parser.add_argument(
            '--action',
            help='action (default deny)')
        parser.add_argument(
            '--enabled',
            action='store_true',
            help='enabled (default True)')

    def args2body(self, parsed_args):
        body = {
            self.resource: {},
        }
        quantumv20.update_dict(parsed_args, body[self.resource],
                               ['name', 'description', 'shared', 'protocol',
                                'source_ip_address', 'destination_ip_address',
                                'source_port', 'destination_port',
                                'action', 'enabled', 'tenant_id'])
        return body


class UpdateFirewallRule(quantumv20.UpdateCommand):
    """Update a given firewall rule."""

    resource = 'firewall_rule'
    log = logging.getLogger(__name__ + '.UpdateFirewallRule')


class DeleteFirewallRule(quantumv20.DeleteCommand):
    """Delete a given firewall rule."""

    resource = 'firewall_rule'
    log = logging.getLogger(__name__ + '.DeleteFirewallRule')
