import os
import sys

# sys.path.insert(0, os.path.abspath("../"))
sys.path.insert(0, os.path.dirname(__file__))


# 请不要随意修改类名
class {{cookiecutter.module_name}}(object):
    
    def __init__(self, conf={}):
        '''

        :param input:
        '''
        self.checkpoint_dir = os.path.dirname(__file__) + "/results"
        pass

    def train(self, conf={}):
        '''
        在此编写模型的训练代码
        :param conf:
        :return:
        '''
        # 参数和返回值请参照下面的格式填写, 以便自动生成参数配置
        param1 = conf['param1']  # value_type: str # description: some description
        param2 = conf['param2']  # value_type: str # description: some description
        # 编写你的代码
        return {'ret1': 'cat', 'ret2': 'dog'}

    def predict(self, conf={}):
        '''
        在此编写模型预测代码
        :param conf:
        :return:
        '''
        # 参数和返回值请参照下面的格式填写, 以便自动生成参数配置
        param1 = conf['param1']  # value_type: str # description: some description
        param2 = conf['param2']  # value_type: str # description: some description
        # 编写你的代码
        return {'ret1': 'cat', 'ret2': 'dog'}

    def load_model(self):
        '''
        在此加载模型的结构以及权重， 并返回模型实例
        :param conf:
        :return: 模型实例
        '''
        pass
 
