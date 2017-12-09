# coding=utf-8
from __future__ import (division,
                        absolute_import,
                        print_function,
                        unicode_literals)

import os
import warnings

import openpyxl
from openpyxl.utils.exceptions import InvalidFileException

from jinja2 import Environment, FileSystemLoader, select_autoescape


__version__ = "0.1.2"


# Exception list

class DifferentRenderClassError(Exception):
    pass


class SourceTemplateNotLoadError(Exception):
    """ テンプレートを読み込めなかったときの例外 """
    pass


class SourceDataNotLoadError(Exception):
    """ データを読み込めなかったときの例外 """
    pass


# ソースのテンプレとデータを持たせるクラス
class Source(object):

    def __init__(self, source_template_filepath: str, data_filepath: str):
        self.template_filepath = source_template_filepath
        self.data_filepath = data_filepath

        # 各ファイルを読み込んで読み込めるか確認する
        self.template_workbook = self._template_load()
        self.data_workbook = self._data_load()

        self.data_map = None

    def _template_load(self):
        """ テンプレートを読み込む 読み込めない場合は例外を送る """

        # 開発者の考慮があって warnings.warn("Discarded range with reserved name") という警告を出している。必要ないので無効化している。
        # ref http://stackoverflow.com/questions/30169149/what-causes-userwarning-discarded-range-with-reserved-name-openpyxl
        # ref https://groups.google.com/forum/#!topic/openpyxl-users/FsQDyspBo58
        warnings.simplefilter("ignore")

        try:
            load_template = openpyxl.load_workbook(self.template_filepath, data_only=True, read_only=True)
        except InvalidFileException:
            msg = "this file cant load by openpyxl"
            raise SourceTemplateNotLoadError(msg)

        return load_template

    # レキサーのひとつになるリストの関係で、パーサーをどのように回してデータを保持するかが課題になるかな
    # パーサーは何をパースする？ -> template, data: dataはいらないかな。parse側でデータを呼び出せばいい
    # 全体をパースすることをparseとすればいいか。

    def _data_load(self):
        """ データを読み込む 読み込めない場合は例外を送る """

        # 開発者の考慮があって warnings.warn("Discarded range with reserved name") という警告を出している。必要ないので無効化している。
        # ref http://stackoverflow.com/questions/30169149/what-causes-userwarning-discarded-range-with-reserved-name-openpyxl
        # ref https://groups.google.com/forum/#!topic/openpyxl-users/FsQDyspBo58
        warnings.simplefilter("ignore")

        try:
            load_data = openpyxl.load_workbook(self.data_filepath, data_only=True, read_only=True)
        except InvalidFileException:
            msg = "this file cant load by openpyxl"
            raise SourceDataNotLoadError(msg)

        return load_data

    def _template_parse(self) -> dict:
        # テンプレートパーサーを実行
        template_map = dict()

        # ワークシートでループ. セル番号と対応をセットにした辞書を作る
        for ws in self.template_workbook.worksheets:
            template_map[ws.title] = dict()
            # セルの値があるまでの範囲を取得
            for row in ws.rows:
                for cell in row:
                    # info:2017-07-19:ひとまずテンプレート変数のみ対応
                    # レキサーを呼び出して、結果を取り出す
                    lexerd_name = self._lexer_variable(cell.value, "{{", "}}")

                    if lexerd_name:
                        # {"A1" : "example"} のようにセルのアドレスとテンプレートの値に設定
                        template_map[ws.title][lexerd_name] = cell.coordinate

        return template_map

    def _lexer_variable(self, cell_text: str, val_start_str="{{", val_end_str="}}"):
        """
        テンプレート変数なら、変数名を返す。そうでない場合はNoneを返す
        """
        cell_text = str(cell_text).strip()
        if cell_text.startswith(val_start_str) and cell_text.endswith(val_end_str):
            # {"A1" : "example"} のようにセルのアドレスとテンプレートの値に設定
            return cell_text[len(val_start_str):-len(val_end_str)].strip()

    def parse(self) -> dict:
        """テンプレートとデータを元に、データマップを作成する。"""

        # TODO:2017-08-07: 同じソース変数がある時のエラーを考えてない。例外を出すように変更すること
        source_data_map = dict()
        # パーサーのときの問題は、テンプレートパーサーで潰すか例外を出す
        template_map = self._template_parse()
        # excel_template_mapを元にデータを名寄せする。render_data_mapへ記述する
        for data_ws in self.data_workbook.worksheets:

            # データ側にテンプレートと同じワークシートの名前がアレば処理する
            if data_ws.title in template_map.keys():
                for tmpl_value_name, cell_addr in template_map[data_ws.title].items():
                    # キーをとバリューを共に生成する。
                    source_data_map[tmpl_value_name] = data_ws[cell_addr].value
        return source_data_map

class BaseRender(object):
    """レンダリングクラスのベースクラス。これ自身では何も行わない"""

    def __init__(self):
        pass

    def render(self):
        pass


class TextRender(BaseRender):
    """jinja2のテンプレートを元にレンダリングする
    renderの返す結果はjinja2でレンダリングした文字列"""

    def __init__(self, template_filepath: str, export_data_map: dict, template_encoding="utf-8"):
        super().__init__()

        self.data_map = export_data_map

        # ファイルパスをぶんりして、ファイル名, ディレクトリパスを分離する
        self.export_dirname, self.basename = os.path.split(template_filepath)

        self.jinja2_env = Environment(
            loader=FileSystemLoader(self.export_dirname, encoding=template_encoding),
            autoescape=select_autoescape(['html', 'xml']))

        self.template = self.jinja2_env.get_template(self.basename)

    def render(self):
        return self.template.render(self.data_map)



def main():
    pass


if __name__ == "__main__":
    main()
    # write code...
