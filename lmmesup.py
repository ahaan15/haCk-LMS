import selenium
from selenium import webdriver
from getpass import getpass
import os

def submit_assignment(file_tup):
    # Using Firefox to access web
    driver = webdriver.Firefox()

    driver.get('http://lms.bennett.edu.in/login/index.php')

    BU_id = driver.find_element_by_name('username')
    BU_pass = driver.find_element_by_name('password')

    print("\nUse quotes to enter the username...(no need to write: @bennett.edu.in)\n")
    BU_id.send_keys(input("bennett username: "))
    print("\nThis is all one time only...after this you can directly run the script!\n\nDon't Worry..We'll not steal any of your data (WE SWEAR!)\n")#todo
    BU_pass.send_keys(getpass("bennett password: "))
 

    login_button = driver.find_element_by_name('submit')
    login_button.click()  

    courses_button = driver.find_element_by_something('')
    courses_button.click()

    folder = file_tup[0]

    if folder == 'ECSE204L':
        s_course = driver.find_element_by_link_text('add course name(full)')
    elif folder == 'ECSE205L':
        s_course = driver.find_element_by_link_text('')
    elif folder == 'ECSE208L':
        s_course = driver.find_element_by_link_text('')
    elif folder == 'ECSE210L':
        s_course = driver.find_element_by_link_text('')
    elif folder == 'ECSE212P':
        s_course = driver.find_element_by_link_text('')


# if __name__ == "__main__":    
# 	# Build tuple of (folder, file) to turn in
#     submission_dir = 'completed_assignments'
#     dir_list = list(os.listdir(submission_dir))

#     for directory in dir_list:
# 	    file_list = list(os.listdir(os.path.join(submission_dir, directory)))
# 	    if len(file_list) != 0:
# 	        file_tup = (directory, file_list[0])

#     if len(file_tup) == 0:
#         print('Pls give some files dude..-_-..')

#     else:
#         print('Assignment "{}" for "{}" found.'.format(file_tup[1], file_tup[0]))
#         input('Press enter to proceed: ')
#         submit_assignment(file_tup)