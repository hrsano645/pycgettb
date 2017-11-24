# coding=utf-8
from __future__ import (division,
                         absolute_import,
                         print_function,
                         unicode_literals)

import unittest
import datetime

from pycgettb import Source
from pycgettb import BaseRender, TextRender
from pycgettb import SourceTemplateNotLoadError, SourceDataNotLoadError
import openpyxl

class SouceTemplateTestCase(unittest.TestCase):

    # テンプレートがロードできるか
    # テンプレートタグのレキサーが想定通りに動くか

    def test_load_template(self):
        source_template = Source("./testfiles/template.xlsx", "./testfiles/data.xlsx")
        self.assertIsInstance(source_template.template_workbook, openpyxl.workbook.Workbook)
        self.assertIsInstance(source_template.data_workbook, openpyxl.workbook.Workbook)

    def test_except_load_template(self):

        with self.assertRaises(SourceTemplateNotLoadError):
            Source("./testfiles/result.txt", "./testfiles/data.xlsx")
    def test_except_load_data(self):

        with self.assertRaises(SourceDataNotLoadError):
            Source("./testfiles/template.xlsx", "./testfiles/result.txt")

    def test_parser(self):
        equal_data = {'title': 'Example Title', 'date_1': datetime.datetime(2017, 1, 1, 0, 0), 'name_1': 'suzuki',
                        'note_1': '日本語テスト', 'date_2': datetime.datetime(2017, 1, 2, 0, 0), 'name_2': 'sato',
                        'note_2': None}

        source_template = Source("./testfiles/template.xlsx", "./testfiles/data.xlsx")
        data_map = source_template.parse()
        # print(data_map)
        self.assertDictEqual(data_map, equal_data)


class TextRenderTestCase(unittest.TestCase):
    # データがパースできるか
    # 渡したテンプレートのマップを使ってレンダリングできるか？

    def setUp(self):
        source = Source("./testfiles/template.xlsx", "./testfiles/data.xlsx")
        self.data_map = source.parse()
        # print(self.data_map)

    def test_isinstance_base(self):
        textrender = TextRender("./testfiles/export_template.html", self.data_map)
        self.assertIsInstance(textrender, BaseRender)

    def test_rendering(self):
        with open("./testfiles/result.txt", encoding="utf-8") as equal_text_file:
            equal_text = equal_text_file.read()
        # print(equal_text)
        textrender = TextRender("./testfiles/export_template.html", self.data_map)
        # print(textrender.render())
        self.assertEqual(textrender.render(), equal_text)

if __name__ == '__main__':
    unittest.main()
