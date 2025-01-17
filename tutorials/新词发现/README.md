﻿**smoothnlp.algorithm.phrase.phrase_extraction**

>我们提供了一个短语抽取函数`extract_phrase`，抽取过程考虑了词语本身及其上下文特征。本函数可以用于不同领域的短语抽取。

## 介绍

* 本项目所用数据来自smoothnlp的开源金融文本数据集，数据集包括：企业工商信息、金融讯息新闻、专栏咨询、投资机构信息、投资事件

* 数据集获取方式：  
`git clone https://github.com/smoothnlp/FinancialDatasets.git`

* 函数调用方式:  

```python
from smoothnlp.algorithm.phrase import extract_phrase
extract_phrase(corpus,top_k,chunk_size,max_n,min_freq)
``` 

* 参数说明：
```python
corpus:     必需，file open()、database connection或list
            example:corpus = open(file_name, 'r', encoding='utf-8')
                    corpus = conn.execute(query)
                    corpus = list(***)
top_k:      float or int,表示短语抽取的比例或个数
chunk_size: int,用chunksize分块大小来读取文件
max_n:      int,抽取ngram及以下
min_freq:   int,抽取目标的最低词频
```

* 针对不同应用场景, 我们支持不同的文本输入方式：

```python
## 利用数据库内容作为输入
cursor = conn.execute(query)

## 输入文件
file = open(file_name, 'r')

## 输入文本列表
list = [str1,str2,...]
```

## 效果展示
**-- 评估语料**

| 数据集名称 | 数据量 | 总字数 | 数据领域 | 下载地址 |
|:-:|:---:|:---:|:-:|:---:|
|专栏资讯数据集|10,000条|28,129,311|金融|https://github.com/smoothnlp/FinancialDatasets |
|金融新闻数据集|20,000条|25,295,513|金融|https://github.com/smoothnlp/FinancialDatasets |
|36氪新闻数据集| 111,935条 | 196,288,902 |金融|  https://github.com/smoothnlp/FinancialDatasets|
|医疗行业数据集|1000条| 49,466 |医疗|http://www.sdspeople.fudan.edu.cn/zywei/DATA130006/final-project/index.html |


* 专栏资讯数据集top100 ,短语抽取用时1min 47s

|**亚马逊**|**阿里巴巴**|**短视频**|**腾讯**|**蘑菇街**|**浏览器**|**今日头条**|**苹果**|**苏宁**|**李彦宏**|
|:-:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|**支付宝**|**爱奇艺**|**以及**|**虽然**|**科技**|**广告**|**品牌**|**消费者**|**人工智能**|**技术**|
|**瑞幸咖啡**|**进行**|**CEO**|**市场**|**Uber**|**选择**|**今日头条**|**产品**|**蚂蚁金服**|**企业**|
|**自动驾驶**|**汽车**|**支付宝**|**已经**|**苏宁**|**贾跃亭**|**互联网**|**内容**|**共享单车**|**营销**|
|**蜻蜓FM**|**能够**|**健康**|**区块链**|**腾讯**|**京东**|**苹果**|**酒店**|**百度糯米**|**VR**|
|**可以**|**饿了么**|**美团点评**|**政府**|**搜索**|**新零售**|**智能音箱**|**战略**|**手机**|**搜索引擎**|
|**医疗**|**业务**|**机器人**|**谷歌**|**周鸿祎**|**管理**|**斗鱼**|**微信**|**系统**|**APP**|
|**搜狗**|**社交**|**淘宝**|**阿里**|**芯片**|**网络**|**供应链**|**百度**|**直播**|**金融**|
|**软件**|**边缘计算**|**行业**|**阅读**|**申请**|**沃尔玛**|**小程序**|**教育**|**百度地图**|**世界杯**|
|**合作伙伴**|**包括**|**银行**|**罗永浩**|**豌豆荚**|**设备**|**特斯拉**|**AI**|**ofo**|**诺基亚**|

* 金融新闻数据集top100, 短语抽取用时1min 35s

|**以及**|**平台**|**阿里巴巴**|**组织**|**项目**|**市场**|**贾跃亭**|**网络**|**教育**|**技术**|
|:-:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|**亚马逊**|**柬埔寨**|**服务**|**品牌**|**人工智能**|**消费者**|**儿童**|**用户**|**企业**|**集团**|
|**产品**|**互联网**|**实施**|**申请**|**选择**|**碧桂园**|**旅游**|**投资者**|**风险**|**疫苗**|
|**使用**|**建设**|**系统**|**蚂蚁金服**|**销售**|**国际**|**计划**|**虽然**|**共享单车**|**科创板**|
|**IPO**|**游戏**|**价格**|**参与**|**能够**|**Uber**|**中国**|**问题**|**内容**|**基金**|
|**包括**|**网络安全**|**业务**|**货币政策**|**或者**|**委员会**|**进行**|**区块链**|**深圳**|**行业**|
|**进一步**|**已经**|**世界**|**公司**|**购买**|**金融机构**|**必须**|**科技**|**苹果**|**直接**|
|**拼多多**|**积极**|**滴滴**|**世界杯**|**上市公司**|**通过**|**北京**|**调整**|**特斯拉**|**客户**|
|**哈尔滨**|**综合**|**实现**|**团队**|**国家**|**MLF**|**汽车**|**鼓励**|**酒店**|**芯片**|
|**短视频**|**管理**|**奢侈品**|**表示**|**跨境电商**|**ofo**|**经济**|**政策**|**ETF**|**香港**|

* 36氪新闻数据集top100, 短语抽取用时2min 22s

|**哔哩哔哩**|**阿里巴巴**|**贾跃亭**|**以及**|**搜索引擎**|**谷歌**|**特斯拉**|**苹果**|**屈臣氏**|**碧桂园**|
|:-:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|**亚马逊**|**豌豆荚**|**苏宁**|**沃尔玛**|**跨境电商**|**蚂蚁金服**|**粉丝**|**短视频**|**华谊兄弟**|**儿童**|
|**好莱坞**|**凭借**|**人工智能**|**石墨烯**|**申请**|**玻璃**|**蘑菇街**|**共享单车**|**并且**|**拒绝**|
|**迪士尼**|**烹饪**|**机器人**|**垃圾分类**|**游戏**|**柬埔寨**|**加密货币**|**呼吁**|**数字货币**|**独角兽**|
|**雾霾**|**王者荣耀**|**抄袭**|**系统**|**逐渐**|**基础设施**|**比特币**|**瑞幸咖啡**|**俄罗斯**|**智能硬件**|
|**测试**|**今日头条**|**滴滴**|**爱奇艺**|**平台**|**健康**|**广告**|**选择**|**补贴**|**团队**|
|**瑜伽**|**摩拜单车**|**研究院**|**实验室**|**甚至**|**虚拟现实**|**农夫山泉**|**政策**|**泡沫**|**酒店**|
|**麦当劳**|~~并没有~~|**追踪**|**旅游**|**肿瘤**|**医疗器械**|**区块链**|**教育**|**智能音箱**|**浏览器**|
|**购买**|**品牌**|**激光雷达**|**蜘蛛侠**|**长租公寓**|**为什么**|**直播**|**幼儿园**|**互联网**|**表示**|
|**俱乐部**|**星巴克**|**网络**|**小程序**|**组织**|**支付宝**|**芯片**|**集团**|**富士康**|**机器学习**|

* 医疗行业数据集top20, 短语抽取用时2.55s

|布洛芬|精神状态|双歧杆菌|阿奇霉素|**妈咪爱**|母乳|**治疗**|**益生菌**|**显示**|**频繁**|
| :-:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|**蒙脱石散**|**精神**|**连续**|**疫苗**|**偶尔**|**黄疸**|**流鼻涕**|**检查**|**肺炎**|**拉肚子**|

## algorithm

* 词语的score计算通过内部的get_scores函数实现，score公式如下：

![](https://latex.codecogs.com/png.latex?AMI=\frac{1}{n}%20\log_{%20}{\frac{p%28W%29}{p%28c_{1}%29%20\cdots%20p%28c_{n}%29}})

![](https://latex.codecogs.com/png.latex?L%28W%29=\log_{%20}{\frac{LE%20\cdot%20e^{RE}+RE%20\cdot%20e^{LE}}{|LE-RE|}})

![](https://latex.codecogs.com/png.latex?score=AMI+L%28W%29)

* hanlp提出的score计算方法如下：

![](https://latex.codecogs.com/png.latex?score_{HanLP}=min%28LE,RE%29+pmi)

下面是HanLP和SmoothNLP短语抽取top500结果的**精准度对比** ,及**top100**词展示   
使用的文本是5000条36kr新闻文本

* **HanLP** top500词精准度28.2%

|互联网公司|新浪微博| ~~已经成为~~| ~~中国市场~~| ~~视频网站~~| ~~过程中~~| ~~会不会~~| 移动互联网|资本市场| 电商平台|
|:-:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|**用户体验**|**互联网企业**|**传统企业**|~~会成为~~|~~中国互联网~~|**产品服务**|~~会出现~~|**创业公司**|**社交网络**|**乐视**|
|~~中移动~~|~~用户提供~~|**移动端**|**互联网金融**|~~是否会~~|~~会更~~|**电商企业**|**用户需求**|**团购网站**|**手机厂商**|
|**互联网思维**|**手机市场**|**小米手机**|~~会发现~~|~~市场中~~|~~中国企业~~|~~更重要~~|~~非常重要~~|~~肯定会~~|~~必然会~~|
|~~想做~~|~~用户使用~~|~~用户会~~|**国内市场**|**传统行业**|**微博微信**|~~会越来越~~|~~做产品~~|~~早已经~~|**互联网行业**|
|~~做手机~~|~~会选择~~|**智能电视**|**生活服务**|**互联网巨头**|~~已经形成~~|**电商网站**|**移动支付**|**社交媒体**|**媒体平台**|
|~~市场已经~~|~~会更多~~|~~市场发展~~|**应用商店**|**解决问题**|~~做事情~~|~~中国电商~~|~~视频内容~~|~~几乎没有~~|**腾讯微博**|
|~~用户进行~~|**大众点评**|~~提供服务~~|**网络视频**|**广告收入**|~~自然会~~|~~真正意义~~|**微信支付**|**企业文化**|**粉丝经济**|
|~~没有太多~~|~~成为中国~~|~~已经不再~~|**更强**|**云服务**|~~重要原因~~|**手机行业**|~~会继续~~|**产品经理**|**互联网电视**|
|~~线城市~~|~~更需要~~|~~应该会~~|**苹果手机**|**电商行业**|**全球市场**|**移动搜索**|~~会用户~~|~~服务能力~~|**投资机构**|


* **SmoothNLP** top500词精准度**96.4%**

|**阿里巴巴**|**以及**|**周鸿祎**|**还是**|**亚马逊**|**甚至**|**用户**|**技术**|**腾讯**|**支付宝**|
| :-:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|**百度**|**李彦宏**|**CEO**|**选择**|**消费者**|**诺基亚**|**市场**|**游戏**|**服务**|**已经**|
|**苹果**|**淘宝**|**京东**|**新浪微博**|**开始**|**品牌**|**小米**|**苏宁**|**广告**|**为什么**|
|**可穿戴设备**|**平台**|**O2O**|**浏览器**|**产品**|**可以**|**谷歌**|**乔布斯**|**宣布**|**包括**|
|**汽车**|**如何**|**移动互联网**|**遭遇**|**或者**|**颠覆**|**团队**|**搜索引擎**|**阿里**|**应该**|
|**特斯拉**|**战略**|**刘强东**|**电商**|**娱乐**|**BAT**|**摩托罗拉**|**进入**|**电子商务**|**进行**|
|**内容**|**似乎**|**网络**|**提升**|**陌陌**|**公司**|**互联网金融**|**能够**|**这样**|**获得**|
|**发展**|**乐视**|**互联网**|**粉丝**|**合作伙伴**|**天猫**|**58同城**|**优酷土豆**|**希望**|**怎么**|
|**互联网思维**|**三星**|**通过**|**世界**|**虚拟现实**|**直接**|**购买**|**手机**|**计划**|**马云**|
|**设计**|**这个**|**中国**|**非常**|**张朝阳**|**信息**|**渠道**|**搜狗**|**继续**|**实现**|



