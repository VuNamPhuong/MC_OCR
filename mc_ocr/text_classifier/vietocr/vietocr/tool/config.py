import yaml
from mc_ocr.text_classifier.vietocr.vietocr.tool.utils import download_config

url_config = {
        'vgg_transformer':'vgg-transformer.yml',
        'resnet_transformer':'resnet_transformer.yml',
        'resnet_fpn_transformer':'resnet_fpn_transformer.yml',
        'vgg_seq2seq':'vgg-seq2seq.yml',
        'vgg_convseq2seq':'vgg_convseq2seq.yml',
        'vgg_decoderseq2seq':'vgg_decoderseq2seq.yml',
        'base':'base.yml',
        }


class Cfg(dict):
    def __init__(self, config_dict):
        super(Cfg, self).__init__(**config_dict)
        self.__dict__ = self

    @staticmethod
    def load_config_from_file(fname):
        base_config = download_config(url_config['base'])

        with open(fname, encoding='utf-8') as f:
            config = yaml.safe_load(f)
        base_config.update(config)

        return Cfg(base_config)

    @staticmethod
    def load_config_from_name(name):
        with open(base_config_path, encoding='utf-8') as f:
            base_config = yaml.safe_load(f)

        with open(seq2seq_config_path, encoding='utf-8') as f:
            config = yaml.safe_load(f)

        base_config.update(config)
        return Cfg(base_config)

    @staticmethod
    def load_config(base_config_path, config_path):
        with open(base_config_path, encoding='utf-8') as f:
            base_config = yaml.safe_load(f)

        with open(config_path, encoding='utf-8') as f:
            config = yaml.safe_load(f)

        base_config.update(config)
        return Cfg(base_config)



    def save(self, fname):
        with open(fname, 'w') as outfile:
            yaml.dump(dict(self), outfile, default_flow_style=False, allow_unicode=True)

