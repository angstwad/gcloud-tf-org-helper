# Copyright 2019 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import argparse

import yaml

_resources = []
_outputs = []

_ORGANIZATION = """\
data "google_organization" "default" {{
  organization = "{organization}"
}}

"""

_FOLDER = """\
resource "google_folder" "{resource_name}" {{
    display_name = "{name}"
    parent = "{parent}"
}}

"""

_OUTPUT = """\
output "{folder_name}_folder_name" {{
  value = "{parent}"
}}

"""


def walker(org, parent, lineage):
    for key, val in org.items():
        if lineage:
            new_lineage = "{}_{}".format(lineage, key)
        else:
            new_lineage = key

        _resources.append(_FOLDER.format(resource_name=new_lineage,
                                         name=key,
                                         parent=parent))

        new_parent = '${{google_folder.{}.name}}'.format(new_lineage)

        _outputs.append(_OUTPUT.format(folder_name=new_lineage,
                                       parent=new_parent))

        if val:
            walker(val, new_parent, new_lineage)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'org_file',
        type=argparse.FileType(),
        help='Org hierarchy YAML file'
    )
    parser.add_argument(
        '-o',
        '--outfile',
        default='organization.tf',
        help='File to write; default: organization.tf'
    )
    return parser.parse_args()


def main():
    args = parse_args()
    data = yaml.safe_load(args.org_file)

    _resources.append(_ORGANIZATION.format(organization=data['org']['id']))

    walker(
        data['org']['children'],
        '${data.google_organization.default.name}',
        ''
    )

    with open(args.outfile, 'w') as f:
        f.writelines(_resources)
        f.writelines(_outputs)


if __name__ == '__main__':
    main()
