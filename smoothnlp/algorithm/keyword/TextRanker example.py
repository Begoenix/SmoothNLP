import TextRanker as TR
word_in = ["我/w","爱/v","中国/n","中国/n","爱/v","我/w"]# 输入的分词结果示例

SI = TR.RandomScoreInitializer(word_in) # 调用权重初始化类
score = SI.set_by_unit()# 调用类中的具体的初始化方法

Graph = TR.CooccurenceGraph(
                            dict_weight = score,
                            list_relation = SI.obj,
                            span = 1)
                            # 调用构图类并构图

Ranker = TR.TextRanker(d = 0.8, graph = Graph.graph)# 调用textrank工具
Ranker.rank(iter_time = 10)# 迭代求权重，迭代次数自定义，此处为10
out1 = Ranker.get_topk(topk = 2)# 返回weight前二的词
print(out1)

