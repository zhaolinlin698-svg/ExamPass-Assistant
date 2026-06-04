#!/usr/bin/env python3
"""Generate Part 1 (结构生物化学, Ch1-18) knowledge guide in deep-learning mode."""

import sys
sys.path.insert(0, '/workspace/ExamPass-Assistant')
from scripts.template_engine import save_knowledge_html

body = r"""

<h2>第一篇导论：结构生物化学 —— 生命的分子逻辑</h2>

<p><span class="kp">结构生物化学的核心命题</span><span class="exp">是：生命大分子（蛋白质、核酸、糖类、脂质）的化学结构如何决定其生物学功能？为什么这些特定的分子被进化选中来执行生命活动？本篇从最简单的氨基酸出发，一路构建到复杂蛋白质机器、核酸信息载体、酶的催化奇迹，建立「结构--性质--功能」三位一体的思维框架。</span></p>

<h2>第1章 绪论：什么是生物化学</h2>

<h3>1.1 生物化学的定义与范畴 <span class="tag-info">了解</span></h3>

<p><span class="kp">生物化学</span><span class="exp">是研究生命体内化学组成、化学反应及其与生命活动关系的科学。它是化学和生物学的桥梁——用化学的语言（分子结构、化学反应、能量变化）来解释生物学的现象（遗传、代谢、信号转导）。</span></p>

<p><strong>直觉类比</strong>：如果把细胞比作一座工厂，生物化学要回答三个层次的问题：(1) 工厂用了什么原料和零件？（结构生物化学）(2) 生产线怎么运转？能量从哪来？（代谢生物化学）(3) 产品说明书存在哪？怎么被读取执行的？（分子生物学）</p>

<h3>1.2 生物化学的三个分支 <span class="tag-key">重点</span></h3>

<table>
<tr><th>分支</th><th>核心问题</th><th>关键词</th></tr>
<tr><td><span class="kp">结构生物化学</span></td><td>生物分子的化学结构是怎样的？</td><td>蛋白质构象、DNA双螺旋、酶活性中心</td></tr>
<tr><td><span class="kp">代谢生物化学</span></td><td>营养物质如何转化释放能量？</td><td>糖酵解、三羧酸循环、氧化磷酸化</td></tr>
<tr><td><span class="kp">分子生物学</span></td><td>遗传信息如何储存、传递和表达？</td><td>DNA复制、转录、翻译、基因调控</td></tr>
</table>

<blockquote>易错：杨荣武第四版将全书分为这三大篇，与第三版的八篇结构不同。考研命题基于第四版目录结构，务必对照新版本复习。</blockquote>

<h3>1.3 生命的化学基础 <span class="tag-freq">高频</span></h3>

<p><span class="kp">生物体的化学组成</span><span class="exp">：C、H、O、N四种元素占生物体干重的96%以上。碳的特殊性在于其四价、成键角度109.5°，能够形成稳定的单键、双键和三键，构建出无限的分子多样性。</span></p>

<p><strong>为什么是碳而不是硅？</strong>硅虽然也是四价，但Si-Si键不稳定，Si-O键却极稳定（石英），所以硅基生命在热力学上倾向于形成岩石而非灵活的大分子。而C-C键和C-O键能相近，允许碳骨架在保持稳定的同时被氧化分解——这恰好满足代谢的需求。</p>

<p><span class="kp">生物大分子的共同逻辑</span><span class="exp">：(1) 由少数几种单体缩聚而成（氨基酸→蛋白质、核苷酸→核酸、单糖→多糖）；(2) 脱水缩合，水解断裂；(3) 序列决定构象，构象决定功能。</span></p>

<blockquote>易错：「脱水缩合」和「水解」是可逆的一对反应方向，前者需要能量（ATP驱动），后者释放能量。考试常考脱水缩合形成的是什么键——肽键（蛋白质）、磷酸二酯键（核酸）、糖苷键（多糖）。</blockquote>

<h2>第2章 氨基酸：蛋白质的字母表</h2>

<h3>2.1 氨基酸的通式与手性 <span class="tag-must">必考</span></h3>

<p><strong>核心问题</strong>：20种标准氨基酸共享同一个基本骨架，但它们侧链的微小差异决定了蛋白质功能的巨大差异。</p>

<p><span class="kp">氨基酸通式</span>：$$\mathrm{H_2N-CHR-COOH}$$<span class="exp">，中心Cα连接着一个氨基(-NH₂)、一个羧基(-COOH)、一个H原子和一个可变的侧链R基。除甘氨酸（R=H）外，所有标准氨基酸的Cα都是手性碳，且天然蛋白质中几乎全是L型。</span></p>

<p><strong>为什么是L型？</strong>这不是化学上的必然，而是进化的偶然——最早的生命随机选择了L-氨基酸。一旦选定，后续所有酶的特异性口袋都只识别L构型，形成了路径依赖。在实验室化学合成中，L和D各一半（消旋体），但生命选择了手性纯。</p>

<p><span class="kp">手性判断规则</span><span class="exp">：以甘油醛为参照，L型氨基酸的氨基在Fischer投影式中位于左侧。注意：L/D标注的是构型，不是旋光方向（+/-）。L型氨基酸可以是右旋(+)也可以是左旋(-)，两者没有必然对应关系。</span></p>

<blockquote>易错：(1) 甘氨酸没有手性碳，因为R=H导致Cα上两个相同基团；(2) L/D是构型（相对甘油醛），(+)/(-)是旋光性（实验测定），绝不能混用；(3) 苏氨酸和异亮氨酸有两个手性碳，但天然形式均为L-构型（Cα为L）。</blockquote>

<h3>2.2 氨基酸的分类（按侧链R基）<span class="tag-must">必考</span></h3>

<p><strong>为什么要分类？</strong>R基的化学性质——疏水性、极性、电荷、大小——决定了氨基酸在蛋白质折叠中的去向（内部/表面）、在酶催化中的作用（亲核/酸碱/金属配位）、以及在蛋白质-蛋白质相互作用中的识别。</p>

<table>
<tr><th>类别</th><th>R基特征</th><th>成员（单字母缩写）</th><th>在蛋白质中的典型角色</th></tr>
<tr><td><span class="kp">疏水（非极性）</span></td><td>烷基链、芳环，不溶于水</td><td>G, A, V, L, I, P, F, W, M</td><td>蛋白质内部疏水核心、膜蛋白跨膜区</td></tr>
<tr><td><span class="kp">极性不带电</span></td><td>含-OH、-SH、酰胺基</td><td>S, T, C, Y, N, Q</td><td>酶活性中心亲核试剂、磷酸化位点（S/T/Y）</td></tr>
<tr><td><span class="kp">酸性（带负电）</span></td><td>侧链含羧基，pH 7解离为-COO⁻</td><td>D (Asp), E (Glu)</td><td>金属离子配位（Ca²⁺、Mg²⁺）、酸碱催化</td></tr>
<tr><td><span class="kp">碱性（带正电）</span></td><td>侧链含氨基/胍基/咪唑基，pH 7质子化</td><td>K (Lys), R (Arg), H (His)</td><td>结合带负电的DNA/底物、His酸碱催化（pKa≈6）</td></tr>
</table>

<p><strong>深度理解——每个氨基酸的独特性</strong>：</p>
<ul>
<li><span class="kp">甘氨酸 (Gly, G)</span><span class="exp">——唯一无手性的氨基酸，R=H使其构象自由度最大。在蛋白质中出现在紧密转角处（需要极小侧链的位置），也是胶原蛋白中每第三个残基（Gly-X-Y重复）。</span></li>
<li><span class="kp">脯氨酸 (Pro, P)</span><span class="exp">——唯一的亚氨基酸，侧链与主链N形成五元环。这限制了Cα-N键的旋转（φ角固定在-60°左右），使Pro成为α螺旋的"破坏者"和β转角的常见组分。</span></li>
<li><span class="kp">半胱氨酸 (Cys, C)</span><span class="exp">——含巯基(-SH)，两个Cys的-SH可氧化形成二硫键(-S-S-)。二硫键是共价交联（不同于非共价的氢键/疏水力），能显著稳定蛋白质的三维结构，在分泌蛋白中尤其重要。</span></li>
<li><span class="kp">组氨酸 (His, H)</span><span class="exp">——侧链咪唑基pKa≈6.0，在生理pH附近既能作为质子供体又能作为受体。这是His成为酶催化中最重要的亲核/酸碱催化剂的原因——它进可攻退可守。</span></li>
</ul>

<blockquote>易错：(1) 考试常要求默写20种氨基酸的结构、三字母和单字母缩写；(2) Pro是亚氨基酸，其「氨基」实为亚氨基(-NH-)；(3) Cys的-SH在氧化环境下形成二硫键，还原环境下断裂——这是可逆的；(4) 酸性氨基酸是Asp和Glu，其酰胺形式Asn和Gln属于极性不带电类，这是两个不同的类别。</blockquote>

<h3>2.3 氨基酸的酸碱性质 <span class="tag-must">必考</span></h3>

<p><span class="kp">等电点（pI）</span><span class="exp">：氨基酸净电荷为零时的pH值。对于中性氨基酸（一个-NH₃⁺，一个-COO⁻），pI = (pK₁ + pK₂) / 2；对于酸性氨基酸（两个-COOH），pI = (pK₁ + pK_R) / 2；对于碱性氨基酸，pI = (pK_R + pK₂) / 2。</span></p>

<p><strong>直觉理解</strong>：等电点就是氨基酸的「盈亏平衡点」。(1) pH &lt; pI：溶液中H⁺多，-COO⁻被质子化，净电荷为正；(2) pH &gt; pI：溶液中H⁺少，-NH₃⁺脱质子化，净电荷为负；(3) pH = pI：正负电荷恰好相等，净电荷为零，溶解度最低。</p>

<p><span class="kp">滴定曲线</span><span class="exp">：氨基酸的滴定曲线是理解缓冲区和pKa的绝佳工具。中性氨基酸有两个缓冲平台（对应-COO⁻和-NH₃⁺的电离），酸性氨基酸三个平台（多一个侧链羧基），碱性氨基酸三个平台（多一个侧链氨基）。</span></p>

<blockquote>易错：等电点时氨基酸溶解度最小的原因是分子间没有静电排斥力，容易聚集沉淀——而不是因为「不带电」。事实上等电点时分子内部正负电荷互相抵消，但整体对外呈电中性。此原理也是等电聚焦电泳分离蛋白质的基础。</blockquote>

<h3>2.4 氨基酸的化学反应 <span class="tag-key">重点</span></h3>

<table>
<tr><th>反应</th><th>靶向基团</th><th>试剂</th><th>应用/意义</th></tr>
<tr><td>茚三酮反应</td><td>α-氨基</td><td>茚三酮</td><td>氨基酸定性/定量检测（蓝紫色），Pro产生黄色</td></tr>
<tr><td>Edman降解</td><td>α-氨基（N端）</td><td>PITC</td><td>蛋白质测序——从N端逐一切除氨基酸并鉴定</td></tr>
<tr><td>Sanger反应</td><td>α-氨基</td><td>DNFB (FDNB)</td><td>鉴定多肽N端氨基酸（历史上首次用于测序胰岛素）</td></tr>
<tr><td>Ellman反应</td><td>-SH（Cys）</td><td>DTNB</td><td>定量游离巯基（产生黄色TNB⁻，412nm检测）</td></tr>
</table>

<h2>第3章 蛋白质的结构：从序列到三维世界</h2>

<h3>3.1 肽键与多肽链 <span class="tag-must">必考</span></h3>

<p><strong>核心问题</strong>：氨基酸如何连接成蛋白质？这个连接方式有什么几何限制？</p>

<p><span class="kp">肽键</span><span class="exp">是一个氨基酸的α-羧基与下一个氨基酸的α-氨基脱水缩合形成的酰胺键(-CO-NH-)。肽键具有约40%的双键性质——这是因为酰胺N上的孤对电子与羰基C=O共轭（共振结构），使C-N键具有部分双键特征。</span></p>

<p><strong>肽键的双键性质——深远的结构意义</strong>：(1) 肽键不能自由旋转，六个原子(Cα-CO-NH-Cα)位于同一平面上，形成肽平面；(2) 肽键可以是顺式或反式，但反式构象能量低（侧链不冲突），蛋白质中绝大部分肽键为反式；(3) Pro的肽键情况特殊，因为其五元环的结构，顺式(~10%)和反式(~90%)都可能出现。</p>

<p><span class="kp">多肽链的方向性</span><span class="exp">：N端→C端。写蛋白质序列时总是N端在左、C端在右。例如 Ala-Gly-Phe 表示Ala的N端游离、Phe的C端游离。</span></p>

<p><span class="kp">Ramachandran图</span><span class="exp">（拉氏图）：以φ角(N-Cα)为横轴、ψ角(Cα-C)为纵轴，绘制每个残基的二面角。大多数残基落在允许区域内（α螺旋区、β折叠区）。甘氨酸因其R=H而允许范围最广，脯氨酸因其环状结构而限制最严。</span></p>

<blockquote>易错：(1) 肽键≠普通的C-N单键，它因共振而有约40%双键特征；(2) 肽平面的旋转发生在Cα-N(φ)和Cα-C(ψ)两个单键上，而非肽键本身；(3) Ramachandran图的白色区域（不允许区）对应原子间空间碰撞，说明蛋白质折叠受立体化学严格约束。</blockquote>

<h3>3.2 蛋白质的层次结构 <span class="tag-must">必考</span></h3>

<table>
<tr><th>结构层次</th><th>定义</th><th>稳定力</th><th>例子</th></tr>
<tr><td><span class="kp">一级结构</span></td><td>氨基酸的线性序列（N→C）</td><td>共价键（肽键）</td><td>胰岛素A链21残基+B链30残基</td></tr>
<tr><td><span class="kp">二级结构</span></td><td>主链局部规则性折叠</td><td>主链间氢键（C=O···H-N）</td><td>α螺旋、β折叠、β转角</td></tr>
<tr><td><span class="kp">超二级结构</span></td><td>二级结构的组合单元</td><td>疏水力+氢键</td><td>βαβ单元、螺旋-转角-螺旋</td></tr>
<tr><td><span class="kp">结构域</span></td><td>独立折叠的功能/结构单元</td><td>疏水核心等</td><td>Ig结构域、SH2结构域</td></tr>
<tr><td><span class="kp">三级结构</span></td><td>整条多肽链的三维折叠</td><td>疏水力+氢键+离子键+二硫键</td><td>肌红蛋白的球状折叠</td></tr>
<tr><td><span class="kp">四级结构</span></td><td>多条多肽链的组装</td><td>亚基间非共价力</td><td>血红蛋白α₂β₂四聚体</td></tr>
</table>

<blockquote>易错：(1) 二硫键是稳定三级结构的共价键，但不参与二级结构（α螺旋、β折叠只靠主链氢键）；(2) 并非所有蛋白质都有四级结构——单亚基蛋白质（如肌红蛋白）只有三级；(3) 结构域和亚基是不同的概念：结构域是同一条链内的折叠单元，亚基是不同多肽链。</blockquote>

<h3>3.3 α螺旋 <span class="tag-must">必考</span></h3>

<p><span class="kp">α螺旋（α-helix）</span><span class="exp">是蛋白质中最常见的二级结构之一。主链绕一个假想的中轴右手螺旋上升，每圈3.6个氨基酸残基，螺距0.54nm（即每个残基上升0.15nm）。</span></p>

<p><strong>螺旋的稳定力——主链氢键</strong>：第i个残基的C=O与第i+4个残基的N-H形成氢键，方向几乎平行于螺旋轴。这种「i→i+4」的氢键模式使螺旋内部高度有规律。注意：氢键在螺旋内部，所有R基朝外。</p>

<p><strong>影响α螺旋稳定性的因素</strong>：</p>
<ul>
<li><span class="kp">Pro（破坏者）</span><span class="exp">——其N上无H可参与氢键，且五元环引入刚性的扭结，使主链无法维持螺旋几何。</span></li>
<li><span class="kp">Gly（不稳定）</span><span class="exp">——构象熵太大，在螺旋中的固定构象在热力学上不利。</span></li>
<li><span class="kp">连续的同电荷残基</span><span class="exp">——Lys-Lys-Lys或Glu-Glu-Glu在螺旋中每隔0.15nm出现一个电荷，强烈排斥。</span></li>
<li><span class="kp">空间位阻大的残基</span><span class="exp">——Ile、Val等大侧链如果连续出现，空间冲突。</span></li>
</ul>

<p><strong>为什么α螺旋是右手的？</strong>因为所有天然氨基酸是L型，L型氨基酸的侧链在右手螺旋中处于更有利的取向（朝外远离螺旋轴），左手螺旋中L侧链会与主链C=O冲突。这是进化的精妙——一级结构的L手性决定了高级结构的螺旋手性。</p>

<h3>3.4 β折叠 <span class="tag-must">必考</span></h3>

<p><span class="kp">β折叠（β-sheet）</span><span class="exp">：多条β链（β-strand，拉伸的锯齿形构象）通过链间主链氢键并列排列形成的片层结构。β链中相邻残基的R基交替朝上和朝下。</span></p>

<table>
<tr><th>特征</th><th>平行β折叠</th><th>反平行β折叠</th></tr>
<tr><td>链方向</td><td>同向（N→C一致）</td><td>反向（N→C交替）</td></tr>
<tr><td>氢键几何</td><td>弯曲，略弱</td><td>直线型，更强</td></tr>
<tr><td>Cα距离</td><td>0.65nm</td><td>0.70nm</td></tr>
<tr><td>重复距离</td><td>0.325nm/残基</td><td>0.35nm/残基（交替）</td></tr>
<tr><td>常见位置</td><td>蛋白质疏水核心内部</td><td>表面和内部均有</td></tr>
</table>

<p><span class="kp">β转角（β-turn）</span><span class="exp">：由4个残基组成的急转弯结构，连接相邻的两条反平行β链。第1和第4个残基的C=O与N-H间形成氢键（i→i+3）。Pro和Gly在β转角中出现频率最高——Pro因其刚性转角倾向，Gly因体积小适合紧密转角。</span></p>

<blockquote>易错：(1) α螺旋靠链内氢键（i→i+4），β折叠靠链间氢键——稳定力的来源和方向不同；(2) 丝心蛋白（fibroin）几乎全是β折叠，但α角蛋白（keratin）几乎全是α螺旋——环境决定了哪种二级结构占优势。</blockquote>

<h3>3.5 蛋白质折叠与三级结构 <span class="tag-key">重点</span></h3>

<p><strong>核心问题</strong>：一条无规的多肽链如何自发折叠成精确的三维结构？</p>

<p><span class="kp">Anfinsen实验</span><span class="exp">（诺贝尔奖级发现）：将RNase A用尿素（破坏氢键）和β-巯基乙醇（还原二硫键）完全变性展开后，去除变性剂，RNase A自发恢复全部酶活性。核心结论：蛋白质的一级结构包含了决定其三维结构所需的全部信息。</span></p>

<p><strong>热力学视角——疏水效应是折叠的主要驱动力</strong>：蛋白质折叠不是靠「形成」有利相互作用（氢键在折叠态和伸展态中都大量存在），而是靠「避免」不利效应——暴露疏水基团于水中会导致水的熵减（水分子在疏水表面形成有序的笼状结构）。因此，<span class="kp">疏水残基被埋入蛋白质内部</span>释放了这些有序水分子，是折叠的主要热力学驱动力。</p>

<p><span class="kp">Levinthal悖论</span><span class="exp">：一条100残基的多肽链，如果每个残基有3种可能构象，总共3¹⁰⁰≈10⁴⁷种可能构象。即使以飞秒级速度搜索，宇宙的年龄都不够用。但蛋白质在毫秒到秒级就完成了折叠——说明折叠不是随机搜索，而是沿着特定的「漏斗形」能垒路径进行的。</span></p>

<p><strong>折叠模型</strong>：</p>
<ul>
<li><span class="kp">框架模型</span><span class="exp">：二级结构先形成，再对接成三级结构。</span></li>
<li><span class="kp">疏水坍缩模型</span><span class="exp">：疏水残基先聚集成核心（类似油滴在水中），再在其中调整二级结构。</span></li>
<li><span class="kp">成核-凝聚模型</span><span class="exp">（当前主流）：少量关键残基先形成折叠核，其余部分围绕核快速凝聚折叠。</span></li>
</ul>

<h3>3.6 分子伴侣与错误折叠疾病 <span class="tag-key">重点</span></h3>

<p><span class="kp">分子伴侣（chaperone）</span><span class="exp">：帮助其他蛋白质正确折叠但不成为最终结构一部分的蛋白质。它们不是「告诉」蛋白质怎么折叠，而是防止错误折叠和聚集——给新生肽链或变性蛋白提供一个安全的折叠环境。</span></p>

<p><strong>关键分子伴侣</strong>：</p>
<ul>
<li><span class="kp">Hsp70系统</span><span class="exp">（DnaK/DnaJ/GrpE）：结合新生肽链的疏水区，防止过早折叠或聚集。ATP水解驱动构象变化、释放底物。</span></li>
<li><span class="kp">Chaperonin（GroEL/GroES）</span><span class="exp">：双七元环桶状结构，为蛋白质提供一个隔离的「折叠笼」。GroES盖子关闭后，桶内环境改变，蛋白质在其中独立折叠。</span></li>
</ul>

<p><span class="kp">错误折叠与疾病</span><span class="exp">：朊病毒（PrP^Sc）是PrP蛋白的异常构象，它可以「传染」正常PrP转变为致病构象。阿尔茨海默症中的Aβ聚集、帕金森症中的α-突触核蛋白聚集也都是蛋白错误折叠和淀粉样纤维化的结果。</span></p>

<h2>第4章 蛋白质的功能：结构与功能的完美联姻</h2>

<h3>4.1 氧结合蛋白：肌红蛋白与血红蛋白 <span class="tag-must">必考</span></h3>

<p><strong>核心问题</strong>：为什么需要专门蛋白质来运氧？O₂在水中的溶解度极低(~0.1mM)，无法满足组织呼吸需求。蛋白质通过将O₂结合在血红素的Fe²⁺上，大大提高了氧的携带能力。</p>

<p><span class="kp">肌红蛋白（Myoglobin, Mb）</span><span class="exp">：单亚基，含一个血红素辅基，位于肌肉组织中。其功能是储存O₂——在肌肉高强度活动时释放O₂给线粒体。Mb的氧合曲线是双曲线（hyperbolic），反映了简单的结合平衡：Mb + O₂ ⇌ MbO₂。</span></p>

<p><span class="kp">血红蛋白（Hemoglobin, Hb）</span><span class="exp">：α₂β₂四聚体（四个亚基，各含一个血红素），位于红细胞中。其功能是运输O₂——在肺部高pO₂处结合O₂，在组织低pO₂处释放O₂。Hb的氧合曲线是S形（sigmoidal），反映了协同效应。</span></p>

<p><strong>S形曲线的生物学意义</strong>：(1) Hb在肺部(pO₂≈100 torr)几乎100%饱和；(2) 在组织(pO₂≈30 torr)时饱和度大幅下降，释放出大量O₂；(3) 在运动肌肉(pO₂≈10 torr)时进一步释放。如果Hb的曲线也是双曲线，那它在组织中的释氧能力将大打折扣。</p>

<h3>4.2 协同效应与别构调控 <span class="tag-must">必考</span></h3>

<p><span class="kp">协同效应（cooperativity）</span><span class="exp">：一个亚基结合O₂后，使同一分子中其他亚基更容易（或更难）结合O₂。Hb表现为正协同效应——结合第一个O₂最困难，结合第四个O₂最容易。</span></p>

<p><strong>MWC模型（对称/协同模型）</strong>：</p>
<ul>
<li>Hb存在两种构象状态：<span class="kp">T态（tense，低亲和力）</span>和<span class="kp">R态（relaxed，高亲和力）</span></li>
<li>所有亚基必须同时处于T或R态（对称性约束）</li>
<li>无氧时平衡偏向T态；O₂结合后T/R平衡逐渐移向R态</li>
<li>这解释了S形曲线——低浓度时O₂主要遇见低亲和力的T态，结合弱；一旦浓度足够使一个亚基从T→R转变，其他亚基也跟着转换，结合力急剧上升</li>
</ul>

<p><strong>KNF模型（序列模型）</strong>：认为配体结合引发单个亚基构象变化，通过亚基界面传递给相邻亚基。两种模型都有实验证据支持，考试一般以MWC模型为主。</p>

<p><span class="kp">别构效应物（allosteric effectors）</span>：</p>
<ul>
<li><span class="kp">2,3-BPG</span><span class="exp">（2,3-二磷酸甘油酸）：结合在Hb中央空腔，稳定T态，降低O₂亲和力——促使O₂释放。这是高原适应的机制之一（高原缺氧→红细胞内2,3-BPG升高→Hb释氧增强→组织供氧不降低）。</span></li>
<li><span class="kp">Bohr效应</span><span class="exp">：H⁺和CO₂降低Hb与O₂的亲和力。在活跃代谢的组织中，CO₂↑→碳酸酐酶催化CO₂+H₂O→H₂CO₃→H⁺+HCO₃⁻，pH↓。H⁺与Hb结合稳定T态，促进O₂释放——恰好是组织需要O₂的时候。</span></li>
</ul>

<blockquote>易错：(1) 2,3-BPG只影响Hb，不影响Mb（Mb是单亚基，无别构位点）；(2) Bohr效应是「低pH降低O₂亲和力」而非「高pH提高亲和力」；(3) HbF（胎儿血红蛋白，α₂γ₂）对2,3-BPG亲和力低，因此对O₂亲和力比HbA高——因为γ链的His143Ser替代减少了一个正电荷，弱化了与2,3-BPG的静电结合，这使胎儿能从母体血中有效摄取O₂。</blockquote>

<h3>4.3 免疫球蛋白与分子识别 <span class="tag-key">重点</span></h3>

<p><span class="kp">抗体（免疫球蛋白，Ig）</span><span class="exp">由两条重链（H链）和两条轻链（L链）通过二硫键连接成Y形结构。每条链的N端为可变区（V区，负责抗原识别），C端为恒定区（C区，负责效应功能）。</span></p>

<p><strong>免疫多样性的产生机制</strong>（不是基因数量的无限膨胀）：</p>
<ul>
<li><span class="kp">V(D)J重组</span><span class="exp">——在B细胞发育中，多个V、D、J基因片段随机选取一个组合（类似从三个大桶中各抽一个球），组合数= V段数 × D段数 × J段数</span></li>
<li><span class="kp">连接多样性</span><span class="exp">——V、D、J连接点可以添加或删除少量核苷酸</span></li>
<li><span class="kp">体细胞高频突变</span><span class="exp">——在抗原刺激后，V区基因以极高频率发生点突变，由自然选择筛选出亲和力更高的突变体（亲和力成熟）</span></li>
</ul>

<p><strong>直觉类比</strong>：抗体多样性像乐高积木——不是给每个形状开模具，而是提供几种基础积木（V、D、J段），通过不同的排列组合产生海量变化。</p>

<h3>4.4 肌肉收缩的分子机制 <span class="tag-key">重点</span></h3>

<p><span class="kp">肌小节（sarcomere）</span><span class="exp">是肌肉收缩的最小单位。肌球蛋白（myosin，粗丝）的头部以ATP为动力在肌动蛋白（actin，细丝）上「行走」，使粗细丝相对滑动。</span></p>

<p><strong>肌球蛋白-肌动蛋白循环（四步）</strong>：</p>
<ol>
<li><span class="kp">ATP结合</span><span class="exp">：ATP与肌球蛋白头部结合，降低头部对肌动蛋白的亲和力，头部脱离肌动蛋白。</span></li>
<li><span class="kp">ATP水解</span><span class="exp">：ATP→ADP+Pi，肌球蛋白头部构象变化，「扳起」（cocking）到高能状态。</span></li>
<li><span class="kp">与肌动蛋白结合</span><span class="exp">：Pi释放，头部与肌动蛋白紧密结合。</span></li>
<li><span class="kp">力产生（power stroke）</span><span class="exp">：ADP释放，头部恢复低能构象，带动肌动蛋白丝滑动~10nm。</span></li>
</ol>

<p><strong>Ca²⁺的调控角色</strong>：肌肉放松时，原肌球蛋白(tropomyosin)挡住肌球蛋白在肌动蛋白上的结合位点。神经冲动→肌质网释放Ca²⁺→Ca²⁺与肌钙蛋白(troponin)结合→原肌球蛋白构象变化→暴露肌动蛋白结合位点→收缩启动。</p>

<p><strong>Deep principle</strong>：这是化学能（ATP→ADP+Pi）→机械能（肌丝滑动的力）的完美转化，且每次转化都通过精确的构象变化（而非宏观机器的齿轮啮合）来实现——蛋白质构象变化就是纳米尺度的机械工程。</p>

<h2>第5章 蛋白质的性质及研究方法</h2>

<h3>5.1 蛋白质的理化性质 <span class="tag-freq">高频</span></h3>

<p><span class="kp">两性解离与等电点</span><span class="exp">：蛋白质的净电荷随pH变化。等电点时净电荷为零，溶解度最低（无静电排斥→聚集沉淀）。不同蛋白pI不同（多数在pH 4~7），等电聚焦电泳利用此原理分离蛋白质。</span></p>

<p><span class="kp">胶体性质</span><span class="exp">：蛋白质分子大小在1~100nm（胶体范围），在水溶液中形成稳定的亲水胶体。稳定因素：(1) 表面水化层；(2) 表面电荷（非等电点时互相排斥）。破坏这些因素（加盐、调pH到pI、加有机溶剂）使蛋白质沉淀——盐析、等电点沉淀、有机溶剂沉淀的原理。</span></p>

<p><span class="kp">蛋白质变性</span><span class="exp">：空间构象被破坏但一级结构完好的过程。变性因素包括热、强酸强碱、尿素、SDS、有机溶剂、重金属等。变性后疏水核心暴露，溶解度下降，生物活性丧失。</span></p>

<blockquote>易错：(1) 变性≠沉淀，变性的蛋白质可能仍溶解（如可溶性变性蛋白），沉淀的蛋白质可能未变性（如盐析）；(2) 变性只是去折叠（unfolding），一级结构没断，不同于水解；(3) 有些变性是可逆的（复性），如RNase A实验。</blockquote>

<h3>5.2 蛋白质分离纯化技术 <span class="tag-must">必考</span></h3>

<table>
<tr><th>方法</th><th>分离原理</th><th>关键细节</th></tr>
<tr><td><span class="kp">盐析</span></td><td>不同蛋白在不同(NH₄)₂SO₄浓度下沉淀</td><td>硫酸铵最常用——高溶解度、高离子强度、对蛋白稳定</td></tr>
<tr><td><span class="kp">凝胶过滤/分子筛</span></td><td>按分子大小分离</td><td>大分子先出（走空隙），小分子后出（进凝胶孔）。注意：非按分子量——形状也影响</td></tr>
<tr><td><span class="kp">离子交换层析</span></td><td>按净电荷分离</td><td>阳离子交换（带负电树脂结合正电蛋白）、阴离子交换（带正电树脂结合负电蛋白），NaCl梯度洗脱</td></tr>
<tr><td><span class="kp">亲和层析</span></td><td>特异性配体-蛋白结合</td><td>分辨率最高，一步可达高纯度。His-tag+Ni-NTA是最常用的重组蛋白纯化</td></tr>
<tr><td><span class="kp">SDS-PAGE</span></td><td>按分子量分离</td><td>SDS结合蛋白→所有蛋白带均匀负电荷→迁移率仅取决于分子量</td></tr>
<tr><td><span class="kp">等电聚焦</span></td><td>按pI分离</td><td>pH梯度中蛋白迁移到pI位置停住</td></tr>
<tr><td><span class="kp">2D电泳</span></td><td>等电聚焦 + SDS-PAGE</td><td>先按pI，再按分子量，高分辨率</td></tr>
</table>

<p><strong>蛋白质测序——Edman降解法</strong>：PITC与N端氨基酸的α-NH₂反应→酸性条件下切下N端氨基酸→PTH-氨基酸→HPLC鉴定→下一个循环。优点：每次只切一个N端；局限：只能测~50残基，长链需要先断裂成短肽再分别测序。</p>

<blockquote>易错：(1) SDS-PAGE中，小分子迁移快、大分子慢，不要记反；(2) 凝胶过滤中大小分子顺序相反——大分子快（不进孔）、小分子慢（进孔多）；(3) 带His-tag的重组蛋白用Ni-NTA亲和层析纯化，原理是His的咪唑基与Ni²⁺配位。</blockquote>

<h2>第6章 核苷酸：核酸的建筑模块</h2>

<h3>6.1 核苷酸的结构组分 <span class="tag-must">必考</span></h3>

<p><span class="kp">核苷酸 = 碱基 + 戊糖 + 磷酸</span><span class="exp">。碱基和戊糖组成核苷（nucleoside），核苷加磷酸是核苷酸（nucleotide）。注意命名：腺嘌呤+核糖=腺苷(adenosine)，腺苷+磷酸=腺苷酸(AMP)。</span></p>

<table>
<tr><th>组分</th><th>DNA</th><th>RNA</th></tr>
<tr><td>戊糖</td><td>2'-脱氧核糖（2'-无-OH）</td><td>核糖（2'-有-OH）</td></tr>
<tr><td>嘌呤碱基</td><td>A（腺嘌呤）、G（鸟嘌呤）</td><td>A、G</td></tr>
<tr><td>嘧啶碱基</td><td>C（胞嘧啶）、T（胸腺嘧啶）</td><td>C、U（尿嘧啶，代替T）</td></tr>
</table>

<p><strong>为什么DNA用T而RNA用U？</strong>这是一个经典的进化解释题。胞嘧啶会自发脱氨基变为尿嘧啶（C→U，每天每个细胞发生约100次）。如果DNA也用U，就无法区分自然的U和由C脱氨错误产生的U。但DNA用T，当C脱氨产生U时，修复酶（尿嘧啶DNA糖苷酶UDG）可以识别U为异常碱基并移除。RNA是临时性分子，不需要长期保真，且在tRNA等中U的修饰衍生物功能多样，所以RNA保留U。</p>

<h3>6.2 核苷酸的功能——不仅仅是核酸原料 <span class="tag-key">重点</span></h3>

<ul>
<li><span class="kp">ATP</span><span class="exp">——细胞能量货币。两个高能磷酸酐键（~P），水解ΔG°\'≈ -30.5 kJ/mol。注意：「高能键」指水解时释放大量自由能，不是键本身能量格外高，而是产物比反应物稳定得多（共振稳定化+电荷分离解除+离子化+H⁺水合补偿）。</span></li>
<li><span class="kp">cAMP / cGMP</span><span class="exp">——第二信使。腺苷酸环化酶催化ATP→cAMP，cAMP激活PKA→信号放大。</span></li>
<li><span class="kp">NAD⁺ / FAD</span><span class="exp">——电子载体。NAD⁺接受一个H⁻（两个电子+一个质子）→NADH；FAD接受2H→FADH₂。</span></li>
<li><span class="kp">CoA（辅酶A）</span><span class="exp">——酰基载体。乙酰CoA是代谢的核心十字路口。</span></li>
</ul>

<h2>第7章 核酸的结构与功能</h2>

<h3>7.1 DNA双螺旋 <span class="tag-must">必考</span></h3>

<p><strong>Watson-Crick双螺旋（B-DNA）的核心参数</strong>：</p>
<ul>
<li>两条链反向平行（一条5'→3'，另一条3'→5'）</li>
<li>右手双螺旋，直径约2nm</li>
<li>螺距3.4nm，每圈10bp（碱基对间距0.34nm）</li>
<li>碱基对在螺旋内部（疏水），糖-磷酸骨架在外（亲水，带负电）</li>
<li>A-T配对（2个氢键），G-C配对（3个氢键）</li>
<li>大沟（major groove, 2.2nm宽）和小沟（minor groove, 1.2nm宽）交替出现</li>
</ul>

<p><strong>为什么最重要的是碱基互补配对？</strong>因为它同时解决了DNA的两个核心功能：(1) <span class="kp">储存遗传信息</span>——碱基序列即信息；(2) <span class="kp">忠实复制</span>——A-T、G-C的氢键配对模式保证了每条链都可以作为合成互补链的模板。Watson和Crick论文的最后一句名言：「我们注意到，我们所假设的特定配对方式直接暗示了一种可能的遗传物质复制机制。」</p>

<p><strong>大沟和小沟的功能意义</strong>：大多数DNA结合蛋白（转录因子、限制酶）通过识别大沟中的碱基对来结合特定序列——因为大沟提供了足够的空间和碱基特异性读出。同一碱基对在大沟和小沟中暴露出不同的氢键供体/受体模式，使蛋白质能区分A-T和T-A、G-C和C-G（形成序列特异性识别）。</p>

<h3>7.2 DNA的构象多样性 <span class="tag-key">重点</span></h3>

<table>
<tr><th>类型</th><th>A-DNA</th><th>B-DNA</th><th>Z-DNA</th></tr>
<tr><td>螺旋手性</td><td>右手</td><td>右手</td><td>左手</td></tr>
<tr><td>每圈碱基对</td><td>11</td><td>10</td><td>12</td></tr>
<tr><td>碱基对倾角</td><td>~20°（倾斜）</td><td>~0°（垂直）</td><td>~7°</td></tr>
<tr><td>存在条件</td><td>脱水、RNA双链区</td><td>正常生理条件</td><td>交替GC序列、高盐</td></tr>
<tr><td>大沟/小沟</td><td>深窄大沟+宽浅小沟</td><td>宽大沟+窄小沟</td><td>平坦大沟+深窄小沟</td></tr>
</table>

<p><strong>B↔Z转变的生物学意义</strong>：Z-DNA可能在基因表达调控中起作用（某些转录激活因子特异识别Z-DNA）。Z-DNA形成需要能量输入（B→Z自由能增加），细胞中Z-DNA的负超螺旋有利于Z-DNA形成。</p>

<h3>7.3 RNA结构与功能多样性 <span class="tag-must">必考</span></h3>

<p><strong>核心思想</strong>：RNA不像DNA那样永远规整地保持双螺旋。RNA是单链的，通过链内碱基配对形成复杂的局部二级结构（茎-环、假结等），这些结构赋予RNA多样化的功能——从信息传递（mRNA）到催化（核酶）到结构支架（rRNA）。</p>

<table>
<tr><th>RNA类型</th><th>功能</th><th>特征</th></tr>
<tr><td><span class="kp">mRNA</span></td><td>携带遗传信息从DNA到核糖体</td><td>5'帽子+编码区+3' polyA尾。原核mRNA多为多顺反子，真核几乎全是单顺反子</td></tr>
<tr><td><span class="kp">tRNA</span></td><td>翻译密码子为氨基酸</td><td>三叶草二级结构→倒L形三级结构。含大量稀有碱基（D、ψ等）</td></tr>
<tr><td><span class="kp">rRNA</span></td><td>核糖体结构和催化核心</td><td>占细胞总RNA的~80%。23S/28S rRNA是肽酰转移酶的催化组分（核酶）</td></tr>
<tr><td><span class="kp">miRNA / siRNA</span></td><td>基因沉默</td><td>~22nt，与AGO蛋白结合，通过碱基互补靶向mRNA使其降解或翻译抑制</td></tr>
</table>

<blockquote>易错：(1) 真核mRNA的5'帽子是7-甲基鸟苷酸通过5'-5'三磷酸桥连接在mRNA的5'端——注意是反向连接（5'对5'，而非正常的5'对3'）；(2) tRNA的3'端总是CCA-OH，氨基酸连在末端A的3'-OH上（氨酰化反应）。</blockquote>

<h2>第8章 核酸的性质及研究方法</h2>

<h3>8.1 DNA的变性、复性与杂交 <span class="tag-must">必考</span></h3>

<p><span class="kp">DNA变性（denaturation/melting）</span><span class="exp">：双螺旋中的氢键断裂、两条链分开成为无规卷曲单链的过程。变性不切断磷酸二酯键（一级结构保持完整）。</span></p>

<p><span class="kp">增色效应（hyperchromic effect）</span><span class="exp">：DNA变性时A₂₆₀吸光度增加~30-40%。原理：双链中碱基紧密堆积，碱基环的π电子互相作用抑制紫外吸收；解链后碱基暴露，吸收增加。这是监测DNA变性的标准方法。</span></p>

<p><span class="kp">熔解温度（Tm, melting temperature）</span><span class="exp">：DNA变性达50%时的温度。Tm受以下因素影响：(1) G-C含量↑→Tm↑（G-C有3个氢键，A-T只有2个）；(2) 盐浓度↑→Tm↑（阳离子屏蔽磷酸骨架的负电荷排斥）；(3) pH极端→Tm↓；(4) 有机溶剂→Tm↓。</span></p>

<p><strong>经验公式</strong>（在标准缓冲液中）：$$T_m(^\circ\mathrm{C}) = 69.3 + 0.41 \times (\%\mathrm{GC})$$</p>

<p><span class="kp">DNA复性（renaturation/reannealing）</span><span class="exp">：变性DNA的两条互补单链重新退火形成双螺旋。复性速率取决于：(1) DNA浓度（浓度越高碰撞越快）；(2) 基因组复杂度（序列越复杂越慢——因为互补链需要更长的时间来找对「另一半」）；(3) 离子强度；(4) 温度（最佳复性温度≈Tm-25°C）。</span></p>

<p><span class="kp">Cot曲线</span><span class="exp">：以初始DNA浓度(C₀)×时间(t)为横坐标绘制复性百分比曲线。Cot₁/₂（半数复性时的Cot值）与基因组复杂度成正比——基因组越小/序列越简单，复性越快。人类基因组中有高度重复序列（极快复性，Cot₁/₂很小）、中等重复序列（如rRNA基因）和单拷贝序列（极慢复性，Cot₁/₂巨大）。</span></p>

<p><span class="kp">核酸分子杂交</span><span class="exp">：利用变性和复性原理，用已知的单链核酸探针检测样品中的互补序列。Southern blot（DNA检测DNA）、Northern blot（RNA检测RNA）、FISH（荧光原位杂交）、基因芯片都是杂交原理的不同应用形式。</span></p>

<blockquote>易错：(1) Tm不是DNA完全熔解的温度，是50%变性的温度；(2) 较高的Tm反映了DNA结构稳定性的增加，不是因为GC对本身更强壮，而是因为GC对有3个氢键+更好的碱基堆积相互作用；(3) Southern blot测DNA, Northern blot测RNA, Western blot测蛋白——命名极易混淆：Southern是发明人的名字，其他是戏仿。</blockquote>

<h2>第9章 酶学概论</h2>

<h3>9.1 酶是生物催化剂 <span class="tag-must">必考</span></h3>

<p><strong>核心问题</strong>：为什么生命需要酶？热力学上可行的反应不一定能在生理条件下发生——因为活化能太高。酶通过降低活化能（ΔG‡），使反应速率提高10⁶~10¹²倍，但酶不改变反应的平衡常数和ΔG。</p>

<p><strong>直觉类比</strong>：化学反应就像翻越一座山。底物在山的一边，产物在山的另一边。反应速率取决于翻山的速度——即有多少分子有足够的能量翻过山顶（活化能，ΔG‡）。酶的作用不是把山铲平（改变ΔG），而是在山中间挖一条隧道——降低了需要攀爬的高度（降低ΔG‡），更多分子能通过隧道到达对面。</p>

<p><span class="kp">酶的催化特性</span>：</p>
<ul>
<li><span class="kp">高效性</span><span class="exp">——速率提升可达10¹²倍（如脲酶催化尿素水解比非催化快10¹⁴倍）</span></li>
<li><span class="kp">专一性（特异性）</span><span class="exp">——绝对专一性（只催化一种底物）、相对专一性（催化一类类似底物）、立体专一性（只识别一个手性异构体）</span></li>
<li><span class="kp">温和条件</span><span class="exp">——常温常压中性pH，而化学催化剂常需高温高压强酸强碱</span></li>
<li><span class="kp">可调控性</span><span class="exp">——别构调控、共价修饰、酶量调控、抑制剂等多种调节方式</span></li>
</ul>

<h3>9.2 酶的结构基础——活性中心 <span class="tag-must">必考</span></h3>

<p><span class="kp">活性中心（active site）</span><span class="exp">是酶分子上结合底物并将其转化为产物的特定区域。它通常是一个三维的裂缝或口袋，仅占酶总体积的一小部分（~5-10%）。</span></p>

<p><strong>活性中心的组成</strong>：</p>
<ul>
<li><span class="kp">结合基团（binding groups）</span><span class="exp">——负责识别和结合底物，通常通过氢键、疏水力、离子键与底物相互作用</span></li>
<li><span class="kp">催化基团（catalytic groups）</span><span class="exp">——直接参与化学键的断裂和形成，通常是Ser、His、Asp、Glu、Cys、Lys等具有功能侧链的残基</span></li>
</ul>

<p><strong>酶的催化机制分类</strong>：</p>
<ul>
<li><span class="kp">酸碱催化</span><span class="exp">——活性中心的氨基酸侧链作为质子供体（酸）或受体（碱），稳定过渡态</span></li>
<li><span class="kp">共价催化</span><span class="exp">——酶与底物形成共价中间体（如Ser-OH亲核攻击形成酰基-酶中间体）</span></li>
<li><span class="kp">金属离子催化</span><span class="exp">——金属离子（Zn²⁺, Mg²⁺, Fe²⁺等）提供Lewis酸催化、稳定负电荷、介导氧化还原</span></li>
<li><span class="kp">邻近与定向效应</span><span class="exp">——将两个底物在活性中心以正确的空间取向「摆放」在一起，使有效浓度极大提高</span></li>
<li><span class="kp">过渡态稳定化</span><span class="exp">——活性中心的形状不是完美匹配底物，而是完美匹配过渡态——酶与过渡态的紧密结合降低了活化能</span></li>
</ul>

</body><!-- CONTINUED IN PART 2 -->

"""

# Save the HTML
output_path = '/workspace/output/生物化学_第一篇_结构生物化学_知识精讲.html'
save_knowledge_html(body, output_path, '第一篇 结构生物化学（第1-18章）知识精讲')
print(f'Generated: {output_path}')