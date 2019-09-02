from smoothnlp import logger

__all__ = ["RandomScoreInitializer","AverageScoreInitializer","CustomeInitializer","CooccurenceConstructor","TextRanker"]

class BaseKeywordExtractor():
    
    def fit(self):
        pass

    def get_kws(self,topk:int=100,threshold:float=None):
        pass

    def get_token_score(self, token):
        pass

