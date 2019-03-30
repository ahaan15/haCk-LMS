import selenium
from selenium import webdriver
from getpass import getpass
import os

def submit_assignment(files_list):

  driver = webdriver.Firefox()
  driver.get('http://lms.bennett.edu.in/login/index.php')

  BU_id = driver.find_element_by_name('username')
  BU_pass = driver.find_element_by_name('password')
  
  print("\nUse quotes to enter the username...(no need to write: @bennett.edu.in)\n")
  BU_id.send_keys(input("bennett username: "))
  print("\nDon't Worry..We'll not steal any of your data (WE SWEAR!)\n")
  BU_pass.send_keys(getpass("bennett password: "))

  login_button = driver.find_element_by_name('submit')
  login_button.click()

  courses_button = driver.find_element_by_link_text('Courses')
  courses_button.click()

  folder = files_list[0]

  if folder == 'ECSE204L':
	  select_course = driver.find_element_by_link_text('ECSE204L: Operating System')
  elif folder == 'ECSE205L':
	  select_course = driver.find_element_by_link_text('ECSE205L: Software Engineering')
  elif folder == 'ECSE208L':
	  select_course = driver.find_element_by_link_text('ECSE208L: Computer Networks ')
  elif folder == 'ECSE210L':
	  select_course = driver.find_element_by_link_text('ECSE210L: Design and Analysis of Algorithms ')
  elif folder == 'ECSE212P':
	  select_course = driver.find_element_by_link_text('ECSE212P: Competitive Programming')
  
  select_course.click()

  assignment_button = driver.find_element_by_class_name('activity assign modtype_assign ')
  assignment_button.click()

  file_name = files_list[1]
  file_locator = file_name.split('-')[0]

  specific_assigment = driver.find_element_by_link_text(file_locator)
  specific_assigment.click()

  try:
    add_submission_btn = driver.find_element_by_css_selector('input[type=submit][value=Add Submission]')
  except:
    print("\nWarning: This feature needs to be properly added...Please do not to use this\n\nShows up when - Assignment already submitted / Saved in draft\n")
	#submit_assignment_btn = driver.find_element_by_css_selector('')
  
  add_submission_btn.click()

  file_submissions = driver.find_element_by_css_selector('div.filemanager-container')
  file_submissions.click()

  choose_file = driver.find_element_by_name('attachments[0][uploaded_data]')
	# Send the name of the file to the button
  file_location = os.path.join(submission_dir, folder, file_name)
  choose_file.send_keys(file_location)

  upload = driver.find_element_by_css_selector('button.fp-upload-btn btn-primary btn')
  upload.click()

  submit_assignment = driver.find_element_by_css_selector('input[name=submitbutton][value=Save changes][type=submit]')
  submit_assignment.click()
  
  return "Successfully Submitted(Draft)!"

if __name__ == "__main__":

  submission_dir = 'completed_assignments'
  dir_list = list(os.listdir(submission_dir))

  for directory in dir_list:
    file_list = list(os.listdir(os.path.join(submission_dir, directory)))
    if len(file_list) != 0:
      files_list = (directory, file_list[0])

    if len(files_list) == 0:
      print('Pls give some files to upload..-_-..')

    else:
      print('Assignment "{}" for "{}" found.'.format(files_list[1], files_list[0]))
      input('Press enter to proceed')
      submit_assignment(files_list)