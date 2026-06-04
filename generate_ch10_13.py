#!/usr/bin/env python3
"""生成第一篇结构生物化学第10-13章的知识精讲和自测题HTML。
第10章 酶学导论 | 第11章 酶动力学 | 第12章 酶的作用机制 | 第13章 酶的调节
"""

import sys
sys.path.insert(0, '/workspace/scripts')
from template_engine import save_knowledge_html, save_test

# ============================================================
# 第10-13章 知识精讲 (深度学习模式)
# ============================================================

knowledge_body = r'''

<div class="chapter-overview card" style="border-left: 4px solid #e74c3c;">
<h3>本篇核心地位</h3>
<p>第10-13章构成<strong>酶学模块</strong>，是结构生物化学中<strong>考研分值最高、命题最密集</strong>的板块。酶动力学（第11章）和酶调节（第13章）每年必出大题。掌握本篇需要做到：(1) 理解酶的催化本质，(2) 掌握M-M动力学及其抑制类型的双倒数图判别，(3) 熟悉催化三联体等经典机制，(4) 理解别构调节和共价修饰的级联放大逻辑。</p>
</div>

<!-- ===== 第10章 ===== -->
<h2>第10章 酶学导论</h2>

<div class="motivation card">
<h3>动机推演</h3>
<p>为什么生命需要酶？</p>
<p>化学反应需要<strong>活化能</strong>。没有催化剂时，生物体内绝大多数反应的速率慢到毫无生理意义。酶的进化使得反应速率提升10⁶~10¹⁷倍——这不是小修小补，而是从"不可能"到"瞬间完成"的质变。理解酶的本质，就理解了生命为什么能以化学方式运转。</p>
</div>

<h3>10.1 酶的定义与化学本质 <span class="tag-must">必考</span></h3>

<div class="intuitive-analogy card">
<h3>直觉类比</h3>
<p>酶就像细胞内的<strong>"专业技师"</strong>——每个技师（酶）只擅长一种活（专一性），干活极快（高效性），只在温和条件下工作（常温常压），且工作状态可被调节（可调控性）。没有技师，原料自己反应几乎等于不发生。</p>
</div>

<p><span class="kp">酶（enzyme）</span>是由活细胞产生的、具有催化活性的生物大分子。绝大多数酶的化学本质是<strong>蛋白质</strong>，少数是<strong>RNA</strong>（核酶，ribozyme）。酶所催化的反应称为<strong>酶促反应</strong>，被酶作用的物质称为<strong>底物</strong>（substrate）。</p>

<div class="test-point card">
<h3>考研考点</h3>
<ul>
<li><strong>填空题/判断题高频：</strong>「所有酶都是蛋白质」——<strong>错误</strong>。核酶的发现（Cech & Altman, 1989年诺贝尔化学奖）证明了RNA也具有催化功能。</li>
<li><strong>名词解释高频：</strong>酶、核酶(ribozyme)、底物、酶促反应。</li>
</ul>
</div>

<h3>10.2 酶与一般化学催化剂的比较</h3>

<table class="compare-table">
<tr><th>比较维度</th><th>酶（生物催化剂）</th><th>一般化学催化剂</th></tr>
<tr><td><strong>高效性</strong></td><td>极高——催化效率可达10⁶~10¹⁷倍提升</td><td>一般——通常10²~10⁴倍提升</td></tr>
<tr><td><strong>专一性</strong></td><td>极高——对底物和反应类型有严格选择性</td><td>低——通常对一类反应有效</td></tr>
<tr><td><strong>反应条件</strong></td><td>温和——常温、常压、近中性pH</td><td>常需高温、高压、极端pH</td></tr>
<tr><td><strong>可调控性</strong></td><td>精确——别构调节、共价修饰、酶量调控</td><td>一般不可调控</td></tr>
<tr><td><strong>化学本质</strong></td><td>蛋白质（或RNA）</td><td>无机物或简单有机物</td></tr>
</table>

<div class="pitfall card">
<h3>易错辨析</h3>
<p><strong>误区：</strong>酶只能加快反应，不能改变反应平衡。<br>
<strong>正解：</strong>这是正确的结论。酶<strong>不改变</strong>反应的平衡常数(K<sub>eq</sub>)和ΔG，只降低活化能从而加速达到平衡的过程。考试常以判断/选择题考察这一点。</p>
</div>

<h3>10.3 酶的活性中心与必需基团 <span class="tag-freq">高频</span></h3>

<p><span class="kp">活性中心（active center）</span>是酶分子上直接参与底物结合和催化的一小部分区域，通常由空间上靠近但一级序列上可能远离的若干氨基酸残基组成。</p>

<p>活性中心的基团分为两类：</p>
<ul>
<li><span class="kp">结合基团</span><span class="exp">——负责识别和结合底物，决定酶的专一性</span></li>
<li><span class="kp">催化基团</span><span class="exp">——直接参与化学键的断裂和形成，负责催化功能</span></li>
</ul>

<p><span class="kp">必需基团（essential groups）</span>是酶发挥催化活性所必需的化学基团，包括活性中心的基团和活性中心以外对维持酶构象必需的基团。必需基团≠全在活性中心。</p>

<div class="pitfall card">
<h3>易错辨析</h3>
<p><strong>误区：</strong>必需基团就是活性中心的氨基酸残基。<br>
<strong>正解：</strong>活性中心外的某些残基也是必需基团——它们可能不直接参与催化，但对维持酶的正确三维构象至关重要。化学修饰这些残基一样会导致酶失活。</p>
</div>

<h3>10.4 酶的专一性 <span class="tag-freq">高频</span></h3>

<p>酶的专一性（specificity）是酶区别于一般催化剂的最显著特征。根据严格程度分为：</p>

<table>
<tr><th>专一性类型</th><th>定义</th><th>实例</th></tr>
<tr><td><span class="kp">绝对专一性</span></td><td>只作用于一种底物，催化一种反应</td><td>脲酶——只水解尿素，不对任何其他酰胺作用</td></tr>
<tr><td><span class="kp">相对专一性（基团专一性）</span></td><td>对底物的特定化学基团有要求，对其余部分容忍变化</td><td>胰蛋白酶——水解Lys或Arg的C端肽键</td></tr>
<tr><td><span class="kp">相对专一性（键专一性）</span></td><td>只要求特定的化学键，对键两侧基团容忍度更大</td><td>酯酶——水解各种酯键</td></tr>
<tr><td><span class="kp">立体专一性</span></td><td>区别底物的立体异构体（光学异构或几何异构）</td><td>L-氨基酸氧化酶只作用于L-氨基酸</td></tr>
</table>

<div class="intuitive-analogy card">
<h3>直觉类比</h3>
<p>专一性就像<strong>锁和钥匙</strong>——绝对专一性是一把钥匙只开一把锁；基团专一性是一把钥匙能开所有「同一个品牌」的锁；键专一性是一把钥匙能开所有类型的锁，只要锁孔形状一样；立体专一性则是钥匙只能从一个方向插入（左手钥匙打不开右手锁）。</p>
</div>

<h3>10.5 酶的命名与分类 <span class="tag-must">必考</span></h3>

<p>国际酶学委员会（IEC）将酶按催化反应类型分为<strong>六大类</strong>：</p>

<table>
<tr><th>类别</th><th>催化反应类型</th><th>典型例子</th></tr>
<tr><td><span class="kp">1. 氧化还原酶</span></td><td>电子转移（氧化还原反应）</td><td>乳酸脱氢酶(LDH)、细胞色素c氧化酶</td></tr>
<tr><td><span class="kp">2. 转移酶</span></td><td>转移功能基团（除H以外）</td><td>己糖激酶(转移磷酸基)、氨基转移酶</td></tr>
<tr><td><span class="kp">3. 水解酶</span></td><td>水解反应（加水断裂化学键）</td><td>胰蛋白酶、淀粉酶、脂肪酶</td></tr>
<tr><td><span class="kp">4. 裂合酶</span></td><td>非水解性地断裂C-C/C-N等键（消除反应）</td><td>醛缩酶、延胡索酸酶</td></tr>
<tr><td><span class="kp">5. 异构酶</span></td><td>催化分子内异构化</td><td>磷酸己糖异构酶、磷酸丙糖异构酶</td></tr>
<tr><td><span class="kp">6. 连接酶</span></td><td>利用ATP的能量连接两个分子</td><td>DNA连接酶、丙酮酸羧化酶</td></tr>
</table>

<div class="pitfall card">
<h3>易错辨析</h3>
<p><strong>误区：</strong>裂合酶（lyase）与水解酶（hydrolase）都会断裂化学键，分不清。<br>
<strong>正解：</strong>水解酶<strong>加水</strong>断裂（如肽键水解），裂合酶<strong>不加水</strong>，通过消除反应断裂C-C或C-N键并产生双键。简单口诀——「水解酶加水，裂合酶不加水」。</p>
</div>

<h3>10.6 辅因子：辅酶与辅基 <span class="tag-freq">高频</span></h3>

<table>
<tr><th>类型</th><th>与酶的结合方式</th><th>化学本质</th><th>实例</th></tr>
<tr><td><span class="kp">辅酶（coenzyme）</span></td><td>非共价结合，<strong>疏松</strong>（可透析除去）</td><td>小分子有机物</td><td>NAD⁺、NADP⁺、CoA、FAD</td></tr>
<tr><td><span class="kp">辅基（prosthetic group）</span></td><td>共价或极紧密非共价结合，<strong>牢固</strong>（不可透析除去）</td><td>有机物或金属离子</td><td>FAD（有些酶中为共价结合）、血红素、生物素</td></tr>
<tr><td><span class="kp">金属离子</span></td><td>可松可紧</td><td>金属元素</td><td>Zn²⁺（碳酸酐酶）、Mg²⁺（激酶）、Fe²⁺/Fe³⁺</td></tr>
</table>

<p>金属离子的作用：(1) 参与底物结合和定向；(2) 通过静电效应稳定过渡态；(3) 作为亲电催化剂（Lewis酸）；(4) 参与电子传递（氧化还原酶中的Fe、Cu等）。</p>

<h3>10.7 酶活力的测定 <span class="tag-freq">高频</span></h3>

<ul>
<li><span class="kp">酶活力单位（IU）</span><span class="exp">：在特定条件下（最适pH、最适温度），每分钟催化转化1 μmol底物所需的酶量。</span></li>
<li><span class="kp">Katal（kat）</span><span class="exp">：国际单位制——每秒催化转化1 mol底物。1 kat = 6×10⁷ IU。</span></li>
<li><span class="kp">比活力（specific activity）</span><span class="exp">：每毫克蛋白质所含的酶活力单位数（IU/mg或kat/mg）。比活力 = 总活力/总蛋白量，是衡量酶<strong>纯度</strong>的指标——纯化倍数越高，比活力越大。</span></li>
</ul>

<h3>10.8 核酶（ribozyme）<span class="tag-must">必考</span></h3>

<div class="card" style="border-left: 4px solid #e74c3c;">
<p><strong>核酶发现——打破「酶=蛋白质」的教条</strong></p>
<p>1982年，Thomas Cech发现四膜虫（Tetrahymena）的rRNA前体在<strong>完全无蛋白质</strong>的条件下可以进行自我剪接（self-splicing），证明RNA分子本身具有催化活性。同年，Sidney Altman发现RNase P中的RNA组分才是真正的催化剂。两人共享<strong>1989年诺贝尔化学奖</strong>。</p>
<p><strong>深远意义：</strong>核酶的发现为"RNA世界"假说提供了关键证据——在DNA和蛋白质出现之前，RNA可能同时承担遗传信息存储和催化功能。</p>
</div>

<!-- ===== 第11章 ===== -->
<h2>第11章 酶动力学 <span class="tag-must">考研重中之重</span></h2>

<div class="motivation card">
<h3>动机推演</h3>
<p>酶动力学的核心问题：<strong>速率怎么变？受什么控制？</strong></p>
<p>如果我们知道了v₀与[S]的定量关系，就可以获得Km和Vmax这两个刻画酶特征的关键参数，进而深入理解酶的催化效率和调控机制。抑制剂研究不仅为药物开发提供理论依据（如磺胺类药物），更是考研中区分三种可逆抑制类型的必考点。</p>
</div>

<h3>11.1 Michaelis-Menten方程的推导前提 <span class="tag-must">必考</span></h3>

<p>M-M方程建立在以下关键假设之上：</p>

<ol>
<li><span class="kp">稳态假设（steady-state assumption）</span>：在反应的初始阶段，酶-底物复合物[ES]的浓度保持恒定，即 d[ES]/dt = 0（ES的形成速率 = ES的分解速率）。这是推导的核心前提。</li>
<li><span class="kp">初始速度条件</span>：[S] &gt;&gt; [E]，[S]几乎不变；[P] ≈ 0，逆反应可忽略。因此只考虑正向初始速度v₀。</li>
<li>反应模型：$E + S \xrightleftharpoons[k_{-1}]{k_1} ES \xrightarrow{k_{cat}} E + P$</li>
</ol>

<div class="pitfall card">
<h3>易错辨析</h3>
<p><strong>误区：</strong>稳态假设等同于平衡假设。<br>
<strong>正解：</strong>平衡假设要求k₁[E][S] = k₋₁[ES]（即ES仅通过解离回到E+S，不考虑催化步骤）。稳态假设更一般——ES的形成速率 = 分解速率（包括催化和解离两条路径的总和），即k₁[E][S] = (k₋₁ + k<sub>cat</sub>)[ES]。当k<sub>cat</sub> &lt;&lt; k₋₁时，稳态假设退化为平衡假设。</p>
</div>

<h3>11.2 M-M方程及其参数 <span class="tag-must">必考</span></h3>

<p class="formula">$$v_0 = \frac{V_{\max}[S]}{K_m + [S]}$$</p>

<table>
<tr><th>参数</th><th>定义</th><th>物理意义</th><th>单位</th></tr>
<tr><td><span class="kp">K<sub>m</sub></span></td><td>$\displaystyle\frac{k_{-1}+k_{\mathrm{cat}}}{k_1}$</td><td>使v₀=V<sub>max</sub>/2时的底物浓度。反映酶与底物的<strong>亲和力</strong>——K<sub>m</sub>越小，亲和力越大。当k<sub>cat</sub> &lt;&lt; k₋₁时，K<sub>m</sub>≈K<sub>d</sub>（解离常数）</td><td>mol/L (M)</td></tr>
<tr><td><span class="kp">V<sub>max</sub></span></td><td>$k_{\mathrm{cat}}[E]_{total}$</td><td>所有酶分子被底物<strong>饱和</strong>时的最大速率。与[E]成正比</td><td>mol·L⁻¹·s⁻¹</td></tr>
<tr><td><span class="kp">k<sub>cat</sub></span></td><td>催化常数（转换数，turnover number）</td><td>每个酶分子在饱和条件下每秒转化的底物分子数。k<sub>cat</sub> = V<sub>max</sub>/[E]<sub>total</sub></td><td>s⁻¹</td></tr>
<tr><td><span class="kp">k<sub>cat</sub>/K<sub>m</sub></span></td><td>催化效率/专一性常数</td><td>综合衡量酶催化效率的最优参数——考虑结合(K<sub>m</sub>)和催化(k<sub>cat</sub>)两方面。上限受扩散控制(~10⁸-10⁹ M⁻¹s⁻¹)，达到此上限的酶称为<strong>动力学完美酶</strong></td><td>M⁻¹·s⁻¹</td></tr>
</table>

<div class="intuitive-analogy card">
<h3>直觉类比</h3>
<ul>
<li><strong>K<sub>m</sub></strong> ≈ 网店对顾客的<strong>吸引力</strong>——K<sub>m</sub>越小，说明只需很少底物就能半饱和，酶对底物的亲和力越强。</li>
<li><strong>V<sub>max</sub></strong> = 高峰时段的最大<strong>处理速度</strong>——取决于店员数量([E])和每位店员的速度(k<sub>cat</sub>)。</li>
<li><strong>k<sub>cat</sub></strong> = 每位店员的<strong>单件处理速度</strong>。</li>
<li><strong>k<sub>cat</sub>/K<sub>m</sub></strong> = 综合<strong>性价比</strong>——既考虑吸引顾客的能力，又考虑处理速度。</li>
</ul>
</div>

<h3>11.3 Lineweaver-Burk双倒数作图 <span class="tag-must">必考</span></h3>

<p>将M-M方程取倒数得到线性形式：</p>

<p class="formula">$$\frac{1}{v_0} = \left(\frac{K_m}{V_{\max}}\right) \cdot \frac{1}{[S]} + \frac{1}{V_{\max}}$$</p>

<p>以1/v₀为Y轴、1/[S]为X轴作图，得到一条直线：</p>
<ul>
<li><span class="kp">Y截距</span> = 1/V<sub>max</sub></li>
<li><span class="kp">X截距</span> = −1/K<sub>m</sub></li>
<li><span class="kp">斜率</span> = K<sub>m</sub>/V<sub>max</sub></li>
</ul>

<div class="test-point card">
<h3>考研考点</h3>
<p>双倒数图是<strong>区分三种可逆抑制剂类型的最直观工具</strong>。只看直线的交点位置即可判断抑制类型。这是每年必考的内容。</p>
</div>

<h3>11.4 多底物反应机制 <span class="tag-freq">高频</span></h3>

<table>
<tr><th>机制</th><th>底物结合顺序</th><th>产物释放顺序</th><th>双倒数图特征</th><th>实例</th></tr>
<tr><td><span class="kp">顺序机制(Ordered)</span></td><td>A先B后，严格有序</td><td>P先Q后</td><td>交于一点</td><td>乳酸脱氢酶(NAD⁺先，乳酸后)</td></tr>
<tr><td><span class="kp">随机机制(Random)</span></td><td>A、B无先后顺序</td><td>P、Q无先后</td><td>交于一点</td><td>己糖激酶（部分）</td></tr>
<tr><td><span class="kp">乒乓机制(Ping-Pong)</span></td><td>A进入→P释放→B进入→Q释放</td><td>交替进行</td><td><strong>平行线</strong></td><td>氨基转移酶、胰凝乳蛋白酶</td></tr>
</table>

<div class="intuitive-analogy card">
<h3>直觉类比</h3>
<p>乒乓机制就像<strong>接力赛</strong>——第一位跑者(A)先到，交棒(P)出去后，第二位跑者(B)才进场接棒继续跑。第一个底物的一部分被酶临时"扣留"（形成共价中间物），第二个底物随后与酶结合完成反应。</p>
</div>

<h3>11.5 温度与pH的影响 <span class="tag-freq">高频</span></h3>

<ul>
<li><span class="kp">最适温度</span><span class="exp">：速率随温度先升后降——升温加速分子运动（Arrhenius效应），但过高温度导致蛋白质变性失活。注意：<strong>最适温度不是酶的特征常数</strong>，随反应时间、底物浓度等条件变化。</span></li>
<li><span class="kp">最适pH</span><span class="exp">：活性中心关键残基的离子化状态依赖pH——过高或过低pH会破坏活性中心的正确质子化状态。同样，<strong>最适pH不是酶的特征常数</strong>。</span></li>
</ul>

<div class="pitfall card">
<h3>易错辨析</h3>
<p><strong>误区：</strong>最适温度/最适pH是酶的特征常数。<br>
<strong>正解：</strong>它们随实验条件（反应时间、缓冲液类型、底物浓度等）而变化，不是酶的特征常数。K<sub>m</sub>才是酶的特征常数。</p>
</div>

<h3>11.6 可逆抑制与不可逆抑制</h3>

<ul>
<li><span class="kp">不可逆抑制</span><span class="exp">：抑制剂与酶的必需基团以<strong>共价键</strong>结合，使酶永久失活。如有机磷农药与丝氨酸蛋白酶活性中心Ser的-OH共价结合。</span></li>
<li><span class="kp">可逆抑制</span><span class="exp">：抑制剂与酶以<strong>非共价键</strong>（氢键、疏水作用等）可逆结合，透析或稀释可恢复活性。</span></li>
</ul>

<h3>11.7 三种可逆抑制的动力学特征 <span class="tag-must">必考——考研核心考点</span></h3>

<table>
<tr><th>抑制类型</th><th>抑制剂结合对象</th><th>K<sub>m</sub></th><th>V<sub>max</sub></th><th>双倒数图特征</th></tr>
<tr><td><span class="kp">竞争性抑制</span></td><td>仅游离酶E（竞争活性中心）</td><td><strong>↑（增大）</strong></td><td><strong>不变</strong></td><td>直线<strong>交于Y轴同一点</strong>（1/V<sub>max</sub>相同）</td></tr>
<tr><td><span class="kp">非竞争性抑制</span></td><td>E和ES均可（不竞争活性中心）</td><td><strong>不变</strong></td><td><strong>↓（减小）</strong></td><td>直线<strong>交于X轴同一点</strong>（−1/K<sub>m</sub>相同）</td></tr>
<tr><td><span class="kp">反竞争性抑制</span></td><td>仅ES复合物</td><td><strong>↓（减小）</strong></td><td><strong>↓（减小）</strong></td><td>直线<strong>平行</strong>（斜率不变）</td></tr>
</table>

<div class="intuitive-analogy card">
<h3>直觉类比</h3>
<ul>
<li><strong>竞争性</strong>：一个冒牌顾客（抑制剂）堵在店门口，真顾客（底物）多了就能挤进去——被饱和时速度不变（V<sub>max</sub>不变），但需要更多顾客才能达到同样的速度（K<sub>m</sub>增大）。</li>
<li><strong>非竞争性</strong>：有人在后门给店员捣乱——不管来多少顾客，捣乱的人让一部分店员永远无法工作，最大处理量降低（V<sub>max</sub>↓），但顾客吸引力不变（K<sub>m</sub>不变）。</li>
<li><strong>反竞争性</strong>：只有顾客进了店、店员正在服务时才有人来捣乱——顾客进来了反而被缠住（K<sub>m</sub>↓，因为ES被抑制剂"锁住"了使表观亲和力增大），但最大处理速度也下降（V<sub>max</sub>↓）。</li>
</ul>
</div>

<div class="card" style="border-left: 4px solid #27ae60;">
<h3>磺胺类药物——竞争性抑制的经典范例</h3>
<p>磺胺类药物是对氨基苯甲酸（PABA）的<strong>结构类似物</strong>。细菌需要PABA合成叶酸（二氢叶酸），磺胺竞争性地抑制二氢蝶酸合成酶，阻断叶酸合成→细菌不能合成核酸→抑菌。人类细胞不合成叶酸（从食物获取），因此磺胺对人有选择性毒性。这体现了竞争性抑制的三要素：(1)结构类似物；(2)竞争活性中心；(3)提高底物浓度可逆转抑制。</p>
</div>

<div class="pitfall card">
<h3>易错辨析——三种抑制的双倒数图终极判别</h3>
<table>
<tr><th>看图特征</th><th>判定</th></tr>
<tr><td>所有直线交于Y轴同一点</td><td>= 竞争性：V<sub>max</sub>不变，K<sub>m</sub>增大</td></tr>
<tr><td>所有直线交于X轴同一点</td><td>= 非竞争性：K<sub>m</sub>不变，V<sub>max</sub>减小</td></tr>
<tr><td>所有直线互相平行</td><td>= 反竞争性：V<sub>max</sub>↓，K<sub>m</sub>↓（等比例减小）</td></tr>
<tr><td>交于第二象限某一点</td><td>= 竞争性（交点不在轴上）或混合型抑制的特殊情况</td></tr>
</table>
</div>

<!-- ===== 第12章 ===== -->
<h2>第12章 酶的作用机制</h2>

<div class="motivation card">
<h3>动机推演</h3>
<p>核心问题：<strong>酶如何在物理化学层面实现催化的"魔法"？</strong></p>
<p>酶促反应速率可以达到非催化反应的10¹⁷倍——这不是巧合。酶的催化效率来自多种策略的精妙组合：邻近效应、定向效应、酸碱催化、共价催化、金属离子催化，以及最重要的——过渡态稳定化。</p>
</div>

<h3>12.1 过渡态理论 <span class="tag-must">必考</span></h3>

<p><span class="kp">过渡态</span>是反应物→产物转化路径上能量最高的不稳定状态。酶的催化本质是：<strong>酶的活性中心与反应的过渡态具有最高的亲和力</strong>，通过稳定过渡态来降低活化能（ΔG<sup>‡</sup>）。</p>

<div class="card" style="border-left: 4px solid #8e44ad;">
<h3>Deep Principle——过渡态稳定化</h3>
<p>酶最稳定结合的不是底物也不是产物，而是<strong>过渡态</strong>。如果酶与底物结合得过紧（活性中心完美匹配底物构象），反而会增加底物→过渡态变形所需的能量，使活化能升高。因此一个好酶的活性中心不完全匹配底物，而是完美匹配过渡态的几何形状和电荷分布。这就是为什么过渡态类似物往往是酶的极强抑制剂（如脯氨酸消旋酶的吡咯-2-羧酸抑制剂，K<sub>i</sub>在pM级）。</p>
</div>

<h3>12.2 酶降低活化能的主要机制 <span class="tag-freq">高频</span></h3>

<table>
<tr><th>机制</th><th>原理</th><th>效应</th></tr>
<tr><td><span class="kp">邻近效应与定向效应</span></td><td>将底物分子以正确的空间取向固定在活性中心，大大增加有效碰撞概率</td><td>等效于将有效浓度提高10³~10⁵倍</td></tr>
<tr><td><span class="kp">酸碱催化</span></td><td>活性中心的氨基酸侧链（His的咪唑基、Asp/Glu的羧基、Lys的氨基等）作为质子供体或受体</td><td>在近中性pH下实现强酸强碱才能完成的质子转移</td></tr>
<tr><td><span class="kp">共价催化</span></td><td>酶与底物形成瞬时的共价中间物（如酰基-酶中间体）</td><td>将单步高活化能反应拆分为两步低活化能反应</td></tr>
<tr><td><span class="kp">金属离子催化</span></td><td>金属离子作为Lewis酸（亲电催化剂）、静电稳定剂或氧化还原中心</td><td>极化底物化学键使其更易断裂</td></tr>
<tr><td><span class="kp">底物应变（构象变形）</span></td><td>酶与底物结合迫使底物采取接近过渡态的扭曲构象</td><td>降低到达过渡态所需的额外变形能</td></tr>
</table>

<div class="intuitive-analogy card">
<h3>直觉类比</h3>
<p>酶就像一位<strong>经验丰富的拆弹专家</strong>——(1)把两个线头精确定位对齐（邻近+定向），(2)用专用的酸/碱溶液处理接点（酸碱催化），(3)必要时先接上自己的工具再剪（共价催化），(4)利用金属钳子帮忙夹住（金属催化），(5)把雷管预先扭到快要裂的位置（底物应变）。每一步都是为降低"引爆炸弹"的活化能。</p>
</div>

<h3>12.3 丝氨酸蛋白酶——催化三联体 <span class="tag-must">必考</span></h3>

<p><span class="kp">丝氨酸蛋白酶家族</span>（胰凝乳蛋白酶、胰蛋白酶、弹性蛋白酶）共享相同的<strong>催化三联体（catalytic triad）</strong>和两步共价催化机制，是酶催化机制的经典范例。</p>

<p><strong>催化三联体：</strong></p>
<ul>
<li><span class="kp">Asp¹⁰²</span><span class="exp">——-COO⁻通过氢键定向His⁵⁷的咪唑环，提高His的pK<sub>a</sub>使其成为更好的碱</span></li>
<li><span class="kp">His⁵⁷</span><span class="exp">——咪唑基作为一般酸碱催化剂：第一步从Ser¹⁹⁵接受质子（碱），第二步给离去基团提供质子（酸）</span></li>
<li><span class="kp">Ser¹⁹⁵</span><span class="exp">——被His活化为强亲核试剂Ser-O⁻，直接攻击底物羰基碳</span></li>
</ul>

<p><strong>催化机制（两步共价催化）：</strong></p>
<ol>
<li><span class="kp">酰化阶段</span>：Ser¹⁹⁵-O⁻亲核攻击底物肽键的羰基碳 → 形成四面体过渡态（氧负离子穴oxyanion hole中Gly和Ser的主链-NH稳定此过渡态） → C端肽段离去 → 形成<strong>酰基-酶中间体</strong></li>
<li><span class="kp">脱酰阶段</span>：水分子进入活性中心 → His⁵⁷从水接受质子 → OH⁻攻击酰基-酶中间体 → 第二次四面体过渡态 → 释放N端肽段 → 酶恢复自由态</li>
</ol>

<div class="test-point card">
<h3>考研考点</h3>
<p><strong>简答题必考：</strong>"简述丝氨酸蛋白酶的催化机制"。得分要点：①命名催化三联体和各自角色；②两步机制（酰化+脱酰）；③氧负离子穴的作用；④以胰凝乳蛋白酶、胰蛋白酶、弹性蛋白酶为例说明底物特异性的结构基础（S1口袋不同）。</p>
</div>

<h3>12.4 溶菌酶 <span class="tag-freq">高频</span></h3>

<p><span class="kp">溶菌酶（lysozyme）</span>是第一个被阐明三维结构（Phillips, 1965）和催化机制的酶。催化细菌细胞壁肽聚糖中NAM-NAG间的β-1,4-糖苷键水解。</p>

<p><strong>核心机制：</strong></p>
<ul>
<li><span class="kp">Glu³⁵</span>（pK<sub>a</sub> ≈ 6.5，非寻常高值）：作为一般酸催化剂，提供质子给糖苷键的O</li>
<li><span class="kp">Asp⁵²</span>（pK<sub>a</sub> ≈ 3.5）：静电稳定糖基正离子过渡态（碳正离子）</li>
<li><span class="kp">底物应变</span>：D糖环被扭曲成半椅式构象——这恰好降低到达过渡态所需的能量</li>
</ul>

<h3>12.5 碳酸酐酶 <span class="tag-freq">高频</span></h3>

<p><span class="kp">碳酸酐酶</span>是已知催化效率最高的酶之一，k<sub>cat</sub>/K<sub>m</sub> ≈ 10⁸ M⁻¹·s⁻¹，接近扩散控制极限。催化反应：CO₂ + H₂O ⇌ HCO₃⁻ + H⁺。</p>

<p><strong>催化机制：</strong></p>
<ul>
<li>活性中心Zn²⁺配位一个水分子</li>
<li>Zn²⁺的Lewis酸效应将水的pK<sub>a</sub>从15.7降至~7——在生理pH下产生高浓度OH⁻（极强的亲核试剂）</li>
<li>OH⁻攻击CO₂的碳原子形成HCO₃⁻</li>
<li>催化效率极高的原因：活性中心精确构造使得每一步都无"浪费"的能量障碍</li>
</ul>

<!-- ===== 第13章 ===== -->
<h2>第13章 酶的调节 <span class="tag-must">考研重点</span></h2>

<div class="motivation card">
<h3>动机推演</h3>
<p>为什么需要调节？</p>
<p>细胞内同时进行数千种化学反应，必须精确协调。代谢网络需要<strong>开关</strong>和<strong>调速器</strong>来响应环境变化和内部需求。酶的调节机制从快（毫秒级，别构调节）到慢（小时级，酶量调节）构成分级调控网络。</p>
</div>

<h3>13.1 别构调节（Allosteric Regulation）<span class="tag-must">必考</span></h3>

<p><span class="kp">别构酶</span>是代谢调控的核心——效应物（effector）结合在活性中心以外的<strong>别构位点</strong>，通过构象变化影响催化活性。</p>

<p><strong>别构酶的特征：</strong></p>
<ul>
<li><span class="kp">多亚基结构</span>（具有四级结构）——单亚基酶不可能有别构效应</li>
<li><span class="kp">S形（sigmoidal）v-[S]曲线</span>——而非M-M酶的双曲线。S形曲线反映亚基间的<strong>正协同效应</strong>（一个亚基结合底物后，通过构象变化使相邻亚基更易结合底物）</li>
<li><span class="kp">反馈抑制（feedback inhibition）</span>——代谢途径的终产物抑制该途径第一个关键酶，防止产物过量积累</li>
</ul>

<div class="intuitive-analogy card">
<h3>直觉类比</h3>
<p>S形曲线就像一个<strong>无级调速开关</strong>——低速段迟钝（需要一定底物浓度才能启动），中速段灵敏（底物微小变化引起速率骤变），高速段饱和。这种特性使酶在生理底物浓度范围内具有"开关式"调控能力，M-M酶的双曲线则做不到这一点。</p>
</div>

<p><strong>经典别构酶范例——ATCase：</strong></p>
<ul>
<li>催化嘧啶生物合成第一步（氨甲酰磷酸 + Asp → N-氨甲酰天冬氨酸）</li>
<li>别构抑制剂：CTP（嘧啶终产物→反馈抑制）</li>
<li>别构激活剂：ATP（嘌呤核苷酸→嘌呤和嘧啶需协调合成）</li>
<li>结构：6催化亚基（2三聚体）+ 6调节亚基（3二聚体），T（紧张态）↔ R（松弛态）转变</li>
</ul>

<h3>13.2 共价修饰调节 <span class="tag-must">必考</span></h3>

<table>
<tr><th>修饰方式</th><th>关键酶</th><th>效果</th><th>可逆性</th></tr>
<tr><td><span class="kp">磷酸化/去磷酸化</span></td><td>蛋白激酶(PK) / 蛋白磷酸酶(PP)</td><td>激活或抑制（取决于靶蛋白）</td><td>完全可逆</td></tr>
<tr><td><span class="kp">酶原激活</span></td><td>特定蛋白水解酶</td><td>不可逆激活</td><td>不可逆（蛋白水解）</td></tr>
<tr><td><span class="kp">乙酰化/去乙酰化</span></td><td>HAT / HDAC</td><td>改变染色质结构、酶活性</td><td>可逆</td></tr>
<tr><td><span class="kp">泛素化</span></td><td>E1-E2-E3级联</td><td>靶向蛋白酶体降解</td><td>可逆（去泛素化酶）</td></tr>
</table>

<p><strong>酶原激活——安全机制：</strong></p>
<ul>
<li><span class="kp">胰蛋白酶原 → 胰蛋白酶</span>：肠激酶切除N端六肽 → 构象重排 → 活性中心形成。在胰腺中合成无活性的酶原，到达肠道后才激活，保护胰腺自身不被消化。</li>
<li><span class="kp">凝血级联</span>：凝血因子以酶原形式循环，血管损伤时逐级激活。一个因子催化激活多个下游因子，产生<strong>级联放大效应</strong>。</li>
</ul>

<h3>13.3 别构调节与共价修饰的级联放大 <span class="tag-freq">高频</span></h3>

<div class="card" style="border-left: 4px solid #2980b9;">
<h3>级联放大——信号转导的核心原理</h3>
<p>一个激素分子结合受体 → 激活多个G蛋白 → 每个G蛋白激活一个腺苷酸环化酶 → 产生多个cAMP → 每个cAMP激活一个PKA → PKA磷酸化多个靶酶。总放大倍数可达<strong>10⁶~10⁸</strong>。这就是为什么pM-nM浓度的激素就能引起巨大的细胞响应。</p>
</div>

<h3>13.4 同工酶 <span class="tag-must">必考</span></h3>

<p><span class="kp">同工酶（isozyme）</span>：催化<strong>相同化学反应</strong>但具有不同一级结构、K<sub>m</sub>值和调控特性的酶。</p>

<p><strong>乳酸脱氢酶（LDH）——最经典的同工酶范例：</strong></p>
<ul>
<li>LDH是四聚体，由H亚基（心肌型）和M亚基（骨骼肌型）以不同比例组合</li>
<li>五种同工酶：<span class="kp">LDH₁(H₄)、LDH₂(H₃M)、LDH₃(H₂M₂)、LDH₄(HM₃)、LDH₅(M₄)</span></li>
<li>催化反应：丙酮酸 + NADH + H⁺ ⇌ 乳酸 + NAD⁺</li>
</ul>

<table>
<tr><th>同工酶</th><th>亚基组成</th><th>主要分布组织</th><th>对丙酮酸K<sub>m</sub></th><th>生理意义</th></tr>
<tr><td><span class="kp">LDH₁</span></td><td>H₄</td><td>心肌、红细胞</td><td>小（高亲和力）</td><td>有氧组织——偏好乳酸→丙酮酸方向，被高浓度丙酮酸抑制</td></tr>
<tr><td><span class="kp">LDH₅</span></td><td>M₄</td><td>骨骼肌、肝脏</td><td>大（低亲和力）</td><td>糖酵解组织——偏好丙酮酸→乳酸方向，不被高浓度丙酮酸抑制</td></tr>
</table>

<div class="test-point card">
<h3>考研考点</h3>
<p><strong>LDH同工酶的临床诊断意义——经常考选择题/简答题：</strong></p>
<ul>
<li>心肌梗死：心肌细胞坏死释放LDH₁入血 → <strong>血清LDH₁ > LDH₂</strong>（正常情况LDH₂ > LDH₁）——这是心梗的诊断指标之一</li>
<li>肝脏疾病：肝细胞损伤 → 血清LDH₅升高</li>
<li>同工酶谱的电泳分离：LDH₁移动最快（最靠近阳极），LDH₅最慢</li>
</ul>
</div>

<div class="pitfall card">
<h3>易错辨析</h3>
<p><strong>误区：</strong>同工酶就是同一基因编码的不同形式。<br>
<strong>正解：</strong>同工酶<strong>由不同基因编码</strong>或由同一基因的不同等位基因编码，具有不同的氨基酸序列。它们不是翻译后修饰产生的不同形式（那是"酶的多种形式"而非严格意义上的同工酶）。</p>
</div>

<h3>13.5 酶量的调节 <span class="tag-freq">高频</span></h3>

<p>在基因表达水平调控酶的合成速率和降解速率——是比别构调节和共价修饰更慢但更持久的调控方式。典型例子：</p>
<ul>
<li>乳糖操纵子：乳糖诱导β-半乳糖苷酶的合成（底物诱导）</li>
<li>胆固醇反馈抑制HMG-CoA还原酶的合成（终产物抑制酶基因表达）</li>
<li>激素（如糖皮质激素）诱导糖异生关键酶PEPCK的合成</li>
</ul>

<div class="card" style="border-left: 4px solid #27ae60;">
<h3>本章考研命题趋势总结</h3>
<p><strong>四种酶调控机制的时间尺度对比：</strong></p>
<table>
<tr><th>调控方式</th><th>响应时间</th><th>持续时间</th><th>典型例子</th></tr>
<tr><td>别构调节</td><td>毫秒~秒</td><td>短（随效应物浓度变化）</td><td>PFK-1被ATP抑制、被AMP激活</td></tr>
<tr><td>共价修饰</td><td>秒~分钟</td><td>中等</td><td>糖原磷酸化酶的磷酸化/去磷酸化</td></tr>
<tr><td>酶原激活</td><td>秒~分钟</td><td>不可逆（一次性）</td><td>消化酶原、凝血因子</td></tr>
<tr><td>酶量调控</td><td>小时~天</td><td>长（持久）</td><td>激素诱导/抑制酶基因表达</td></tr>
</table>
</div>

'''

# Save knowledge HTML
save_knowledge_html(knowledge_body,
                    '/workspace/output/生物化学_第10-13章_知识精讲.html',
                    '生物化学 第10-13章 酶学 — 知识精讲')

print("✅ 第10-13章知识精讲已生成")

# ============================================================
# 第10-13章 自测题（共28题，满分100分）
# ============================================================

questions = [
    # ─── 单选题 (10题，每题3分，共30分) ───
    {
        "type": "single_choice",
        "points": 3,
        "question": "下列关于酶的叙述，哪一项是<strong>错误</strong>的？",
        "options": [
            "A. 酶是生物催化剂，绝大多数化学本质是蛋白质",
            "B. 所有的酶都是蛋白质",
            "C. 核酶是具有催化活性的RNA",
            "D. 酶的催化效率远高于一般化学催化剂"
        ],
        "answer": "B",
        "explanation": "核酶（ribozyme）的发现证明RNA也具有催化功能，因此'所有酶都是蛋白质'是错误的。Cech和Altman因发现核酶获得1989年诺贝尔化学奖。",
        "pitfall": "错误选C——核酶确实是RNA，C是正确的。注意题目问的是'错误'的叙述。"
    },
    {
        "type": "single_choice",
        "points": 3,
        "question": "酶促反应中，酶的作用是？",
        "options": [
            "A. 改变反应的平衡常数",
            "B. 降低反应的活化能",
            "C. 增加反应的ΔG",
            "D. 改变反应的平衡点"
        ],
        "answer": "B",
        "explanation": "酶通过稳定过渡态降低活化能（ΔG‡），从而加速反应速率，但不改变反应的平衡常数（Keq）和ΔG。这是酶的最基本特征。",
        "pitfall": "错误选A或D——酶不改变平衡常数和平衡点，只加速到达平衡的过程。"
    },
    {
        "type": "single_choice",
        "points": 3,
        "question": "下列关于Km的叙述，哪一项是<strong>正确</strong>的？",
        "options": [
            "A. Km是ES复合物的解离常数",
            "B. Km与酶浓度有关",
            "C. Km是酶的特征常数，不同底物有不同的Km值",
            "D. Km越大表示酶与底物亲和力越大"
        ],
        "answer": "C",
        "explanation": "Km是酶的特征常数（与酶浓度无关）。同一酶对不同底物的Km不同。Km越小表示亲和力越大。Km一般不等于Kd（除非kcat << k-1时）。",
        "pitfall": "错误选A——Km = (k-1 + kcat)/k1，而Kd = k-1/k1，只有在kcat << k-1时Km才近似等于Kd。错误选B——Km与[E]无关。错误选D——Km越小亲和力越大。"
    },
    {
        "type": "single_choice",
        "points": 3,
        "question": "在Lineweaver-Burk双倒数作图中，竞争性抑制剂的动力学特征是？",
        "options": [
            "A. 直线交于Y轴同一点",
            "B. 直线交于X轴同一点",
            "C. 直线互相平行",
            "D. 直线交于原点"
        ],
        "answer": "A",
        "explanation": "竞争性抑制剂Vmax不变、Km增大。在双倒数图中，Y截距=1/Vmax不变→所有直线交于Y轴同一点。X截距=−1/Km随抑制剂浓度增大而向原点移动。",
        "pitfall": "错误选B——交于X轴同一点是非竞争性抑制的特征（Km不变）。错误选C——平行线是反竞争性抑制的特征。三种抑制的双倒数图判别是每年必考内容。"
    },
    {
        "type": "single_choice",
        "points": 3,
        "question": "磺胺类药物的抗菌机理是？",
        "options": [
            "A. 不可逆抑制细菌转肽酶",
            "B. 作为PABA的结构类似物，竞争性抑制二氢蝶酸合成酶",
            "C. 非竞争性抑制细菌DNA复制",
            "D. 反竞争性抑制细菌蛋白质合成"
        ],
        "answer": "B",
        "explanation": "磺胺是对氨基苯甲酸（PABA）的结构类似物，竞争性地抑制细菌的二氢蝶酸合成酶，阻断叶酸合成。这是竞争性抑制的经典临床范例。人类细胞不合成叶酸（从食物获取），因此磺胺对人有选择性毒性。",
        "pitfall": "错误选A——有机磷农药才是不可逆抑制丝氨酸蛋白酶（胆碱酯酶）。磺胺是可逆竞争性抑制剂。"
    },
    {
        "type": "single_choice",
        "points": 3,
        "question": "丝氨酸蛋白酶的催化三联体由哪三个残基组成？",
        "options": [
            "A. Ser-His-Asp",
            "B. Ser-His-Glu",
            "C. Cys-His-Asp",
            "D. Ser-Lys-Asp"
        ],
        "answer": "A",
        "explanation": "催化三联体为Ser195-His57-Asp102（胰凝乳蛋白酶编号）。Asp的-COO⁻定向His咪唑环→His从Ser接受质子→Ser-O⁻作为亲核试剂攻击底物羰基碳。",
        "pitfall": "错误选B——是Asp而非Glu。错误选C——Cys-His-Asp是某些半胱氨酸蛋白酶的催化三联体（如caspase），不要与丝氨酸蛋白酶混淆。"
    },
    {
        "type": "single_choice",
        "points": 3,
        "question": "别构酶通常表现出的v-[S]曲线形状是？",
        "options": [
            "A. 双曲线",
            "B. S形曲线",
            "C. 直线",
            "D. 指数曲线"
        ],
        "answer": "B",
        "explanation": "别构酶具有多亚基结构和正协同效应，v-[S]曲线呈S形（sigmoidal）。S形曲线在中间底物浓度范围形成敏感的'开关区域'，使代谢调控更精准。M-M酶则呈双曲线。",
        "pitfall": "错误选A——双曲线是M-M酶的特征（无协同效应）。S形曲线的生物学意义是常考的简答题。"
    },
    {
        "type": "single_choice",
        "points": 3,
        "question": "乳酸脱氢酶（LDH）同工酶中，主要分布在心肌的是？",
        "options": [
            "A. LDH₁ (H₄)",
            "B. LDH₃ (H₂M₂)",
            "C. LDH₅ (M₄)",
            "D. LDH₂ (H₃M)"
        ],
        "answer": "A",
        "explanation": "LDH₁(H₄)主要分布在心肌和红细胞。心肌是有氧组织，LDH₁对丙酮酸Km小且被高浓度丙酮酸抑制，偏好乳酸→丙酮酸的方向。心肌梗死时血清LDH₁>LDH₂是诊断指标之一。",
        "pitfall": "错误选C——LDH₅(M₄)主要分布在骨骼肌和肝脏。错误选D——LDH₂也分布在心肌，但LDH₁含量最多且是临床诊断的指标。"
    },
    {
        "type": "single_choice",
        "points": 3,
        "question": "下列哪种维生素的活性形式是辅酶A（CoA）？",
        "options": [
            "A. 维生素B₁",
            "B. 维生素B₂",
            "C. 维生素B₅（泛酸）",
            "D. 维生素B₆"
        ],
        "answer": "C",
        "explanation": "泛酸（维生素B₅）是CoA的前体。CoA的-SH与酰基形成高能硫酯键，是酰基转移反应的关键辅酶。B₁→TPP，B₂→FAD/FMN，B₆→PLP。",
        "pitfall": "维生素与辅酶的对应关系是填空题和选择题的高频考点，需要准确记忆。"
    },
    {
        "type": "single_choice",
        "points": 3,
        "question": "关于辅酶和辅基的区别，下列叙述正确的是？",
        "options": [
            "A. 辅酶是与酶蛋白共价结合的辅助因子",
            "B. 辅基可用透析法除去",
            "C. 辅酶与酶蛋白结合疏松，可用透析法除去",
            "D. 辅酶和辅基没有本质区别"
        ],
        "answer": "C",
        "explanation": "辅酶与酶蛋白以非共价键疏松结合，可通过透析除去（如NAD⁺）。辅基与酶蛋白结合紧密（共价或极强非共价），不可透析除去（如生物素、血红素）。",
        "pitfall": "错误选A——辅酶是非共价疏松结合，辅基才是共价或紧密非共价结合。错误选B——辅基结合牢固，透析无法除去。"
    },

    # ─── 判断题 (5题，每题2分，共10分) ───
    {
        "type": "true_false",
        "points": 2,
        "question": "酶只能加快反应速率，不能改变反应的平衡常数。",
        "answer": "正确",
        "explanation": "正确。酶通过降低活化能加速反应达到平衡的过程，但不改变反应的Keq和ΔG。这是酶的基本属性。",
        "pitfall": "这道题是正确的，不要因为题干看起来简单就怀疑自己。"
    },
    {
        "type": "true_false",
        "points": 2,
        "question": "在非竞争性抑制中，Km不变但Vmax减小。",
        "answer": "正确",
        "explanation": "正确。非竞争性抑制剂结合在活性中心外，不影响底物与酶的结合（Km不变），但结合了抑制剂的酶分子无法催化（Vmax减小）。",
        "pitfall": "注意区分：竞争性=Km↑Vmax不变；非竞争性=Km不变Vmax↓；反竞争性=Km↓Vmax↓。"
    },
    {
        "type": "true_false",
        "points": 2,
        "question": "Km是酶的特征常数，其值越大表示酶与底物的亲和力越大。",
        "answer": "错误",
        "explanation": "Km越大表示达到半饱和所需的底物浓度越高，即亲和力越小。Km与亲和力成反比关系。",
        "pitfall": "Km和亲和力的关系容易搞反——记住'小Km=大亲和力'（需要很少底物就能半饱和）。"
    },
    {
        "type": "true_false",
        "points": 2,
        "question": "酶原激活是一种可逆的共价修饰调节方式。",
        "answer": "错误",
        "explanation": "酶原激活是通过蛋白质部分水解切除特定肽段来实现的，是不可逆的过程。可逆的共价修饰是磷酸化/去磷酸化、乙酰化/去乙酰化等。",
        "pitfall": "酶原激活≠共价修饰调节。共价修饰调节（如磷酸化）是可逆的；酶原激活（如胰蛋白酶原→胰蛋白酶）是通过蛋白水解断裂，不可逆。"
    },
    {
        "type": "true_false",
        "points": 2,
        "question": "同工酶是由同一基因编码、经不同翻译后修饰产生的酶的不同形式。",
        "answer": "错误",
        "explanation": "同工酶由不同基因编码（如LDH的H亚基和M亚基分别由不同基因编码），具有不同的氨基酸序列。由同一基因经不同翻译后修饰产生的称为'酶的多种形式'，不是严格意义上的同工酶。",
        "pitfall": "同工酶的严格定义：不同基因编码+催化相同反应+不同理化性质。同一基因的翻译后修饰产物不是同工酶。"
    },

    # ─── 填空题 (6题，每空2分，共20分) ───
    {
        "type": "fill_blank",
        "points": 4,
        "question": "Michaelis-Menten方程的推导基于两个关键前提：(1) ____，即d[ES]/dt = 0；(2) ____条件，即[S] >> [E]且[P] ≈ 0。",
        "answer": ["稳态假设", "初始速度"],
        "explanation": "稳态假设（steady-state assumption）是M-M方程推导的核心——ES的形成速率等于分解速率。初始速度条件保证了只考虑正向反应，忽略逆反应和底物消耗。",
        "pitfall": "第一空不要写成'平衡假设'——平衡假设（d[ES]/dt=0仅考虑k1/k-1平衡）是稳态假设的特例（当kcat<<k-1时）。M-M推导用的是更一般的稳态假设。"
    },
    {
        "type": "fill_blank",
        "points": 4,
        "question": "在Lineweaver-Burk双倒数图中，Y轴截距等于____，X轴截距等于____。",
        "answer": ["1/Vmax", "-1/Km"],
        "explanation": "双倒数方程：1/v0 = (Km/Vmax)·(1/[S]) + 1/Vmax。当1/[S]=0时，Y=1/Vmax；当1/v0=0时，X=-1/Km。",
        "pitfall": "注意X截距是负值（-1/Km），不要忘记负号。"
    },
    {
        "type": "fill_blank",
        "points": 4,
        "question": "酶活力的国际单位（IU）定义为在特定条件下每分钟催化转化____ μmol底物所需的酶量。Katal（kat）定义为每秒催化转化____ mol底物。",
        "answer": ["1", "1"],
        "explanation": "1 IU = 每分钟转化1 μmol底物。1 kat = 每秒转化1 mol底物。换算关系：1 kat = 6×10⁷ IU。",
        "pitfall": "IU是μmol/min级别，kat是mol/s级别。注意单位换算，1 kat = 6×10⁷ IU。"
    },
    {
        "type": "fill_blank",
        "points": 4,
        "question": "丝氨酸蛋白酶催化肽键水解分两步：第一步是____阶段，形成酰基-酶中间体；第二步是____阶段，水分子亲核攻击释放产物。",
        "answer": ["酰化", "脱酰"],
        "explanation": "酰化阶段：Ser-O⁻攻击底物羰基→形成四面体过渡态→C端肽段离去→酰基-酶中间体。脱酰阶段：水分子被His活化→OH⁻攻击酰基-酶→释放N端肽段→酶恢复自由态。",
        "pitfall": "两个阶段顺序不要记反——先酰化（底物与酶共价连接），后脱酰（水解释放）。"
    },
    {
        "type": "fill_blank",
        "points": 2,
        "question": "碳酸酐酶的活性中心含有金属离子____，它通过Lewis酸效应降低配位水分子的pKa，使其在生理pH下产生高浓度OH⁻作为亲核试剂。",
        "answer": "Zn²⁺",
        "explanation": "Zn²⁺的Lewis酸效应将配位水的pKa从15.7降至~7，在生理条件下产生高浓度OH⁻。这是金属离子催化的经典范例。",
        "pitfall": "注意是Zn²⁺，不是Mg²⁺。Mg²⁺在激酶中常见（与ATP配位）。碳酸酐酶的Zn²⁺催化CO₂+H₂O↔HCO₃⁻+H⁺。"
    },
    {
        "type": "fill_blank",
        "points": 2,
        "question": "在乒乓机制（Ping-Pong机制）的双底物反应中，双倒数图呈现出____线的特征。",
        "answer": "平行",
        "explanation": "乒乓机制的双倒数图呈现平行线特征——这是由于第一个底物结合后先释放第一个产物，酶变为修饰形式，再与第二个底物反应。这与反竞争性抑制的双倒数图特征相同。",
        "pitfall": "乒乓机制的平行线≠反竞争性抑制的平行线——前者是多底物动力学，后者是单底物+抑制剂的动力学。虽然在双倒数图上都表现为平行线，但实验设计和解释完全不同。"
    },

    # ─── 简答题 (5题，共32分) ───
    {
        "type": "short_answer",
        "points": 8,
        "question": "请从双倒数图的特征、Km和Vmax的变化三个角度，对比竞争性抑制、非竞争性抑制和反竞争性抑制的动力学差异。",
        "answer": "【竞争性抑制】抑制剂与底物竞争活性中心。Km增大（表观亲和力下降），Vmax不变（高[S]可完全竞争赢抑制剂）。双倒数图：所有直线交于Y轴同一点（1/Vmax相同），X截距随[I]增大向原点移动。\n\n【非竞争性抑制】抑制剂结合在活性中心外，与E和ES均可结合。Km不变（不干扰底物结合），Vmax减小（部分酶分子永久失活）。双倒数图：所有直线交于X轴同一点（-1/Km相同），Y截距随[I]增大而增大。\n\n【反竞争性抑制】抑制剂仅与ES复合物结合。Km减小（ES被锁定使表观亲和力增大），Vmax减小。双倒数图：所有直线互相平行（斜率不变，Km和Vmax等比例减小）。",
        "explanation": "三种可逆抑制的动力学比较是考研的绝对必考点。评分关键：(1)准确描述每种抑制剂结合对象；(2)正确指出Km和Vmax变化方向；(3)准确描述双倒数图特征（交点位置）。三者缺一不可。",
        "pitfall": "容易混淆非竞争性和反竞争性：(1)非竞争性是结合E和ES，反竞争性仅结合ES；(2)非竞争性Km不变，反竞争性Km减小；(3)非竞争性交于X轴同一点，反竞争性是平行线。"
    },
    {
        "type": "short_answer",
        "points": 8,
        "question": "简述丝氨酸蛋白酶的催化三联体组成及催化机制（以胰凝乳蛋白酶为例）。",
        "answer": "【催化三联体组成】Ser195-His57-Asp102。Asp102的-COO⁻通过氢键定向His57的咪唑环→His57从Ser195的-OH接受质子→Ser195变为强亲核试剂Ser-O⁻。\n\n【催化机制——两步共价催化】\n(1) 酰化阶段：Ser195-O⁻亲核攻击底物肽键的羰基碳→形成四面体过渡态（氧负离子穴中Gly193和Ser195的主链NH稳定此过渡态）→C端肽段离去（His57给离去基团-NH提供质子）→形成酰基-酶中间体（Ser195的O与底物N端以酯键连接）。\n(2) 脱酰阶段：水分子进入活性中心→His57从水接受质子→OH⁻攻击酰基-酶中间体→第二次四面体过渡态→释放N端肽段→酶恢复自由态。\n\n【底物特异性】三种丝氨酸蛋白酶催化机制相同，但S1口袋结构不同决定了底物特异性：胰凝乳蛋白酶偏好Phe/Tyr/Trp（深疏水口袋），胰蛋白酶偏好Lys/Arg（底部有Asp189负电），弹性蛋白酶偏好Gly/Ala（入口被Val/Thr封闭）。",
        "explanation": "评分要点：①催化三联体每个残基的具体角色（不能只说名字）；②两步机制+酸-碱-共价催化的协同；③氧负离子穴的作用；④底物特异性的结构基础。",
        "pitfall": "常见失误：(1)把催化三联体写成Ser-His-Glu（是Asp不是Glu）；(2)忽略了氧负离子穴；(3)把两步顺序搞反（先酰化后脱酰）。"
    },
    {
        "type": "short_answer",
        "points": 6,
        "question": "什么是别构调节？别构酶的v-[S]曲线为什么呈S形？S形曲线有什么生理意义？",
        "answer": "【定义】别构调节是指效应物（激活剂或抑制剂）结合在酶活性中心以外的别构位点，通过引起酶构象变化来调控催化活性的方式。别构酶通常具有多亚基结构（四级结构）。\n\n【S形曲线原因】别构酶各亚基之间存在正协同效应（positive cooperativity）：第一个底物分子结合后，通过构象变化使相邻亚基对底物的亲和力增大→第二个底物更容易结合→第三个更易……这种协同效应使v-[S]曲线偏离M-M双曲线，呈现S形。\n\n【生理意义】S形曲线在中间底物浓度范围形成陡峭的'开关区域'——在此区域内底物浓度的微小变化即可引起反应速率的剧烈改变。这使酶能对代谢物浓度的细微波动做出灵敏响应，实现精准的代谢调控。相比之下，M-M酶的双曲线在生理底物浓度范围内更像'渐变调光器'，缺乏这种开关式调控能力。",
        "explanation": "评分要点：(1)别构调节的定义（别构位点≠活性中心）；(2)正协同效应导致S形曲线；(3)S形曲线的生理意义（灵敏度+开关效应）。",
        "pitfall": "别构酶必须是多亚基的（具有四级结构），单亚基酶不可能有别构效应。S形曲线不是所有多亚基酶都有——只有存在正协同效应时才呈S形。"
    },
    {
        "type": "short_answer",
        "points": 5,
        "question": "什么是同工酶？以乳酸脱氢酶（LDH）为例，说明同工酶的组成、组织分布差异及其生理意义。",
        "answer": "【定义】同工酶（isozyme）是指催化相同化学反应，但由不同基因编码、具有不同氨基酸序列和理化性质的酶。\n\n【LDH同工酶】LDH是由H亚基（心肌型）和M亚基（骨骼肌型）组成的四聚体，共5种：LDH₁(H₄)、LDH₂(H₃M)、LDH₃(H₂M₂)、LDH₄(HM₃)、LDH₅(M₄)。\n\n【组织分布差异】心肌中LDH₁(H₄)为主，对丙酮酸Km小（高亲和力）且被高浓度丙酮酸抑制→心肌是有氧组织，偏好乳酸→丙酮酸方向；骨骼肌中LDH₅(M₄)为主，对丙酮酸Km大且不被抑制→剧烈运动时大量丙酮酸可快速转化为乳酸。\n\n【临床意义】心肌梗死时血清LDH₁>LDH₂（正常是LDH₂>LDH₁）→可作为心梗诊断指标。肝脏疾病时LDH₅升高。",
        "explanation": "评分要点：(1)同工酶定义（不同基因编码+相同反应）；(2)LDH五种同工酶的亚基组成；(3)LDH₁和LDH₅的Km差异和生理意义；(4)临床诊断应用。",
        "pitfall": "LDH₁和LDH₅的Km对比是考点——LDH₁对丙酮酸Km小（高亲和力），LDH₅对丙酮酸Km大（低亲和力）。心梗时LDH₁释放入血导致LDH₁>LDH₂（翻转现象）。"
    },
    {
        "type": "short_answer",
        "points": 5,
        "question": "简述核酶（ribozyme）的发现及其生物学意义。",
        "answer": "【发现】1982年，Thomas Cech发现四膜虫rRNA前体在完全无蛋白质的条件下可以自我剪接，证明RNA具有催化功能。同年，Sidney Altman发现RNase P中的RNA组分是真正的催化剂。两人共享1989年诺贝尔化学奖。\n\n【生物学意义】\n(1) 打破了'酶=蛋白质'的传统教条，证明RNA也可以是生物催化剂。\n(2) 为'RNA世界'假说提供了关键实验证据——在生命起源早期，RNA可能同时承担遗传信息存储（类似DNA）和催化功能（类似蛋白质酶）。\n(3) 核糖体的肽酰转移酶中心完全由rRNA组成（最近的蛋白质在18Å外），说明蛋白质合成机器本质上也是核酶——生命的最后共同祖先（LUCA）的蛋白质合成可能由RNA完成。",
        "explanation": "评分要点：(1)发现者和年代（Cech 1982，诺贝尔奖1989）；(2)'酶不全是蛋白质'的概念突破；(3)RNA世界假说的意义。",
        "pitfall": "不要把Cech和Altman搞混——Cech发现的是自我剪接rRNA（I类内含子），Altman发现的是RNase P的RNA催化组分。两人并列获奖。"
    },

    # ─── 综合题 (1题，8分) ───
    {
        "type": "short_answer",
        "points": 8,
        "question": "【综合分析题】某研究生用一种新合成的化合物X进行酶抑制实验，得到以下数据：不含抑制剂时Km=2.0×10⁻⁵ M，Vmax=100 μmol/min；含抑制剂X时Km=2.0×10⁻⁵ M，Vmax=50 μmol/min。请判断：(1)化合物X属于哪种类型的可逆抑制剂？(2)在Lineweaver-Burk双倒数图上，有抑制剂和无抑制剂时的两条直线有何特征关系？(3)如果增加底物浓度到原来的10倍，能否完全恢复酶活？为什么？",
        "answer": "(1) 非竞争性抑制剂。判断依据：加入抑制剂后Km不变（仍为2.0×10⁻⁵ M），Vmax从100降至50 μmol/min——符合非竞争性抑制的动力学特征（Km不变，Vmax减小）。\n\n(2) 在双倒数图上，两条直线交于X轴同一点（-1/Km）。因为Km不变，X截距相同；而Vmax不同，Y截距（1/Vmax）不同：无抑制剂时Y截距=0.01，有抑制剂时Y截距=0.02。\n\n(3) 不能完全恢复。因为非竞争性抑制剂结合在活性中心外的位点，与E和ES均可结合——抑制剂的存在会使一部分酶分子永久性地失活（即使所有剩余酶分子被底物饱和，Vmax也只能达到无抑制剂时的50%）。增加底物浓度只能使不被抑制的酶分子饱和，但无法'挤走'已经结合在别构位点的抑制剂。",
        "explanation": "这是一道典型的实验数据分析题，考察从数据逆推抑制类型的能力。核心判断依据：(1)Km不变→排除竞争性(Km↑)和反竞争性(Km↓)；(2)Vmax减小→确定为非竞争性抑制。",
        "pitfall": "容易混淆：(1)看到Vmax减小就以为是反竞争性——但反竞争性Km也减小；(2)认为增加底物浓度可以恢复酶活——只有竞争性抑制才能被高底物浓度逆转。"
    },
]

# Save test HTML
save_test(questions,
          '/workspace/output/生物化学_第10-13章_自测题.html',
          '生物化学 第10-13章 酶学 — 自测题',
          subtitle="满分 100 分 | 建议 60 分钟 | 含单选10题30分 + 判断5题10分 + 填空6题20分 + 简答5题32分 + 综合8分",
          duration_minutes=60)

print("✅ 第10-13章自测题已生成")
print("\n全部完成！输出文件：")
print("  /workspace/output/生物化学_第10-13章_知识精讲.html")
print("  /workspace/output/生物化学_第10-13章_自测题.html")