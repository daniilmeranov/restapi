import unittest
import requests
import yaml


class TestCreateIssue(unittest.TestCase):

	def test_create_issue(self):
		url = self.base_url + '/issue'
		params = {
			'project': 'API',
			'summary': 'Awesome summary MDK',
			'description': 'Created by MDK'
		}

		r = requests.put(url, data=params, auth=self.creds)
		location = r.headers['Location']

		self.assertEqual(r.status_code, 201)

		issue_id = r.headers['Location'].split('/')[-1]

