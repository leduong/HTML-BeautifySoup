#!/usr/bin/env python
# -*- coding: utf-8 -*-
# HTMLBeautifySoup (for Sublime Text 2 & 3) v1.1
# by Le Dang Duong
# 12 Aug 2014
# url:			https://github.com/leduong
# e-mail:		i[at]leduong[dot].com

import sublime, sublime_plugin, re

from HTMLParser import HTMLParser
from bs4 import BeautifulSoup

indent_width=4
r = re.compile(r'^(\s*)', re.MULTILINE)

class HtmlBeautifulsoupCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		if self.view.sel()[0].empty():
			region = sublime.Region(0, self.view.size())
			sublime.status_message('Beautifying Entire File')
			rawcode = self.view.substr(region)
			# print region
		else:
			region = self.view.line(self.view.sel()[0])
			sublime.status_message('Beautifying Selection Only')
			rawcode = self.view.substr(self.view.sel()[0])
			# print region
		rawcode = rawcode.replace('\n','').replace('{','~').replace('}','`')
		soup = BeautifulSoup(u''.join(rawcode))

		unformatted_tag_list = []

		for i, tag in enumerate(soup.find_all(['span', 'a', 'strong', 'em', 'b', 'i', 'input', 'button', 'script', 'option', 'label'])):
			unformatted_tag_list.append(unicode(str(tag), 'utf-8'))
			tag.replace_with('{' + u"unformatted_tag_list[{0}]".format(i) + '}')
		rawcode = soup.prettify().format(unformatted_tag_list=unformatted_tag_list)
		rawcode = HTMLParser().unescape(rawcode.replace('~','{').replace('`','}').replace('> <','><'))
		self.view.replace(edit, region, r.sub(r'\1' * indent_width, rawcode))
