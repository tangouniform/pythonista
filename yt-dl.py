#!python

import appex
import requests
import youtube_dl
import clipboard
import glob
import os
import console

def main():
	if appex.is_running_extension():
		link = appex.get_text()
		if link:
			ydl_opts = {'outtmpl': '%(title)s.%(ext)s'}
			with youtube_dl.YoutubeDL(ydl_opts) as ydl:
				ydl.download([link])
				list_of_files = glob.glob('*.*')
				latest_file = max(list_of_files, key=os.path.getctime)
				console.open_in(latest_file)

if __name__ == '__main__':
	main()
