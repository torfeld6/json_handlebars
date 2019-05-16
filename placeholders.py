# coding=utf-8
import json
import re
from pprint import pprint

with open('test.json') as f:
    config = json.load(f)

op = re.compile('{{([a-z]+)}}', re.IGNORECASE)
lp = re.compile('{{([a-z]+)\\.([a-z]+)}}', re.IGNORECASE)


def parse_list(_list, root):

    # multiply children with placeholders
    for item in _list:
        if not isinstance(item, dict):
            continue

        for item_key in item:
            if not isinstance(item[item_key], unicode):
                continue

            m = lp.match(item[item_key])
            if not m:
                continue

            root_key_singular = m.group(1)
            root_key_plural = root_key_singular + 's'

            if not root.get(root_key_plural) or not isinstance(root[root_key_plural], list):
                continue

            for root_item in root[root_key_plural]:
                copy = item.copy()

                for copy_key in copy:
                    m = lp.match(copy[copy_key])
                    if not m:
                        continue

                    root_item_key = m.group(2)
                    if root_item_key not in root_item:
                        del copy[copy_key]
                        continue

                    copy[copy_key] = root_item[root_item_key]

                _list.append(copy)

            _list.remove(item)
            break

    # parse children
    for child in _list:
        parse(child, root)


def parse_object(_object, root):

    # replace placeholders
    for key in _object:
        if not isinstance(_object[key], unicode):
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


if isinstance(config, dict):
    config = [config]

for org_config in config:
    parse(org_config)

pprint(config)
