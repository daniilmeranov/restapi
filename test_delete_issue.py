import unittest
import requests
import yaml

from base_api import BaseApi

class TestDeleteIssue(BaseApi):

	def test_delete_issue(self):
		issue_id = self.create_issue()
		url = self.base_url + '/issue/' + issue_id

		r = requests.delete(url, cookies=self.cookies)
		self.assertEqual(r.status_code, 200)

		r = requests.get(url, cookies=self.cookies)
		self.assertEqual(r.status_code, 404)

	def test_get_not_existed_issue(self):
		url = self.base_url + '/issue/' + 'NOTEXISTED'

		r = requests.get(url, cookies=self.cookies)
		self.assertEqual(r.status_code, 404)
