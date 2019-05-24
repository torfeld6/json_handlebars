# coding=utf-8
import collections
import json
import os
import re

import click

op = re.compile('{{([a-z]+)}}', re.IGNORECASE)
lp = re.compile('{{([a-z]+)\\.([a-z]+)}}', re.IGNORECASE)


def parse_list(_list, root):
    # multiply children with placeholders
    template_items = []

    for item in _list:
        if not isinstance(item, dict):
            continue

        for item_key in item:
            if not isinstance(item[item_key], basestring):
                continue

            m = lp.match(item[item_key])
            if not m:
                continue

            template_items.append(item)

            root_key_singular = m.group(1)
            root_key = root_key_singular + 's'

            if not root.get(root_key) or not isinstance(root[root_key], list):
                continue

            for root_item in root[root_key]:
                copy = item.copy()

                for copy_key in copy:
                    if not isinstance(copy[copy_key], basestring):
                        continue

                    m = lp.match(copy[copy_key])
                    if not m:
                        continue

                    root_item_key = m.group(2)
                    if root_item_key not in root_item:
                        del copy[copy_key]
                        continue

                    copy[copy_key] = root_item[root_item_key]

                _list.append(copy)
            break

    for item in template_items:
        _list.remove(item)

    # parse children
    for item in _list:
        parse(item, root)


def parse_object(_object, root):
    # replace placeholders
    for key in _object:
        if not isinstance(_object[key], basestring):
            continue

        m = op.match(_object[key])

        if not m:
            continue

        root_key = m.group(1)

        if not root.get(root_key):
            continue

        _object[key] = root[root_key]

    # parse children
    for key in _object:
        parse(_object[key], root)


def parse(item, root=None):
    if root is None:
        root = item

    if isinstance(item, list):
        parse_list(item, root)
    elif isinstance(item, dict):
        parse_object(item, root)


@click.command()
@click.argument('path', type=click.Path(exists=True))
def cli(path):
    dirname = os.path.dirname(path)
    filename, ext = os.path.splitext(path)
    output_path = os.path.join(dirname, filename + '_output' + ext)

    with open(path) as f:
        config = json.load(f, object_pairs_hook=collections.OrderedDict)

    if isinstance(config, dict):
        config = [config]

    for org_config in config:
        parse(org_config)

    with open(output_path, 'wb+') as f:
        json.dump(config, f, indent=4)

    click.echo('output: ' + output_path)


if __name__ == '__main__':
    cli()
