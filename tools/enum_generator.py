from typing import Dict

if __name__ == '__main__':
    f = open(file='./enums.h')

    result = 'from enum import Enum'

    enum_type = ''
    enum_desc = ''
    enums: Dict[str, Dict[str, str]] = dict()

    for line in f.readlines():
        line = line[:-1].strip()
        if len(line) == 0:
            continue
        if '/**' == line:
            enum_type = ''
            enum_desc = ''
            enums = dict()
            result +='\n\n'
            continue
        if '*' == line:
            enum_desc += '\n'
            continue
        if '*/' == line:
            continue
        if line.startswith('* '):
            comment = line[len('* '):]
            if comment.startswith('@'):
                key, desc = comment[1:].split(': ', 1)
                enums.update({key: {'desc': desc, 'value': None}})
            else:
                enum_desc += f'    {comment}\n'
            continue
        if line.startswith('typedef enum {'):
            continue
        if line.startswith('/*'):
            continue
        if line.startswith('} '):
            # enum end
            enum_type = line[2:-1]
            enum_desc = enum_desc[len(enum_type) + 4 + 2+4+1:-1]  # remove first name +\n\n last \n
            result += f'''
class {enum_type}(Enum):
    """
    {enum_desc}
    """
'''
            for member in enums.items():
                result += f'''
    {member[0]} = {member[1]['value']}
    """
    {member[1]['desc']}
    """'''
            continue

        key, value = line.replace(',', '').split('=', 1)
        key = key.strip()
        value = value.strip()

        if key in enums.keys():
            enums[key]['value'] = value
            continue
        else:
            print(f'type: {enum_type}  {key} = {value}')

    f2 = open('MMEnums.py', 'w')
    f2.write(result)
    f2.close()
