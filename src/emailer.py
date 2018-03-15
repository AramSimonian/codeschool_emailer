
def get_email_address(email_filename):

    emails = {}
    try:

        email_file = open(email_filename, 'r')

        for line in email_file:
            (email, name) = line.split(',')
            emails[email] = name.strip()
    except FileNotFoundError as err:
        print(err)

    return emails

def get_schedule(schedule):
    try:
        schedule_file = open(schedule, 'r')
        schedule_details = schedule_file.read()
    except FileNotFoundError as err:
        print(err)

    return schedule_details

def main():
    emails = get_email_address('emails.txt')
    print(emails)

    schedule = get_schedule('schedule.txt')
    print(schedule)
