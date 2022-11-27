import unittest

import HtmlTestRunner

import tema_10
import test_tema_09_login


class MyTestsuite(unittest.TestCase):
    def test_suite(self):
        smoke_test = unittest.TestSuite()
        smoke_test.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(tema_10.TestStatusCode),
            unittest.defaultTestLoader.loadTestsFromTestCase(test_tema_09_login.TestLogin)
        ])

        runner = HtmlTestRunner.HTMLTestRunner(
            combine_reports=True,
            report_title='Raport test',
            report_name='Smoke Test'
        )

        runner.run(smoke_test)
