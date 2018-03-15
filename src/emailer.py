
def get_email_address(email_filename):

    emails = {}
    try:

        email_file = open(email_filename.name, 'r')

        for line in email_file:
            (email, name) = line.split(',')
            emails[email] = name.strip()
    except FileNotFoundError as err:
        print(err)

    return emails
