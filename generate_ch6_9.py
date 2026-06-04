#!/usr/bin/env python3
"""生成《生物化学原理》第四版 第一篇 第6-9章 知识精讲 + 自测题 HTML。"""

import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'scripts'))
from template_engine import save_knowledge_html, save_test

# 中文双引号（避免与Python字符串定界符冲突）
LQ = '\u201c'  # "
RQ = '\u201d'  # "

# ══════════════════════════════════════════════════════════════════════════
#  知识精讲 body_html
# ══════════════════════════════════════════════════════════════════════════

body_html = f'''
<style>
/* ── 自定义卡片 & 模块 ── */
.card {{
  background: var(--card-bg); border: 1px solid var(--card-border);
  border-radius: var(--radius); padding: 14px 18px; margin: 12px 0;
}}
.card-title {{
  font-weight: 700; font-size: 1.05em; color: #1a1a2e;
  border-left: 4px solid var(--accent); padding-left: 10px; margin-bottom: 8px;
}}
.analogy {{
  background: #f0f9ff; border-left: 3px solid #0ea5e9;
  padding: 8px 14px; margin: 10px 0; border-radius: 0 var(--radius) var(--radius) 0;
  font-size: 0.95em; color: #0c4a6e;
}}
.analogy::before {{ content: "💡 直觉类比："; font-weight: 700; }}
.motivation {{
  background: #fefce8; border-left: 3px solid #eab308;
  padding: 8px 14px; margin: 10px 0; border-radius: 0 var(--radius) var(--radius) 0;
  font-size: 0.95em;
}}
.motivation::before {{ content: "🧠 动机推演："; font-weight: 700; }}
.pitfall-box {{
  background: #fef2f2; border-left: 3px solid #ef4444;
  padding: 8px 14px; margin: 10px 0; border-radius: 0 var(--radius) var(--radius) 0;
  font-size: 0.95em;
}}
.pitfall-box::before {{ content: "⚠️ 易错辨析："; font-weight: 700; color: #991b1b; }}
.highlight-box {{
  background: #fef3c7; border: 1px solid #f59e0b;
  padding: 10px 16px; margin: 10px 0; border-radius: var(--radius);
  font-size: 0.95em;
}}
.highlight-box::before {{ content: "🔥 考研高频："; font-weight: 700; color: #92400e; }}
</style>

<h2>第6章　核酸的结构与功能</h2>

<div class="motivation">
遗传信息如何从上一代传递到下一代？又如何从DNA{LQ}翻译{RQ}成蛋白质？
这一切的物理基础就是核酸的分子结构。理解核酸的化学组成与三维结构，是打开分子生物学的第一把钥匙。
</div>

<h3>6.1 核酸的化学组成</h3>

<div class="card">
<div class="card-title">核苷酸 = 碱基 + 戊糖 + 磷酸</div>
<p>核酸（DNA/RNA）是由<strong>核苷酸</strong>通过3{LQ},5{RQ}-磷酸二酯键连接而成的多聚体。
每个核苷酸由三部分组成：</p>
<table>
<tr><th>组分</th><th>DNA</th><th>RNA</th></tr>
<tr><td>碱基</td><td>A, G, C, T</td><td>A, G, C, U</td></tr>
<tr><td>戊糖</td><td>β-D-2{LQ}-脱氧核糖</td><td>β-D-核糖</td></tr>
<tr><td>磷酸</td><td>磷酸基团</td><td>磷酸基团</td></tr>
</table>
<p><strong>嘌呤</strong>（A腺嘌呤、G鸟嘌呤）：双环结构（嘧啶环+咪唑环）。<br>
<strong>嘧啶</strong>（C胞嘧啶、T胸腺嘧啶、U尿嘧啶）：单环结构。</p>
</div>

<div class="analogy">
碱基就像字母表中的字母——只有4种（ATCG或AUCG），但它们的排列组合可以编码整个生物体的全部信息。
这就像二进制只用0和1，却能表达无穷无尽的信息。
</div>

<div class="pitfall-box">
<strong>易错点1：</strong>DNA含T（胸腺嘧啶），RNA含U（尿嘧啶）——T比U多一个5-甲基。<br>
<strong>易错点2：</strong>核苷 = 碱基+戊糖（去掉磷酸）；核苷酸 = 碱基+戊糖+磷酸。
命名常考：腺嘌呤+核糖 = 腺苷（adenosine）；腺苷+磷酸 = 腺苷酸（AMP）。<br>
<strong>易错点3：</strong>DNA的戊糖是<em>脱氧</em>核糖（2{RQ}位为—H而非—OH），这是DNA比RNA化学稳定性更高的根本原因。
</div>

<h3>6.2 DNA双螺旋结构（Watson-Crick模型，1953）</h3>

<div class="highlight-box">
这是生物化学<strong>最核心的结构模型</strong>，考研几乎是必考题。以下参数必须烂熟于心。
</div>

<div class="card">
<div class="card-title">B-DNA 关键参数</div>
<table>
<tr><th>参数</th><th>数值</th><th>记忆技巧</th></tr>
<tr><td>螺距（pitch）</td><td><strong>3.4 nm</strong></td><td>{LQ}34{RQ} → 3.4</td></tr>
<tr><td>每圈碱基对数</td><td><strong>10.5 bp</strong></td><td>≈10，螺旋对称</td></tr>
<tr><td>相邻碱基对间距（rise）</td><td>0.34 nm</td><td>3.4 ÷ 10 = 0.34</td></tr>
<tr><td>直径</td><td><strong>2 nm</strong></td><td></td></tr>
<tr><td>螺旋方向</td><td><strong>右手螺旋</strong></td><td>绝大多数情况</td></tr>
<tr><td>两条链方向</td><td><strong>反平行</strong></td><td>5{RQ}→3{RQ} 与 3{RQ}→5{RQ}</td></tr>
</table>
</div>

<div class="card">
<div class="card-title">碱基互补配对</div>
<p>A 与 T 之间形成 <strong>2</strong> 个氢键（A=T）；G 与 C 之间形成 <strong>3</strong> 个氢键（G≡C）。</p>
<p>因此 <strong>GC含量越高，DNA越稳定，Tm值越高</strong>。</p>
</div>

<div class="card">
<div class="card-title">大沟（Major groove）与小沟（Minor groove）</div>
<p>由于碱基对与糖环的连接方式不对称，双螺旋表面形成宽窄交替的两条沟。</p>
<p><strong>大沟</strong>富含碱基特异性信息（氢键供体/受体模式），是<strong>蛋白质（转录因子等）识别DNA序列</strong>的主要场所。
小沟相对信息贫乏但也可被某些小分子/蛋白质识别。</p>
</div>

<div class="analogy">
把双螺旋想象成一条螺旋楼梯：磷酸-糖骨架是两侧的扶手（亲水，朝外），
碱基对是中间的台阶（疏水，堆叠在内）。大沟和小沟就是扶手外侧宽窄交替的凹槽。
</div>

<h3>6.3 Chargaff规则</h3>

<div class="card">
<p>① [A] = [T]，[G] = [C]（在双链DNA中）<br>
② [A] + [G] = [T] + [C]（嘌呤总数 = 嘧啶总数）<br>
③ <strong>不同物种</strong>DNA碱基组成不同（物种特异性），但<strong>同一物种不同组织</strong>相同</p>
<p>这是Watson-Crick提出碱基配对模型的重要实验依据。</p>
</div>

<h3>6.4 DNA的变性与复性</h3>

<div class="card">
<div class="card-title">DNA变性（Denaturation）</div>
<p>在高温、极端pH等条件下，氢键断裂，双链解开成单链。<strong>不破坏共价键</strong>（磷酸二酯键完好）。</p>
<ul>
  <li><strong>增色效应</strong>（Hyperchromic effect）：变性后A<sub>260</sub>升高约30-40%（碱基从堆叠状态暴露出来）</li>
  <li><strong>解链温度 Tm</strong>：A<sub>260</sub>升高达到最大值一半时的温度</li>
  <li><strong>Tm值与GC含量正相关</strong>：G≡C有三个氢键，更稳定。经验公式：Tm ≈ 4(G+C) + 2(A+T)（适用于短片段）</li>
</ul>
</div>

<div class="card">
<div class="card-title">DNA复性（Renaturation / Annealing）</div>
<p>缓慢降温时，互补单链重新配对恢复双螺旋。</p>
<ul>
  <li><strong>Cot曲线</strong>：以初始浓度(C<sub>0</sub>) × 时间(t) 为横轴，复性程度为纵轴</li>
  <li>Cot<sub>1/2</sub> 值反映基因组复杂度——<strong>基因组越大、重复序列越少，复性越慢，Cot<sub>1/2</sub>越大</strong></li>
</ul>
</div>

<div class="pitfall-box">
<strong>易错：</strong>变性是{LQ}解链{RQ}而非{LQ}降解{RQ}。不要混淆氢键断裂（物理变化，可逆）和磷酸二酯键水解（化学变化，不可逆）。
Tm是{LQ}一半解链{RQ}时的温度，不是{LQ}完全解链{RQ}的温度。
</div>

<h3>6.5 DNA的超螺旋与拓扑异构酶</h3>

<div class="card">
<p>环状DNA（如细菌染色体、质粒）可形成<strong>超螺旋</strong>（supercoil）。</p>
<ul>
  <li><strong>负超螺旋</strong>：螺旋不足（underwound），有利于DNA复制和转录时局部解链</li>
  <li><strong>拓扑异构酶Ⅰ</strong>：切断一条链，改变Lk ±1，不需ATP</li>
  <li><strong>拓扑异构酶Ⅱ</strong>（DNA旋转酶gyrase）：切断两条链，改变Lk ±2，<strong>需ATP</strong>。在原核生物中引入负超螺旋</li>
</ul>
</div>

<h3>6.6 RNA的种类与功能</h3>

<div class="card">
<div class="card-title">mRNA（信使RNA）</div>
<ul>
  <li>携带遗传信息从DNA到核糖体</li>
  <li>原核mRNA为多顺反子，真核mRNA为单顺反子</li>
  <li>真核mRNA有5{RQ}帽和3{RQ} polyA尾</li>
  <li><strong>密码子</strong>（codon）：三个连续核苷酸编码一个氨基酸</li>
</ul>
</div>

<div class="card">
<div class="card-title">tRNA（转运RNA）</div>
<ul>
  <li>二级结构：<strong>三叶草结构</strong>（氨基酸臂、TΨC臂、反密码子臂、D臂、可变臂）</li>
  <li>三级结构：<strong>倒L型</strong></li>
  <li>3{RQ}端均为<strong>CCA</strong>（氨基酸连接位点）</li>
  <li>反密码子环含<strong>反密码子</strong>，与mRNA密码子反向互补配对</li>
  <li>含大量稀有碱基（如二氢尿嘧啶D、假尿苷Ψ）</li>
</ul>
</div>

<div class="card">
<div class="card-title">rRNA（核糖体RNA）</div>
<table>
<tr><th></th><th>原核(70S)</th><th>真核(80S)</th></tr>
<tr><td>大亚基</td><td>50S (23S + 5S rRNA)</td><td>60S (28S + 5.8S + 5S rRNA)</td></tr>
<tr><td>小亚基</td><td>30S (16S rRNA)</td><td>40S (18S rRNA)</td></tr>
</table>
<p>rRNA是核糖体的<strong>结构和催化核心</strong>（肽酰转移酶活性来自23S/28S rRNA，即核酶ribozyme）。</p>
</div>

<h3>6.7 核酸的化学性质</h3>

<div class="card">
<ul>
  <li><strong>紫外吸收</strong>：碱基的共轭双键系统在<strong>260 nm</strong>有最大吸收峰</li>
  <li>蛋白质在280 nm有最大吸收（常考对比：A<sub>260</sub>/A<sub>280</sub>判断核酸纯度）</li>
  <li><strong>酸水解</strong>：RNA中2{RQ}-OH邻近参与，RNA比DNA更容易被稀碱水解（DNA对碱相对稳定）</li>
</ul>
</div>

<h2>第7章　糖类的结构与功能</h2>

<div class="motivation">
糖不仅是{LQ}燃料分子{RQ}，更是细胞识别的{LQ}分子语言{RQ}。从单糖的立体化学到多糖的超分子结构，
理解糖的构型和构象，是理解糖生物学功能的前提。
</div>

<h3>7.1 单糖的结构与分类</h3>

<div class="card">
<div class="card-title">单糖分类</div>
<table>
<tr><th>分类标准</th><th>类别</th><th>示例</th></tr>
<tr><td>羰基类型</td><td>醛糖（aldose）</td><td>葡萄糖、核糖</td></tr>
<tr><td></td><td>酮糖（ketose）</td><td>果糖</td></tr>
<tr><td>碳原子数</td><td>丙糖、丁糖、戊糖、己糖</td><td>核糖=戊醛糖；葡萄糖=己醛糖；果糖=己酮糖</td></tr>
<tr><td>环状结构</td><td>吡喃糖（六元环）</td><td>α/β-D-吡喃葡萄糖</td></tr>
<tr><td></td><td>呋喃糖（五元环）</td><td>β-D-呋喃果糖</td></tr>
<tr><td>构型（D/L）</td><td>D型</td><td>天然糖几乎都是D型</td></tr>
</table>
</div>

<h3>7.2 葡萄糖的立体化学</h3>

<div class="highlight-box">
糖的立体化学是考研选择题、判断题的高频考点，尤其是D/L命名法和α/β异头碳的区别。
</div>

<div class="card">
<div class="card-title">Fischer投影式 → Haworth透视式 → 椅式构象</div>
<ul>
  <li><strong>Fischer投影式</strong>：线性表达，竖键朝后，横键朝前</li>
  <li><strong>D/L 规则</strong>：离羰基最远的手性碳（葡萄糖为C5）上的—OH在右边为D，左边为L</li>
  <li><strong>Haworth透视式</strong>：C5上的—OH与羰基加成形成半缩醛环。D型糖的CH<sub>2</sub>OH在环上方</li>
  <li><strong>异头碳（anomeric carbon）</strong>：环化后新产生的手性碳C1</li>
  <li><strong>α-异头体</strong>：C1—OH 与 C5—CH<sub>2</sub>OH 在环的<strong>异侧</strong>（trans）</li>
  <li><strong>β-异头体</strong>：C1—OH 与 C5—CH<sub>2</sub>OH 在环的<strong>同侧</strong>（cis）</li>
  <li><strong>变旋现象</strong>（mutarotation）：α和β在溶液中通过开链形式互变，比旋光度逐渐变化至平衡值</li>
</ul>
</div>

<div class="card">
<div class="card-title">椅式构象（chair conformation）</div>
<p>吡喃葡萄糖最稳定的构象是<strong>椅式</strong>，所有大取代基（—OH、—CH<sub>2</sub>OH）都在<strong>平伏键</strong>（equatorial）上，
这在β-D-葡萄糖中完美实现——所有—OH都是平伏的，因此β-D-葡萄糖是自然界最丰富的有机化合物。</p>
</div>

<div class="pitfall-box">
<strong>易错辨析：</strong><br>
① D/L 是<strong>构型</strong>（configuration），基于Fischer投影式，不能互变；α/β是<strong>异头构型</strong>，在溶液中可通过开链互变。<br>
② D ≠ d（右旋），L ≠ l（左旋）。D/L是构型标记，d/l是旋光方向，两者没有必然对应关系！<br>
③ 天然氨基酸都是L型，天然单糖几乎都是D型——两者恰好相反，考研常混在一起考。
</div>

<h3>7.3 重要二糖</h3>

<div class="card">
<table>
<tr><th>二糖</th><th>组成</th><th>糖苷键</th><th>还原性</th></tr>
<tr><td><strong>麦芽糖</strong></td><td>Glc + Glc</td><td>α-1,4</td><td>有（保留游离异头碳）</td></tr>
<tr><td><strong>蔗糖</strong></td><td>Glc + Fru</td><td>α-1,2-β</td><td><strong>无</strong>（两个异头碳都参与成键）</td></tr>
<tr><td><strong>乳糖</strong></td><td>Gal + Glc</td><td>β-1,4</td><td>有</td></tr>
</table>
</div>

<div class="pitfall-box">
<strong>关键辨析：</strong>蔗糖是<strong>唯一没有还原性的常见二糖</strong>，因为葡萄糖的C1和果糖的C2（都是异头碳）均参与了糖苷键形成，没有游离异头碳。
这也是斐林试剂/本尼迪克特试剂测试中蔗糖呈阴性的原因。
</div>

<h3>7.4 重要多糖</h3>

<div class="card">
<div class="card-title">淀粉（Starch）</div>
<ul>
  <li><strong>直链淀粉</strong>（amylose）：α-1,4糖苷键连接，线性螺旋结构</li>
  <li><strong>支链淀粉</strong>（amylopectin）：α-1,4主链 + <strong>α-1,6分支点</strong>（每24-30个残基一个分支）</li>
  <li>遇碘：直链淀粉呈蓝色，支链淀粉呈紫红色</li>
</ul>
</div>

<div class="card">
<div class="card-title">糖原（Glycogen）</div>
<ul>
  <li>动物的储能多糖，结构类似支链淀粉但<strong>分支更多、更密集</strong>（每8-12个残基一个分支）</li>
  <li>高度分支化有利于快速动员——糖原磷酸化酶从非还原端同时切割多条链</li>
</ul>
</div>

<div class="card">
<div class="card-title">纤维素（Cellulose）</div>
<ul>
  <li>β-1,4糖苷键连接的直链葡萄糖聚合物</li>
  <li>链间形成大量<strong>氢键</strong>，构成坚韧的纤维束（微纤维→纤维素纤维）</li>
  <li><strong>人体不能消化纤维素</strong>——缺乏纤维素酶（β-1,4-葡聚糖酶）</li>
  <li>反刍动物瘤胃中的微生物可产生纤维素酶</li>
</ul>
</div>

<div class="analogy">
淀粉（α-1,4）和纤维素（β-1,4）仅一个糖苷键构型之差（α vs β），
但α连接使淀粉链弯曲成螺旋（可被淀粉酶识别），β连接使纤维素链笔直伸展形成纤维——
小小的立体化学差异决定了完全不同的生物学命运。
</div>

<h3>7.5 糖蛋白与蛋白聚糖</h3>

<div class="card">
<table>
<tr><th></th><th>糖蛋白（Glycoprotein）</th><th>蛋白聚糖（Proteoglycan）</th></tr>
<tr><td>糖含量</td><td>较少（&lt;50%）</td><td><strong>很高</strong>（可达95%）</td></tr>
<tr><td>糖链结构</td><td>短链、分支寡糖</td><td>长链、无分支的GAG（糖胺聚糖）</td></tr>
<tr><td>功能</td><td>细胞识别、免疫、激素受体</td><td>结构支撑、润滑（如软骨中的aggrecan）</td></tr>
<tr><td>连接方式</td><td>N-连接（Asn）或O-连接（Ser/Thr）</td><td>核心蛋白+多条GAG链</td></tr>
</table>
</div>

<h2>第8章　脂类与生物膜</h2>

<div class="motivation">
水是生命之母，但生命的边界需要用{LQ}不溶于水{RQ}的材料来构建。
脂类正是这种{LQ}水-油边界{RQ}的分子基础——它们既能构成分隔内外的屏障，又能保持足够的流动性来维持生命活动。
</div>

<h3>8.1 脂肪酸</h3>

<div class="card">
<div class="card-title">命名与分类</div>
<ul>
  <li><strong>饱和脂肪酸</strong>：无双键，如棕榈酸(16:0)、硬脂酸(18:0)</li>
  <li><strong>不饱和脂肪酸</strong>：含一个或多个双键（天然多为顺式），如油酸(18:1 Δ⁹)</li>
  <li><strong>ω命名法</strong>：从甲基端（ω端）开始编号，ω-3（如α-亚麻酸）、ω-6（如亚油酸、花生四烯酸）</li>
  <li><strong>必需脂肪酸</strong>：人体不能合成，须从食物获取——<strong>亚油酸</strong>(18:2 ω-6)和<strong>α-亚麻酸</strong>(18:3 ω-3)</li>
</ul>
</div>

<div class="pitfall-box">
花生四烯酸(20:4 ω-6)可由亚油酸合成，通常不被归为严格必需脂肪酸，但有些教材也将其列入，注意题干语境。
ω-3（如EPA、DHA）和ω-6脂肪酸在体内有相反的炎症调节作用，ω-3抗炎、ω-6促炎，平衡很重要。
</div>

<h3>8.2 三酰甘油（Triacylglycerol, TAG）</h3>

<div class="card">
<ul>
  <li>甘油 + 3分子脂肪酸 → 三酰甘油（酯键连接）</li>
  <li><strong>最重要的储能形式</strong>——单位质量的储能是糖原的约6倍（疏水、不需水合）</li>
  <li>储存在脂肪细胞（adipocyte）的脂滴中，几乎占据整个细胞体积</li>
</ul>
</div>

<h3>8.3 膜脂——甘油磷脂与鞘脂</h3>

<div class="card">
<div class="card-title">甘油磷脂（Glycerophospholipid）</div>
<ul>
  <li>甘油-3-磷酸为骨架，C1和C2位酯化两分子脂肪酸，磷酸基团上连接极性头部</li>
  <li><strong>磷脂酰胆碱</strong>（PC，卵磷脂）——头部：胆碱</li>
  <li><strong>磷脂酰乙醇胺</strong>（PE，脑磷脂）——头部：乙醇胺</li>
  <li><strong>磷脂酰丝氨酸</strong>（PS）——头部：丝氨酸</li>
  <li><strong>两亲性分子</strong>：两条脂肪酸尾（疏水）+ 磷酸头部（亲水），是生物膜的基本结构单元</li>
</ul>
</div>

<div class="card">
<div class="card-title">鞘脂（Sphingolipid）</div>
<ul>
  <li>以<strong>鞘氨醇</strong>（sphingosine）代替甘油为骨架</li>
  <li>鞘磷脂：鞘氨醇+脂肪酸+磷酸胆碱，是髓鞘的主要成分</li>
  <li>脑苷脂/神经节苷脂：含糖基头部，参与细胞识别</li>
</ul>
</div>

<h3>8.4 胆固醇（Cholesterol）</h3>

<div class="card">
<ul>
  <li>结构：<strong>环戊烷多氢菲</strong>骨架（四环稠合）+ 异辛基侧链</li>
  <li><strong>两亲性</strong>：极性—OH（亲水头部）很小，庞大的甾环和侧链（疏水）很大</li>
  <li>插入膜磷脂之间，调节膜的<strong>流动性</strong>——低温阻止磷脂结晶（维持流动），高温限制过度运动（维持刚性）</li>
  <li>是<strong>所有类固醇激素</strong>（性激素、皮质激素）、<strong>胆汁酸</strong>和<strong>维生素D</strong>的前体</li>
</ul>
</div>

<div class="analogy">
胆固醇就像细胞膜的{LQ}调温器{RQ}（buffer）——在天冷时防止膜{LQ}冻住{RQ}（像防冻剂），
在天热时防止膜{LQ}融化{RQ}（像稳定剂），维持膜在最佳流动状态。
</div>

<h3>8.5 生物膜——流动镶嵌模型（Singer-Nicolson, 1972）</h3>

<div class="highlight-box">
流动镶嵌模型是膜生物学的基石，也是每年必考的核心概念。
</div>

<div class="card">
<div class="card-title">模型核心要点</div>
<ul>
  <li><strong>脂双层</strong>是膜的{LQ}基质{RQ}：磷脂形成连续的脂双层，是膜的基本结构</li>
  <li><strong>膜蛋白</strong>{LQ}漂浮{RQ}其中：蛋白质像{LQ}冰山{RQ}一样镶嵌在脂双层{LQ}海洋{RQ}中</li>
  <li><strong>膜是不对称的</strong>：内外层脂质组成不同，蛋白质有明确的拓扑方向</li>
  <li><strong>膜是流动的</strong>：脂质和蛋白质可以在膜平面内自由侧向扩散</li>
</ul>
</div>

<h3>8.6 膜脂的运动方式</h3>

<div class="card">
<table>
<tr><th>运动方式</th><th>描述</th><th>速度</th></tr>
<tr><td><strong>侧向扩散</strong></td><td>同一单层内横向移动</td><td>很快（≈10⁷次/秒换位）</td></tr>
<tr><td><strong>旋转运动</strong></td><td>绕自身长轴旋转</td><td>很快</td></tr>
<tr><td><strong>翻转运动（flip-flop）</strong></td><td>从内层翻到外层（或反之）</td><td><strong>极慢</strong>（需flippase/floppase酶催化）</td></tr>
</table>
</div>

<div class="pitfall-box">
<strong>易错：</strong>翻转运动（flip-flop）在无酶催化时<strong>几乎不发生</strong>（半衰期可达数天），
因为极性头部穿过疏水核心在热力学上极为不利。这与侧向扩散形成鲜明对比，是维持膜不对称性的关键。
</div>

<h3>8.7 膜的相变</h3>

<div class="card">
<ul>
  <li><strong>相变温度 Tm</strong>：从凝胶态（有序）转变为液晶态（流动）的温度</li>
  <li>脂肪酸链越<strong>长</strong>→ 范德华力越大 → Tm<strong>越高</strong></li>
  <li>脂肪酸链<strong>不饱和度越高</strong>（顺式双键产生扭结）→ 堆积越松散 → Tm<strong>越低</strong></li>
  <li>胆固醇使相变变得平缓（消除尖锐的相变点）</li>
</ul>
</div>

<h3>8.8 膜蛋白的类型</h3>

<div class="card">
<table>
<tr><th>类型</th><th>与膜的关系</th><th>去除方法</th><th>实例</th></tr>
<tr><td><strong>整合蛋白</strong></td><td>穿膜或深埋脂双层中</td><td>需去垢剂破坏膜结构</td><td>离子通道、GPCR、转运蛋白</td></tr>
<tr><td><strong>外周蛋白</strong></td><td>通过静电/氢键结合于膜表面</td><td>高盐/pH变化即可</td><td>细胞色素c、锚蛋白</td></tr>
<tr><td><strong>脂锚定蛋白</strong></td><td>共价连接脂质插入膜中</td><td>需酶切割脂锚</td><td>GPI锚定蛋白、Ras蛋白</td></tr>
</table>
</div>

<h2>第9章　维生素与辅酶</h2>

<div class="motivation">
维生素本身不是能量来源，也不是结构材料，但缺乏任何一种都可能导致严重的代谢疾病。
因为它们中的大多数在体内转化为<strong>辅酶</strong>——酶的{LQ}化学工具包{RQ}，承担着酶无法用氨基酸侧链完成的化学任务。
</div>

<h3>9.1 维生素的分类</h3>

<div class="card">
<div class="card-title">水溶性 vs 脂溶性</div>
<table>
<tr><th></th><th>水溶性维生素</th><th>脂溶性维生素</th></tr>
<tr><td>成员</td><td>B族（B1,B2,B3,B5,B6,B7,B9,B12）+ C</td><td>A, D, E, K</td></tr>
<tr><td>储存</td><td>不易储存，需经常补充</td><td>可在肝脏/脂肪中储存</td></tr>
<tr><td>过量</td><td>一般从尿排出，毒性较小</td><td>可蓄积中毒（尤其A和D）</td></tr>
<tr><td>功能</td><td>主要转化为辅酶</td><td>多为激素前体/抗氧化</td></tr>
</table>
</div>

<h3>9.2 水溶性维生素及其辅酶形式（🔥 核心考点）</h3>

<div class="highlight-box">
以下对应关系是考研选择题的{LQ}钉子户{RQ}考点，必须做到条件反射式的记忆。
</div>

<div class="card">
<table>
<tr><th>维生素</th><th>别名</th><th>辅酶形式</th><th>功能类型</th></tr>
<tr><td><strong>B₁</strong></td><td>硫胺素</td><td><strong>TPP</strong>（焦磷酸硫胺素）</td><td>α-酮酸<strong>脱羧</strong>、转酮醇酶</td></tr>
<tr><td><strong>B₂</strong></td><td>核黄素</td><td><strong>FAD / FMN</strong></td><td><strong>氧化还原</strong>（递氢体）</td></tr>
<tr><td><strong>B₃</strong></td><td>烟酸/烟酰胺</td><td><strong>NAD⁺ / NADP⁺</strong></td><td><strong>氧化还原</strong>脱氢（递氢体）</td></tr>
<tr><td><strong>B₅</strong></td><td>泛酸</td><td><strong>CoA</strong>（辅酶A）</td><td><strong>酰基转移</strong></td></tr>
<tr><td><strong>B₆</strong></td><td>吡哆醇</td><td><strong>PLP</strong>（磷酸吡哆醛）</td><td><strong>转氨/脱羧</strong>（氨基酸代谢）</td></tr>
<tr><td><strong>B₇</strong></td><td>生物素</td><td><strong>生物素（羧化酶辅基）</strong></td><td><strong>CO₂转移</strong>（羧化反应）</td></tr>
<tr><td><strong>B₉</strong></td><td>叶酸</td><td><strong>THF</strong>（四氢叶酸）</td><td><strong>一碳单位</strong>转移</td></tr>
<tr><td><strong>B₁₂</strong></td><td>钴胺素</td><td><strong>辅酶B₁₂</strong>（5{RQ}-脱氧腺苷钴胺素/甲基钴胺素）</td><td><strong>变位/甲基转移</strong></td></tr>
<tr><td><strong>C</strong></td><td>抗坏血酸</td><td>抗坏血酸本身</td><td><strong>抗氧化</strong>、脯氨酸/赖氨酸羟化辅因子</td></tr>
</table>
</div>

<div class="pitfall-box">
<strong>高频混淆点：</strong><br>
① B₃（烟酸）→ <strong>NAD</strong>，不是NADPH直接来源（那需要磷酸化反应）<br>
② B₂（核黄素）→ <strong>FAD/FMN</strong>，注意FAD来自B₂而非B₃<br>
③ B₆ → <strong>PLP</strong>，涉及所有氨基酸转氨酶，也涉及脱羧酶（如GABA合成）<br>
④ B₇（生物素）结合于羧化酶的<strong>赖氨酸残基</strong>上<br>
⑤ B₁₂是<strong>唯一含金属元素（Co）</strong>的维生素
</div>

<h3>9.3 脂溶性维生素</h3>

<div class="card">
<table>
<tr><th>维生素</th><th>别名</th><th>活性形式</th><th>核心功能</th></tr>
<tr><td><strong>A</strong></td><td>视黄醇</td><td>视黄醛、视黄酸</td><td><strong>视觉</strong>（视紫红质成分）、上皮组织维持、基因表达调控</td></tr>
<tr><td><strong>D</strong></td><td>钙化醇</td><td>1,25-(OH)₂-D₃</td><td><strong>钙磷代谢</strong>调节（促进肠道钙吸收）</td></tr>
<tr><td><strong>E</strong></td><td>生育酚</td><td>α-生育酚</td><td><strong>抗氧化</strong>（保护膜脂免受自由基氧化）</td></tr>
<tr><td><strong>K</strong></td><td>叶绿醌</td><td>维生素K本身</td><td><strong>凝血因子γ-羧化</strong>辅因子（Gla残基形成）</td></tr>
</table>
</div>

<div class="pitfall-box">
<strong>易错辨析：</strong><br>
① 维生素D是<strong>激素前体</strong>（更像激素），而非典型的酶辅因子<br>
② 维生素K的功能是<strong>γ-羧化</strong>（Glu → Gla），不是氧化磷酸化<br>
③ 维生素A的活性形式：视黄醛（视觉）、视黄酸（基因调控）——注意区分<br>
④ 缺乏症快速对照：A→夜盲；D→佝偻病/软骨病；E→溶血性贫血；K→出血倾向；B₁→脚气病；B₃→糙皮病；B₉→巨幼红细胞性贫血；B₁₂→恶性贫血；C→坏血病
</div>

<div class="card">
<div class="card-title">维生素缺乏症速查表 <span class="tag-key">高频考点</span></div>
<table>
<tr><th>维生素</th><th>缺乏症</th><th>维生素</th><th>缺乏症</th></tr>
<tr><td>B₁</td><td>脚气病（beriberi）</td><td>C</td><td>坏血病（scurvy）</td></tr>
<tr><td>B₃</td><td>糙皮病（pellagra，3D症状）</td><td>A</td><td>夜盲症、干眼症</td></tr>
<tr><td>B₉</td><td>巨幼红细胞性贫血</td><td>D</td><td>佝偻病/骨软化症</td></tr>
<tr><td>B₁₂</td><td>恶性贫血</td><td>K</td><td>出血倾向</td></tr>
</table>
</div>
'''

# ══════════════════════════════════════════════════════════════════════════
#  自测题（25题，满分100分）
# ══════════════════════════════════════════════════════════════════════════

questions = [
    # ── 第6章 核酸 ──
    {
        'type': 'single',
        'points': 4,
        'question': 'B-DNA双螺旋的螺距（pitch）是多少？',
        'options': ['A. 0.34 nm', 'B. 2.0 nm', 'C. 3.4 nm', 'D. 34 nm'],
        'answer': 'C',
        'explanation': 'B-DNA螺距为3.4 nm（34 Å），每圈含10.5个碱基对，相邻碱基对间距0.34 nm，直径2 nm。这些是碱基对堆积形成的宏观参数。',
        'pitfall': '3.4 nm和0.34 nm容易混淆——记住螺距=10×rise，即3.4 = 10 × 0.34。直径2 nm是另一个独立参数，并非螺距的一半。'
    },
    {
        'type': 'single',
        'points': 4,
        'question': '下列关于DNA碱基配对的说法，哪一项是正确的？',
        'options': [
            'A. A与C之间形成2个氢键',
            'B. G与C之间形成3个氢键，因此GC含量越高Tm越低',
            'C. A与T之间形成2个氢键，G与C之间形成3个氢键',
            'D. 碱基配对主要依靠磷酸二酯键维持'
        ],
        'answer': 'C',
        'explanation': f'A=T形成2个氢键，G≡C形成3个氢键。GC含量越高，DNA越稳定，Tm值越高（而非越低）。碱基配对依靠氢键和碱基堆积力，磷酸二酯键连接的是核苷酸之间的糖-磷酸骨架。',
        'pitfall': 'GC含量与Tm正相关，不是负相关——氢键越多越难解开，需要更高温度。这是选择题常见干扰项。'
    },
    {
        'type': 'single',
        'points': 4,
        'question': 'Chargaff规则指出，在双链DNA中：',
        'options': [
            'A. [A] = [C], [G] = [T]',
            'B. [A] + [T] = [G] + [C]',
            'C. [A] = [T], [G] = [C], 且[A]+[G] = [T]+[C]',
            'D. DNA碱基组成在所有物种中都相同'
        ],
        'answer': 'C',
        'explanation': f'Chargaff规则的核心：(1) A=T, G=C；(2) 嘌呤总数=嘧啶总数（A+G = T+C）。不同物种DNA碱基组成不同（物种特异性），但同一物种不同组织相同。',
        'pitfall': '选项B写的是A+T=G+C，这不对——应该是A+G = T+C（嘌呤=嘧啶）。A+T不一定等于G+C，GC含量因物种而异。'
    },
    {
        'type': 'single',
        'points': 4,
        'question': 'DNA变性时发生的现象是：',
        'options': [
            'A. 磷酸二酯键断裂',
            'B. 氢键断裂，双链解开，A₂₆₀升高',
            'C. A₂₆₀吸光度降低',
            'D. 一级结构被破坏'
        ],
        'answer': 'B',
        'explanation': f'DNA变性是指氢键断裂导致双链解开，不涉及共价键（磷酸二酯键）的断裂，一级结构保持完整。碱基从堆叠状态暴露出来导致增色效应（A₂₆₀升高约30-40%）。',
        'pitfall': f'变性的本质是{LQ}解链{RQ}而非{LQ}降解{RQ}，不要混淆。A₂₆₀是升高（增色效应），不是降低。'
    },
    {
        'type': 'single',
        'points': 4,
        'question': 'tRNA的三级结构是：',
        'options': [
            'A. 三叶草结构',
            'B. 倒L型结构',
            'C. 双螺旋结构',
            'D. β-折叠桶结构'
        ],
        'answer': 'B',
        'explanation': f'tRNA的二级结构是{LQ}三叶草{RQ}结构（cloverleaf），三级结构（空间折叠后的最终形状）是倒L型。三叶草的四个臂在空间中折叠成倒L的形态。',
        'pitfall': '三叶草 = 二级结构（平面图），倒L型 = 三级结构（空间构象）。这是考研经典辨析题，极易混淆。'
    },
    {
        'type': 'judge',
        'points': 3,
        'question': f'RNA由于2{RQ}位含有—OH基团，比DNA更容易被稀碱水解。',
        'answer': True,
        'explanation': f'RNA的核糖2{RQ}位—OH可以邻近参与磷酸二酯键的碱催化水解（形成2{RQ},3{RQ}-环状磷酸中间体），而DNA的2{RQ}-脱氧核糖无此—OH，对稀碱相对稳定。这是DNA作为遗传物质长期储存的化学优势。',
        'pitfall': ''
    },
    {
        'type': 'blank',
        'points': 4,
        'question': '核酸在______nm波长处有最大紫外吸收，这是由碱基的______系统所致。',
        'answer': '260; 共轭双键',
        'explanation': f'嘌呤和嘧啶碱基含共轭双键系统，最大紫外吸收在260 nm。蛋白质的最大吸收在280 nm（来自Trp和Tyr）。A₂₆₀/A₂₈₀比值常用于判断核酸纯度。',
        'pitfall': '260 nm（核酸）vs 280 nm（蛋白质）是经典对比，注意不要颠倒。'
    },
    {
        'type': 'blank',
        'points': 4,
        'question': f'所有tRNA分子的3{RQ}端均以______三核苷酸序列结尾，这是氨基酸的连接位点。',
        'answer': 'CCA',
        'explanation': f'tRNA的3{RQ}端CCA序列是高度保守的，氨基酸通过酯键连接到末端腺苷酸（A）的3{RQ}—OH上。部分tRNA的CCA是转录后添加的。',
        'pitfall': f'注意是CCA（3{RQ}端），不是5{RQ}端。方向性很重要。'
    },

    # ── 第7章 糖类 ──
    {
        'type': 'single',
        'points': 4,
        'question': '在Fischer投影式中，D-葡萄糖的判定标准是：',
        'options': [
            'A. C1上的—OH在右边',
            'B. 离羰基最远的手性碳（C5）上的—OH在右边',
            'C. 所有—OH都在右边',
            'D. 旋光方向为右旋'
        ],
        'answer': 'B',
        'explanation': 'D/L构型由离羰基最远的手性碳（葡萄糖为C5）上的—OH方向决定：在Fischer投影式中，—OH在右边为D，左边为L。天然单糖几乎都是D型。',
        'pitfall': 'D/L ≠ d/l！D/L是构型标记（基于Fischer投影式），d/l是旋光方向（基于实验测定），两者没有必然对应关系。'
    },
    {
        'type': 'single',
        'points': 4,
        'question': f'蔗糖没有还原性的原因是：',
        'options': [
            'A. 它是一种多糖',
            'B. 两个单糖的异头碳都参与了糖苷键的形成',
            'C. 它只含酮糖',
            'D. 它的糖苷键是β构型'
        ],
        'answer': 'B',
        'explanation': f'蔗糖由葡萄糖（C1）和果糖（C2）通过α-1,2-β糖苷键连接，两个单糖的异头碳均参与了成键，溶液中没有游离异头碳可以开环转变为醛基，因此无还原性，斐林试剂检测呈阴性。',
        'pitfall': '蔗糖是唯一没有还原性的常见二糖。麦芽糖和乳糖各有1个游离异头碳，有还原性。记住：看游离异头碳的有无。'
    },
    {
        'type': 'single',
        'points': 4,
        'question': '人体不能消化纤维素，其根本原因是：',
        'options': [
            'A. 纤维素分子量太大',
            'B. 纤维素含α-1,4糖苷键，人体缺乏α-淀粉酶以外的α-糖苷酶',
            'C. 纤维素含β-1,4糖苷键，人体缺乏相应的β-1,4-葡聚糖酶',
            'D. 纤维素在水中不溶'
        ],
        'answer': 'C',
        'explanation': f'纤维素由葡萄糖以β-1,4糖苷键连接而成，人体消化酶（如α-淀粉酶）只能水解α-糖苷键，缺乏能够水解β-1,4糖苷键的纤维素酶。反刍动物瘤胃中的共生微生物可产生纤维素酶。',
        'pitfall': '注意：纤维素是β-1,4，淀粉/糖原是α-1,4。一个β之差决定了能否被人体利用——考试常把α/β写反作为干扰项。'
    },
    {
        'type': 'single',
        'points': 4,
        'question': '下列哪种糖的糖苷键类型是α-1,4？',
        'options': [
            'A. 纤维素',
            'B. 乳糖',
            'C. 麦芽糖',
            'D. 蔗糖'
        ],
        'answer': 'C',
        'explanation': f'麦芽糖由两分子葡萄糖以α-1,4糖苷键连接。纤维素是β-1,4，乳糖是β-1,4（半乳糖-葡萄糖），蔗糖是α-1,2-β。',
        'pitfall': f'麦芽糖(α-1,4)、乳糖(β-1,4)和纤维素(β-1,4)的糖苷键类型容易记混。记忆诀窍：麦芽→α（{LQ}麦{RQ}和{LQ}α{RQ}像），乳糖→β（{LQ}乳{RQ}有弧度像β）。'
    },
    {
        'type': 'judge',
        'points': 3,
        'question': f'D-葡萄糖和L-葡萄糖互为对映体，天然蛋白质中的氨基酸为L型，天然糖类为D型。',
        'answer': True,
        'explanation': f'D-葡萄糖和L-葡萄糖互为镜像对映体（enantiomer）。自然界具有手性选择性：氨基酸几乎都是L型，单糖几乎都是D型。这一点在大分子识别中至关重要。',
        'pitfall': '注意：天然氨基酸=L型，天然单糖=D型——恰好相反。这是考研填空题/判断题的高频考点。'
    },
    {
        'type': 'blank',
        'points': 4,
        'question': '糖原与支链淀粉的结构相似，但糖原的分支更密集，平均每______个葡萄糖残基就有一个α-1,6分支点。',
        'answer': '8-12',
        'explanation': f'糖原的分支密度（每8-12个残基一个分支点）高于支链淀粉（每24-30个残基一个分支点），高度分支化使糖原磷酸化酶能从多个非还原端同时释放葡萄糖，实现快速动员。',
        'pitfall': f'糖原8-12，支链淀粉24-30——记住糖原更像{LQ}灌木{RQ}（分支密集），支链淀粉像{LQ}稀疏的树{RQ}。'
    },

    # ── 第8章 脂类与生物膜 ──
    {
        'type': 'single',
        'points': 4,
        'question': '下列脂肪酸中，属于必需脂肪酸的是：',
        'options': [
            'A. 油酸(18:1)',
            'B. 棕榈酸(16:0)',
            'C. 亚油酸(18:2 ω-6)',
            'D. 硬脂酸(18:0)'
        ],
        'answer': 'C',
        'explanation': f'必需脂肪酸是人体不能合成、必须从食物获取的脂肪酸，主要包括亚油酸（18:2 ω-6）和α-亚麻酸（18:3 ω-3）。人体缺乏在脂肪酸链的Δ9位以外引入双键的酶（缺乏Δ12和Δ15去饱和酶）。',
        'pitfall': f'油酸(18:1 Δ⁹)人体可合成，不是必需脂肪酸。必需脂肪酸的共同特征：在ω端有双键（ω-6或ω-3系列）。'
    },
    {
        'type': 'single',
        'points': 4,
        'question': '下列关于生物膜中脂质运动的描述，哪项正确？',
        'options': [
            'A. 翻转运动（flip-flop）发生频率很高',
            'B. 侧向扩散速度远大于翻转运动',
            'C. 翻转运动不需要酶催化',
            'D. 脂质分子不能在膜平面内移动'
        ],
        'answer': 'B',
        'explanation': '侧向扩散在膜单层内非常快（≈10⁷次/秒），而翻转运动（flip-flop）极慢，无酶催化时半衰期可达数天到数周，需要flippase/floppase/scramblase等酶的催化。这是维持膜脂不对称性的关键。',
        'pitfall': '翻转运动≠侧向扩散。翻转是跨双层的（热力学不利），侧向是在同一单层内的（极快）。两者速度差可达10⁹倍以上。'
    },
    {
        'type': 'single',
        'points': 4,
        'question': '关于膜相变温度Tm，下列说法正确的是：',
        'options': [
            'A. 脂肪酸链越长，Tm越低',
            'B. 脂肪酸不饱和度越高，Tm越低',
            'C. 胆固醇使Tm升高',
            'D. Tm与脂肪酸组成无关'
        ],
        'answer': 'B',
        'explanation': f'顺式双键在脂肪酸链中产生{LQ}扭结{RQ}（kink），使脂质堆积松散，降低相变温度。链越长→范德华力越强→Tm越高。胆固醇的作用是{LQ}缓冲{RQ}——使相变变得平缓而非升高或降低Tm。',
        'pitfall': 'A反了：链越长Tm越高（更稳定）。C不准确：胆固醇是{LQ}缓冲调节{RQ}而非单纯升高。记住：不饱和=松散=低Tm；长链=紧密=高Tm。'
    },
    {
        'type': 'judge',
        'points': 3,
        'question': '整合膜蛋白（integral protein）可以通过高盐溶液从膜上去除。',
        'answer': False,
        'explanation': '整合膜蛋白深埋于脂双层中（或穿膜），其疏水区域与脂质疏水尾部相互作用，只有用去垢剂（detergent）破坏膜结构才能将其提取出来。高盐溶液只能去除外周膜蛋白（通过静电和氢键结合于膜表面）。',
        'pitfall': '整合蛋白=需要去垢剂；外周蛋白=高盐/pH变化即可去除。这是实验方法的经典考点。'
    },
    {
        'type': 'blank',
        'points': 4,
        'question': '胆固醇的甾核骨架结构为______，其分子具有两亲性：______基团为亲水头部。',
        'answer': '环戊烷多氢菲; 3β-羟基（或—OH/羟基）',
        'explanation': f'胆固醇含环戊烷多氢菲（四环稠合甾核）+异辛基侧链，仅C3位有一个—OH（亲水头部），其余为疏水的甾环和侧链。这种极端的两亲性分布使其在膜中垂直排列，—OH朝向水相，甾环插入脂双层。',
        'pitfall': f'胆固醇亲水部分仅一个—OH，疏水部分很大——因此它不是典型的{LQ}去垢剂{RQ}式两亲分子，而是膜的{LQ}流变性调节剂{RQ}。'
    },

    # ── 第9章 维生素与辅酶 ──
    {
        'type': 'single',
        'points': 4,
        'question': '维生素B₁（硫胺素）的辅酶形式是：',
        'options': ['A. FAD', 'B. NAD⁺', 'C. TPP', 'D. CoA'],
        'answer': 'C',
        'explanation': '硫胺素（B₁）→ TPP（焦磷酸硫胺素），参与α-酮酸的氧化脱羧（如丙酮酸脱氢酶复合体中的E₁亚基）和磷酸戊糖途径中的转酮醇酶反应。',
        'pitfall': f'B₁→TPP（脱羧），B₂→FAD（氧化还原），B₃→NAD（脱氢），B₅→CoA（酰基转移）。四种B族维生素的辅酶容易张冠李戴，需要建立各自的{LQ}记忆锚点{RQ}。'
    },
    {
        'type': 'single',
        'points': 4,
        'question': '在转氨反应中作为辅酶的化合物PLP来源于哪种维生素？',
        'options': ['A. 维生素B₁', 'B. 维生素B₂', 'C. 维生素B₃', 'D. 维生素B₆'],
        'answer': 'D',
        'explanation': 'PLP（磷酸吡哆醛）来源于维生素B₆（吡哆醇/吡哆醛/吡哆胺），是所有转氨酶（aminotransferase）和许多氨基酸脱羧酶的辅酶。PLP与底物氨基酸形成Schiff碱中间体。',
        'pitfall': 'B₆→PLP→转氨/脱羧，这是代谢章节的核心考点。B₁→TPP→脱羧（针对α-酮酸），B₆→PLP→转氨（针对氨基酸），两者都涉及{LQ}脱羧{RQ}但底物不同。'
    },
    {
        'type': 'single',
        'points': 4,
        'question': '唯一含有金属元素的维生素是：',
        'options': ['A. 维生素B₁', 'B. 维生素B₆', 'C. 维生素B₁₂', 'D. 维生素C'],
        'answer': 'C',
        'explanation': f'维生素B₁₂（钴胺素）含有一个Co（钴）离子，位于咕啉环（corrin ring）的中心，是唯一含金属元素的维生素。Co可形成Co—C键，参与分子内重排（变位酶）和甲基转移反应。',
        'pitfall': f'B₁₂中的金属是Co（钴）——不要与其他含金属的辅基混淆（如血红素含Fe、叶绿素含Mg）。这是{LQ}唯一性{RQ}考点，选择题特征明显。'
    },
    {
        'type': 'single',
        'points': 4,
        'question': '维生素K在体内的主要功能是：',
        'options': [
            'A. 抗氧化作用',
            'B. 参与视觉色素的形成',
            'C. 作为凝血因子γ-羧化的辅因子',
            'D. 促进钙的吸收'
        ],
        'answer': 'C',
        'explanation': '维生素K是γ-谷氨酰羧化酶的辅因子，催化凝血因子Ⅱ(凝血酶原)、Ⅶ、Ⅸ、Ⅹ中特定谷氨酸残基(Glu)的γ-羧化形成γ-羧基谷氨酸(Gla)，使其获得Ca²⁺结合能力，从而参与凝血级联反应。',
        'pitfall': f'K→凝血（{LQ}K{RQ}可联想{LQ}K血{RQ}=koagulation）。D→钙吸收。E→抗氧化。A→视觉。四个脂溶性维生素功能各有侧重，不要搞混。'
    },
    {
        'type': 'blank',
        'points': 3,
        'question': '维生素B₇（生物素）是______酶的辅基，其功能是转移______。',
        'answer': '羧化; CO₂（或二氧化碳/一碳单位中的CO₂）',
        'explanation': '生物素共价连接于羧化酶的赖氨酸残基ε-氨基上，作为CO₂的载体。如丙酮酸羧化酶（糖异生关键酶）、乙酰CoA羧化酶（脂肪酸合成关键酶）等。生物素通过其脲基环与CO₂形成N-羧基生物素中间体。',
        'pitfall': f'生物素转移的是CO₂（羧化），不是一碳单位（那是THF/Folate的功能）。这是两个容易混淆的{LQ}碳单元转移{RQ}体系。'
    },
    {
        'type': 'short',
        'points': 8,
        'question': '简述DNA双螺旋结构（Watson-Crick模型）的基本特征。（提示：从链的方向、碱基配对、沟结构、稳定力等方面回答）',
        'answer': f'①两条多核苷酸链反向平行（一条5{RQ}→3{RQ}，另一条3{RQ}→5{RQ}），围绕同一轴右手螺旋。②糖-磷酸骨架在外侧（亲水），碱基对在内侧（疏水），碱基平面垂直于螺旋轴。③碱基互补配对：A=T（2个氢键），G≡C（3个氢键）。④螺旋表面形成大沟（major groove）和小沟（minor groove），大沟是蛋白质识别DNA序列的主要场所。⑤稳定力包括：碱基堆积力（疏水作用+范德华力，主要贡献）、氢键、离子键（磷酸基团与Mg²⁺等阳离子）。',
        'explanation': 'B-DNA参数：螺距3.4 nm、每圈10.5 bp、直径2 nm、相邻碱基对间距0.34 nm。这些参数是理解DNA复制、转录和蛋白质-DNA识别的基础。',
        'pitfall': '注意区分{LQ}主要稳定力{RQ}：碱基堆积力（疏水+范德华）比氢键贡献更大，氢键主要贡献碱基配对的特异性（而非稳定性）。'
    },
]

# ══════════════════════════════════════════════════════════════════════════
#  生成输出
# ══════════════════════════════════════════════════════════════════════════

output_dir = os.path.join(os.path.dirname(__file__), 'output')
os.makedirs(output_dir, exist_ok=True)

save_knowledge_html(
    body_html=body_html,
    output_path=os.path.join(output_dir, '生物化学_第6-9章_知识精讲.html'),
    title='生物化学原理 · 第一篇 第6-9章 知识精讲'
)

save_test(
    questions=questions,
    output_path=os.path.join(output_dir, '生物化学_第6-9章_自测题.html'),
    title='生物化学原理 · 第一篇 第6-9章 自测题',
    subtitle='核酸 · 糖类 · 脂类与生物膜 · 维生素与辅酶',
    duration_minutes=45
)

print('✅ 已生成:')
print(f'   {os.path.join(output_dir, "生物化学_第6-9章_知识精讲.html")}')
print(f'   {os.path.join(output_dir, "生物化学_第6-9章_自测题.html")}')
print(f'   自测题共 {len(questions)} 题，满分 {sum(q["points"] for q in questions)} 分')