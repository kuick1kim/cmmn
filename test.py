

import os, time

import common_git

timek = time.strftime('%Y-%m-%d %H:%M:%S')
common_git.update('KMS-'+timek)

# common_git.force_upload()

# common_git.look_log()