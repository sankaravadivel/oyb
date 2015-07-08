from os.path import expanduser
import os

USER_PREF_HOME_DIR_NAME = ".oyb"

def get_user_pref_home(create_if_not_exists=True):
    path = _get_user_pref_home()
    if create_if_not_exists and not os.path.exists(path):
        os.makedirs(path)
    return path

def _get_user_pref_home():
    user_home = get_user_home()
    pref_full_path = os.path.join(user_home, USER_PREF_HOME_DIR_NAME)
    print(pref_full_path)
    return pref_full_path

def create_user_pref_home():
    user_home = get_user_home()
    pref_full_path = os.path.join(user_home, USER_PREF_HOME_DIR_NAME)
    if not os.path.exists(pref_full_path):
        os.makedirs(pref_full_path)

def get_user_home():
    return expanduser("~")

                
