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
    """��Hanlp�����ķִʽ��Ϊ��׼��̬����"word/wp"����list����ʽչʾ��

    ��obj = ['word1/wp1','word2/wp2'......]

    �����н���̬Ϊ������Ե�Ԫ����ɵ�list��

    ��self.object = [(word1,wp1),(word2,wp2)......]
    
    ����Ľ��Ϊһ��������Ԫ��Ϊkey���ֵ䣬ֵΪȨ��,

    ��self.score = {word1:weight1,word2:weight2......}

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
    """����random��������Ȩ�ؽ��г�ʼ��"""
    class_type = "RANDOM"
    

    def __init__(self, obj):
        
        super(RandomScoreInitializer, self).__init__(obj)

    def set_by_unit(self):
        """��ʼ��Ȩ����0-1֮��"""

        for word in self.obj:
            self.score[word] = rd.random()

        return self.score

    def set_by_radint(self, start, end):
        """��ʼ��Ȩ��Ϊ����������֮��ȡ�����ֵ"""

        for word in self.obj:
            self.score[word] = rd.randint(start, end)

        return self.socre

    def set_by_uniform(self, start, end):
        """��ʼ��Ȩ��Ϊ��������֮��ȡ�������ֵ"""

        for word in self.obj:
            self.score[word] = rd.uniform(start, end)

        return self.score

        

        


class AverageScoreInitializer(VertexInitializer):
    """ƽ������ʼ��"""
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
    """ʹ�����е��ֵ���и�Ȩ���ֵ�ĸ�ʽΪ{tuple1:weight1,tuple2:weight2......}"""
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
    """�ڵ�Ϊ�����ԵΪ�������ﰴ��ĳ��Ҫ��

    ��ʹ�����Զ����ʹ�õ�ǰ�汾��ʼ���ĺ�����ǰ����ֵĴ���

    �ڵ�ĳ�ʼ�����С�Ȩ�ء��������ԡ��롰�ôʳ��ֵĴ�������

    ��Ե������ֻ�С����ʹ�ͬ���ֵĴ�����

    ����֧���Զ������ԣ��������
    
    ��ʼ�������У�dict_weight�Ǵ���Ȩ�صĴʵ䣬

                  ��ʽΪ{(word1,wp1):weight1,(word2,wp2):weight2......}
    
                  list_relation�ǰ���ԭ�ķִʲ����������Ĵ��б�

                  ������ֵ��Ⱥ�˳�����������г��ֵ��Ⱥ�˳��Ϊ׼��

                  ��ʽΪ[(word1,wp1),(word2,wp2)......]
                  
    ʹ�õ�ͼ������networkx��
    
    """


    def __init__(self, dict_weight, list_relation):
        self.graph = nx.Graph(
                        wp = str, weight = float,
                        occur_times = int)
        self.dict_weight = dict_weight
        self.list_relation = list_relation

    def add_tag(self, tag_name, dict_tag, flag):
        """������Ӻ���������

                        tag_nameΪҪ��ӵ����ԣ�

                        dict_tagΪ��ΪĿ�����ƣ�ֵΪĿ��ֵ���ֵ䣻

                        flagΪ��Ҫ������Եı�ʶ��

                        "N"Ϊ��ڵ����ֵ��"E"Ϊ���Ե���ֵ

        dict_tag�������ʽӦΪ:

                        flagΪ"N"ʱ��
        
                        dict_tag

                        = {(word1,wp1):tag_value1,......}

                        flagΪ"E"ʱ��

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
        """���Ĵ���ڵ�����"""
        
        self.graph.nodes[token_name][tag] = new_value

    def set_edge_weight(self, token1, token2, tag, new_value):
        """���ı�Ե����"""
        
        self.graph.edges[token1, token2][tag] = new_value

        



class CooccurenceGraph(BaseGraph):
    """�������ݴ���ǰ����ֹ�ϵΪ���ӵ�ͼ��"""
    graph_type = "COOCCURENCE"


    def __init__(self, dict_weight, list_relation, span):
        """����

        spanΪ�����Ѱ�Ĵ�����

        ����spanΪ2ʱ��word1����������ʶ��������ӹ�ϵ���Դ����ơ�

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
    """��֧��ʹ��networkx���������޷���ͼ"""
    

    def __init__(self, d, graph):
        """����

        dΪ����������

        graphΪ������޷���ͼ��

        """

        self.block = d
        self.graph = graph
        self.weight = dict # Ȩ�شʵ�

    def rank(self, iter_time = int):
        """��Graph����Walk, ��������Vertex Score

        ����iter_timeΪ�����Ĵ���

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
        """����score����threshold������token

        ��withScoreΪTrue���򷵻�һ�������Ĵʵ䣬��Ϊ�ʣ�ֵΪȨ��
        
        ��withScoreΪFalse���򷵻�һ���������б�����Ԫ��Ϊ��

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
        """����topk������Ҫ��token

        ��withScoreΪTrue���򷵻�һ�������Ĵʵ䣬��Ϊ�ʣ�ֵΪȨ��
        
        ��withScoreΪFalse���򷵻�һ���������б�����Ԫ��Ϊ��
        
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
        """�����ض�token��score"""

        return self.weight[token]
            

        
        

        
        



    

    










    
