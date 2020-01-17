# 设置lstm训练参数
class TrainingConfig(object):
    batch_size = 16
    # 学习速率
    lr = 0.001
    epoches = 5
    print_step = 500


class LSTMConfig(object):
    emb_size = 128  # 词向量的维数
    hidden_size = 128  # lstm隐向量的维数