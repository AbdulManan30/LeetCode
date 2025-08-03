'''
Given a text file file.txt that contains a list of phone numbers (one per line), write a one-liner bash script to print all valid phone numbers.

You may assume that a valid phone number must appear in one of the following two formats: (xxx) xxx-xxxx or xxx-xxx-xxxx. (x means a digit)

You may also assume each line in the text file must not contain leading or trailing white spaces.

Example:

Assume that file.txt has the following content:

987-123-4567
123 456 7890
(123) 456-7890
Your script should output the following valid phone numbers:

987-123-4567
(123) 456-7890
'''

def valid_phone_numbers(file_path):
    totalNumbers = ""
    with open(file_path) as file:
        arr = file.read().split('\n')
        for number in arr:
            if(number[3]=="-" and number[7] == "-" and len(number[8:]) == 4): # Check first format
                totalNumbers += number + "\n"
            if(number.startswith('(') and number[4] == ")" and number[9]=="-" and len(number[10:]) == 4):
                totalNumbers += number + "\n"
    return totalNumbers.strip()
    
print(valid_phone_numbers('Problem-5.txt'))