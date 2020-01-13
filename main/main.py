import requests
import re

class PyParser:
	def __init__(self):
		self.main()

	def main(self):
		url = self.get_url()
		html = requests.Session().get(url)

		parsed_result = self.get_parsed_result(html)

	def get_url(self):
		return input("Input url")

	def get_parsed_result(self,html):
		result = html.text

		while True:
			parse_mode = self.set_parse_mode()
			if parse_mode == 0:
				result = self.parse_html_with_find_mode(result)
			elif parse_mode == 1:
				result = self.parse_html_with_replace_mode(result)
			else:
				break

			print(result)

	def get_regexp(self):
		return input("Input first regexp")

	def set_parse_mode(self):
		return input("0 : Find mode(re.compile)"
					 "1 : Replace mode(re.sub)")

	def parse_html_with_find_mode(self,result):
		target_html = self.get_regexp()
		return re.compile(target_html).search(result).group()

	def parse_html_with_replace_mode(self,result):
		target_html = self.get_regexp()
		replaced_html = self.get_regexp()
		return re.sub(target_html,replaced_html,result)
