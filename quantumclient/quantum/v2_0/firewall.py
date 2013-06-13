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


class ListFirewall(quantumv20.ListCommand):
    """List firewalls that belong to a given tenant."""

    resource = 'firewall'
    log = logging.getLogger(__name__ + '.ListFirewall')
    list_columns = ['id', 'name', 'description',
                    'shared', 'admin_state_up', 'status',
                    'firewall _policy_id']
    _formatters = {}
    pagination_support = True
    sorting_support = True


class ShowFirewall(quantumv20.ShowCommand):
    """Show information of a given firewall."""

    resource = 'firewall'
    log = logging.getLogger(__name__ + '.ShowFirewall')


class CreateFirewall(quantumv20.CreateCommand):
    """Create a firewall."""

    resource = 'firewall'
    log = logging.getLogger(__name__ + '.CreateFirewall')

    def add_known_arguments(self, parser):
        parser.add_argument(
            '--name',
            help='name for the firewall')
        parser.add_argument(
            '--description',
            help='description for the firewall rule')
        parser.add_argument(
            '--shared',
            action='store_true',
            help='shared (default True)')
        parser.add_argument(
            '--admin_state_up',
            help='action (default True)')
        parser.add_argument(
            '--firewall_policy_id'
            help='firewall policy id')

    def args2body(self, parsed_args):
        body = {
            self.resource: {},
        }
        quantumv20.update_dict(parsed_args, body[self.resource],
                               ['name', 'description', 'shared',
                                'tenant_id'])
        return body


class UpdateFirewall(quantumv20.UpdateCommand):
    """Update a given firewall."""

    resource = 'firewall'
    log = logging.getLogger(__name__ + '.UpdateFirewall')


class DeleteFirewall(quantumv20.DeleteCommand):
    """Delete a given firewall."""

    resource = 'firewall'
    log = logging.getLogger(__name__ + '.DeleteFirewall')
