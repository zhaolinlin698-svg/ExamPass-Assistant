#!/usr/bin/env python3
"""Generate Part 1 continuation (Ch10-18)."""

import sys
sys.path.insert(0, '/workspace/ExamPass-Assistant')
from scripts.template_engine import save_knowledge_html

body = r"""

<h2>第10章 酶动力学：酶有多快、多强？</h2>

<h3>10.1 Michaelis-Menten方程 <span class="tag-must">必考</span></h3>

<p><strong>核心问题</strong>：酶促反应速率如何随底物浓度变化？这为什么是双曲线？</p>

<p><span class="kp">Michaelis-Menten方程</span>：$$v_0 = \frac{V_{\max}[S]}{K_m + [S]}$$</p>

<p><span class="exp">其中v₀为初始反应速率，Vmax为最大反应速率（所有酶分子被底物饱和时的速率），[S]为底物浓度，Km为米氏常数——使v₀=Vmax/2时的底物浓度。</span></p>

<p><strong>推导——稳态假设</strong>：M-M方程的推导基于以下关键假设：</p>
<ol>
<li><span class="kp">稳态假设</span><span class="exp">：酶-底物复合物[ES]的浓度在初始阶段保持恒定（d[ES]/dt=0）——这意味着ES的形成速率等于其分解速率。</span></li>
<li><span class="kp">初始速度条件</span><span class="exp">：测量v₀时，[S] &gt;&gt; [E]，且[S]几乎不变，[P]≈0（逆反应可忽略）。</span></li>
<li>反应模型：E + S ⇌ ES → E + P（k₁和k₋₁为结合/解离速率常数，kcat为催化常数）</li>
</ol>

<p>推导过程：稳态时 k₁[E][S] = (k₋₁ + kcat)[ES]，代入[E]_{total} = [E] + [ES]，整理得：</p>

$$K_m = \frac{k_{-1} + k_{\mathrm{cat}}}{k_1}$$
$$v_0 = \frac{k_{\mathrm{cat}}[E]_{\mathrm{total}}[S]}{K_m + [S]}$$

<h3>10.2 Km、Vmax和kcat的物理意义 <span class="tag-must">必考</span></h3>

<table>
<tr><th>参数</th><th>定义</th><th>物理意义</th></tr>
<tr><td><span class="kp">K_m</span></td><td>(k₋₁ + kcat)/k₁</td><td>底物与酶的亲和力度量——Km越小，亲和力越大（需要更低浓度就能达到半饱和）。当kcat&lt;&lt;k₋₁时，Km≈k₋₁/k₁=Kd（解离常数），此时Km直接反映亲和力</td></tr>
<tr><td><span class="kp">V_{\max}</span></td><td>kcat[E]total</td><td>底物饱和时的最大速率——酶越多、或每个酶分子越快，Vmax越大</td></tr>
<tr><td><span class="kp">k_{\mathrm{cat}}</span></td><td>催化常数/转换数</td><td>每个酶分子在饱和条件下每秒转化的底物分子数。kcat=Vmax/[E]total。单位s⁻¹</td></tr>
<tr><td><span class="kp">k_{\mathrm{cat}}/K_m</span></td><td>催化效率/专一性常数</td><td>综合衡量酶的催化效率——不仅考虑催化速度，还考虑底物结合能力。上限受扩散控制（~10⁸-10⁹ M⁻¹s⁻¹）</td></tr>
</table>

<blockquote>易错：(1) Km不是ES的解离常数Kd，除非kcat远小于k₋₁；一般来说Km≥Kd；(2) Km是酶的特征常数，与酶浓度[E]无关，但Vmax随[E]线性变化；(3) 同一酶对不同底物的Km不同——Km最小的底物不一定是生理底物，但常被称为「最适底物」。</blockquote>

<h3>10.3 Lineweaver-Burk双倒数作图 <span class="tag-key">重点</span></h3>

<p><span class="kp">双倒数方程</span>：$$\frac{1}{v_0} = \left(\frac{K_m}{V_{\max}}\right) \cdot \frac{1}{[S]} + \frac{1}{V_{\max}}$$</p>

<p><span class="exp">以1/v₀为Y轴、1/[S]为X轴做图，得到一条直线：(1) Y截距=1/Vmax；(2) X截距=-1/Km；(3) 斜率=Km/Vmax。</span></p>

<p><strong>为什么常用双倒数图？</strong>虽然M-M曲线本身就可以拟合出Km和Vmax，但双倒数直线更容易肉眼判断抑制剂类型：(1) 竞争性抑制——Vmax不变、Km增大（交于Y轴同一点）；(2) 非竞争性抑制——Vmax减小、Km不变（交于X轴同一点）；(3) 反竞争性抑制——Vmax和Km等比例减小（平行线）。</p>

<h3>10.4 酶抑制剂 <span class="tag-must">必考</span></h3>

<table>
<tr><th>抑制类型</th><th>结合位点</th><th>Km变化</th><th>Vmax变化</th><th>双倒数图特征</th></tr>
<tr><td><span class="kp">竞争性</span></td><td>活性中心（与S竞争）</td><td>↑（表观增大）</td><td>不变</td><td>交于Y轴同一点</td></tr>
<tr><td><span class="kp">非竞争性</span></td><td>活性中心外（ES均可结合）</td><td>不变</td><td>↓</td><td>交于X轴同一点</td></tr>
<tr><td><span class="kp">反竞争性</span></td><td>只结合ES（不跟游离E结合）</td><td>↓</td><td>↓</td><td>平行线</td></tr>
</table>

<p><strong>临床实例</strong>：</p>
<ul>
<li><span class="kp">甲氨蝶呤（methotrexate）</span><span class="exp">——叶酸的结构类似物，竞争性抑制二氢叶酸还原酶(DHFR)，阻断核苷酸合成，用于抗癌。</span></li>
<li><span class="kp">青霉素</span><span class="exp">——不可逆抑制细菌转肽酶（共价结合活性中心Ser），阻断细胞壁合成。注意：青霉素是自杀性抑制剂（mechanism-based inhibitor），不同于可逆竞争性抑制剂。</span></li>
<li><span class="kp">别嘌呤醇</span><span class="exp">——黄嘌呤氧化酶的自杀性底物，用于治疗痛风（降低尿酸产生）。</span></li>
</ul>

<blockquote>易错：(1) 竞争性抑制剂不改变Vmax是因为提高[S]可以「竞争赢」抑制剂——当[S]→∞时所有酶仍可被底物饱和；(2) 非竞争性抑制剂改变Vmax是因为即使[S]→∞，一部分酶因结合了抑制剂而不能催化——相当于「坏掉的」酶分子；(3) 不可逆抑制剂≠竞争性抑制剂，前者与酶共价结合永久失活。</blockquote>

<h2>第11章 酶的催化机制：有机化学的巅峰艺术</h2>

<h3>11.1 丝氨酸蛋白酶 <span class="tag-must">必考</span></h3>

<p><strong>核心问题</strong>：一个简单的蛋白水解反应，酶如何实现如此高的速率提升？</p>

<p><span class="kp">丝氨酸蛋白酶家族</span><span class="exp">（胰蛋白酶、胰凝乳蛋白酶、弹性蛋白酶）共享相同的催化三联体（Ser-His-Asp）和两步共价催化机制，但底物特异性不同。</span></p>

<p><strong>催化三联体的协同作用——电荷中继网络</strong>：</p>
<ul>
<li><span class="kp">Asp¹⁰²</span><span class="exp">的-COO⁻通过氢键定向His⁵⁷的咪唑环（提高其pKa，使其成为更好的碱）</span></li>
<li><span class="kp">His⁵⁷</span><span class="exp">的咪唑基作为一般酸碱催化剂：在第一步中作为碱从Ser¹⁹⁵的-OH接受一个质子，在第二步中作为酸给离去基团提供质子</span></li>
<li><span class="kp">Ser¹⁹⁵</span><span class="exp">的-OH在His⁵⁷的帮助下变为更强的亲核试剂（醇盐离子，Ser-O⁻），攻击底物的羰基碳</span></li>
</ul>

<p><strong>反应机制（两步共价催化）</strong>：</p>
<ol>
<li><span class="kp">酰化阶段</span><span class="exp">：Ser¹⁹⁵-O⁻亲核攻击底物肽键的羰基碳→形成四面体过渡态（氧负离子穴oxyanion hole中的Gly和Ser的主链NH稳定此过渡态）→羰基碳重新sp²杂化→C端肽段离去（His⁵⁷给离去基团-NH提供质子）→形成酰基-酶中间体（Ser¹⁹⁵的O与底物N端部分以酯键相连）</span></li>
<li><span class="kp">脱酰阶段</span><span class="exp">：水分子进入活性中心→His⁵⁷从水接受质子→产生的OH⁻攻击酰基-酶中间体→第二次四面体过渡态→释放N端肽段→酶恢复自由状态</span></li>
</ol>

<p><strong>三种丝氨酸蛋白酶的底物特异性差异</strong>：</p>
<ul>
<li><span class="kp">胰凝乳蛋白酶</span><span class="exp">——S1口袋深而疏水（含Ser¹⁸⁹），偏好Phe/Tyr/Trp等大疏水残基的C端肽键</span></li>
<li><span class="kp">胰蛋白酶</span><span class="exp">——S1口袋底部有Asp¹⁸⁹（带负电），偏好Lys/Arg等碱性残基的C端肽键（静电吸引）</span></li>
<li><span class="kp">弹性蛋白酶</span><span class="exp">——S1口袋入口被Val²¹⁶和Thr²²⁶封闭，只能容纳Gly/Ala等小残基</span></li>
</ul>

<p><strong>Deep insight</strong>：三种酶共享相同的折叠骨架和催化机制（趋异进化），通过简单地「装修」底物结合口袋（换几个残基）就实现了底物特异性的分化——这是蛋白质工程学中最优雅的设计范例。</p>

<h3>11.2 溶菌酶与过渡态稳定化 <span class="tag-key">重点</span></h3>

<p><span class="kp">溶菌酶（lysozyme）</span><span class="exp">是第一个被阐明了三维结构和催化机制的酶（Phillips, 1965）。它催化细菌细胞壁的肽聚糖中NAM-NAG间的β-1,4-糖苷键水解。</span></p>

<p><strong>核心机制</strong>：</p>
<ul>
<li><span class="kp">Glu³⁵（pKa≈6.5，非寻常高）</span><span class="exp">作为一般酸催化剂，提供质子给糖苷键的O</span></li>
<li><span class="kp">Asp⁵²（pKa≈3.5）</span><span class="exp">作为亲核基团/静电稳定剂，稳定底物的正电荷中间体（碳正离子过渡态）</span></li>
<li>底物的D糖环被扭曲成半椅式构象——这恰好降低过渡态的能量（酶「掰弯」底物使其更像过渡态）</li>
</ul>

<p><strong>Deep principle——过渡态稳定化</strong>：酶最稳定结合的是反应的过渡态，不是底物也不是产物。如果酶与底物结合得太紧（底物的几何形状完美契合活性中心），那么底物→过渡态的变形需要额外能量，活化能反而升高。因此，好酶的活性中心不完全匹配底物，而是完美匹配过渡态的几何形状和电荷分布。</p>

<h3>11.3 其他重要催化机制范例 <span class="tag-freq">高频</span></h3>

<ul>
<li><span class="kp">碳酸酐酶</span><span class="exp">——Zn²⁺配位的水分子pKa从15.7降至~7（Zn²⁺的Lewis酸效应），使H₂O→OH⁻成为极强的亲核试剂。催化效率kcat/Km≈10⁸ M⁻¹s⁻¹，接近扩散控制极限。</span></li>
<li><span class="kp">限制性内切酶EcoRV</span><span class="exp">——通过Mg²⁺介导的催化，精确识别GATATC序列。非特异序列结合时不催化（Mg²⁺不在正确位置），带来极高的序列选择性。</span></li>
</ul>

<h2>第12章 核酶：RNA也能当酶？</h2>

<h3>12.1 核酶的发现与意义 <span class="tag-must">必考</span></h3>

<p><strong>颠覆性发现</strong>：1982年，Cech发现四膜虫rRNA前体可以在完全无蛋白质的情况下自我剪接（self-splicing），证明RNA具有催化功能。1989年获诺贝尔化学奖。Altman发现RNase P中的RNA组分是催化的真正执行者。</p>

<p><strong>为什么这是革命性的？</strong>在核酶发现之前，「酶==蛋白质」是生物化学的教条。核酶的发现打破了这一教条，同时也为「RNA世界」假说提供了关键证据——在DNA和蛋白质出现之前，RNA可能同时承担遗传信息存储（类似DNA）和催化（类似蛋白质酶）双重功能。</p>

<h3>12.2 核酶的类型与机制 <span class="tag-key">重点</span></h3>

<table>
<tr><th>核酶类型</th><th>来源</th><th>催化反应</th><th>机制关键点</th></tr>
<tr><td><span class="kp">I类内含子</span></td><td>四膜虫rRNA等</td><td>自我剪接（两步转酯反应）</td><td>外源G的3'-OH作亲核攻击</td></tr>
<tr><td><span class="kp">II类内含子</span></td><td>线粒体/叶绿体</td><td>自我剪接</td><td>内部A的2'-OH作亲核，形成套索</td></tr>
<tr><td><span class="kp">RNase P</span></td><td>所有生物</td><td>tRNA 5'端加工</td><td>RNA是催化亚基，蛋白辅助</td></tr>
<tr><td><span class="kp">锤头状核酶</span></td><td>植物类病毒</td><td>RNA链特异性切割</td><td>Mg²⁺辅助的一般酸碱催化</td></tr>
<tr><td><span class="kp">核糖体</span></td><td>所有生物</td><td>肽键形成（肽酰转移）</td><td>23S/28S rRNA是催化剂，蛋白只是支架</td></tr>
</table>

<p><strong>Deep insight——核糖体是核酶</strong>：这个发现极其重要。肽酰转移酶中心完全由rRNA组成，最近的蛋白在18Å外——蛋白质只提供结构框架。这意味着生命的最后共同祖先(LUCA)的蛋白质合成机器可能完全是RNA组成的，蛋白质后来才接管了大多数催化功能，因为20种氨基酸侧链比4种碱基提供了更丰富的化学功能。</p>

<blockquote>易错：(1) 并非所有内含子都是核酶——mRNA内含子（剪接体催化）和tRNA内含子需要蛋白质酶；(2) 核酶不一定完全是RNA——RNase P的RNA组分和蛋白质组分协同工作；(3) 肽键形成由rRNA催化≠核糖体是纯RNA机器——核糖体蛋白（r-proteins）对结构维持、组装和辅助功能仍然重要。</blockquote>

<h2>第13章 酶活性的调节</h2>

<h3>13.1 别构调控 <span class="tag-must">必考</span></h3>

<p><span class="kp">别构酶（allosteric enzyme）</span><span class="exp">是代谢调控的核心——调节物结合在活性中心以外的别构位点，通过构象变化影响催化活性。大多数别构酶位于代谢途径的关键调控节点（如糖酵解中的PFK-1）。</span></p>

<p><strong>别构调控的v vs [S]曲线</strong>：别构酶通常表现为S形曲线（而非M-M双曲线），这反映了正协同效应。S形曲线在中间[S]范围产生一个「开关式」的敏感区域——在此区域内，[S]的微小变化即可引起反应速率的大幅变化，赋予代谢精准的调控响应。</p>

<p><span class="kp">关键别构酶范例——ATCase（天冬氨酸转氨甲酰酶）</span>：</p>
<ul>
<li>催化嘧啶核苷酸生物合成的第一步（氨甲酰磷酸+天冬氨酸→N-氨甲酰天冬氨酸）</li>
<li><span class="kp">别构抑制剂 CTP</span><span class="exp">（嘧啶核苷酸的终产物）——反馈抑制。CTP结合后T/R平衡移向T态</span></li>
<li><span class="kp">别构激活剂 ATP</span><span class="exp">（嘌呤核苷酸）——嘌呤和嘧啶的合成需要平衡协调，高ATP信号激活嘧啶合成</span></li>
<li>结构：催化亚基6个（两个三聚体）+ 调节亚基6个（三个二聚体），T↔R转变涉及催化亚基间的相对旋转</li>
</ul>

<blockquote>易错：(1) 别构调控与M-M酶的区别在于别构酶具有四级结构（多亚基）且v-[S]曲线为S形；(2) 别构激活剂≠竞争性活化——它不在活性中心，而是改变T/R平衡；(3) 反馈抑制是最常见的别构调控模式——代谢途径的终产物抑制该途径的第一个关键酶。</blockquote>

<h3>13.2 共价修饰调控 <span class="tag-must">必考</span></h3>

<table>
<tr><th>修饰类型</th><th>关键酶</th><th>效果</th><th>可逆性</th></tr>
<tr><td><span class="kp">磷酸化/去磷酸化</span></td><td>蛋白激酶/蛋白磷酸酶</td><td>激活或抑制（取决于靶蛋白）</td><td>完全可逆</td></tr>
<tr><td><span class="kp">乙酰化/去乙酰化</span></td><td>HAT/HDAC</td><td>组蛋白：染色质松→转录激活</td><td>完全可逆</td></tr>
<tr><td><span class="kp">泛素化</span></td><td>E1-E2-E3级联</td><td>靶向蛋白酶体降解（K48链）</td><td>去泛素化酶可逆转</td></tr>
<tr><td><span class="kp">ADP-核糖基化</span></td><td>细菌毒素等</td><td>修饰Gs蛋白→腺苷酸环化酶持续激活</td><td>取决于具体酶</td></tr>
</table>

<p><strong>磷酸化/去磷酸化——酶调控的「开关」</strong>：蛋白质磷酸化是翻译后修饰中最普遍、最重要的调控方式。Ser/Thr/Tyr的-OH被ATP磷酸化→引入带负电的大基团→改变局部电荷和构象→改变蛋白活性。蛋白激酶(PK)和蛋白磷酸酶(PP)的可逆平衡决定了磷酸化水平。人类基因组编码~500种蛋白激酶（激酶组kinome），反映了磷酸化调控在信号转导中的核心地位。</p>

<p><span class="kp">酶原激活——不可逆的调控方式</span>：</p>
<ul>
<li><span class="kp">胰蛋白酶原→胰蛋白酶</span><span class="exp">：肠激酶切除N端六肽→构象重排→活性中心形成。这是消化酶的安全机制——在胰腺中合成的是无活性的酶原，到达肠道后才被激活。</span></li>
<li><span class="kp">凝血级联</span><span class="exp">：凝血因子以酶原形式在血液中循环，血管损伤时按级联顺序逐一激活。级联反应通过酶激活酶的方式产生巨大的放大效应——一个分子激活成千上万个下游分子。</span></li>
</ul>

<blockquote>易错：(1) 酶原激活不同于别构调控——它是不可逆的（或需要特定抑制剂）；(2) 磷酸化不总是激活——酪氨酸羟化酶的磷酸化激活，而糖原合酶的磷酸化则抑制；(3) 级联放大是信号转导的核心原理——一个上游信号分子可以激活多个下游效应器，产生信号放大。</blockquote>

<h3>13.3 同工酶 <span class="tag-freq">高频</span></h3>

<p><span class="kp">同工酶（isozyme）</span><span class="exp">：催化相同反应但具有不同氨基酸序列、Km值、调控特性的酶。典型例子——乳酸脱氢酶LDH₁（H₄，心肌型）和LDH₅（M₄，骨骼肌型）。</span></p>

<p><strong>LDH同工酶的生理意义</strong>：LDH催化丙酮酸↔乳酸。心肌中LDH₁对底物丙酮酸的Km小且被高浓度丙酮酸抑制——心肌是有氧组织，不希望浪费葡萄糖在无氧酵解，反而希望乳酸→丙酮酸用于氧化。骨骼肌中LDH₅对丙酮酸Km大且不被高浓度抑制——骨骼肌在剧烈运动时大量产生丙酮酸需要快速转为乳酸。同一反应，不同组织用不同同工酶精细调控——进化的精妙。</p>

<h2>第14章 维生素与辅酶</h2>

<h3>14.1 水溶性维生素与辅酶 <span class="tag-must">必考</span></h3>

<table>
<tr><th>维生素</th><th>活性形式（辅酶）</th><th>催化的反应类型</th><th>关键机制</th></tr>
<tr><td><span class="kp">B₁（硫胺素）</span></td><td>TPP</td><td>α-酮酸脱羧、转酮醇反应</td><td>噻唑环C2的碳负离子</td></tr>
<tr><td><span class="kp">B₂（核黄素）</span></td><td>FAD / FMN</td><td>氧化还原（1e⁻或2e⁻转移）</td><td>异咯嗪环接受H⁺+e⁻</td></tr>
<tr><td><span class="kp">B₃（烟酸）</span></td><td>NAD⁺ / NADP⁺</td><td>氧化还原（H⁻转移）</td><td>烟酰胺环接受H⁻</td></tr>
<tr><td><span class="kp">B₅（泛酸）</span></td><td>CoA</td><td>酰基转移</td><td>-SH与酰基形成硫酯键</td></tr>
<tr><td><span class="kp">B₆（吡哆醇）</span></td><td>PLP</td><td>氨基转移、脱羧、消旋</td><td>PLP与α-NH₂形成Schiff碱</td></tr>
<tr><td><span class="kp">B₇（生物素）</span></td><td>生物素</td><td>羧基转移（CO₂固定）</td><td>通过酰胺键与Lys连接（生物素化）</td></tr>
<tr><td><span class="kp">B₉（叶酸）</span></td><td>THF</td><td>一碳单位转移</td><td>N⁵、N¹⁰位携带甲基/甲烯基/甲酰基</td></tr>
<tr><td><span class="kp">B₁₂（钴胺素）</span></td><td>甲基钴胺素/腺苷钴胺素</td><td>重排（甲基丙二酰CoA→琥珀酰CoA）、甲基转移</td><td>Co-C键均裂产生自由基</td></tr>
</table>

<p><strong>Deep principle——为什么进化选择这些辅酶？</strong>20种氨基酸侧链虽然丰富，但缺乏某些关键催化能力：稳定碳负离子（TPP的噻唑环）、进行单电子氧化还原（FAD/FMN的异咯嗪环）、转移酰基（CoA的-SH形成高能硫酯）、一碳单位迁移（THF的N⁵,N¹⁰位）。辅酶弥补了氨基酸化学功能的不足——它们是从RNA世界中「继承」来的古老催化工具。</p>

<h3>14.2 PLP——生化反应的万能催化剂 <span class="tag-must">必考</span></h3>

<p><span class="kp">磷酸吡哆醛（PLP）</span><span class="exp">是B₆的活性形式，催化几乎所有涉及α-氨基酸的转化反应：转氨基、脱羧、消旋、α,β-消除、β,γ-消除等。</span></p>

<p><strong>PLP催化的统一机制——电子下沉（electron sink）</strong>：PLP的醛基与氨基酸的α-NH₂形成Schiff碱（亚胺），随后吡啶环作为「电子下沉」稳定各种转化中间体的负电荷。具体反应路径取决于从Cα上断裂哪个键——这由酶活性中心的特定残基定向决定：</p>
<ul>
<li>断裂Cα-H + Cα-COOH → 脱羧反应</li>
<li>断裂Cα-H + Cα-R → 转氨反应（变为酮酸+PLP→PMP）</li>
<li>断裂Cα-N → 消旋</li>
</ul>

<p><strong>直觉类比</strong>：PLP就像一把瑞士军刀——它的化学机制是统一的（形成Schiff碱→电子引流→断裂选定的键），但不同的酶（转氨酶、脱羧酶、消旋酶）通过控制哪个键被稳定/活化来决定「用这把刀的哪个功能」。</p>

<h3>14.3 脂溶性维生素简介 <span class="tag-freq">高频</span></h3>

<table>
<tr><th>维生素</th><th>活性形式</th><th>主要功能</th><th>缺乏症</th></tr>
<tr><td><span class="kp">A（视黄醇）</span></td><td>视黄醛、视黄酸</td><td>视觉（视紫红质）、基因转录调控</td><td>夜盲症、干眼症</td></tr>
<tr><td><span class="kp">D（钙化醇）</span></td><td>1,25-(OH)₂-D₃</td><td>钙磷代谢（类固醇激素）</td><td>佝偻病（儿童）、骨软化（成人）</td></tr>
<tr><td><span class="kp">E（生育酚）</span></td><td>α-生育酚</td><td>抗氧化（保护膜脂不饱和脂肪酸）</td><td>神经病变（罕见）</td></tr>
<tr><td><span class="kp">K（叶绿醌）</span></td><td>维生素K</td><td>γ-羧基化（凝血因子II,VII,IX,X的Gla修饰）</td><td>出血倾向</td></tr>
</table>

<h2>第16章 糖类：能量的第一来源</h2>

<h3>16.1 单糖的结构 <span class="tag-must">必考</span></h3>

<p><span class="kp">糖类的化学通式</span><span class="exp">：(CH₂O)n。最简单的是三碳糖（甘油醛和二羟丙酮），生物化学中最重要的是六碳糖（葡萄糖、果糖、半乳糖）和五碳糖（核糖、脱氧核糖）。</span></p>

<p><span class="kp">葡萄糖的结构关键点</span>：</p>
<ul>
<li>D-葡萄糖是六碳醛糖（aldohexose），天然氨基酸为L型，天然糖为D型——又是一个进化巧合</li>
<li>溶液中99%为环状半缩醛形式：C₁醛基与C₅-OH反应形成六元吡喃环，产生两个异头体α和β</li>
<li><span class="kp">变旋现象（mutarotation）</span><span class="exp">：纯α-D-葡萄糖([α]=+112°)溶于水后旋光度随时间变化，最终稳定在+52.7°，此时达到α (~36%)和β (~64%)的平衡混合物</span></li>
</ul>

<p><span class="kp">异头碳（anomeric carbon）</span><span class="exp">：单糖环化后产生的新手性中心。α型：异头碳的-OH与环平面另一侧（与决定D/L的末端CH₂OH反方向）的参考碳异侧；β型：同侧。</span></p>

<blockquote>易错：(1) D/L和α/β是两个不同的概念——D/L描述的是离醛基最远的手性碳（C₅），α/β描述的是异头碳（C₁）；(2) 溶液中开链形式极少（~0.02%），但就是这极少部分参与了还原反应（Fehling试剂检测还原糖就是基于开链醛基）。</blockquote>

<h3>16.2 重要的二糖和多糖 <span class="tag-key">重点</span></h3>

<table>
<tr><th>糖</th><th>组成</th><th>连接键</th><th>功能/特征</th></tr>
<tr><td><span class="kp">蔗糖</span></td><td>Glc (α1↔2β) Fru</td><td>α,β-1,2-糖苷键</td><td>非还原糖（两个异头碳都参与成键）</td></tr>
<tr><td><span class="kp">乳糖</span></td><td>Gal (β1→4) Glc</td><td>β-1,4-糖苷键</td><td>还原糖（Glc的异头碳游离）</td></tr>
<tr><td><span class="kp">麦芽糖</span></td><td>Glc (α1→4) Glc</td><td>α-1,4-糖苷键</td><td>淀粉水解产物</td></tr>
<tr><td><span class="kp">淀粉（直链）</span></td><td>Glc聚合物</td><td>α-1,4-糖苷键</td><td>植物储能，螺旋结构（每圈6个Glc）</td></tr>
<tr><td><span class="kp">淀粉（支链）</span></td><td>Glc聚合物</td><td>α-1,4 + α-1,6（分支）</td><td>分支点每24-30残基</td></tr>
<tr><td><span class="kp">糖原</span></td><td>Glc聚合物</td><td>α-1,4 + α-1,6（更频繁分支）</td><td>动物储能，分支点每8-12残基</td></tr>
<tr><td><span class="kp">纤维素</span></td><td>Glc聚合物</td><td>β-1,4-糖苷键</td><td>植物细胞壁，直线排列形成微纤维</td></tr>
</table>

<p><strong>Deep insight——α vs β糖苷键的「小差异，大后果」</strong>：淀粉(α-1,4)和纤维素(β-1,4)仅差一个异头构型，但结构天壤之别：(1) α糖苷键使链弯曲成螺旋——适合作为可溶性储能分子（易被淀粉酶水解）；(2) β糖苷键使链呈直线——相邻链间形成大量氢键构成不溶性纤维——适合结构支撑。人类能消化淀粉但消化不了纤维素，正是因为α-淀粉酶只识别α糖苷键。</p>

<h2>第17章 脂质：不仅仅是脂肪</h2>

<h3>17.1 脂肪酸 <span class="tag-must">必考</span></h3>

<p><span class="kp">脂肪酸</span><span class="exp">是长链羧酸（通常C12-C24），分饱和（无双键）和不饱和（含1个或多个双键）。自然界中的双键几乎全是顺式（cis），顺式双键在烃链中引入约30°的拐角，影响膜的流动性和堆积。</span></p>

<p><strong>脂肪酸的系统命名与简写</strong>：</p>
<ul>
<li>棕榈酸（16:0）——C16饱和脂肪酸</li>
<li>油酸（18:1 Δ⁹或ω-9）——C18单不饱和，双键在C9-C10</li>
<li>亚油酸（18:2 Δ⁹,¹²或ω-6）——C18双不饱和（必需脂肪酸，人体不能合成）</li>
<li>α-亚麻酸（18:3 Δ⁹,¹²,¹⁵或ω-3）——C18三不饱和（也是必需脂肪酸）</li>
</ul>

<p><span class="kp">ω命名法</span><span class="exp">：从甲基端（ω端，离羧基最远）开始编号。ω-3指最后一个双键在距甲基端第3个碳处。人类不能合成ω-3和ω-6必需脂肪酸，因为无法在脂肪酸链的ω-3和ω-6位置引入双键。</span></p>

<h3>17.2 三酰甘油（脂肪）<span class="tag-key">重点</span></h3>

<p><span class="kp">三酰甘油（TAG）</span><span class="exp">：甘油骨架上酯化三个脂肪酸。是生物体最浓缩的储能形式（完全氧化释放~38 kJ/g，而糖类仅~17 kJ/g）。原因是脂肪酸的碳骨架比糖更还原（高比例C-H键），氧化时释放更多能量。</span></p>

<p><strong>脂肪在脂肪细胞中以脂滴形式储存</strong>：几乎无水的油性核心，这极大降低了储存体积（1g脂肪仅占1.2mL，而1g糖原需3-4mL因为高度水化）。</p>

<h3>17.3 膜脂 <span class="tag-must">必考</span></h3>

<table>
<tr><th>类型</th><th>结构</th><th>分布/功能</th></tr>
<tr><td><span class="kp">磷脂（甘油磷脂）</span></td><td>甘油-2-PO₄⁻-X + 两个FA</td><td>膜主要成分（PC, PE, PS, PI等）。两亲性——疏水尾+亲水头</td></tr>
<tr><td><span class="kp">鞘脂</span></td><td>鞘氨醇骨架 + 一个FA + 极性头</td><td>神经髓鞘、信号转导（神经酰胺→鞘磷脂→神经节苷脂）</td></tr>
<tr><td><span class="kp">胆固醇</span></td><td>四环甾核 + 羟基 + 短烃链</td><td>动物细胞膜（调节流动性）、类固醇激素前体</td></tr>
</table>

<p><strong>膜的流动镶嵌模型（Singer-Nicolson, 1972）</strong>：磷脂双分子层是膜的「溶剂」，蛋白质漂浮其中或镶嵌其上。膜是流动的二维液体——磷脂可以在同一单层内横向扩散，但几乎不会翻转（flip-flop，需要翻转酶）。胆固醇在膜中「缓冲」流动性——高温时限制磷脂运动（降低流动性），低温时阻止磷脂紧密堆积（提高流动性）。</p>

<h2>第18章 激素</h2>

<h3>18.1 激素的分类与信号机制 <span class="tag-key">重点</span></h3>

<table>
<tr><th>分类</th><th>化学本质</th><th>受体位置</th><th>信号机制</th><th>例子</th></tr>
<tr><td><span class="kp">脂溶性激素</span></td><td>类固醇、甲状腺激素</td><td>胞内/核内受体</td><td>慢——调控基因转录</td><td>雌二醇、可的松、T₃、视黄酸</td></tr>
<tr><td><span class="kp">水溶性激素</span></td><td>多肽/蛋白质、氨基酸衍生物</td><td>细胞膜表面受体</td><td>快——第二信使级联</td><td>胰岛素、胰高血糖素、肾上腺素</td></tr>
</table>

<p><strong>为什么需要两种完全不同的信号机制？</strong>脂溶性激素可以穿膜直达胞内靶点（慢但持久，因为需要转录翻译），水溶性激素无法穿膜必须通过膜受体→胞内信号转导（快但短暂，响应迅速）。进化为不同的生理需求提供了不同的解决方案。</p>

<h3>18.2 第二信使与信号级联 <span class="tag-must">必考</span></h3>

<p><span class="kp">cAMP信号通路</span><span class="exp">：激素（如肾上腺素）与G蛋白偶联受体(GPCR)结合→激活Gs蛋白（GTP交换GDP）→Gsα-GTP激活腺苷酸环化酶→ATP→cAMP（第二信使）→cAMP激活PKA→PKA磷酸化下游靶蛋白→细胞响应。</span></p>

<p><strong>信号放大的数字</strong>：一个激素分子→激活一个受体→激活多个Gs蛋白→每个Gs激活一个腺苷酸环化酶→产生多个cAMP→每个cAMP激活一个PKA→PKA磷酸化多个靶酶。总放大倍数可达10⁶~10⁸。这就是为什么极低浓度（nM-pM）的激素就能引发巨大细胞响应。</p>

<p><span class="kp">磷脂酰肌醇信号通路</span><span class="exp">：GPCR→Gq蛋白激活PLCβ→PIP₂裂解为IP₃和DAG（两个第二信使）→IP₃打开内质网Ca²⁺通道→Ca²⁺激活PKC和其他Ca²⁺敏感蛋白→DAG直接激活PKC。</span></p>

<blockquote>易错：(1) cAMP和cGMP是第二信使，不是激素本身——它们只在胞内传递信号；(2) G蛋白的「开」是GTP结合态，「关」是GDP结合态（Gsα自身具有GTPase活性，缓慢水解GTP关闭信号）；(3) 霍乱毒素通过ADP-核糖基化修饰Gsα，使其GTPase活性丧失→Gsα持续激活→cAMP持续升高→肠上皮细胞大量分泌Cl⁻和水→腹泻。</blockquote>

"""

# Save the HTML
output_path = '/workspace/output/生物化学_第一篇_结构生物化学_Ch10-18.html'
save_knowledge_html(body, output_path, '第一篇 结构生物化学（第10-18章）知识精讲')
print(f'Generated: {output_path}')