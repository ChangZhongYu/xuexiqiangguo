import json

class JsonTool:
    @staticmethod
    def read_json_file(file_path, encoding='utf-8'):
        """
        读取指定路径的JSON文件。

        :param file_path: JSON文件的路径。
        :param encoding: 文件的编码方式，默认为 'utf-8'。
        :return: 若文件读取和解析成功，返回JSON数据的字典；若出现错误，返回 None。
        """
        try:
            # 以指定编码方式打开文件
            with open(file_path, 'r', encoding=encoding) as f:
                # 解析JSON文件内容并返回
                return json.load(f)
        except FileNotFoundError:
            # 若文件未找到，打印错误信息
            print(f"JSON文件未找到: {file_path}")
            return None
        except json.JSONDecodeError as e:
            # 若JSON解析失败，打印错误信息
            print(f"JSON解析失败: {file_path} 错误: {str(e)}")
            return None
        except Exception as e:
            # 若出现其他异常，打印错误信息
            print(f"读取JSON文件异常: {file_path} 错误: {str(e)}")
            return None

    @staticmethod
    def extract_specific_values(data, search_string):
        """
        从JSON数据中提取包含特定字符串的channel_name和对应的channel_id。

        :param data: 包含JSON数据的字典。
        :param search_string: 需要查找的特定字符串。
        :return: 包含符合条件的channel_id和channel_name的字典。
        """
        result = {}
        for item in data.values():
            if search_string in item.get('channel_name', ''):
                result[item['channel_id']] = item['channel_name']
        return result

    @staticmethod
    def write_json_file(data, file_path, encoding='utf-8', indent=4):
        """
        将字典数据按名称排序后写入到本地的JSON文件。

        :param data: 要写入的字典数据。
        :param file_path: 目标JSON文件的路径。
        :param encoding: 文件的编码方式，默认为 'utf-8'。
        :param indent: JSON文件的缩进空格数，默认为 4。
        :return: 若写入成功，返回 True；若出现错误，返回 False。
        """
        try:
            # 按 channel_name 排序
            sorted_data = dict(sorted(data.items(), key=lambda item: item[1]))
            # 以指定编码方式打开文件，使用写入模式
            with open(file_path, 'w', encoding=encoding) as f:
                # 将排序后的字典数据以指定缩进写入到文件中
                json.dump(sorted_data, f, ensure_ascii=False, indent=indent)
            return True
        except Exception as e:
            # 若出现异常，打印错误信息
            print(f"写入JSON文件异常: {file_path} 错误: {str(e)}")
            return False

if __name__ == '__main__':
    print("JsonTool")