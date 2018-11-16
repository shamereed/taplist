# BEER LIST UTIL
import requests, sqlite3


def replace_space(str_):
    return str_.replace(' ', '-').lower()


def replace_large_space(str_):
    if str_.startswith('UPDATED:'):
        str_ = str_[17:]
    str_ = str_.replace('/n', ' ')

    str_ = str_.replace('	', ' ')
    str_ = str_.replace('		', ' ')

    str_ = str_.replace('  ', ' ')
    str_ = str_.replace('   ', ' ')
    str_ = str_.replace('     ', ' ')
    return str_


def replace_slash(str_):
    return str_.replace('/', '').lower()


def replace_period(str_):
    return str_.replace('.', '-').lower()


def replace_line_break(str_):
    return str_.replace('\n', '-')


def send_email(msg):
    return requests.post(
        "https://api.mailgun.net/v3/sandboxec1254f2c19c40a2a160cffb18bb1886.mailgun.org/messages",
        auth=("api", "key-e5dc1ad3337539060a5624c71821f434"),
        data={"from": "Mailgun Sandbox <postmaster@sandboxec1254f2c19c40a2a160cffb18bb1886.mailgun.org>",
              "to": "Shane <shanem.reed@gmail.com>",
              "subject": "PHILLY TAP LIST",
              "text": msg})


def strip_html_list(elements):
    clean_list = []
    for element in elements:
        if element.text.startswith(".") or element.text.startswith(" "):
            continue
        name = (element.text.strip()).upper().encode('ascii', 'ignore')
        name = replace_large_space(name)
        clean_list.append(name)
        print name
    return clean_list


def strip_html_list_to_file(name, elements):
    fp = open('tap_list.txt', 'a')
    fp.write(name.upper() + ':\n')
    clean_list = []
    for element in elements:
        if element.text.startswith(".") or element.text.startswith(" "):
            continue
        name = (element.text.strip()).upper().encode('ascii', 'ignore')
        clean_list.append(name)
        print name
        fp.write(name + '\n')
    fp.write('\n')
    fp.close()
    return clean_list


def create_taplist_tables():
    conn = sqlite3.connect("taplist.db")
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE bar
                  (name text, location text, taplistID integer)
                """)
    cursor.execute("""CREATE TABLE taplist
                  (name text, location text, taplistID integer)
                """)