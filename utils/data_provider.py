from utils.json_util import JSONUtil

class DataProvider:
    @staticmethod
    def get_data_from_json(file_path):
        return JSONUtil.read_data(file_path)
    
    