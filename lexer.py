#TODO: FIX BUG

import re
import sys

token_patterns = [
    (r'^PRINT$',                    'PRINT'),
    (r'^([a-z][a-z\d]*)([$#%]);*$', 'ID'),
    (r'^\+$',                       'PLUS'),
    (r'^-$',                        'MINUS'),
    (r'^\*$',                       'TIMES'),
    (r'^/$',                        'DIV'),
    (r'^\^$',                       'POWER'),
    (r'^=$',                        'ASSIGN'),
    (r'^-*\d*;*$',                  'INT_CONST'),
    (r'^-*\d*\.\d*;*$',             'REAL_CONST'),
    (r'^"[a-z\d]*";*$',             'STRING')
]

def get_id_type(suffix):
    if suffix == '%':
        return 'REAL'
    elif suffix == '#':
        return 'INTEGER'
    else:
        return 'STRING'

def process_item(item, out_file):
    token_count = 0
    for pattern, token in token_patterns:
        match = re.search(pattern, item)
        if match:
            has_semi      = item[-1] == ';'
            formated_item = item
            if has_semi:
                formated_item = item[:-1]

            if token == 'ID':
                out_file.write('%s\t%s\t%s\n' % (token, match.group(1), get_id_type(match.group(2))))
                token_count += 1
            elif token in ['REAL_CONST', 'INT_CONST', 'STRING']:
                out_file.write('%s\t%s\n' % (token, formated_item))
                token_count += 1
            else:
                out_file.write('%s\n' % token)
                token_count += 1

            if(has_semi):
                out_file.write('SEMICOLON\n')
                token_count += 1
            break
    return token_count

def lex(file_path):
    print 'Processing input file', file_path
    input_file  = open(file_path, 'rU')
    out_file    = open('input.out', 'w')
    token_count = 0

    for line in input_file:
        buffer = line.split()
        for item in buffer:
            token_count += process_item(item, out_file)

    input_file.close()
    out_file.close()
    print token_count, 'tokens produced'
    print 'Result in file input.out'


def main():
    file_path = sys.argv[1]
    lex(file_path)

if __name__ == '__main__':
    main()
