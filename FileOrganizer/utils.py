#! /usr/bin/env python
import time
import os
import sys		
	
	
# ------------- #
# Logging class #
# ------------- #
class Log:

    now = time.strftime('%Y-%m-%d %H:%M:%S')

    @staticmethod
    def info(msg):

        if not Config.app_debug:
            return

        sys.stdout.write('[%s]: %s\n' % (Log.now, msg.strip()))

    @staticmethod
    def fatal(msg):

        sys.stdout.write('[%s]: %s\n' % (Log.now, msg.strip()))
        sys.exit(1)	
	

#config class
class Config:

	home = os.path.expanduser('~')
	filelistdir = os.path.join(home,'File Organizer')
	
		
	app_debug=True
	save=False
	
	filelist = os.path.join(filelistdir,'filelist')
	filelist_list = []
	EXT=['.mp4','.mp3','.flv','.mkv','.3gp','.avi','.m4a','.pdf']
	
	@staticmethod
	def check_filelist_location():
	
		if not os.path.exists(Config.filelistdir):
			Log.info('creating file list directory at %s' % Config.filelistdir)
			os.mkdir(Config.filelistdir)
	
		if os.path.exists(Config.filelist):
			Log.info('removing %s' % Config.filelist)
			os.remove(Config.filelist)