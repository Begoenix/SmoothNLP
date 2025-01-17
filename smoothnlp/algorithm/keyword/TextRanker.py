# -*- encoding: gbk -*-
# By Begoenix


from __future__ import absolute_import, unicode_literals
from operator import itemgetter
import networkx as nx
import random as rd
from collections import defaultdict




#-------------------------------ScoreInitializer--------------------------------
#===============================================================================



class VertexInitializer():
    """以Hanlp给出的分词结果为标准形态，即"word/wp"并以list的形式展示，

    即obj = ['word1/wp1','word2/wp2'......]

    类内中介形态为词与词性的元组组成的list，

    即self.object = [(word1,wp1),(word2,wp2)......]
    
    输出的结果为一个以以上元组为key的字典，值为权重,

    即self.score = {word1:weight1,word2:weight2......}

    """
    
    def __init__(self, obj):
        list_word = []
        
        for word in obj:
            tem = word.split("/")
            tuple_word = (tem[0], tem[1])
            list_word += [tuple_word]
            
        self.obj = list_word
        self.score = defaultdict(float)
        

        
class RandomScoreInitializer(VertexInitializer):
    """基于random函数对字权重进行初始化"""
    class_type = "RANDOM"
    

    def __init__(self, obj):
        
        super(RandomScoreInitializer, self).__init__(obj)

    def set_by_unit(self):
        """初始化权重在0-1之间"""

        for word in self.obj:
            self.score[word] = rd.random()

        return self.score

    def set_by_radint(self, start, end):
        """初始化权重为给定的整数之间取随机整值"""

        for word in self.obj:
            self.score[word] = rd.randint(start, end)

        return self.socre

    def set_by_uniform(self, start, end):
        """初始化权重为给定的数之间取随机浮点值"""

        for word in self.obj:
            self.score[word] = rd.uniform(start, end)

        return self.score

        

        


class AverageScoreInitializer(VertexInitializer):
    """平均数初始化"""
    class_type = "AVERAGE"


    def __init__(self, obj):
        
        super(AverageScoreInitializer, self).__init__(obj)

    def set_by_simple(self):
        for word in self.obj:
            self.score[word] = 1/len(self.obj)

        for token,value in self.score.items():
            self.score[token] = 1/len(self.score)

        return self.score



class CustomeInitializer(VertexInitializer):
    """使用已有的字典进行赋权，字典的格式为{tuple1:weight1,tuple2:weight2......}"""
    class_type = "CUSTOM"


    def __init__(self, obj, reference):
        self.reference = reference
        super(CustomeInitializer,self).__init__(obj)
        
    def set_by_dict(self):
        for word in self.obj:
            if word in self.reference:
                self.score[word] = self.reference[word]
            else:
                self.score[word] = 1 / len(sel.object)

        return self.score


#===============================================================================







#-------------------------------GraphConstructor--------------------------------
#===============================================================================


class BaseGraph():
    """节点为词语，边缘为两个词语按照某种要求

    （使用者自定义或使用当前版本初始化的函数）前后出现的次数

    节点的初始属性有“权重”、“词性”与“该词出现的次数”，

    边缘的属性只有“两词共同出现的次数”

    该类支持自定义属性，详见下文
    
    初始化参数中，dict_weight是词语权重的词典，

                  格式为{(word1,wp1):weight1,(word2,wp2):weight2......}
    
                  list_relation是按照原文分词并初步处理后的词列表，

                  词语出现的先后顺序以其在文中出现的先后顺序为准，

                  格式为[(word1,wp1),(word2,wp2)......]
                  
    使用的图表依赖networkx包
    
    """


    def __init__(self, dict_weight, list_relation):
        self.graph = nx.Graph(
                        wp = str, weight = float,
                        occur_times = int)
        self.dict_weight = dict_weight
        self.list_relation = list_relation

    def add_tag(self, tag_name, dict_tag, flag):
        """属性添加函数，参数

                        tag_name为要添加的属性；

                        dict_tag为键为目标名称，值为目标值的字典；

                        flag为需要添加属性的标识，

                        "N"为向节点添加值，"E"为向边缘添加值

        dict_tag的输入格式应为:

                        flag为"N"时，
        
                        dict_tag

                        = {(word1,wp1):tag_value1,......}

                        flag为"E"时，

                        dict_tag

                        = {(word1,word2):tag_value1,......}

        """
        
        if flag == "N":            
            for token,value in dict_tag.items():
                if token[0] in self.graph.nodes:
                    self.graph.add_node(token[0], tag_name = value)
                else:
                    self.graph.add_node(
                            token[0], wp = k[1],
                            weight = 1 / len(dict_tag),
                            occur_times = 0, tag_name = value)

        elif flag == "E":
            for token,value in dict_tag.items():
                if (token[0], token[1]) in self.graph.edges():
                    self.graph.add_edge(
                            token[0], token[1],
                            tag_name = value)
                    self.graph[token[0]][token[1]]["co_times"] += 1
                else:
                    self.graph.add_edge(
                            token[0], token[1],
                            co_times = 1, tag_name = value)


    def set_word_score(self, token_name, tag, new_value):
        """更改词语节点属性"""
        
        self.graph.nodes[token_name][tag] = new_value

    def set_edge_weight(self, token1, token2, tag, new_value):
        """更改边缘属性"""
        
        self.graph.edges[token1, token2][tag] = new_value

        



class CooccurenceGraph(BaseGraph):
    """构建根据词语前后出现关系为链接的图表"""
    graph_type = "COOCCURENCE"


    def __init__(self, dict_weight, list_relation, span):
        """参数

        span为向后搜寻的次数，

        例如span为2时，word1与其后两个词都存在连接关系，以此类推。

        """
        
        
        super(CooccurenceGraph,self).__init__(dict_weight, list_relation)

        
        for token,value in self.dict_weight.items():
            self.graph.add_node(
                    token[0], wp = token[1],
                    weight = value, occur_times = 0)


        for n in range(len(self.list_relation)):
            word_now = self.list_relation[n][0]
            num_now = n
            
            for w in range(num_now+1, num_now+1+span):
                if w >= len(self.list_relation):
                    break
                else:
                    word_next = self.list_relation[w][0]
                    if (word_now, word_next) in self.graph.edges():
                        self.graph[word_now][word_next]["co_times"] += 1
                    else:
                        self.graph.add_edge(word_now, word_next, co_times = 1)
                    self.graph.nodes[word_now]["occur_times"] += 1
                    self.graph.nodes[word_next]["occur_times"] += 1
                    






#===============================================================================







#----------------------------------TextRanker-----------------------------------
#===============================================================================

class TextRanker():
    """仅支持使用networkx包构建的无方向图"""
    

    def __init__(self, d, graph):
        """参数

        d为阻塞参数；

        graph为输入的无方向图。

        """

        self.block = d
        self.graph = graph
        self.weight = dict # 权重词典

    def rank(self, iter_time = int):
        """在Graph进行Walk, 迭代计算Vertex Score

        参数iter_time为迭代的次数

        """
        for i in range(iter_time):
            for word in self.graph.nodes():
                weight_sum = sum(self.graph.edges[word, e]["co_times"]
                                 * self.graph.nodes[e]["weight"]
                                 for e in self.graph.adj[word])
                
                occur_times = self.graph.nodes[word]["occur_times"]
                weight_final = weight_sum / occur_times
                                
                self.graph.nodes[word]["weight"] = \
                (1 - self.block) + self.block * weight_final

        self.weight = nx.get_node_attributes(self.graph, "weight")
        sorted_list = sorted(
                        self.weight.items(),
                        key = lambda x:x[1],
                        reverse = True)
        
        weight_tem = {}
        for token in sorted_list:
            weight_tem[token[0]] = self.weight[token[0]]

        self.weight = weight_tem

    def get_tokens(self, threshold, withScore = True):
        """返回score超过threshold的所有token

        若withScore为True，则返回一个排序后的词典，键为词，值为权重
        
        若withScore为False，则返回一个排序后的列表，表中元素为词

        """

        list_out = []
        
        for token,value in self.weight.items():
            if value >= threshold:
                list_out += [token]
            else:
                break

        if withScore:
            dict_out = {}
            for token in list_out:
                dict_out[token] = self.weight[token]
                
            return dict_out

        else:
            
            return list_out

    def get_topk(self, topk = int, withScore = True):
        """返回topk个最重要的token

        若withScore为True，则返回一个排序后的词典，键为词，值为权重
        
        若withScore为False，则返回一个排序后的列表，表中元素为词
        
        """
        num_res = topk
        if withScore:
            dict_out = {}
            for token, value in self.weight.items():
                if num_res > 0:
                    dict_out[token] = value
                    num_res -= 1
                else:
                    break
                    
            return dict_out

        else:
            list_out = []
            for token, value in self.weight.items():
                if num_res > 0:
                    list_out += [token]
                    num_res -= 1
                else:
                    break

            return list_out


    def get_token_score(self, token):
        """返回特定token的score"""

        return self.weight[token]
            

        
        

        
        



    

    










    
