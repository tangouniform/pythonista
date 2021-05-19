#!python3
"""
Open url in Chrome — Pythonista for iOS app extension.

1. take media url from appex(share)/clipboard/command-line
2. open it in Google Chrome iphone app

e.g., to watch Youtube video using PIP.

It accepts a media url from any site supported by youtube_dl
https://rg3.github.io/youtube-dl/supportedsites.html
"""
import sys
from urllib.parse import quote

import youtube_dl

import appex
import clipboard
import console
#sys.path.append('.')
import appex_webbrowser as webbrowser

def open(webpage_url):
	"""Play media on *webpage_url* in Google Chrome"""
	with youtube_dl.YoutubeDL(dict(forceurl=True)) as ydl:
		r = ydl.extract_info(webpage_url, download=False)
		media_url = r['formats'][-1]['url']
	webbrowser.open('googlechromes://' + media_url[8:] )

def main():
	if not appex.is_running_extension():
		if len(sys.argv) == 2:
			url = sys.argv[1]
		else:
			url = clipboard.get()
	else:
		url = appex.get_url() or appex.get_text()
	if url:
		open(url)
		console.hud_alert('Done.')
	else:
		console.hud_alert('No input URL found.')
  
if __name__ == '__main__':
	console.show_activity()
	try:
		main()
	finally:
		console.hide_activity()
