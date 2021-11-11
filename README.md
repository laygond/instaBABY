## Installation
Get driver to use the Firefox browser
'''
sudo apt install firefox-geckodriver
'''
Install all necessary python modules
'''
mkvirtualenv INSTAPY -p python3  # (OPTIONAL)
pip install instapy
'''

## Run Quickstart Simulation 
'''
workon INSTAPY      # Turn on virtual env (OPTIONAL)
python quickstart.py 
'''

## Run Special Cases
To run `python comment_post_continously.py` you will have to add a line of code to the instapy library in the `comment_util.py` file under the function `process_comments` right after :
'''
commented_image, message = verify_commented_image(browser, link, owner, logger)

# LAYGOND ## ADDED FOR MULTIPLE COMMENTS
commented_image = None
'''
This allows an already commented post to be commented again.


## Resources
[Check for changes to InstaPy here](https://github.com/timgrossmann/InstaPy/blob/master/CHANGELOG.md#breaking-changes)
https://realpython.com/instagram-bot-python-instapy/
https://kev-dev.medium.com/simple-unfollower-bot-with-instapy-ffb89e8ba76b
https://pypi.org/project/instapy/0.1.0/
[kinda selenium](https://medium.com/@gdceccarini/interact-with-followers-of-an-instagram-profile-using-instapy-a09b02243924)
[Chrome driver? Ubuntu](https://github.com/InstaPy/instapy-docs/blob/master/How_Tos/How_To_DO_Ubuntu_on_Digital_Ocean.md)