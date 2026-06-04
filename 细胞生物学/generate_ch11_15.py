#!/usr/bin/env python3
"""Generate knowledge HTML and test HTML for chapters 11-15."""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'ExamPass-Assistant', 'scripts'))
from template_engine import save_knowledge_html, save_test

BASE = '/workspace/细胞生物学'

# ============================================================
# Chapter 11: 细胞周期与细胞分裂
# ============================================================

CH11_KNOWLEDGE = r"""
<h2>十一、细胞周期与细胞分裂</h2>

<h3>11.1 细胞周期概述 <span class="tag-must">必考</span></h3>
<p><span class="kp">细胞周期（Cell Cycle）</span><span class="exp">——细胞从一次分裂结束到下一次分裂结束所经历的过程，是细胞增殖的基本方式。</span></p>
<p><strong>细胞周期的时相</strong>：</p>
<table>
  <tr><th>时相</th><th>主要事件</th><th>持续时间</th></tr>
  <tr><td><span class="kp">G₁期</span></td><td>RNA和蛋白质合成，细胞生长</td><td>可变（最长）</td></tr>
  <tr><td><span class="kp">S期</span></td><td>DNA复制，组蛋白合成</td><td>~6-8小时</td></tr>
  <tr><td><span class="kp">G₂期</span></td><td>合成有丝分裂所需蛋白（微管蛋白等）</td><td>~2-4小时</td></tr>
  <tr><td><span class="kp">M期</span></td><td>有丝分裂（核分裂）+ 胞质分裂</td><td>~1小时</td></tr>
</table>
<p><span class="kp">G₀期细胞</span><span class="exp">——退出细胞周期、暂时不增殖的细胞，可被诱导重新进入细胞周期。</span></p>
<p><span class="kp">周期中细胞（Cycling Cell）</span><span class="exp">——正在细胞周期中循环增殖的细胞。</span></p>

<h3>11.2 有丝分裂（Mitosis）<span class="tag-must">必考</span></h3>
<p><strong>前期</strong>：</p>
<ul>
  <li>染色质凝缩为染色体（每条染色体含两条姐妹染色单体）</li>
  <li>中心体分离，向两极移动，形成纺锤体</li>
  <li>核仁解体，核被膜崩解</li>
</ul>
<p><strong>中期</strong>：</p>
<ul>
  <li>染色体排列在赤道板上</li>
  <li>动粒微管与染色体着丝粒连接</li>
  <li>染色体形态最清晰（核型分析的最佳时期）</li>
</ul>
<p><strong>后期</strong>：</p>
<ul>
  <li><span class="kp">后期A</span><span class="exp">——动粒微管缩短，姐妹染色单体向两极分离</span></li>
  <li><span class="kp">后期B</span><span class="exp">——极微管滑动，两极距离增大</span></li>
</ul>
<p><strong>末期</strong>：</p>
<ul>
  <li>染色体解螺旋为染色质</li>
  <li>核被膜重新形成，核仁出现</li>
  <li>胞质分裂（收缩环由肌动蛋白和肌球蛋白组成）</li>
</ul>

<h3>11.3 减数分裂（Meiosis）<span class="tag-must">必考</span></h3>
<p><span class="kp">减数分裂</span><span class="exp">——生殖细胞特有的分裂方式，DNA复制一次，细胞分裂两次，产生染色体数减半的配子。</span></p>

<h4>减数分裂I（同源染色体分离）</h4>
<ul>
  <li><span class="kp">前期I</span><span class="exp">——同源染色体配对（联会）、交叉互换（重组）</span></li>
  <li><span class="kp">中期I</span><span class="exp">——同源染色体对排列在赤道板上</span></li>
  <li><span class="kp">后期I</span><span class="exp">——同源染色体分离（着丝粒不分裂）</span></li>
</ul>

<h4>减数分裂II（类似有丝分裂）</h4>
<ul>
  <li>着丝粒分裂，姐妹染色单体分离</li>
</ul>

<h3>11.4 有丝分裂与减数分裂的比较 <span class="tag-must">必考</span></h3>
<table>
  <tr><th>特征</th><th>有丝分裂</th><th>减数分裂</th></tr>
  <tr><td>DNA复制次数</td><td>1次</td><td>1次</td></tr>
  <tr><td>分裂次数</td><td>1次</td><td>2次</td></tr>
  <tr><td>子细胞数</td><td>2</td><td>4</td></tr>
  <tr><td>染色体数</td><td>不变（2n --&gt; 2n）</td><td>减半（2n --&gt; n）</td></tr>
  <tr><td>同源染色体配对</td><td>无</td><td>有（联会）</td></tr>
  <tr><td>基因重组</td><td>无</td><td>有（交叉互换）</td></tr>
  <tr><td>发生场所</td><td>体细胞</td><td>生殖细胞</td></tr>
</table>
<blockquote>易错：减数分裂DNA复制一次但分裂两次，最后染色体数减半。有丝分裂DNA复制一次分裂一次，染色体数不变。</blockquote>

<h3>11.5 细胞周期同步化 <span class="tag-freq">高频</span></h3>
<ul>
  <li><span class="kp">自然同步化</span><span class="exp">——某些生物体自然存在的同步分裂（如果蝇早期胚胎）</span></li>
  <li><span class="kp">人工同步化</span><span class="exp">——药物阻断（如胸腺嘧啶脱氧核苷阻断S期）、饥饿法等</span></li>
</ul>
"""

CH11_TEST = [
    {"type": "choice", "points": 3,
     "question": "细胞周期中DNA复制发生在：",
     "options": ["G₁期", "S期", "G₂期", "M期"],
     "answer": 1, "explanation": "DNA复制发生在S期（Synthesis phase）。G₁期细胞生长，G₂期准备分裂，M期进行分裂。"},
    {"type": "choice", "points": 3,
     "question": "减数分裂中同源染色体分离发生在：",
     "options": ["前期I", "中期I", "后期I", "后期II"],
     "answer": 2, "explanation": "后期I是同源染色体分离的时期（着丝粒不分裂）。后期II是姐妹染色单体分离（着丝粒分裂），类似有丝分裂。"},
    {"type": "multi", "points": 4,
     "question": "减数分裂不同于有丝分裂的特点包括：",
     "options": ["有同源染色体联会", "DNA复制一次", "发生基因重组", "分裂两次", "子细胞染色体数不变"],
     "answer": [0, 2, 3], "explanation": "有丝分裂和减数分裂的DNA都复制一次；减数分裂子细胞染色体数减半。联会、基因重组、分裂两次是减数分裂特有的。"},
    {"type": "tf", "points": 2,
     "question": "G₀期细胞是永久退出细胞周期、不再增殖的细胞。",
     "options": [], "answer": 1,
     "explanation": "错误。G₀期细胞是暂时退出细胞周期的细胞，在适当刺激下可以重新进入细胞周期。永久退出细胞周期的细胞是终末分化细胞。"},
    {"type": "short", "points": 8,
     "question": "比较有丝分裂和减数分裂的异同。",
     "answer": -1,
     "explanation": "<strong>相同</strong>：DNA都复制一次；都形成纺锤体；都有染色体的凝缩和分离。<br><strong>不同</strong>：(1)有丝分裂分裂1次，减数分裂分裂2次；(2)有丝分裂子细胞染色体数不变，减数分裂减半；(3)减数分裂有联会和交叉互换（基因重组），有丝分裂没有；(4)有丝分裂发生在体细胞，减数分裂发生在生殖细胞。"},
    {"type": "essay", "points": 12,
     "question": "论述细胞周期各时相的主要事件。",
     "answer": -1,
     "explanation": "<strong>G₁期</strong>：RNA和蛋白质大量合成，细胞生长，合成DNA复制所需的酶和蛋白质，是细胞周期中最长的时相。<br><strong>S期</strong>：DNA复制，组蛋白合成，每条染色体由1条DNA分子变为2条姐妹染色单体。<br><strong>G₂期</strong>：合成微管蛋白等有丝分裂相关蛋白，检查DNA复制是否完成。<br><strong>M期</strong>：前期染色质凝缩、纺锤体形成；中期染色体排列在赤道板；后期姐妹染色单体分离；末期核膜重建、胞质分裂。"}
]

# ============================================================
# Chapter 12: 细胞周期调控与癌症
# ============================================================

CH12_KNOWLEDGE = r"""
<h2>十二、细胞周期调控与癌症</h2>

<h3>12.1 细胞周期调控因子 <span class="tag-must">必考</span></h3>
<p><span class="kp">MPF（成熟促进因子/M期促进因子）</span><span class="exp">——由周期蛋白B（Cyclin B）和CDK1（Cdc2）组成的蛋白激酶复合物，驱动细胞从G₂期进入M期。</span></p>

<p><strong>核心调控因子</strong>：</p>
<ul>
  <li><span class="kp">周期蛋白（Cyclin）</span><span class="exp">——浓度随细胞周期波动，周期性合成与降解</span></li>
  <li><span class="kp">周期蛋白依赖性激酶（CDK）</span><span class="exp">——浓度恒定，活性受周期蛋白调控</span></li>
</ul>

<table>
  <tr><th>周期蛋白</th><th>结合的CDK</th><th>作用时相</th></tr>
  <tr><td>Cyclin D</td><td>CDK4/6</td><td>G₁期</td></tr>
  <tr><td>Cyclin E</td><td>CDK2</td><td>G₁/S转换</td></tr>
  <tr><td>Cyclin A</td><td>CDK2/CDK1</td><td>S期和G₂/M转换</td></tr>
  <tr><td>Cyclin B</td><td>CDK1</td><td>G₂/M转换</td></tr>
</table>

<h3>12.2 细胞周期检验点 <span class="tag-must">必考</span></h3>
<p><span class="kp">检验点（Checkpoint）</span><span class="exp">——细胞周期中的监控机制，确保上一阶段完成后再进入下一阶段。</span></p>
<table>
  <tr><th>检验点</th><th>检查内容</th></tr>
  <tr><td><span class="kp">G₁/S检验点（限制点/Restriction point）</span></td><td>细胞大小、营养条件、生长因子、DNA是否损伤</td></tr>
  <tr><td><span class="kp">G₂/M检验点</span></td><td>DNA复制是否完成、是否有损伤、细胞大小</td></tr>
  <tr><td><span class="kp">M期检验点（纺锤体检验点）</span></td><td>染色体是否都正确连接到纺锤体上</td></tr>
</table>
<blockquote>易错：G₁/S检验点也叫限制点（restriction point），通过此点后细胞通常不再依赖生长因子即可完成整个周期。</blockquote>

<h3>12.3 癌细胞的特征 <span class="tag-must">必考</span></h3>
<ul>
  <li><span class="kp">无限增殖</span><span class="exp">——摆脱正常增殖限制</span></li>
  <li><span class="kp">接触抑制丧失</span><span class="exp">——不因细胞密度增加而停止分裂</span></li>
  <li><span class="kp">锚定依赖性丧失</span><span class="exp">——不需要贴壁即可生长</span></li>
  <li><span class="kp">侵袭和转移</span><span class="exp">——侵入周围组织并远处转移</span></li>
  <li><span class="kp">基因组不稳定性</span><span class="exp">——突变率高</span></li>
</ul>

<h3>12.4 癌基因与抑癌基因 <span class="tag-must">必考</span></h3>
<table>
  <tr><th></th><th>原癌基因/癌基因</th><th>抑癌基因</th></tr>
  <tr><td>功能</td><td>促进细胞增殖</td><td>抑制细胞增殖</td></tr>
  <tr><td>突变效应</td><td>功能获得（gain-of-function）</td><td>功能丧失（loss-of-function）</td></tr>
  <tr><td>举例</td><td>Ras、Myc、Src</td><td>p53、Rb、BRCA1</td></tr>
  <tr><td>激活方式</td><td>点突变、扩增、重排</td><td>缺失、突变、甲基化沉默</td></tr>
</table>
<p><span class="kp">p53</span><span class="exp">——「基因组的守护者」，是最重要的抑癌基因之一。在DNA损伤时p53被激活，诱导p21表达，p21抑制CDK活性，使细胞周期阻滞在G₁期，为DNA修复争取时间。若损伤严重，p53则诱导细胞凋亡。</span></p>
<p><span class="kp">Rb蛋白</span><span class="exp">——视网膜母细胞瘤蛋白，调控G₁/S转换。低磷酸化Rb结合E2F抑制转录；高磷酸化Rb释放E2F，促进S期基因转录。</span></p>
<blockquote>易错：原癌基因是正常基因，突变后成为癌基因。癌基因是显性突变（一个等位基因突变即可），抑癌基因是隐性突变（需要两个等位基因都失活）。</blockquote>
"""

CH12_TEST = [
    {"type": "choice", "points": 3,
     "question": "MPF由以下哪两种成分组成？",
     "options": ["Cyclin D + CDK4", "Cyclin B + CDK1", "Cyclin E + CDK2", "Cyclin A + CDK2"],
     "answer": 1, "explanation": "MPF（成熟促进因子）由Cyclin B和CDK1（Cdc2）组成，驱动G₂/M转换。"},
    {"type": "choice", "points": 3,
     "question": "p53基因属于：",
     "options": ["原癌基因", "癌基因", "抑癌基因", "DNA修复基因"],
     "answer": 2, "explanation": "p53是最重要的抑癌基因之一，被称为「基因组的守护者」，在DNA损伤应答和细胞凋亡中发挥关键作用。"},
    {"type": "multi", "points": 4,
     "question": "下列哪些是癌细胞的特征？",
     "options": ["无限增殖", "接触抑制", "锚定依赖性", "侵袭和转移", "基因组不稳定性"],
     "answer": [0, 3, 4], "explanation": "癌细胞丧失接触抑制和锚定依赖性，而不是获得它们。癌细胞具有无限增殖、侵袭转移和基因组不稳定性等特征。"},
    {"type": "tf", "points": 2,
     "question": "原癌基因的突变是隐性突变，需要两个等位基因都突变才会致癌。",
     "options": [], "answer": 1,
     "explanation": "错误。原癌基因突变是显性突变（功能获得），一个等位基因突变即可。抑癌基因的突变才是隐性突变，需要两个等位基因都失活（Knudson二次打击假说）。"},
    {"type": "short", "points": 8,
     "question": "细胞周期存在哪些检验点？说明细胞周期的调控机制。",
     "answer": -1,
     "explanation": "<strong>检验点</strong>：(1)G₁/S检验点（限制点）——检查DNA损伤、营养条件、生长因子；(2)G₂/M检验点——检查DNA复制是否完成、是否有损伤；(3)M期纺锤体检验点——检查染色体是否正常连接到纺锤体。<br><strong>调控机制</strong>：Cyclin周期性合成与降解，结合并激活CDK；CDK磷酸化多种底物驱动周期进程；检验点蛋白（如p53、Rb）在异常时阻止周期进程。"},
    {"type": "essay", "points": 12,
     "question": "论述癌症的发生与原癌基因和抑癌基因的关系。",
     "answer": -1,
     "explanation": "<strong>原癌基因</strong>：正常功能是促进细胞增殖。突变后（点突变、扩增、重排）成为癌基因，功能获得（gain-of-function），一个等位基因突变即可。如Ras突变导致持续激活的信号通路。<br><strong>抑癌基因</strong>：正常功能是抑制增殖或促进凋亡。突变导致功能丧失（loss-of-function），需两个等位基因都失活。如p53缺失使DNA损伤细胞继续增殖；Rb缺失使细胞不受限制地通过G₁/S。<br><strong>多步骤致癌</strong>：癌症发生通常需要多个癌基因的激活和抑癌基因的失活共同作用。"}
]

# ============================================================
# Chapter 13: 细胞分化与干细胞
# ============================================================

CH13_KNOWLEDGE = r"""
<h2>十三、细胞分化与干细胞</h2>

<h3>13.1 细胞分化 <span class="tag-must">必考</span></h3>
<p><span class="kp">细胞分化（Cell Differentiation）</span><span class="exp">——在个体发育过程中，由一种相同的细胞类型经细胞分裂后逐渐在形态、结构和功能上形成稳定性差异，产生不同细胞类型的过程。</span></p>
<p><strong>特点</strong>：</p>
<ul>
  <li><span class="kp">稳定性</span><span class="exp">——分化状态通常是稳定的</span></li>
  <li><span class="kp">全能性 --&gt; 多能性 --&gt; 单能性</span><span class="exp">——分化潜能逐渐缩小</span></li>
  <li><span class="kp">基因选择性表达</span><span class="exp">——不同细胞表达不同的基因，不是基因丢失</span></li>
</ul>

<h3>13.2 细胞全能性与多能性 <span class="tag-must">必考</span></h3>
<table>
  <tr><th>概念</th><th>定义</th><th>举例</th></tr>
  <tr><td><span class="kp">细胞全能性（Totipotency）</span></td><td>能发育成完整个体的能力</td><td>受精卵、早期卵裂球</td></tr>
  <tr><td><span class="kp">多能性（Pluripotency）</span></td><td>能分化成三个胚层的所有细胞类型</td><td>胚胎干细胞</td></tr>
  <tr><td><span class="kp">多潜能性（Multipotency）</span></td><td>能分化成特定谱系的多种细胞</td><td>造血干细胞</td></tr>
  <tr><td><span class="kp">单能性（Unipotency）</span></td><td>只能分化成一种细胞</td><td>表皮干细胞</td></tr>
</table>

<h3>13.3 影响细胞分化的因素 <span class="tag-key">重点</span></h3>
<ul>
  <li><span class="kp">胞内因素</span><span class="exp">——细胞质的不均一性（母体效应基因产物）、细胞的不对称分裂</span></li>
  <li><span class="kp">胞外因素</span><span class="exp">——细胞间相互作用（诱导、抑制）、激素、生长因子、细胞外基质</span></li>
</ul>
<p><span class="kp">胚胎诱导</span><span class="exp">——一种组织通过信号分子诱导邻近组织分化的现象。</span></p>

<h3>13.4 干细胞 <span class="tag-must">必考</span></h3>
<p><span class="kp">干细胞（Stem Cell）</span><span class="exp">——具有自我更新能力和分化潜能的未分化细胞。</span></p>
<p><strong>分类</strong>：</p>
<table>
  <tr><th>类型</th><th>来源</th><th>分化潜能</th></tr>
  <tr><td><span class="kp">胚胎干细胞（ESC）</span></td><td>囊胚内细胞团</td><td>多能性（可分化成所有体细胞类型）</td></tr>
  <tr><td><span class="kp">成体干细胞</span></td><td>成体组织</td><td>多潜能性/单能性</td></tr>
  <tr><td><span class="kp">诱导多能干细胞（iPSC）</span></td><td>体细胞重编程</td><td>多能性（类似ESC）</td></tr>
</table>

<h3>13.5 基因表达调控 <span class="tag-key">重点</span></h3>
<p>细胞分化的本质是<strong>基因的选择性表达</strong>：</p>
<ul>
  <li><span class="kp">管家基因（Housekeeping Gene）</span><span class="exp">——所有细胞都表达的基因，维持基本生命活动（如组蛋白基因、核糖体蛋白基因）</span></li>
  <li><span class="kp">组织特异性基因（奢侈基因）</span><span class="exp">——只在特定细胞类型中表达的基因（如血红蛋白基因只在红细胞表达）</span></li>
</ul>
<p><span class="kp">细胞决定（Cell Determination）</span><span class="exp">——细胞在分化之前就已经被"决定"了分化方向，早于形态上的分化。</span></p>
<blockquote>易错：细胞分化是基因选择性表达的结果，不是基因丢失或不可逆改变。克隆羊多莉的实验证明分化细胞的核仍具有全能性。</blockquote>
"""

CH13_TEST = [
    {"type": "choice", "points": 3,
     "question": "下列关于细胞全能性的描述，正确的是：",
     "options": ["受精卵具有全能性", "胚胎干细胞具有全能性", "成体干细胞具有全能性", "所有体细胞都具有全能性"],
     "answer": 0, "explanation": "受精卵（和早期卵裂球）具有全能性，能发育成完整个体。胚胎干细胞是多能性，成体干细胞是多潜能性/单能性。"},
    {"type": "choice", "points": 3,
     "question": "管家基因的特点是：",
     "options": ["只在特定细胞表达", "在所有细胞都表达", "只在胚胎期表达", "突变后会导致癌症"],
     "answer": 1, "explanation": "管家基因在所有细胞中都表达，维持细胞基本生命活动，如组蛋白基因、核糖体蛋白基因等。"},
    {"type": "tf", "points": 2,
     "question": "细胞分化过程中，细胞会丢失不需要的基因。",
     "options": [], "answer": 1,
     "explanation": "错误。细胞分化是基因选择性表达的结果，不是基因丢失。克隆羊多莉的实验证明分化细胞的细胞核仍具有完整的遗传信息，具有全能性。"},
    {"type": "short", "points": 8,
     "question": "简述受精卵、胚胎干细胞、多能干细胞和单能干细胞的关系。",
     "answer": -1,
     "explanation": "<strong>受精卵</strong>：具有全能性，能发育成完整个体。<br><strong>胚胎干细胞</strong>：来自囊胚内细胞团，具有多能性，能分化成三个胚层的所有细胞类型。<br><strong>多能干细胞</strong>（多潜能干细胞）：能分化成特定谱系的多种细胞，如造血干细胞。<br><strong>单能干细胞</strong>：只能分化成一种细胞类型。<br><strong>关系</strong>：分化潜能逐渐缩小——受精卵（全能）--&gt; ESC（多能）--&gt; 成体干细胞（多潜能/单能）。"},
    {"type": "short", "points": 8,
     "question": "简述影响细胞分化的胞内外因素。",
     "answer": -1,
     "explanation": "<strong>胞内因素</strong>：(1)细胞质的不均一性——母体效应基因产物在卵细胞质中的不对称分布；(2)细胞的不对称分裂——产生两个具有不同胞质成分的子细胞。<br><strong>胞外因素</strong>：(1)细胞间相互作用——胚胎诱导；(2)激素和生长因子；(3)细胞外基质；(4)细胞位置信息。"},
    {"type": "essay", "points": 12,
     "question": "论述干细胞的概念、分类及其在医学中的应用前景。",
     "answer": -1,
     "explanation": "<strong>概念</strong>：干细胞是具有自我更新能力和分化潜能的未分化细胞。<br><strong>分类</strong>：(1)胚胎干细胞（ESC）——多能性；(2)成体干细胞——多潜能性/单能性；(3)诱导多能干细胞（iPSC）——由体细胞重编程获得。<br><strong>应用</strong>：再生医学（组织修复和器官再生）、疾病模型、药物筛选、细胞治疗（如造血干细胞移植治疗白血病）。"}
]

# ============================================================
# Chapter 14: 细胞衰老与凋亡
# ============================================================

CH14_KNOWLEDGE = r"""
<h2>十四、细胞衰老与凋亡</h2>

<h3>14.1 细胞衰老 <span class="tag-must">必考</span></h3>
<p><span class="kp">细胞衰老（Cell Senescence）</span><span class="exp">——细胞增殖能力逐渐下降并最终停止的过程。</span></p>
<p><span class="kp">Hayflick界限</span><span class="exp">——正常人体细胞在体外培养时，分裂次数是有限的（约50-60代），之后细胞停止分裂进入衰老状态。这是细胞衰老的经典实验证据。</span></p>
<p><strong>细胞衰老的特征</strong>：</p>
<ul>
  <li>细胞体积增大、形态变扁平</li>
  <li>细胞周期停滞（G₁期）</li>
  <li>端粒缩短</li>
  <li>$\beta$-半乳糖苷酶活性升高（衰老标志物）</li>
  <li>p53和p21表达升高</li>
</ul>

<h3>14.2 细胞衰老的原因与假说 <span class="tag-key">重点</span></h3>
<ul>
  <li><span class="kp">端粒缩短假说</span><span class="exp">——端粒随每次分裂缩短，缩短到临界长度时触发衰老</span></li>
  <li><span class="kp">氧化损伤假说</span><span class="exp">——活性氧（ROS）积累导致DNA、蛋白质和脂质的损伤</span></li>
  <li><span class="kp">基因调控假说</span><span class="exp">——衰老是遗传程序的一部分</span></li>
</ul>

<h3>14.3 细胞凋亡 <span class="tag-must">必考</span></h3>
<p><span class="kp">细胞凋亡（Apoptosis）</span><span class="exp">——由基因调控的程序性细胞死亡，是主动的、有序的细胞自我消亡过程。</span></p>

<h4>凋亡与坏死的区别</h4>
<table>
  <tr><th>特征</th><th>凋亡</th><th>坏死</th></tr>
  <tr><td>性质</td><td>生理性、主动</td><td>病理性、被动</td></tr>
  <tr><td>细胞形态</td><td>细胞皱缩、染色质凝集</td><td>细胞肿胀、破裂</td></tr>
  <tr><td>细胞膜</td><td>保持完整（形成凋亡小体）</td><td>破裂</td></tr>
  <tr><td>DNA</td><td>有规律断裂（梯状条带）</td><td>随机降解</td></tr>
  <tr><td>炎症反应</td><td>无</td><td>有</td></tr>
  <tr><td>涉及酶</td><td>Caspase家族</td><td>无特异性酶</td></tr>
</table>

<h3>14.4 细胞凋亡的分子机制 <span class="tag-must">必考</span></h3>
<p><strong>Caspase级联反应</strong>：</p>
<ul>
  <li><span class="kp">起始Caspase</span><span class="exp">——Caspase-8, Caspase-9（被凋亡信号激活）</span></li>
  <li><span class="kp">执行Caspase</span><span class="exp">——Caspase-3, Caspase-6, Caspase-7（执行凋亡程序）</span></li>
</ul>

<p><strong>两条主要凋亡通路</strong>：</p>
<ol>
  <li><span class="kp">外源通路（死亡受体通路）</span><span class="exp">——死亡配体（如FasL）与死亡受体（如Fas）结合，激活Caspase-8</span></li>
  <li><span class="kp">内源通路（线粒体通路）</span><span class="exp">——线粒体释放细胞色素c，与Apaf-1和Caspase-9形成凋亡体，激活Caspase-9</span></li>
</ol>
<p><span class="kp">Bcl-2家族</span><span class="exp">——调控凋亡的关键蛋白家族，包括抗凋亡蛋白（Bcl-2、Bcl-XL）和促凋亡蛋白（Bax、Bak）。</span></p>
<p><span class="kp">凋亡小体（Apoptotic Body）</span><span class="exp">——凋亡细胞形成的膜包裹碎片，被吞噬细胞清除，不引起炎症反应。</span></p>
<blockquote>易错：凋亡是主动过程需要能量（ATP），坏死是被动过程。凋亡不引起炎症反应，坏死引起炎症反应。这是两者的重要区别。</blockquote>
"""

CH14_TEST = [
    {"type": "choice", "points": 3,
     "question": "Hayflick界限指的是：",
     "options": ["细胞体外培养的最大分裂次数", "细胞凋亡的临界点", "端粒酶活性的阈值", "细胞分化的不可逆点"],
     "answer": 0, "explanation": "Hayflick界限是指正常人体细胞在体外培养时分裂次数有限（约50-60代），之后停止分裂。"},
    {"type": "choice", "points": 3,
     "question": "下列哪项不是细胞凋亡的特征？",
     "options": ["细胞皱缩", "染色质凝集", "细胞膜破裂", "形成凋亡小体"],
     "answer": 2, "explanation": "细胞膜破裂是坏死的特征。凋亡过程中细胞膜保持完整，最终形成凋亡小体被吞噬。"},
    {"type": "multi", "points": 4,
     "question": "凋亡与坏死的区别包括：",
     "options": ["凋亡是主动的，坏死是被动的", "凋亡引起炎症，坏死不引起", "凋亡DNA有规律断裂，坏死DNA随机降解", "凋亡涉及Caspase，坏死不涉及"],
     "answer": [0, 2, 3], "explanation": "凋亡不引起炎症反应，坏死引起炎症反应。其他三项都是正确的区别。"},
    {"type": "tf", "points": 2,
     "question": "细胞凋亡是主动过程，需要消耗ATP。",
     "options": [], "answer": 0,
     "explanation": "正确。凋亡是程序性细胞死亡，需要能量（ATP）来完成Caspase级联反应等有序过程。"},
    {"type": "short", "points": 8,
     "question": "简述细胞凋亡的概念、形态特征及其与细胞坏死的区别。",
     "answer": -1,
     "explanation": "<strong>概念</strong>：细胞凋亡是由基因调控的程序性细胞死亡，是主动有序的自我消亡过程。<br><strong>形态特征</strong>：细胞皱缩、染色质凝集、细胞膜保持完整、形成凋亡小体。<br><strong>与坏死区别</strong>：(1)凋亡是主动的、生理性的，坏死是被动的、病理性的；(2)凋亡细胞膜完整，坏死细胞膜破裂；(3)凋亡DNA有规律断裂（梯状），坏死DNA随机降解；(4)凋亡不引起炎症，坏死引起炎症。"},
    {"type": "short", "points": 8,
     "question": "简述细胞凋亡的两条主要通路。",
     "answer": -1,
     "explanation": "<strong>外源通路（死亡受体通路）</strong>：死亡配体（FasL等）与死亡受体（Fas等）结合 --&gt; 形成DISC复合物 --&gt; 激活Caspase-8 --&gt; 激活执行Caspase。<br><strong>内源通路（线粒体通路）</strong>：凋亡刺激 --&gt; 线粒体释放细胞色素c --&gt; 与Apaf-1和Caspase-9形成凋亡体 --&gt; 激活Caspase-9 --&gt; 激活执行Caspase。两条通路最终都激活Caspase-3执行凋亡。"}
]

# ============================================================
# Chapter 15: 细胞连接与细胞黏着
# ============================================================

CH15_KNOWLEDGE = r"""
<h2>十五、细胞连接与细胞黏着</h2>

<h3>15.1 细胞连接 <span class="tag-must">必考</span></h3>
<p><span class="kp">细胞连接（Cell Junction）</span><span class="exp">——多细胞生物中，相邻细胞之间或细胞与细胞外基质之间的特化连接结构。</span></p>

<h4>封闭连接（Occluding Junction）</h4>
<p><span class="kp">紧密连接（Tight Junction）</span><span class="exp">——相邻细胞质膜紧密相贴，完全封闭细胞间隙，阻止物质从细胞间隙通过。</span></p>
<ul>
  <li>主要蛋白：Claudin、Occludin</li>
  <li>功能：维持上皮细胞的极性、屏障功能</li>
</ul>

<h4>锚定连接（Anchoring Junction）</h4>
<table>
  <tr><th>类型</th><th>连接对象</th><th>胞内锚定</th><th>跨膜蛋白</th></tr>
  <tr><td><span class="kp">黏着带（Adherens Junction）</span></td><td>细胞-细胞</td><td>微丝</td><td>钙黏蛋白（Cadherin）</td></tr>
  <tr><td><span class="kp">桥粒（Desmosome）</span></td><td>细胞-细胞</td><td>中间纤维</td><td>桥粒芯蛋白等</td></tr>
  <tr><td><span class="kp">黏着斑（Focal Adhesion）</span></td><td>细胞-ECM</td><td>微丝</td><td>整联蛋白（Integrin）</td></tr>
  <tr><td><span class="kp">半桥粒（Hemidesmosome）</span></td><td>细胞-ECM</td><td>中间纤维</td><td>整联蛋白</td></tr>
</table>

<h4>通讯连接（Communicating Junction）</h4>
<p><span class="kp">间隙连接（Gap Junction）</span><span class="exp">——由连接子（Connexon）组成的细胞间通道，允许小分子（&lt;1kD）和离子直接通过。</span></p>
<p><span class="kp">胞间连丝（Plasmodesmata）</span><span class="exp">——植物细胞特有的通讯连接，相邻细胞通过细胞壁上的孔道连通。</span></p>
<p><span class="kp">化学突触（Chemical Synapse）</span><span class="exp">——神经元之间通过神经递质传递信号的连接结构。</span></p>

<h3>15.2 细胞黏着分子 <span class="tag-key">重点</span></h3>
<table>
  <tr><th>家族</th><th>Ca²⁺依赖性</th><th>主要功能</th></tr>
  <tr><td><span class="kp">钙黏蛋白（Cadherin）</span></td><td>依赖</td><td>同嗜性黏着（同类细胞黏着）</td></tr>
  <tr><td><span class="kp">选择素（Selectin）</span></td><td>依赖</td><td>异嗜性黏着（白细胞与内皮细胞）</td></tr>
  <tr><td><span class="kp">整联蛋白（Integrin）</span></td><td>依赖</td><td>细胞与ECM黏着</td></tr>
  <tr><td><span class="kp">免疫球蛋白超家族</span></td><td>不依赖</td><td>多种细胞识别</td></tr>
</table>

<h3>15.3 细胞外基质（ECM）<span class="tag-freq">高频</span></h3>
<p><strong>主要成分</strong>：</p>
<ul>
  <li><span class="kp">胶原（Collagen）</span><span class="exp">——动物体内最丰富的蛋白质，提供抗拉强度</span></li>
  <li><span class="kp">弹性蛋白（Elastin）</span><span class="exp">——提供弹性</span></li>
  <li><span class="kp">蛋白聚糖（Proteoglycan）</span><span class="exp">——形成水合凝胶，抵抗压缩</span></li>
  <li><span class="kp">纤连蛋白（Fibronectin）</span><span class="exp">——连接细胞与ECM</span></li>
  <li><span class="kp">层粘连蛋白（Laminin）</span><span class="exp">——基底膜的主要成分</span></li>
</ul>
<blockquote>易错：胶原是动物体内最丰富的蛋白质，占人体总蛋白的25%以上。考试中常考「最丰富」这个概念。</blockquote>
"""

CH15_TEST = [
    {"type": "choice", "points": 3,
     "question": "紧密连接的主要功能是：",
     "options": ["细胞间通讯", "封闭细胞间隙形成屏障", "锚定细胞骨架", "连接细胞与ECM"],
     "answer": 1, "explanation": "紧密连接（tight junction）完全封闭细胞间隙，阻止物质通过，维持上皮细胞极性和屏障功能。"},
    {"type": "choice", "points": 3,
     "question": "桥粒在胞内与哪种细胞骨架相连？",
     "options": ["微丝", "微管", "中间纤维", "微管和微丝"],
     "answer": 2, "explanation": "桥粒在胞内与中间纤维（如角蛋白纤维）相连，提供强大的机械连接。黏着带/黏着斑与微丝相连。"},
    {"type": "multi", "points": 4,
     "question": "下列哪些属于通讯连接？",
     "options": ["间隙连接", "紧密连接", "胞间连丝", "化学突触", "桥粒"],
     "answer": [0, 2, 3], "explanation": "间隙连接、胞间连丝和化学突触都是通讯连接。紧密连接属于封闭连接，桥粒属于锚定连接。"},
    {"type": "tf", "points": 2,
     "question": "整联蛋白是钙黏蛋白家族的一员。",
     "options": [], "answer": 1,
     "explanation": "错误。整联蛋白和钙黏蛋白是两个不同的细胞黏着分子家族。整联蛋白主要介导细胞与ECM的黏着，钙黏蛋白主要介导细胞与细胞的同嗜性黏着。"},
    {"type": "short", "points": 8,
     "question": "简述细胞连接的分类及其主要功能。",
     "answer": -1,
     "explanation": "<strong>封闭连接</strong>：紧密连接，封闭细胞间隙，维持上皮屏障功能和细胞极性。<br><strong>锚定连接</strong>：黏着带（细胞-细胞，连微丝）、桥粒（细胞-细胞，连中间纤维）、黏着斑（细胞-ECM，连微丝）、半桥粒（细胞-ECM，连中间纤维）。<br><strong>通讯连接</strong>：间隙连接（动物）、胞间连丝（植物）、化学突触（神经元），介导细胞间物质交换和信号传递。"},
    {"type": "short", "points": 8,
     "question": "简述胶原的结构特点和生物学功能。",
     "answer": -1,
     "explanation": "<strong>结构特点</strong>：由三条α链组成三股螺旋，富含甘氨酸（Gly-X-Y重复序列）、脯氨酸和羟脯氨酸。合成过程需要维生素C参与脯氨酸羟化。<br><strong>功能</strong>：(1)提供抗拉强度，是动物体内最丰富的蛋白质；(2)构成ECM的主要骨架；(3)与整联蛋白等结合，参与细胞信号转导；(4)在组织修复和发育中发挥重要作用。"}
]

# ============================================================
# Generate all files
# ============================================================

chapters = [
    ("11-细胞周期与细胞分裂", "第十一章 细胞周期与细胞分裂", CH11_KNOWLEDGE, CH11_TEST),
    ("12-细胞周期调控与癌症", "第十二章 细胞周期调控与癌症", CH12_KNOWLEDGE, CH12_TEST),
    ("13-细胞分化与干细胞", "第十三章 细胞分化与干细胞", CH13_KNOWLEDGE, CH13_TEST),
    ("14-细胞衰老与凋亡", "第十四章 细胞衰老与凋亡", CH14_KNOWLEDGE, CH14_TEST),
    ("15-细胞连接与细胞黏着", "第十五章 细胞连接与细胞黏着", CH15_KNOWLEDGE, CH15_TEST),
]

for folder, title, knowledge, test in chapters:
    dir_path = os.path.join(BASE, folder)
    os.makedirs(dir_path, exist_ok=True)
    
    knowledge_path = os.path.join(dir_path, "知识清单.html")
    save_knowledge_html(knowledge, knowledge_path, title)
    print(f"Generated: {knowledge_path}")
    
    test_path = os.path.join(dir_path, "章节测试.html")
    save_test(test, test_path, title, duration_minutes=45)
    print(f"Generated: {test_path}")

print("\nDone! Chapters 11-15 generated.")