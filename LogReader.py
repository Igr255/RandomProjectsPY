import time

a = time.time()

logs = {}

text = ""
error_msg = ""

err_text_tuples = []  # contains tuples in a format (text, error_msg)

with open("Logs.txt", 'r') as log:
    out = open("Output.txt", 'w')

    log_lst = log.readlines()

    for i in range(len(log_lst)):

        # saves the first part of the log message so it can be used later and adds it to the text string

        if log_lst[i] == '-------------------------------------------------------------------------------\n':
            r = log_lst[i+1]
            if log_lst[i+1] == '<Type: Error>\n':
                if '<Process: ' in log_lst[i+5]:
                    for j in range(i+1, i+6):
                        text += log_lst[j]

                # saves the rest of the log message and adds it to the error_msg variable

                while log_lst[i+6] != '-------------------------------------------------------------------------------\n':
                    error_msg += log_lst[i+6]
                    i += 1

                # checks if the error_msg is in the dictionary (either adds it in the dict or increments the value)

                if error_msg not in logs:
                    logs[error_msg] = 1
                    err_text_tuples.append((text, error_msg))  # creates a tuple and adds it to the list
                else:
                    logs[error_msg] += 1

                # just a reset man

                error_msg = ""
                text = ""

    for items in logs:
        if logs[items] > 2:  # checks if the err_msg appeared in the log file more than twice
            for i in range(len(err_text_tuples)):
                if err_text_tuples[i][1] == items:  # if yes then it searches for the tuple where the  err_message is used
                    out.write('-------------------------------------------------------------------------------\n')  # writes the message into the output text file
                    out.write('Number of occurrence: {}\n'.format(logs[items]))
                    out.write(err_text_tuples[i][0])
                    out.write(items)

    out.write('-------------------------------------------------------------------------------')
    out.write(str(time.time() - a))
