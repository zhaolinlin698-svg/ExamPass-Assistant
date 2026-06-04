#!/usr/bin/env python3
"""Generate all knowledge HTML and test HTML for 细胞生物学 chapters."""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'ExamPass-Assistant', 'scripts'))
from template_engine import save_knowledge_html, save_test

BASE = '/workspace/细胞生物学'

# ============================================================
# Chapter 1: 绪论
# ============================================================

CH01_KNOWLEDGE = """
<h2>一、细胞生物学概述</h2>

<h3>1.1 细胞生物学的研究内容 <span class="tag-key">重点</span></h3>
<p><span class="kp">细胞生物学</span><span class="exp">——是从细胞整体、亚显微和分子三个水平上研究细胞生命活动规律的科学。</span></p>
<p><strong>三个研究层次</strong>：</p>
<ul>
  <li><span class="kp">显微水平</span><span class="exp">——光学显微镜下观察细胞形态结构</span></li>
  <li><span class="kp">亚显微水平</span><span class="exp">——电子显微镜下观察细胞器的超微结构</span></li>
  <li><span class="kp">分子水平</span><span class="exp">——研究生物大分子的结构与功能</span></li>
</ul>
<p><strong>核心研究问题</strong>：</p>
<ul>
  <li>细胞的<strong>结构和功能</strong>的关系</li>
  <li>细胞的<strong>增殖与分化</strong></li>
  <li>细胞的<strong>衰老与死亡</strong></li>
  <li>细胞的<strong>信号转导</strong></li>
  <li>细胞的<strong>起源与进化</strong></li>
</ul>

<h3>1.2 细胞学说的建立与意义 <span class="tag-must">必考</span></h3>
<p><span class="kp">细胞学说（Cell Theory）</span><span class="exp">——由施莱登（Schleiden）和施旺（Schwann）于1838-1839年提出，是生物学的基石之一。</span></p>
<p><strong>核心内容</strong>：</p>
<ol>
  <li><span class="kp">一切生物体都是由细胞构成的</span><span class="exp">——细胞是生物体的基本结构单位</span></li>
  <li><span class="kp">细胞是生命活动的基本单位</span><span class="exp">——每个细胞都是相对独立的生命单位</span></li>
  <li><span class="kp">细胞来自细胞</span><span class="exp">——新细胞由已存在的细胞分裂产生（Virchow, 1855年补充）</span></li>
</ol>
<blockquote>易错：细胞学说的第三条「细胞来自细胞」是Virchow补充的，不是施莱登和施旺原版的内容。考试常考人物对应关系。</blockquote>

<h3>1.3 当前细胞生物学的重点研究领域 <span class="tag-freq">高频</span></h3>
<ul>
  <li><span class="kp">细胞信号转导</span><span class="exp">——研究细胞如何接收和传递信号</span></li>
  <li><span class="kp">细胞周期调控</span><span class="exp">——揭示细胞增殖的分子机制</span></li>
  <li><span class="kp">细胞凋亡</span><span class="exp">——程序性细胞死亡的分子机制</span></li>
  <li><span class="kp">干细胞生物学</span><span class="exp">——干细胞的维持与分化</span></li>
  <li><span class="kp">肿瘤细胞生物学</span><span class="exp">——癌基因与抑癌基因</span></li>
  <li><span class="kp">表观遗传学</span><span class="exp">——不改变DNA序列的基因表达调控</span></li>
</ul>
"""

CH01_TEST = [
    {"type": "choice", "points": 3,
     "question": "细胞学说的建立者是谁？",
     "options": ["施莱登和施旺", "Virchow和Hooke", "Watson和Crick", "达尔文和华莱士"],
     "answer": 0, "explanation": "细胞学说由施莱登（Schleiden）和施旺（Schwann）于1838-1839年提出。Virchow后来补充了「细胞来自细胞」。"},
    {"type": "choice", "points": 3,
     "question": "细胞生物学研究的三个层次不包括：",
     "options": ["显微水平", "亚显微水平", "分子水平", "原子水平"],
     "answer": 3, "explanation": "三个层次为显微水平（光镜）、亚显微水平（电镜）、分子水平。原子水平不属于细胞生物学的研究层次。"},
    {"type": "tf", "points": 2,
     "question": "细胞学说中「细胞来自细胞」是施莱登和施旺最早提出的。",
     "options": [], "answer": 1,
     "explanation": "错误。该论断是Virchow于1855年补充的，不是施莱登和施旺原版的内容。",
     "pitfall": "注意区分细胞学说三位贡献者的具体贡献"},
    {"type": "short", "points": 8,
     "question": "简述细胞学说的主要内容及其意义。",
     "answer": -1,
     "explanation": "<strong>主要内容</strong>：(1)一切生物体都是由细胞构成的；(2)细胞是生命活动的基本单位；(3)细胞来自细胞（Virchow补充）。<br><strong>意义</strong>：细胞学说揭示了生物界的统一性，阐明了动物和植物在结构基础上的共同起源，是生物学发展的基石。"},
    {"type": "essay", "points": 12,
     "question": "论述当前细胞生物学重点研究领域及其在生命科学中的地位。",
     "answer": -1,
     "explanation": "<strong>重点领域</strong>：(1)细胞信号转导——理解细胞通讯机制；(2)细胞周期调控——揭示增殖机制；(3)细胞凋亡——程序性死亡；(4)干细胞生物学——再生医学基础；(5)肿瘤细胞生物学——癌症机制；(6)表观遗传学——基因表达调控新维度。<br><strong>地位</strong>：细胞生物学是生命科学的核心学科，连接分子生物学与个体生物学，是理解生命现象的基础。"}
]

# ============================================================
# Chapter 2: 细胞统一性与多样性
# ============================================================

CH02_KNOWLEDGE = """
<h2>一、细胞的基本特征</h2>

<h3>2.1 细胞的统一性 <span class="tag-key">重点</span></h3>
<p>所有细胞具有以下共性：</p>
<ul>
  <li><span class="kp">相似的化学组成</span><span class="exp">——都以核酸、蛋白质、脂质、糖类为主</span></li>
  <li><span class="kp">细胞膜</span><span class="exp">——所有细胞都有质膜包围，维持内环境稳定</span></li>
  <li><span class="kp">DNA-RNA-蛋白质</span><span class="exp">——遗传信息流方向一致</span></li>
  <li><span class="kp">核糖体</span><span class="exp">——都有核糖体进行蛋白质合成</span></li>
  <li><span class="kp">一分为二的分裂方式</span><span class="exp">——细胞增殖的基本方式</span></li>
</ul>

<h3>2.2 细胞的多样性 <span class="tag-key">重点</span></h3>

<h4>原核细胞 vs 真核细胞</h4>
<table>
  <tr><th>特征</th><th>原核细胞</th><th>真核细胞</th></tr>
  <tr><td>细胞核</td><td>无核膜（拟核）</td><td>有核膜（真核）</td></tr>
  <tr><td>细胞器</td><td>无膜包被细胞器</td><td>有各种膜包被细胞器</td></tr>
  <tr><td>核糖体</td><td>70S</td><td>80S</td></tr>
  <tr><td>细胞骨架</td><td>无</td><td>有微丝、微管、中间纤维</td></tr>
  <tr><td>细胞壁</td><td>肽聚糖</td><td>植物为纤维素</td></tr>
  <tr><td>DNA</td><td>环状，裸露</td><td>线状，与组蛋白结合</td></tr>
  <tr><td>基因表达</td><td>转录翻译偶联</td><td>转录翻译分隔</td></tr>
</table>
<blockquote>易错：原核细胞没有膜包被的细胞器，但有核糖体。核糖体不是膜包被的细胞器。</blockquote>

<h3>2.3 病毒 <span class="tag-freq">高频</span></h3>
<p><span class="kp">病毒（Virus）</span><span class="exp">——非细胞形态的生命体，由核酸（DNA或RNA）和蛋白质外壳构成，必须在活细胞内寄生增殖。</span></p>
<p><strong>病毒的基本特征</strong>：</p>
<ul>
  <li><span class="kp">非细胞形态</span><span class="exp">——没有细胞结构</span></li>
  <li><span class="kp">只有一种核酸</span><span class="exp">——DNA或RNA，不会同时有两种</span></li>
  <li><span class="kp">专性寄生</span><span class="exp">——必须在活细胞内才能增殖</span></li>
  <li><span class="kp">以复制方式增殖</span><span class="exp">——不是分裂</span></li>
</ul>
<p><strong>病毒增殖过程</strong>：吸附 --&gt; 侵入 --&gt; 脱壳 --&gt; 生物合成 --&gt; 装配 --&gt; 释放</p>

<h3>2.4 模式生物 <span class="tag-freq">高频</span></h3>
<table>
  <tr><th>模式生物</th><th>特点</th><th>主要用途</th></tr>
  <tr><td>大肠杆菌（E. coli）</td><td>繁殖快、遗传背景清楚</td><td>原核基因表达调控</td></tr>
  <tr><td>酵母（S. cerevisiae）</td><td>单细胞真核、易培养</td><td>细胞周期、蛋白质相互作用</td></tr>
  <tr><td>线虫（C. elegans）</td><td>细胞数固定、透明</td><td>发育生物学、细胞凋亡</td></tr>
  <tr><td>果蝇（D. melanogaster）</td><td>繁殖快、染色体少</td><td>遗传学、发育生物学</td></tr>
  <tr><td>拟南芥（Arabidopsis）</td><td>基因组小、生长快</td><td>植物分子生物学</td></tr>
  <tr><td>小鼠（M. musculus）</td><td>哺乳动物、基因操作成熟</td><td>人类疾病模型</td></tr>
</table>

<h3>2.5 古核细胞（古细菌）<span class="tag-info">了解</span></h3>
<p><span class="kp">古细菌</span><span class="exp">——形态类似细菌，但分子特征更接近真核生物，是第三类生命形式。生活在极端环境（高温、高盐、厌氧等）。</span></p>
"""

CH02_TEST = [
    {"type": "choice", "points": 3,
     "question": "下列关于原核细胞与真核细胞区别的描述，错误的是：",
     "options": ["原核细胞无核膜", "原核细胞的核糖体为70S", "原核细胞有各种膜包被细胞器", "原核细胞的DNA是环状的"],
     "answer": 2, "explanation": "原核细胞没有膜包被的细胞器（如线粒体、内质网等），这是原核细胞与真核细胞最重要的区别之一。"},
    {"type": "choice", "points": 3,
     "question": "病毒增殖的方式是：",
     "options": ["二分裂", "出芽", "复制", "有丝分裂"],
     "answer": 2, "explanation": "病毒以复制方式增殖，不是分裂。病毒利用宿主细胞的代谢系统复制核酸和蛋白质，然后装配成新的病毒颗粒。"},
    {"type": "multi", "points": 4,
     "question": "下列哪些属于细胞的统一性特征？",
     "options": ["都有细胞膜", "都有核糖体", "遗传物质都是DNA", "都有线粒体", "都以一分为二的方式分裂"],
     "answer": [0, 1, 2, 4], "explanation": "并非所有细胞都有线粒体——原核细胞没有线粒体。其他四项都是所有细胞的共性。"},
    {"type": "tf", "points": 2,
     "question": "古细菌属于原核生物。",
     "options": [], "answer": 0,
     "explanation": "正确。古细菌（古核细胞）在形态上属于原核生物（无核膜），但分子特征上更接近真核生物，是第三类生命形式。"},
    {"type": "short", "points": 8,
     "question": "简述病毒作为非细胞形态生命体的主要特征。",
     "answer": -1,
     "explanation": "(1)非细胞形态，由核酸和蛋白质外壳构成；(2)只含一种核酸（DNA或RNA）；(3)必须在活细胞内寄生增殖（专性寄生）；(4)以复制方式而非分裂方式增殖。"},
    {"type": "essay", "points": 12,
     "question": "病毒是非细胞形态的生命体，结合近年病毒肆虐的实际谈谈你自己对病毒的认识。",
     "answer": -1,
     "explanation": "<strong>答题要点</strong>：(1)病毒的基本特征：非细胞形态、一种核酸、专性寄生；(2)病毒与宿主的关系：侵入--&gt;复制--&gt;致病；(3)近年病毒（如新冠病毒）的传播特点；(4)防治策略：疫苗、抗病毒药物、公共卫生措施。"}
]

# ============================================================
# Chapter 3: 细胞生物学研究方法
# ============================================================

CH03_KNOWLEDGE = """
<h2>三、细胞生物学研究方法</h2>

<h3>3.1 显微镜技术 <span class="tag-must">必考</span></h3>

<h4>光学显微镜</h4>
<p><span class="kp">分辨率</span><span class="exp">——能区分两个点的最小距离。光学显微镜的分辨率极限约为0.2μm。</span></p>
<p>$$d = \\frac{0.61\\lambda}{NA} = \\frac{0.61\\lambda}{n \\sin\\alpha}$$</p>
<p><span class="kp">$\lambda$为波长，$NA$为数值孔径，$n$为介质折射率，$\alpha$为孔径角的一半。</span></p>

<table>
  <tr><th>显微镜类型</th><th>光源</th><th>分辨率</th><th>特点</th></tr>
  <tr><td>普通光学显微镜</td><td>可见光</td><td>~0.2μm</td><td>观察细胞大体结构</td></tr>
  <tr><td>荧光显微镜</td><td>紫外/蓝光</td><td>~0.2μm</td><td>特异性标记蛋白质/核酸</td></tr>
  <tr><td>共聚焦显微镜</td><td>激光</td><td>~0.2μm</td><td>光学切片、三维重建</td></tr>
  <tr><td>相差显微镜</td><td>可见光</td><td>~0.2μm</td><td>观察活细胞，无需染色</td></tr>
</table>

<h4>电子显微镜 <span class="tag-must">必考</span></h4>
<p><span class="kp">电子显微镜</span><span class="exp">——以电子束为光源，分辨率可达0.1nm，远高于光学显微镜。</span></p>

<table>
  <tr><th>类型</th><th>透射电镜（TEM）</th><th>扫描电镜（SEM）</th></tr>
  <tr><td>成像原理</td><td>电子束穿透样品</td><td>电子束扫描样品表面</td></tr>
  <tr><td>观察内容</td><td>内部超微结构</td><td>表面三维形貌</td></tr>
  <tr><td>样品要求</td><td>超薄切片（50-100nm）</td><td>表面喷镀金属</td></tr>
  <tr><td>分辨率</td><td>~0.1nm</td><td>~1-3nm</td></tr>
</table>
<blockquote>易错：(1)透射电镜看内部，扫描电镜看表面。(2)扫描电镜样品不需要超薄切片，但需要喷镀金属。(3)电镜观察的样品必须是死细胞（需固定）。</blockquote>

<h3>3.2 细胞及其组分的分析方法 <span class="tag-key">重点</span></h3>
<ul>
  <li><span class="kp">差速离心</span><span class="exp">——根据细胞器大小和密度不同，在不同离心力下分离细胞组分</span></li>
  <li><span class="kp">密度梯度离心</span><span class="exp">——在密度梯度介质中分离不同密度的细胞器</span></li>
  <li><span class="kp">流式细胞术</span><span class="exp">——对单个细胞进行快速定量分析和分选</span></li>
  <li><span class="kp">免疫荧光技术</span><span class="exp">——用荧光标记抗体定位特定蛋白质</span></li>
  <li><span class="kp">核酸原位杂交</span><span class="exp">——用标记探针检测细胞内特定核酸序列</span></li>
</ul>

<h3>3.3 细胞培养与细胞工程 <span class="tag-freq">高频</span></h3>
<p><span class="kp">细胞培养</span><span class="exp">——在体外模拟体内环境，使细胞生长和增殖的技术。</span></p>
<ul>
  <li><span class="kp">原代培养</span><span class="exp">——直接从组织分离的细胞进行培养</span></li>
  <li><span class="kp">传代培养</span><span class="exp">——原代细胞增殖后转移到新培养瓶</span></li>
  <li><span class="kp">细胞系</span><span class="exp">——可长期传代培养的细胞群体</span></li>
  <li><span class="kp">细胞融合</span><span class="exp">——两个或多个细胞融合成一个杂合细胞</span></li>
</ul>
"""

CH03_TEST = [
    {"type": "choice", "points": 3,
     "question": "与透射电镜相比，扫描电镜的主要特点是：",
     "options": ["分辨率更高", "观察内部超微结构", "观察表面三维形貌", "样品需要超薄切片"],
     "answer": 2, "explanation": "扫描电镜观察样品表面三维形貌，分辨率约1-3nm；透射电镜观察内部超微结构，分辨率约0.1nm，需要超薄切片。"},
    {"type": "choice", "points": 3,
     "question": "光学显微镜的分辨率极限约为：",
     "options": ["0.2nm", "2nm", "0.2μm", "2μm"],
     "answer": 2, "explanation": "光学显微镜分辨率极限约为0.2μm（200nm），受可见光波长限制。"},
    {"type": "tf", "points": 2,
     "question": "电子显微镜的分辨率高于光学显微镜，因为电子束的波长比可见光短。",
     "options": [], "answer": 0,
     "explanation": "正确。分辨率公式 d=0.61λ/NA，波长越短分辨率越高。电子束波长远小于可见光。"},
    {"type": "short", "points": 8,
     "question": "简述差速离心和密度梯度离心的区别。",
     "answer": -1,
     "explanation": "<strong>差速离心</strong>：根据大小和密度差异，在不同离心力下依次沉降不同细胞器（先沉大而重的核，再沉线粒体等）。<br><strong>密度梯度离心</strong>：在密度梯度介质中，细胞器在与其密度相等的介质层中沉降，按密度精确分离。"},
    {"type": "short", "points": 8,
     "question": "简述荧光显微镜和共聚焦显微镜的异同。",
     "answer": -1,
     "explanation": "相同：都使用荧光标记物。不同：(1)共聚焦显微镜使用激光光源，荧光显微镜使用普通光源；(2)共聚焦可以光学切片、三维重建，荧光显微镜不能；(3)共聚焦分辨率略高，可消除焦外荧光干扰。"}
]

# ============================================================
# Chapter 4: 细胞质膜
# ============================================================

CH04_KNOWLEDGE = """
<h2>四、细胞质膜</h2>

<h3>4.1 细胞质膜的结构模型 <span class="tag-must">必考</span></h3>
<p><span class="kp">流动镶嵌模型（Fluid Mosaic Model）</span><span class="exp">——由Singer和Nicolson于1972年提出，是当前公认的质膜结构模型。</span></p>
<p><strong>核心内容</strong>：</p>
<ul>
  <li><span class="kp">脂双层是膜的骨架</span><span class="exp">——磷脂分子亲水头部朝外，疏水尾部朝内</span></li>
  <li><span class="kp">膜蛋白镶嵌在脂双层中</span><span class="exp">——蛋白质以不同方式与脂双层结合</span></li>
  <li><span class="kp">膜具有流动性</span><span class="exp">——脂质和蛋白质都可侧向运动</span></li>
  <li><span class="kp">膜是不对称的</span><span class="exp">——内外两层脂质和蛋白质分布不同</span></li>
</ul>

<h3>4.2 膜脂 <span class="tag-key">重点</span></h3>
<table>
  <tr><th>类型</th><th>特点</th><th>功能</th></tr>
  <tr><td><span class="kp">磷脂</span></td><td>含量最多，甘油磷脂+鞘磷脂</td><td>构成脂双层骨架</td></tr>
  <tr><td><span class="kp">糖脂</span></td><td>含糖基，分布于外叶</td><td>细胞识别、保护</td></tr>
  <tr><td><span class="kp">胆固醇</span></td><td>动物细胞特有，嵌在磷脂之间</td><td>调节膜流动性</td></tr>
</table>

<h3>4.3 膜蛋白 <span class="tag-key">重点</span></h3>
<table>
  <tr><th>类型</th><th>结合方式</th><th>举例</th></tr>
  <tr><td><span class="kp">内在膜蛋白（整合蛋白）</span></td><td>跨膜或深入脂双层</td><td>离子通道、受体</td></tr>
  <tr><td><span class="kp">外在膜蛋白（外周蛋白）</span></td><td>非共价结合在膜表面</td><td>血影蛋白</td></tr>
  <tr><td><span class="kp">脂锚定蛋白</span></td><td>通过共价键与脂质结合</td><td>G蛋白</td></tr>
</table>

<h3>4.4 物质的跨膜运输 <span class="tag-must">必考</span></h3>

<h4>被动运输（不耗能）</h4>
<ul>
  <li><span class="kp">简单扩散</span><span class="exp">——小分子、脂溶性物质直接穿过脂双层（O₂、CO₂、乙醇）</span></li>
  <li><span class="kp">协助扩散</span><span class="exp">——通过通道蛋白或载体蛋白，顺浓度梯度（葡萄糖、氨基酸、离子）</span></li>
</ul>

<h4>主动运输（耗能）</h4>
<ul>
  <li><span class="kp">ATP驱动泵</span><span class="exp">——直接利用ATP水解能量（Na⁺-K⁺泵、Ca²⁺泵）</span></li>
  <li><span class="kp">协同运输</span><span class="exp">——利用一种物质的浓度梯度驱动另一种物质（同向/反向）</span></li>
</ul>

<h4>胞吞与胞吐</h4>
<ul>
  <li><span class="kp">胞吞作用</span><span class="exp">——细胞膜内陷包裹物质进入细胞（吞噬、胞饮、受体介导）</span></li>
  <li><span class="kp">胞吐作用</span><span class="exp">——囊泡与质膜融合释放内容物（组成型、调节型）</span></li>
</ul>

<h3>4.5 细胞表面特化结构 <span class="tag-freq">高频</span></h3>
<ul>
  <li><span class="kp">细胞外被（糖萼）</span><span class="exp">——糖蛋白和糖脂的糖链在细胞表面形成，参与细胞识别和免疫</span></li>
  <li><span class="kp">细胞外基质（ECM）</span><span class="exp">——由细胞分泌的胶原、弹性蛋白、蛋白聚糖等构成</span></li>
  <li><span class="kp">血影（Ghost）</span><span class="exp">——红细胞经低渗处理后，血红蛋白释放，留下的质膜空壳</span></li>
</ul>
<blockquote>易错：血影是研究质膜的重要模型材料，保留了完整的质膜结构和膜骨架。</blockquote>
"""

CH04_TEST = [
    {"type": "choice", "points": 3,
     "question": "流动镶嵌模型的核心内容不包括：",
     "options": ["脂双层是膜的骨架", "膜蛋白镶嵌在脂双层中", "膜具有流动性", "膜两侧的蛋白质分布是对称的"],
     "answer": 3, "explanation": "膜是不对称的——内外两层脂质和蛋白质分布不同。对称性是错误的。"},
    {"type": "choice", "points": 3,
     "question": "下列哪种物质通过简单扩散穿过细胞膜？",
     "options": ["葡萄糖", "Na⁺", "O₂", "氨基酸"],
     "answer": 2, "explanation": "O₂是脂溶性小分子，可直接穿过脂双层（简单扩散）。葡萄糖、氨基酸、Na⁺都需要转运蛋白协助。"},
    {"type": "multi", "points": 4,
     "question": "下列哪些属于主动运输？",
     "options": ["Na⁺-K⁺泵", "葡萄糖的协助扩散", "Ca²⁺泵", "受体介导的胞吞"],
     "answer": [0, 2, 3], "explanation": "Na⁺-K⁺泵和Ca²⁺泵直接消耗ATP；受体介导的胞吞也需要能量。葡萄糖的协助扩散不耗能，属于被动运输。"},
    {"type": "tf", "points": 2,
     "question": "血影是红细胞经低渗处理后的产物，可用于研究质膜结构。",
     "options": [], "answer": 0,
     "explanation": "正确。血影（ghost）是红细胞经低渗处理后血红蛋白释放后留下的空壳，保留了完整的质膜和膜骨架，是研究质膜的好材料。"},
    {"type": "short", "points": 8,
     "question": "比较组成型胞吐途径和调节型胞吐途径的特点及其生物学意义。",
     "answer": -1,
     "explanation": "<strong>组成型胞吐</strong>：持续进行，不需要信号刺激，所有真核细胞都有，运输细胞外基质成分和质膜蛋白。<br><strong>调节型胞吐</strong>：需要特定信号触发（如Ca²⁺内流），存在于分泌细胞，分泌激素、神经递质等。<br><strong>意义</strong>：组成型维持基本功能，调节型实现快速响应。"},
    {"type": "essay", "points": 12,
     "question": "论述生物大分子物质的跨膜运输方式及其特点。",
     "answer": -1,
     "explanation": "<strong>胞吞作用</strong>：(1)吞噬作用——吞噬大颗粒（如细菌）；(2)胞饮作用——吞噬液体和溶质；(3)受体介导的胞吞——特异性高效。<br><strong>胞吐作用</strong>：(1)组成型——持续分泌；(2)调节型——信号触发分泌。<br><strong>特点</strong>：都需要能量，涉及膜的融合和分离，可运输大分子甚至颗粒。"}
]

# ============================================================
# Chapter 5: 内膜系统与蛋白质分选
# ============================================================

CH05_KNOWLEDGE = """
<h2>五、内膜系统与蛋白质分选</h2>

<h3>5.1 内膜系统概述 <span class="tag-key">重点</span></h3>
<p><span class="kp">内膜系统（Endomembrane System）</span><span class="exp">——真核细胞中在结构、功能和发生上相互关联的膜性细胞器系统，包括内质网、高尔基体、溶酶体、内体和分泌泡等。</span></p>
<p><strong>特点</strong>：</p>
<ul>
  <li>各成员在<strong>结构上</strong>通过膜泡运输互相连通</li>
  <li>在<strong>功能上</strong>协同完成蛋白质加工、分选和运输</li>
  <li>在<strong>发生上</strong>都有共同的起源和进化关系</li>
</ul>

<h3>5.2 内质网（ER）<span class="tag-must">必考</span></h3>

<h4>粗面内质网（rER）</h4>
<ul>
  <li><span class="kp">结构</span><span class="exp">——扁平囊状，表面附着核糖体</span></li>
  <li><span class="kp">功能</span><span class="exp">——分泌蛋白和膜蛋白的合成与加工、蛋白质折叠（分子伴侣）、N-连接糖基化</span></li>
</ul>

<h4>滑面内质网（sER）</h4>
<ul>
  <li><span class="kp">结构</span><span class="exp">——管状，无核糖体附着</span></li>
  <li><span class="kp">功能</span><span class="exp">——脂质合成、解毒作用、Ca²⁺储存（肌细胞中为肌质网）</span></li>
</ul>

<h3>5.3 高尔基体 <span class="tag-must">必考</span></h3>
<p><span class="kp">高尔基体</span><span class="exp">——由扁平膜囊堆叠而成，具有极性：顺面（cis面，面向ER）和反面（trans面，面向质膜）。</span></p>
<p><strong>功能</strong>：</p>
<ul>
  <li><span class="kp">蛋白质的糖基化修饰</span><span class="exp">——O-连接糖基化、N-连接糖链的进一步修饰</span></li>
  <li><span class="kp">蛋白质的分选</span><span class="exp">——将蛋白质分选到溶酶体、分泌泡或质膜</span></li>
  <li><span class="kp">溶酶体的形成</span><span class="exp">——溶酶体酶的分选（M6P途径）</span></li>
</ul>

<h3>5.4 溶酶体 <span class="tag-must">必考</span></h3>
<p><span class="kp">溶酶体</span><span class="exp">——含有多种酸性水解酶（最适pH~5.0）的膜包细胞器，是细胞内的消化系统。</span></p>
<table>
  <tr><th>类型</th><th>特点</th></tr>
  <tr><td><span class="kp">初级溶酶体</span></td><td>刚从高尔基体出芽，含酶但未进行消化</td></tr>
  <tr><td><span class="kp">次级溶酶体</span></td><td>与底物融合后，正在进行消化</td></tr>
  <tr><td><span class="kp">残余体</span></td><td>消化完成后剩余的残渣</td></tr>
</table>
<p><strong>功能</strong>：</p>
<ul>
  <li><span class="kp">异噬作用</span><span class="exp">——消化外来物质</span></li>
  <li><span class="kp">自噬作用</span><span class="exp">——消化自身衰老细胞器</span></li>
  <li><span class="kp">自溶作用</span><span class="exp">——细胞死亡时溶酶体膜破裂</span></li>
</ul>

<h3>5.5 蛋白质分选与膜泡运输 <span class="tag-must">必考</span></h3>
<p><span class="kp">信号假说（Signal Hypothesis）</span><span class="exp">——由Blobel提出，分泌蛋白N端有信号肽序列，引导核糖体附着到ER膜上。</span></p>
<p><strong>过程</strong>：</p>
<ol>
  <li>信号肽被<strong>信号识别颗粒（SRP）</strong>识别</li>
  <li>SRP-核糖体复合体结合到ER膜上的<strong>SRP受体</strong></li>
  <li>核糖体附着到<strong>易位子</strong>上，信号肽进入ER腔</li>
  <li>信号肽被<strong>信号肽酶</strong>切除</li>
  <li>新生肽链进入ER腔，分子伴侣帮助折叠</li>
</ol>

<h3>5.6 蛋白质分选的基本途径</h3>
<ul>
  <li><span class="kp">共翻译转运</span><span class="exp">——边翻译边转运（ER、质膜、分泌蛋白、溶酶体蛋白）</span></li>
  <li><span class="kp">翻译后转运</span><span class="exp">——翻译完成后转运（线粒体、叶绿体、过氧化物酶体、细胞核）</span></li>
</ul>
<blockquote>易错：(1)共翻译转运进入ER的蛋白质有信号肽；(2)翻译后转运进入线粒体/叶绿体的蛋白质有导肽（前导序列）；(3)核定位信号（NLS）是翻译后转运进入细胞核的信号。</blockquote>
"""

CH05_TEST = [
    {"type": "choice", "points": 3,
     "question": "下列不属于内膜系统的是：",
     "options": ["内质网", "高尔基体", "溶酶体", "线粒体"],
     "answer": 3, "explanation": "线粒体不是内膜系统成员。内膜系统包括内质网、高尔基体、溶酶体、内体、分泌泡等，它们通过膜泡运输相互联系。"},
    {"type": "choice", "points": 3,
     "question": "信号识别颗粒（SRP）的功能是：",
     "options": ["切除信号肽", "识别信号肽并引导核糖体到ER膜", "帮助蛋白质折叠", "将蛋白质运出细胞核"],
     "answer": 1, "explanation": "SRP识别信号肽，然后引导核糖体-mRNA-新生肽链复合体结合到ER膜上的SRP受体。切除信号肽的是信号肽酶。"},
    {"type": "tf", "points": 2,
     "question": "溶酶体酶的最适pH为7.0左右。",
     "options": [], "answer": 1,
     "explanation": "错误。溶酶体酶是酸性水解酶，最适pH约为5.0。溶酶体膜上的H⁺泵维持内部酸性环境。"},
    {"type": "short", "points": 8,
     "question": "简述溶酶体的发生过程和基本功能。",
     "answer": -1,
     "explanation": "<strong>发生过程</strong>：溶酶体酶在rER合成--&gt;经高尔基体加工（M6P标记）--&gt;从高尔基体trans面出芽形成初级溶酶体--&gt;与内体/底物融合形成次级溶酶体。<br><strong>功能</strong>：异噬作用（消化外来物质）、自噬作用（消化自身衰老细胞器）、自溶作用（细胞死亡时）。"},
    {"type": "short", "points": 8,
     "question": "简述细胞内蛋白质分选的两条基本途径。",
     "answer": -1,
     "explanation": "<strong>共翻译转运</strong>：边翻译边转运，信号肽引导核糖体到ER膜，蛋白质进入ER腔。适用于分泌蛋白、膜蛋白、溶酶体蛋白。<br><strong>翻译后转运</strong>：翻译完成后转运，由导肽/NLS等信号引导。适用于线粒体蛋白、叶绿体蛋白、核蛋白、过氧化物酶体蛋白。"},
    {"type": "essay", "points": 12,
     "question": "描述细胞内分泌蛋白从合成到分泌的全过程。",
     "answer": -1,
     "explanation": "(1)信号肽合成--&gt;SRP识别--&gt;结合SRP受体--&gt;共翻译转运进入ER腔；(2)ER内：信号肽切除、分子伴侣辅助折叠、N-连接糖基化；(3)COPII囊泡运输到高尔基体cis面；(4)高尔基体内：糖链修饰、分选；(5)从trans面出芽形成分泌囊泡；(6)囊泡与质膜融合，胞吐释放。"}
]

# ============================================================
# Generate all files
# ============================================================

chapters = [
    ("01-绪论", "第一章 绪论", CH01_KNOWLEDGE, CH01_TEST),
    ("02-细胞统一性与多样性", "第二章 细胞的统一性与多样性", CH02_KNOWLEDGE, CH02_TEST),
    ("03-细胞生物学研究方法", "第三章 细胞生物学研究方法", CH03_KNOWLEDGE, CH03_TEST),
    ("04-细胞质膜", "第四章 细胞质膜", CH04_KNOWLEDGE, CH04_TEST),
    ("05-内膜系统与蛋白质分选", "第五章 内膜系统与蛋白质分选", CH05_KNOWLEDGE, CH05_TEST),
]

for folder, title, knowledge, test in chapters:
    dir_path = os.path.join(BASE, folder)
    os.makedirs(dir_path, exist_ok=True)
    
    # Knowledge HTML
    knowledge_path = os.path.join(dir_path, "知识清单.html")
    save_knowledge_html(knowledge, knowledge_path, title)
    print(f"Generated: {knowledge_path}")
    
    # Test HTML
    test_path = os.path.join(dir_path, "章节测试.html")
    save_test(test, test_path, title, duration_minutes=45)
    print(f"Generated: {test_path}")

print("\nDone! Generated knowledge and test for 5 chapters.")