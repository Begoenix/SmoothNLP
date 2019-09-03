import TextRanker as TR
word_in = ["我/w","爱/v","中国/n","中国/n","爱/v","我/w"]# 输入的分词结果示例

SI = TR.RandomScoreInitializer(word_in) # 调用权重初始化类
score = SI.unit()# 调用类中的具体的初始化方法

Graph = TR.CooccurenceConstructor(
                            dict_weight = score,
                            list_relation = SI.object,
                            span = 1)
                            # 调用构图类并构图

Ranker = TR.TextRanker(d = 0.8, graph = Graph.graph)# 调用textrank工具
Ranker.rank(args = 10)# 迭代求权重，迭代次数自定义，此处为10

out1 = Ranker.get_token_score("我")# 返回某个词的权重
out2 = Ranker.get_topk(topk = 2)# 返回权重前二的两个词语
out3 = Ranker.get_tokens(threshold = 1)# 返回权重大于1的词语
print(out1, out2, out3)
