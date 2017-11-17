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
    (r'^\($',                       'LPAREN'),
    (r'^\);*$',                     'RPAREN'),
    (r'^-*\d+;*$',                  'INT_CONST'),
    (r'^-*\d+\.\d*;*$',             'REAL_CONST'),
    (r'"([a-z\d\s]*)";*',           'STRING')
]

def strip_newline(str):
    return str.rstrip('\r\n ')

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
            elif token in ['REAL_CONST', 'INT_CONST']:
                out_file.write('%s\t%s\n' % (token, formated_item))
                token_count += 1
            elif token == 'STRING':
                out_file.write('%s\t\n%s\t%s\t\n%s\n' % ('QUOTE', token, match.group(1), 'QUOTE'))
                token_count += 3
            elif token in ['PRINT', 'PLUS', 'MINUS', 'TIMES', 'DIV', 'POWER', 'ASSIGN', 'LPAREN', 'RPAREN']:
                out_file.write('%s\n' % token)
                token_count += 1
            else:
                out_file.truncate(0) #Clear out the results we have so far
                sys.exit('Matched unrecognized item: %n' % formated_item)

            if(has_semi):
                out_file.write('SEMICOLON\n')
                token_count += 1
            break

    if token_count == 0:
        out_file.truncate(0) #Clear out the results we have so far
        sys.exit('Encountered unrecognized item: %s\n' % item)
    return token_count

def lex(file_path):
    print 'Processing input file', file_path
    input_file  = open(file_path, 'rU')
    out_file    = open('input.out', 'w')
    token_count = 0

    for line in input_file:
        buffer = [i for i in re.split("( |\\\".*?\\\";*|'.*?';*)", line) if i.strip()]
        for item in buffer:
            token_count += process_item(strip_newline(item), out_file)

    input_file.close()
    out_file.close()
    print token_count, 'tokens produced'
    print 'Result in file input.out'


def main():
    file_path = sys.argv[1]
    lex(file_path)

if __name__ == '__main__':
    main()
