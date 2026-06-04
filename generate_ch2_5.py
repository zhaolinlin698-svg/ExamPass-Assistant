#!/usr/bin/env python3
"""生成杨荣武《生物化学原理》第四版 第2-5章 知识精讲与自测题 HTML。"""

import sys
sys.path.insert(0, '/workspace/scripts')
from template_engine import save_knowledge_html, save_test


# ═══════════════════════════════════════════════════════════════════════
#  知识精讲 HTML body
# ═══════════════════════════════════════════════════════════════════════

KNOWLEDGE_BODY = r"""

<h2>第2章 氨基酸</h2>

<div class="toc-box" style="background:var(--card-bg);border:1px solid var(--card-border);border-radius:var(--radius);padding:14px 18px;margin-bottom:18px">
  <strong>本章速览</strong>：氨基酸是蛋白质的结构单元。掌握20种标准氨基酸的分类与缩写是后续所有章节的基础，
  等电点(pI)的计算是高频考题，肽键的化学本质是理解蛋白质三维结构的起点。
</div>

<h3>2.1  20种标准氨基酸的结构与分类</h3>

<p><span class="kp">核心知识</span>：组成蛋白质的20种标准氨基酸均为<span class="tag-must">L-α-氨基酸</span>（甘氨酸除外——无手性中心），
通用结构为 $\mathrm{H_2N{-}CHR{-}COOH}$（两性离子形式为 $^+\mathrm{H_3N{-}CHR{-}COO^-}$）。</p>

<div class="card" style="background:var(--card-bg);border:1px solid var(--card-border);border-radius:var(--radius);padding:12px 16px;margin:14px 0">
  <strong>🔑 直觉类比</strong>：如果把蛋白质比作一篇文章，氨基酸就是26个字母——种类有限（20种），
  但排列组合产生无限多样性。三字母缩写像读音提示（如 Gly = glycine），单字母缩写是速记符号。
</div>

<table>
  <tr><th>分类</th><th>氨基酸（三字母 / 单字母）</th><th>R基特征</th></tr>
  <tr><td><strong>非极性脂肪族</strong></td><td>甘氨酸 Gly/G、丙氨酸 Ala/A、缬氨酸 Val/V、亮氨酸 Leu/L、异亮氨酸 Ile/I、脯氨酸 Pro/P</td><td>疏水，形成蛋白质核心</td></tr>
  <tr><td><strong>非极性芳香族</strong></td><td>苯丙氨酸 Phe/F、色氨酸 Trp/W</td><td>含苯环/吲哚环</td></tr>
  <tr><td><strong>含硫</strong></td><td>甲硫氨酸 Met/M、半胱氨酸 Cys/C</td><td>Met含硫醚，Cys含巯基（可形成二硫键）</td></tr>
  <tr><td><strong>极性不带电</strong></td><td>丝氨酸 Ser/S、苏氨酸 Thr/T、天冬酰胺 Asn/N、谷氨酰胺 Gln/Q、酪氨酸 Tyr/Y</td><td>侧链含羟基或酰胺基，亲水</td></tr>
  <tr><td><strong>酸性（负电）</strong></td><td>天冬氨酸 Asp/D、谷氨酸 Glu/E</td><td>侧链含第二个羧基，生理pH带负电</td></tr>
  <tr><td><strong>碱性（正电）</strong></td><td>赖氨酸 Lys/K、精氨酸 Arg/R、组氨酸 His/H</td><td>侧链含氨基/胍基/咪唑基，生理pH带正电</td></tr>
</table>

<div class="card" style="background:#fef2f2;border:2px solid #ef4444;border-radius:var(--radius);padding:12px 16px;margin:14px 0">
  <strong>⚠️ 易错辨析</strong>：<br>
  ① 酪氨酸 Tyr/Y 含酚羟基，属<strong>极性不带电</strong>，非芳香族核心（虽然含苯环）<br>
  ② 组氨酸 His/H 的pK<sub>R</sub> ≈ 6.0，是唯一在生理pH范围内可质子化/去质子化的氨基酸——赋予其缓冲能力和酶催化活性<br>
  ③ 半胱氨酸 Cys/C 的—SH可氧化形成二硫键（胱氨酸），属于非极性但因其功能重要性常单列<br>
  ④ <span class="tag-freq">考研高频</span>：酸性氨基酸 = Asp + Glu（含两个羧基）；碱性氨基酸 = Lys + Arg + His
</div>

<h3>2.2  氨基酸的手性与等电点</h3>

<p><span class="kp">手性</span>：除甘氨酸（R=H，无手性碳）外，所有标准氨基酸的α-碳均为手性中心，天然蛋白质中均为<span class="tag-must">L-构型</span>。
用Fischer投影式表示时，—NH₂在左侧。D-氨基酸存在于细菌细胞壁和某些抗生素中。</p>

<p><span class="kp">等电点 pI</span>：氨基酸净电荷为零时的pH值。对于中性氨基酸（一氨基一羧基）：
$$\mathrm{pI = \frac{pK_1 + pK_2}{2}}$$
对于酸性氨基酸（Asp, Glu）：$\mathrm{pI = \frac{pK_1 + pK_R}{2}}$（取两个较小的pK<sub>a</sub>）
对于碱性氨基酸（Lys, Arg, His）：$\mathrm{pI = \frac{pK_2 + pK_R}{2}}$（取两个较大的pK<sub>a</sub>）</p>

<div class="card" style="background:var(--card-bg);border:1px solid var(--card-border);border-radius:var(--radius);padding:12px 16px;margin:14px 0">
  <strong>🧠 动机推演</strong>：为什么酸性氨基酸pI偏酸（~3），而碱性氨基酸pI偏碱（~9-10）？
  因为pI是净电荷为零的pH——酸性氨基酸需要更酸的pH才能让第二个羧基质子化（中和负电荷），
  而碱性氨基酸需要更碱的pH才能让氨基去质子化（中和正电荷）。
</div>

<h3>2.3  茚三酮反应</h3>

<p><span class="kp">原理</span>：茚三酮与α-氨基酸的游离α-氨基反应，生成蓝紫色产物（Ruhemann紫），
可在570 nm处定量检测。脯氨酸（亚氨基酸）产生黄色产物（440 nm）。</p>

<div class="card" style="background:var(--card-bg);border:1px solid var(--card-border);border-radius:var(--radius);padding:12px 16px;margin:14px 0">
  <strong>🔑 直觉类比</strong>：茚三酮反应就像氨基酸的"指纹显影剂"——只要有游离α-氨基就能显色，
  因此蛋白质（N端游离）也能反应，而肽键内部的氨基酸残基则不能。
</div>

<h3>2.4  非标准氨基酸</h3>

<p>蛋白质中还存在翻译后修饰产生的非标准氨基酸，具有重要生物学功能：</p>

<table>
  <tr><th>非标准氨基酸</th><th>来源</th><th>功能/存在</th></tr>
  <tr><td>4-羟脯氨酸</td><td>脯氨酸羟化（需要维生素C）</td><td>胶原蛋白三股螺旋稳定（缺VC→坏血病）</td></tr>
  <tr><td>5-羟赖氨酸</td><td>赖氨酸羟化</td><td>胶原蛋白交联</td></tr>
  <tr><td>γ-羧基谷氨酸</td><td>谷氨酸γ-羧化（需要维生素K）</td><td>凝血因子（如凝血酶原）结合Ca²⁺</td></tr>
  <tr><td>硒代半胱氨酸</td><td>UGA密码子编码</td><td>"第21种氨基酸"，含硒代半胱氨酸的蛋白质</td></tr>
</table>

<div class="card" style="background:#fef2f2;border:2px solid #ef4444;border-radius:var(--radius);padding:12px 16px;margin:14px 0">
  <strong>⚠️ 易错辨析</strong>：羟脯氨酸和羟赖氨酸并非在翻译时直接掺入，而是翻译后由脯氨酰羟化酶和赖氨酰羟化酶催化羟基化形成。
  <span class="tag-freq">考研高频</span>：维生素C缺乏→脯氨酸羟化受阻→胶原合成障碍→坏血病。
</div>

<h3>2.5  肽键的化学本质</h3>

<p><span class="kp">肽键</span>：一个氨基酸的α-羧基与另一个氨基酸的α-氨基缩合形成的酰胺键（—CO—NH—）。</p>

<div class="card" style="background:var(--card-bg);border:1px solid var(--card-border);border-radius:var(--radius);padding:12px 16px;margin:14px 0">
  <strong>📌 关键特征</strong>：<br>
  ① <span class="tag-must">部分双键性质</span>：肽键中的C—N键具有约40%的双键特性（酰胺共振），键长0.132 nm（介于单键0.147 nm与双键0.127 nm之间），<strong>不能自由旋转</strong><br>
  ② <span class="tag-freq">反式构型</span>：天然蛋白质中绝大多数肽键为<span class="tag-must">反式（trans）</span>，因为空间位阻最小。例外：X-Pro肽键约6%为顺式<br>
  ③ 肽单位（C<sub>α</sub>—CO—NH—C<sub>α</sub>）的六个原子共面
</div>

<div class="card" style="background:var(--card-bg);border:1px solid var(--card-border);border-radius:var(--radius);padding:12px 16px;margin:14px 0">
  <strong>🧠 动机推演</strong>：肽键的部分双键性质是理解蛋白质结构的逻辑起点——正因为肽键不能旋转，
  多肽链主链的构象自由度仅由两个可旋转的单键决定：C<sub>α</sub>—N键（φ角）和C<sub>α</sub>—C键（ψ角）。
  这两个二面角的允许取值直接决定了蛋白质的二级结构类型。
</div>


<h2>第3章 蛋白质的一级结构</h2>

<h3>3.1  一级结构的定义</h3>

<p><span class="kp">蛋白质一级结构</span>：多肽链中氨基酸残基的线性排列顺序（N端→C端），包括二硫键的位置。
一级结构是蛋白质高级结构的基础——氨基酸序列决定了三维折叠方式。<span class="tag-must">Anfinsen实验</span>
（核糖核酸酶变性-复性实验，1972年诺贝尔化学奖）证明了这一原理。</p>

<div class="card" style="background:var(--card-bg);border:1px solid var(--card-border);border-radius:var(--radius);padding:12px 16px;margin:14px 0">
  <strong>🔑 直觉类比</strong>：一级结构就像一篇文章的段落——单词（氨基酸）的顺序决定了句子的意思。
  Anfinsen实验相当于把文章揉成一团（变性），展开后发现仍能读回原来意思（复性）——信息完全储存在序列中。
</div>

<h3>3.2  蛋白质测序方法</h3>

<p><span class="kp">Edman降解法</span>（经典方法）：用异硫氰酸苯酯（PITC）与多肽N端α-氨基反应，
在温和酸性条件下将N端氨基酸以PTH-氨基酸形式切下（不破坏其余肽键），
通过HPLC鉴定PTH-氨基酸种类，循环进行可测定约50个残基序列。</p>

<div class="card" style="background:var(--card-bg);border:1px solid var(--card-border);border-radius:var(--radius);padding:12px 16px;margin:14px 0">
  <strong>📌 Edman降解三步</strong>：<br>
  ① <strong>偶联</strong>：PITC + N端α-NH₂（碱性pH）→ PTC-肽<br>
  ② <strong>裂解</strong>：无水酸条件下，N端氨基酸以ATZ-氨基酸形式选择性裂解<br>
  ③ <strong>转化</strong>：ATZ-氨基酸 → 稳定的PTH-氨基酸 → HPLC鉴定
</div>

<p><span class="kp">质谱法</span>（现代主流）：ESI-MS（电喷雾质谱）和MALDI-TOF-MS可用于精确测定肽段质量。
串联质谱（MS/MS）通过碰撞诱导解离（CID）产生b离子和y离子系列，从碎片谱中解析氨基酸序列。</p>

<div class="card" style="background:var(--card-bg);border:1px solid var(--card-border);border-radius:var(--radius);padding:12px 16px;margin:14px 0">
  <strong>🧠 动机推演</strong>：为什么需要两种方法？Edman降解适合从头测序，但速度慢、需要较多样品；
  质谱法灵敏度极高（fmol级）、速度快，但依赖数据库匹配。两者互补。
</div>

<h3>3.3  重要测序历史：胰岛素</h3>

<p><span class="kp">Sanger测序胰岛素</span>（1953年，弗雷德里克·桑格——1958年诺贝尔化学奖）：
牛胰岛素由A链（21残基）和B链（30残基）通过两个链间二硫键（A7-B7, A20-B19）和一个链内二硫键（A6-A11）连接。
这是人类确定的第一个蛋白质序列，证明了蛋白质具有确定的氨基酸序列。</p>

<p>Sanger策略：① 用过甲酸氧化断裂二硫键，分离A、B链；
② 用多种蛋白酶（胰蛋白酶、胰凝乳蛋白酶等）分别酶解，得到重叠肽段；
③ Edman降解（当时用DNFB法——Sanger试剂）测定各肽段序列；
④ 通过重叠肽段拼接完整序列。</p>

<h3>3.4  同源蛋白质与分子进化</h3>

<p><span class="kp">同源蛋白质</span>：不同物种中执行相同功能的蛋白质（如细胞色素c、血红蛋白），
其氨基酸序列相似程度反映物种间的进化关系。<span class="tag-freq">考研高频</span>：比较细胞色素c序列差异→构建分子进化树。</p>

<p><span class="kp">不变残基</span>：对结构和功能至关重要的残基在进化中保持不变（如活性位点残基、形成二硫键的半胱氨酸）。
<span class="kp">保守替换</span>：由性质相似的氨基酸替换（如Ile↔Leu↔Val），不影响功能。</p>

<div class="card" style="background:var(--card-bg);border:1px solid var(--card-border);border-radius:var(--radius);padding:12px 16px;margin:14px 0">
  <strong>🔑 直觉类比</strong>：同源蛋白质如同同一故事在不同语言中的版本——句子结构（三级结构）高度保守，
  但个别用词（氨基酸）有变化。不变残基就像故事中的主角名字，换了就讲不通了。
</div>


<h2>第4章 蛋白质的三维结构</h2>

<div class="toc-box" style="background:var(--card-bg);border:1px solid var(--card-border);border-radius:var(--radius);padding:14px 18px;margin-bottom:18px">
  <strong>本章速览</strong>：蛋白质三维结构分为四个层次——二级、超二级、三级、四级。
  理解α-螺旋的结构参数（3.6残基/圈、i→i+4氢键）和Ramachandran图是掌握结构生物学的关键。
  血红蛋白α₂β₂是四级结构的经典范例。
</div>

<h3>4.1  二级结构</h3>

<div class="card" style="background:#fef3c7;border:2px solid #f59e0b;border-radius:var(--radius);padding:12px 16px;margin:14px 0">
  <strong>📌 α-螺旋（α-helix）— <span class="tag-must">必考</span></strong><br>
  • 右手螺旋，每圈<span class="tag-must">3.6个氨基酸残基</span>，螺距0.54 nm（即每个残基升高0.15 nm）<br>
  • 氢键模式：<span class="tag-must">第i个残基的C=O与第i+4个残基的NH形成氢键</span>（i→i+4）<br>
  • 所有肽键的C=O和N—H均参与氢键形成（除两端3-4个残基外）<br>
  • 侧链R基指向螺旋外侧，避免空间冲突<br>
  • φ ≈ −57°, ψ ≈ −47°<br>
  • 破坏α-螺旋的残基：脯氨酸（环状结构，无法形成氢键且造成"扭结"）、甘氨酸（太灵活，不利于螺旋稳定）<br>
  • 右旋α-螺旋在能量上最稳定
</div>

<div class="card" style="background:var(--card-bg);border:1px solid var(--card-border);border-radius:var(--radius);padding:12px 16px;margin:14px 0">
  <strong>🔑 直觉类比</strong>：α-螺旋就像螺旋楼梯——每个台阶（残基）旋转100°，
  每走3.6个台阶转完一圈（360°/100° ≈ 3.6）。氢键好比楼梯内侧的扶手，把所有台阶连在一起，
  让整个结构稳固。
</div>

<h3>4.1.2  β-折叠</h3>

<div class="card" style="background:#fef3c7;border:2px solid #f59e0b;border-radius:var(--radius);padding:12px 16px;margin:14px 0">
  <strong>📌 β-折叠（β-sheet）— <span class="tag-freq">高频</span></strong><br>
  • 多肽链几乎完全伸展，呈锯齿状折叠构象<br>
  • 氢键在相邻肽段之间形成（<strong>链间氢键</strong>，不同于α-螺旋的链内氢键）<br>
  • <strong>反平行β-折叠</strong>：相邻肽段方向相反，氢键排列整齐，更稳定<br>
  • <strong>平行β-折叠</strong>：相邻肽段方向相同，氢键排列倾斜，稳定性略低<br>
  • 侧链交替伸向折叠面的上方和下方
</div>

<table>
  <tr><th>特性</th><th>α-螺旋</th><th>β-折叠</th></tr>
  <tr><td>氢键类型</td><td>链内（i→i+4）</td><td>链间</td></tr>
  <tr><td>每残基升高</td><td>0.15 nm</td><td>0.32 nm（反平行）/ 0.34 nm（平行）</td></tr>
  <tr><td>侧链取向</td><td>向外</td><td>交替上下</td></tr>
  <tr><td>破坏因子</td><td>Pro、Gly、连续带电残基</td><td>大侧链残基</td></tr>
</table>

<h3>4.1.3  β-转角与无规卷曲</h3>

<p><span class="kp">β-转角（β-turn）</span>：由4个氨基酸残基组成的180°急转弯，第1个残基的C=O与第4个残基的NH形成氢键。
常含有<span class="tag-freq">甘氨酸（小而灵活）和脯氨酸（天然弯曲）</span>，位于蛋白质表面。</p>

<p><span class="kp">无规卷曲</span>：蛋白质中不规则的环状和卷曲区域，具有特定但非重复的构象。
并非真的"无规"——在同一蛋白质的不同分子中构象相同（由序列编码决定），因此应更准确地称为"环区（loop）"。</p>

<h3>4.2  Ramachandran图</h3>

<div class="card" style="background:var(--card-bg);border:1px solid var(--card-border);border-radius:var(--radius);padding:12px 16px;margin:14px 0">
  <strong>📌 核心概念</strong>：以φ（C<sub>α</sub>—N旋转角）为横轴、ψ（C<sub>α</sub>—C旋转角）为纵轴，
  标注出蛋白质主链构象的允许区域。大多数非甘氨酸残基的(φ, ψ)角落在三个允许区：<br>
  • <strong>右上区</strong>：β-折叠构象（φ ≈ −120°, ψ ≈ +120°）<br>
  • <strong>左下区</strong>：右手α-螺旋构象（φ ≈ −57°, ψ ≈ −47°）<br>
  • <strong>左上区</strong>：左手α-螺旋构象（较少见）
</div>

<div class="card" style="background:#fef2f2;border:2px solid #ef4444;border-radius:var(--radius);padding:12px 16px;margin:14px 0">
  <strong>⚠️ 易错辨析</strong>：<br>
  ① <strong>甘氨酸</strong>：侧链仅为H原子，空间位阻极小 → Ramachandran图中允许区域远大于其他残基 → 结构灵活性最高 → 常出现在转角区域<br>
  ② <strong>脯氨酸</strong>：侧链与主链N共价成环 → φ角被固定约 −60° → Ramachandran图中允许区域非常狭窄 → "结构约束者"
</div>

<div class="card" style="background:var(--card-bg);border:1px solid var(--card-border);border-radius:var(--radius);padding:12px 16px;margin:14px 0">
  <strong>🧠 动机推演</strong>：为什么需要Ramachandran图？肽键的部分双键性质消除了ω旋转自由度，
  理论上每个残基有φ、ψ两个可旋转角。但并非所有(φ, ψ)值都允许——原子间存在空间冲突。
  Ramachandran图用最简单的范德华半径计算预测了允许区域，后被大量高分辨率晶体结构验证。
  这是理论预测与实验数据完美吻合的经典案例。
</div>

<h3>4.3  超二级结构与结构域</h3>

<p><span class="kp">超二级结构（模体/motif）</span>：若干相邻二级结构单元组合形成的特定几何排列，
如βαβ单元、β-发夹、αα单元、希腊钥匙模体、β-迂回等。
是介于二级结构和结构域之间的结构层次。</p>

<p><span class="kp">结构域（domain）</span>：多肽链中独立折叠的结构单位，通常是连续的一段序列（约100-200残基），
具有相对独立的疏水核心。由Gilbert于1978年提出。按二级结构组成分为：
全α域、全β域、α/β域（βαβ交替）、α+β域（α和β区域分离）。</p>

<h3>4.4  三级结构</h3>

<p><span class="kp">三级结构</span>：整条多肽链在空间中折叠形成的完整三维结构。维持三级结构的力包括：</p>

<table>
  <tr><th>作用力类型</th><th>特征</th><th>重要性</th></tr>
  <tr><td><span class="tag-must">疏水作用</span></td><td>非极性侧链聚集成疏水核心，释放有序水分子→熵增</td><td><span class="tag-must">主要驱动力</span></td></tr>
  <tr><td>氢键</td><td>主链和侧链间形成</td><td>稳定二级结构、定向侧链</td></tr>
  <tr><td>离子键（盐桥）</td><td>带相反电荷的侧链间静电吸引</td><td>表面稳定性</td></tr>
  <tr><td>范德华力</td><td>紧密堆积原子间的弱相互作用</td><td>数量大，总体贡献显著</td></tr>
  <tr><td>二硫键</td><td>两个Cys的—SH氧化共价交联</td><td>锁定构象，多见于分泌蛋白</td></tr>
</table>

<div class="card" style="background:var(--card-bg);border:1px solid var(--card-border);border-radius:var(--radius);padding:12px 16px;margin:14px 0">
  <strong>🔑 直觉类比</strong>：疏水作用就像油滴入水——非极性侧链"被迫"聚集在内部（疏水核心），
  就像油滴自发聚成球状以最小化与水接触。极性/带电侧链则面向水环境（蛋白质表面）。
</div>

<h3>4.5  分子伴侣与蛋白质折叠</h3>

<p><span class="kp">分子伴侣</span>：辅助蛋白质正确折叠的蛋白质，自身不是最终功能分子的组成部分。
代表：<span class="tag-freq">Hsp70（DnaK）、Hsp60（GroEL/GroES）</span>。</p>

<p>GroEL/GroES系统：GroEL为双层七聚体环形桶状结构（内腔为疏水环境），GroES为"盖子"。
错误折叠/未折叠蛋白质进入GroEL内腔→GroES盖住→ATP水解驱动构象变化→内腔变为亲水→蛋白质在此"隔离室"中正确折叠→释放。</p>

<h3>4.6  四级结构：血红蛋白 α₂β₂</h3>

<p><span class="kp">四级结构</span>：由两条或以上多肽链（亚基）通过非共价相互作用组装形成的寡聚体结构。</p>

<div class="card" style="background:#fef3c7;border:2px solid #f59e0b;border-radius:var(--radius);padding:12px 16px;margin:14px 0">
  <strong>📌 血红蛋白（Hb）α₂β₂ — <span class="tag-must">必考经典</span></strong><br>
  • 4个亚基：2条α链（141残基）+ 2条β链（146残基）<br>
  • 每个亚基含一个血红素辅基（Fe²⁺结合O₂）<br>
  • 亚基间通过非共价相互作用（疏水作用、氢键、盐桥）紧密结合<br>
  • α₁β₁和α₂β₂接触面大而稳定 → αβ二聚体（基本单位）<br>
  • α₁β₂和α₂β₁接触面较松，在T态↔R态转变中发生滑动
</div>

<h3>4.7  纤维蛋白</h3>

<table>
  <tr><th>蛋白质</th><th>结构特征</th><th>功能</th></tr>
  <tr><td><strong>α-角蛋白</strong></td><td>右手α-螺旋→两股卷曲螺旋（coiled-coil）→原丝→微纤维→大纤维。富含Cys（二硫键交联）</td><td>毛发、指甲、羽毛</td></tr>
  <tr><td><strong>丝心蛋白</strong></td><td>反平行β-折叠层堆积，序列为(Gly-Ala-Gly-Ala-Gly-Ser-Gly-Ala-Ala-Gly-)ₙ</td><td>蚕丝、蜘蛛丝</td></tr>
  <tr><td><strong>胶原蛋白</strong></td><td><span class="tag-must">三股左手螺旋（非α-螺旋！）</span>缠绕成右手超螺旋，序列为<span class="tag-must">(Gly-X-Y)ₙ</span>重复。X常为Pro，Y常为Hyp</td><td>肌腱、骨骼、皮肤</td></tr>
</table>

<div class="card" style="background:#fef2f2;border:2px solid #ef4444;border-radius:var(--radius);padding:12px 16px;margin:14px 0">
  <strong>⚠️ 易错辨析</strong>：胶原蛋白的三股螺旋<strong>不是α-螺旋</strong>！
  胶原蛋白每圈3个残基（而非3.6个），螺距0.86 nm，左手螺旋。
  Gly占据每第三个位置是结构必需——胶原三股螺旋内部空间狭窄，只有H原子（Gly的侧链）才能容纳。
  <span class="tag-freq">考研高频</span>：Gly→Ala突变→空间冲突→三股螺旋不稳定→成骨不全症（OI）。
</div>


<h2>第5章 蛋白质的功能与进化</h2>

<div class="toc-box" style="background:var(--card-bg);border:1px solid var(--card-border);border-radius:var(--radius);padding:14px 18px;margin-bottom:18px">
  <strong>本章速览</strong>：本章的核心是理解蛋白质功能的分子机制——
  以肌红蛋白/血红蛋白为模型理解氧合曲线和别构效应，
  以免疫球蛋白为例理解蛋白质的结构-功能关系，
  以镰刀形细胞贫血为例理解单个氨基酸突变如何导致分子病。
</div>

<h3>5.1  肌红蛋白与血红蛋白的氧合曲线</h3>

<p><span class="kp">肌红蛋白（Mb）</span>：单体（153残基），含一个血红素。氧合曲线为<span class="tag-must">双曲线（hyperbolic）</span>，
符合Michaelis-Menten型饱和动力学，P₅₀ ≈ 2.8 torr。</p>

<p><span class="kp">血红蛋白（Hb）</span>：四聚体 α₂β₂，氧合曲线为<span class="tag-must">S形曲线（sigmoidal）</span>，
P₅₀ ≈ 26 torr。S形曲线说明O₂结合具有<span class="tag-must">正协同效应</span>——第一个O₂的结合促进后续O₂的结合。</p>

<div class="card" style="background:var(--card-bg);border:1px solid var(--card-border);border-radius:var(--radius);padding:12px 16px;margin:14px 0">
  <strong>🔑 直觉类比</strong>：肌红蛋白像一个小公寓——一个人（O₂）住进去很容易，进出门是双曲线。
  血红蛋白像一个四人宿舍——第一个人搬进去把门打开，后面的人就更方便入住（正协同效应，S形曲线）。
</div>

<table>
  <tr><th>特性</th><th>肌红蛋白 (Mb)</th><th>血红蛋白 (Hb)</th></tr>
  <tr><td>亚基数</td><td>1（单体）</td><td>4（α₂β₂四聚体）</td></tr>
  <tr><td>氧合曲线</td><td>双曲线</td><td>S形（sigmoidal）</td></tr>
  <tr><td>P₅₀</td><td>≈ 2.8 torr</td><td>≈ 26 torr</td></tr>
  <tr><td>协同性</td><td>无</td><td>正协同效应（Hill系数 ≈ 2.8）</td></tr>
  <tr><td>生理意义</td><td>在低氧分压下储存O₂</td><td>在肺部结合O₂，在组织释放O₂</td></tr>
</table>

<h3>5.2  别构效应</h3>

<div class="card" style="background:#fef3c7;border:2px solid #f59e0b;border-radius:var(--radius);padding:12px 16px;margin:14px 0">
  <strong>📌 正协同效应（Positive Cooperativity）— <span class="tag-must">必考</span></strong><br>
  • 第一个配体的结合促进后续配体的结合（O₂与Hb的结合）<br>
  • 分子机制：第一个O₂结合→血红素Fe²⁺移入卟啉平面→牵拉近端His F8→F螺旋位移→亚基界面重组→其余亚基转变为高亲和力R态<br>
  • Hill方程：$\log\frac{Y}{1-Y}=n_H\log p\mathrm{O_2} - \log P_{50}$<br>
  • Hill系数 n_H：Mb = 1.0，Hb ≈ 2.8（理论最大4.0）
</div>

<h3>5.2.2  Bohr效应与2,3-BPG</h3>

<p><span class="kp">Bohr效应</span>：H⁺和CO₂促进Hb释放O₂。在活跃代谢的组织中，CO₂↑和H⁺↑（pH↓）
→ Hb对O₂亲和力降低（P₅₀增大）→ 在组织中释放更多O₂。生理意义：代谢越旺盛的组织越需要O₂，Bohr效应精确实现按需供氧。</p>

<div class="card" style="background:var(--card-bg);border:1px solid var(--card-border);border-radius:var(--radius);padding:12px 16px;margin:14px 0">
  <strong>📌 分子机制</strong>：H⁺与β链C端His146的咪唑基结合→形成与Asp94的盐桥→稳定T态→降低O₂亲和力。
  CO₂与N端α-NH₂形成氨基甲酸（carbamate）→产生负电荷→形成盐桥→同样稳定T态。
</div>

<p><span class="kp">2,3-BPG（2,3-二磷酸甘油酸）</span>：红细胞中高浓度存在，
结合于Hb四聚体中央空穴（β₁和β₂亚基之间），与β链的三个正电荷残基（Lys82、His2、His143）形成盐桥，
<span class="tag-must">选择性地稳定T态</span>，使Hb的氧合曲线右移（P₅₀增大），促进O₂释放。</p>

<div class="card" style="background:#fef2f2;border:2px solid #ef4444;border-radius:var(--radius);padding:12px 16px;margin:14px 0">
  <strong>⚠️ 易错辨析</strong>：<br>
  ① 2,3-BPG结合的是<strong>T态（脱氧Hb）</strong>，而非R态（氧合Hb）——中央空穴在R态时变小，容纳不下BPG<br>
  ② 胎儿Hb（HbF，α₂γ₂）：γ链143位为Ser（而非His），减弱与BPG的结合→对O₂亲和力高于成人Hb→有利于从母体获取O₂<br>
  ③ <span class="tag-freq">考研高频</span>：高海拔适应——红细胞中BPG浓度升高，促进组织获氧
</div>

<h3>5.3  别构模型：MWC与KNF</h3>

<table>
  <tr><th>模型</th><th>MWC（协同模型/齐变模型）</th><th>KNF（序变模型）</th></tr>
  <tr><td>提出者</td><td>Monod, Wyman, Changeux (1965)</td><td>Koshland, Némethy, Filmer (1966)</td></tr>
  <tr><td>核心假设</td><td>所有亚基同步转换（全T或全R），T↔R平衡存在</td><td>配体结合一个亚基后，该亚基构象变化，并通过亚基界面影响相邻亚基</td></tr>
  <tr><td>对称性</td><td>始终保持对称（所有亚基相同构象）</td><td>允许不对称（混合T/R亚基）</td></tr>
  <tr><td>数学特征</td><td>方程简单（三参数）</td><td>方程复杂（多参数）</td></tr>
  <tr><td>适用性</td><td>大部分别构蛋白符合</td><td>部分酶遵循</td></tr>
</table>

<div class="card" style="background:var(--card-bg);border:1px solid var(--card-border);border-radius:var(--radius);padding:12px 16px;margin:14px 0">
  <strong>🧠 动机推演</strong>：两个模型分别抓住了别构调控的不同侧面。MWC模型的核心洞察是：
  别构蛋白存在构象平衡（T↔R），配体不"诱导"构象变化，而是选择性地结合已有构象之一
  （构象选择机制→population shift）。KNF模型强调配体结合后亚基构象沿"诱导契合"路径逐步转变。
  血红蛋白的行为介于两者之间——更接近MWC但并非严格的"全或无"。
</div>

<h3>5.4  免疫球蛋白的基本结构</h3>

<div class="card" style="background:var(--card-bg);border:1px solid var(--card-border);border-radius:var(--radius);padding:12px 16px;margin:14px 0">
  <strong>📌 IgG基本结构（Y形分子）</strong><br>
  • 2条<span class="tag-must">重链（H链）</span>（约50 kDa）+ 2条<span class="tag-must">轻链（L链）</span>（约25 kDa）<br>
  • 每条链分为<span class="tag-must">可变区（V区，N端）</span>和<span class="tag-must">恒定区（C区，C端）</span><br>
  • <strong>抗原结合位点</strong>：V_H和V_L共同构成，位于Y形分子两臂顶端（Fab片段）<br>
  • 可变区内有3个高度可变区域（CDR1-CDR3，互补决定区/高变区），直接与抗原接触<br>
  • <strong>绞链区</strong>：连接Fab和Fc的柔性区域，允许两个Fab臂独立运动<br>
  • 链间由二硫键和非共价作用连接
</div>

<div class="card" style="background:var(--card-bg);border:1px solid var(--card-border);border-radius:var(--radius);padding:12px 16px;margin:14px 0">
  <strong>🔑 直觉类比</strong>：抗体像一个Y形夹子——两个上臂的末端（Fab）专门识别和抓住特定的抗原（"分子钳"），
  而"手柄"（Fc）召唤免疫系统的其他成员（补体、巨噬细胞等）来清除被标记的入侵者。
</div>

<h3>5.5  分子病：镰刀形细胞贫血</h3>

<div class="card" style="background:#fef2f2;border:2px solid #ef4444;border-radius:var(--radius);padding:12px 16px;margin:14px 0">
  <strong>📌 镰刀形细胞贫血 — <span class="tag-must">必考经典</span></strong><br>
  • <strong>病因</strong>：HbA β链<span class="tag-must">第6位Glu→Val</span>（单个核苷酸突变：GAG→GTG，A→T颠换）<br>
  • <strong>结构后果</strong>：Val为疏水残基，在脱氧HbS表面形成一个"黏性疏水补丁"，与另一个HbS分子β链的疏水口袋（Phe85、Leu88）结合→HbS多聚化→形成纤维状沉淀<br>
  • <strong>细胞后果</strong>：红细胞从双凹圆盘形变为镰刀形→脆性增加→溶血→贫血<br>
  • <strong>遗传方式</strong>：常染色体隐性遗传（纯合子患病，杂合子为镰刀形细胞性状——有部分保护免于疟疾）<br>
  • <strong>历史意义</strong>：第一种被阐明分子机制的遗传病（Pauling, 1949年，分子病的概念由此诞生）
</div>

<div class="card" style="background:var(--card-bg);border:1px solid var(--card-border);border-radius:var(--radius);padding:12px 16px;margin:14px 0">
  <strong>🧠 动机推演</strong>：Glu与Val的区别——Glu的侧链-COO⁻带负电荷且亲水，Val的侧链-CH(CH₃)₂疏水无电荷。
  仅一个残基的变化就导致蛋白质聚合、细胞变形、疾病表型→深刻证明了Anfinsen原理：
  <strong>序列决定结构，结构决定功能</strong>。这是连接基因型与表型的典范。
</div>

<h3>5.6  蛋白质的分离纯化方法</h3>

<table>
  <tr><th>方法</th><th>原理</th><th>分离依据</th><th><span class="tag-freq">考点</span></th></tr>
  <tr><td><strong>盐析（Salting-out）</strong></td><td>高盐浓度竞争水合水→蛋白质溶解度下降→沉淀析出。常用硫酸铵</td><td>溶解度差异</td><td>不同蛋白质在不同(NH₄)₂SO₄饱和度下析出</td></tr>
  <tr><td><strong>透析（Dialysis）</strong></td><td>半透膜允许小分子通过，截留大分子蛋白质</td><td>分子大小</td><td>用于除盐、换缓冲液</td></tr>
  <tr><td><strong>凝胶过滤层析</strong></td><td>多孔凝胶珠：大蛋白无法进入孔内→先洗脱；小蛋白进入孔内→后洗脱</td><td>分子大小（流体力学半径）</td><td>大分子先出，小分子后出</td></tr>
  <tr><td><strong>离子交换层析</strong></td><td>带电树脂结合相反电荷的蛋白质，用盐梯度或pH梯度洗脱</td><td>电荷</td><td>阳离子交换（CM）：结合正电荷蛋白；阴离子交换（DEAE）：结合负电荷蛋白</td></tr>
  <tr><td><strong>亲和层析</strong></td><td>固定化配体特异性地结合目标蛋白→洗脱杂质→游离配体或变pH洗脱目标蛋白</td><td>特异性结合</td><td>分辨率极高，一步纯化</td></tr>
  <tr><td><strong>SDS-PAGE</strong></td><td>SDS变性蛋白并以1.4 g/g比例结合→消除原有电荷→所有蛋白带相同电荷密度→迁移率仅与分子量相关</td><td>分子量</td><td>小分子量迁移快；还原剂DTT/β-ME破坏二硫键</td></tr>
  <tr><td><strong>等电聚焦</strong></td><td>pH梯度中蛋白质迁移至pI位置（净电荷为零）→停止</td><td>等电点pI</td><td>分辨率极高，可区分单电荷差异</td></tr>
  <tr><td><strong>超速离心</strong></td><td>高离心力场中不同沉降系数的分子分层</td><td>分子量/形状/密度</td><td>沉降系数S（Svedberg单位）</td></tr>
</table>

<div class="card" style="background:var(--card-bg);border:1px solid var(--card-border);border-radius:var(--radius);padding:12px 16px;margin:14px 0">
  <strong>⚠️ 易错辨析</strong>：<br>
  ① 盐析 vs 透析：盐析是让蛋白质<strong>沉淀</strong>，透析是<strong>除盐</strong>。实际流程常为：盐析→透析除盐→层析精纯<br>
  ② 凝胶过滤 vs SDS-PAGE：两者都按分子大小分离，但凝胶过滤中大分子<strong>先</strong>洗脱，SDS-PAGE中大分子迁移<strong>慢</strong>（在凝胶中滞留更长）<br>
  ③ <span class="tag-freq">考研高频</span>：2D电泳 = 等电聚焦（第一维）+ SDS-PAGE（第二维），按pI和分子量两个维度分离
</div>

"""


# ═══════════════════════════════════════════════════════════════════════
#  自测题
# ═══════════════════════════════════════════════════════════════════════

QUESTIONS = [
    # ── 单选题 ──
    {
        "type": "single_choice",
        "points": 3,
        "question": "下列氨基酸中，哪个属于碱性氨基酸？",
        "options": [
            "A. 天冬氨酸 (Asp/D)",
            "B. 谷氨酸 (Glu/E)",
            "C. 精氨酸 (Arg/R)",
            "D. 酪氨酸 (Tyr/Y)"
        ],
        "answer": "C",
        "explanation": "碱性氨基酸包括赖氨酸(Lys/K)、精氨酸(Arg/R)和组氨酸(His/H)。天冬氨酸和谷氨酸是酸性氨基酸，酪氨酸是极性不带电氨基酸。",
        "pitfall": "His虽为碱性氨基酸，但其pK_R≈6.0，在生理pH(7.4)下仅部分质子化，容易被误判为中性。"
    },
    {
        "type": "single_choice",
        "points": 3,
        "question": "α-螺旋每圈含多少个氨基酸残基？",
        "options": [
            "A. 3.0",
            "B. 3.6",
            "C. 4.0",
            "D. 5.4"
        ],
        "answer": "B",
        "explanation": "经典右手α-螺旋每圈含3.6个氨基酸残基，螺距0.54 nm，每个残基升高0.15 nm。这是Pauling和Corey提出α-螺旋模型的核心参数之一。",
        "pitfall": "胶原蛋白的三股螺旋每圈3个残基（非α-螺旋），考试中容易把两种螺旋参数混淆。务必区分：α-螺旋=3.6残基/圈，胶原螺旋=3残基/圈。"
    },
    {
        "type": "single_choice",
        "points": 3,
        "question": "α-螺旋中氢键的形成模式是：",
        "options": [
            "A. 第i个残基的C=O与第i+3个残基的NH",
            "B. 第i个残基的C=O与第i+4个残基的NH",
            "C. 第i个残基的NH与第i+3个残基的C=O",
            "D. 第i个残基的NH与第i+5个残基的C=O"
        ],
        "answer": "B",
        "explanation": "α-螺旋中每个肽键的C=O与沿螺旋方向第4个残基（i+4）的NH形成氢键，这是α-螺旋最特征性的结构参数。3₁₀螺旋为i→i+3，π螺旋为i→i+5。",
        "pitfall": "注意氢键方向：C=O → H-N，而非N-H → O=C。是i的C=O指向i+4的NH，方向由N端向C端。"
    },
    {
        "type": "single_choice",
        "points": 4,
        "question": "镰刀形细胞贫血的分子基础是血红蛋白β链上哪个氨基酸突变？",
        "options": [
            "A. 第6位Glu→Lys",
            "B. 第6位Glu→Val",
            "C. 第6位Val→Glu",
            "D. 第8位Glu→Val"
        ],
        "answer": "B",
        "explanation": "HbS是β链第6位谷氨酸(Glu)突变为缬氨酸(Val)，即Glu6→Val。单个亲水/带电残基被疏水残基替换→脱氧HbS表面产生疏水补丁→聚合→镰刀形细胞。",
        "pitfall": "注意方向：是Glu→Val不是Val→Glu；位置是β链第6位不是第8位。这一突变也是第一种在分子水平被阐明的遗传病。"
    },
    {
        "type": "single_choice",
        "points": 4,
        "question": "维持蛋白质三级结构的主要驱动力是：",
        "options": [
            "A. 氢键",
            "B. 离子键（盐桥）",
            "C. 疏水作用",
            "D. 二硫键"
        ],
        "answer": "C",
        "explanation": "疏水作用（非极性侧链从水中聚集到蛋白质内部）是蛋白质折叠的主要热力学驱动力。虽然氢键、离子键和范德华力也贡献于结构稳定性，但疏水作用贡献了主要的折叠自由能。",
        "pitfall": "二硫键是共价键，强度最大，但它锁定的是已经折叠好的构象，不是折叠过程的驱动力。细胞质蛋白通常不含二硫键，说明折叠不依赖二硫键。"
    },
    {
        "type": "single_choice",
        "points": 4,
        "question": "关于肽键的化学本质，下列叙述错误的是：",
        "options": [
            "A. 肽键具有部分双键性质，不能自由旋转",
            "B. 天然蛋白质中绝大多数肽键为反式构型",
            "C. 肽键的C—N键长介于典型的单键和双键之间",
            "D. X-Pro肽键在任何情况下都是反式构型"
        ],
        "answer": "D",
        "explanation": "前三项均正确。D错误：X-Pro肽键约6%为顺式构型，因为脯氨酸的环状结构降低了顺反两种构型的能量差异。反式构型在X-Pro中仍占优势（约94%），但顺式比例明显高于其他肽键。",
        "pitfall": "脯氨酸的特殊性不仅体现在破坏α-螺旋，还体现在其前一个肽键(X-Pro)有较高的顺式构型比例。这是脯氨酸作为'结构捣乱者'的另一面。"
    },
    {
        "type": "single_choice",
        "points": 4,
        "question": "胶原蛋白的氨基酸序列特征性重复模体是：",
        "options": [
            "A. (Gly-Pro-Pro)ₙ",
            "B. (Gly-X-Y)ₙ",
            "C. (Ala-Gly-Ser)ₙ",
            "D. (Pro-Hyp-Gly)ₙ"
        ],
        "answer": "B",
        "explanation": "胶原蛋白的序列特征为(Gly-X-Y)ₙ重复，其中X常为脯氨酸(Pro)，Y常为羟脯氨酸(Hyp)。每第三个位置必须是Gly，因为三股螺旋内部空间极其狭窄，只有H原子（Gly的侧链）能够被容纳。",
        "pitfall": "A虽也是常见序列（特别是胶原蛋白的模型肽），但(B)是更一般的形式。考题通常考察(Gly-X-Y)ₙ这一概括性表达，以及Gly为何必不可少。"
    },
    {
        "type": "single_choice",
        "points": 4,
        "question": "关于血红蛋白(Hb)和肌红蛋白(Mb)，下列描述正确的是：",
        "options": [
            "A. Hb的氧合曲线为双曲线",
            "B. Mb的氧合曲线为S形曲线",
            "C. Hb具有正协同效应，Mb不具有协同效应",
            "D. Mb的P₅₀大于Hb的P₅₀"
        ],
        "answer": "C",
        "explanation": "Hb四聚体具有正协同效应（S形氧合曲线），Mb单体无协同效应（双曲线）。Hb的P₅₀≈26 torr，Mb的P₅₀≈2.8 torr，因此Mb对O₂亲和力远高于Hb。",
        "pitfall": "P₅₀越小表示亲和力越高，不是越大越高。容易混淆：Mb P₅₀小(2.8)→高亲和力→适合储氧；Hb P₅₀大(26)→低亲和力→适合在组织释放O₂。"
    },
    {
        "type": "single_choice",
        "points": 4,
        "question": "2,3-BPG对血红蛋白的调节机制是：",
        "options": [
            "A. 与R态Hb结合，提高O₂亲和力",
            "B. 与T态Hb结合，降低O₂亲和力",
            "C. 与血红素Fe²⁺竞争O₂结合位点",
            "D. 与O₂协同结合，促进O₂在肺部结合"
        ],
        "answer": "B",
        "explanation": "2,3-BPG结合于Hb四聚体中央空穴（β链之间），选择性地稳定T态（脱氧Hb），使氧合曲线右移，降低O₂亲和力，促进O₂在组织中释放。胎儿HbF因γ链143位Ser而非His，与BPG结合减弱，O₂亲和力更高。",
        "pitfall": "BPG与Hb的结合位点在亚基间中央空穴（正电荷残基），而非血红素铁。它不直接占据O₂结合位点，而是通过稳定T态间接降低O₂亲和力。"
    },
    {
        "type": "single_choice",
        "points": 4,
        "question": "下列关于凝胶过滤层析的叙述，正确的是：",
        "options": [
            "A. 大分子蛋白质先被洗脱",
            "B. 小分子蛋白质先被洗脱",
            "C. 洗脱顺序与分子电荷相关",
            "D. 洗脱顺序与等电点相关"
        ],
        "answer": "A",
        "explanation": "凝胶过滤（分子筛层析）按分子大小分离：大蛋白质无法进入凝胶珠内部孔道，直接流过柱床间隙→先洗脱；小蛋白质能进入孔内→路径更长→后洗脱。分离依据是流体力学半径而非电荷或pI。",
        "pitfall": "注意与SDS-PAGE区别：SDS-PAGE中大分子迁移慢（在凝胶基质中受阻更大），凝胶过滤中大分子先出（不进孔）。两者原理不同——凝胶过滤是'筛分'，SDS-PAGE是'电泳迁移+筛分'。"
    },
    # ── 判断题 ──
    {
        "type": "true_false",
        "points": 2,
        "question": "所有的20种标准氨基酸都具有手性中心（α-碳为手性碳）。",
        "answer": "错误",
        "explanation": "甘氨酸(Gly/G)的侧链为H原子，α-碳上连接两个相同的H原子，不具有手性中心。其余19种氨基酸的α-碳均为手性碳，天然蛋白质中均为L-构型。",
        "pitfall": "甘氨酸是最简单的氨基酸，也是唯一没有手性的标准氨基酸。正因为没有手性，它在Ramachandran图中允许的区域远大于其他氨基酸。"
    },
    {
        "type": "true_false",
        "points": 2,
        "question": "脯氨酸(Pro/P)是α-螺旋的强破坏者，因为它无法形成链内氢键且其环状结构引入'扭结'。",
        "answer": "正确",
        "explanation": "脯氨酸的α-N原子参与吡咯环形成，缺少形成氢键所需的N-H基团（它是亚氨基酸），无法参与α-螺旋的i→i+4氢键。同时环状结构固定φ角，在α-螺旋中引入弯曲，破坏螺旋的规整性。",
        "pitfall": "脯氨酸常位于α-螺旋的N端（前3个残基内）或转角区域。它不是完全不出现于螺旋中——但出现在螺旋内部会中断螺旋。"
    },
    {
        "type": "true_false",
        "points": 3,
        "question": "Bohr效应指的是H⁺和CO₂促进血红蛋白释放O₂，是代谢旺盛组织获取更多O₂的生理调节机制。",
        "answer": "正确",
        "explanation": "Bohr效应由Christian Bohr于1904年发现：pH降低(H⁺↑)和CO₂↑使Hb对O₂亲和力下降→氧合曲线右移→P₅₀增大→在组织中释放更多O₂。分子机制：H⁺与β链His146结合，CO₂与N端形成氨基甲酸，均稳定T态。",
        "pitfall": "注意Bohr效应和Haldane效应的区别：Bohr效应=H⁺/CO₂影响O₂亲和力；Haldane效应=O₂结合影响CO₂/H⁺的运输。两者互为热力学偶联的不同方面。"
    },
    {
        "type": "true_false",
        "points": 3,
        "question": "Anfinsen的核糖核酸酶变性-复性实验证明了蛋白质的一级结构决定其三维结构。",
        "answer": "正确",
        "explanation": "Anfinsen实验(1957年)：用尿素（破坏氢键/疏水作用）和β-巯基乙醇（还原二硫键）使核糖核酸酶完全变性失活→透析去除变性剂和还原剂→酶活性自发恢复。证明氨基酸序列包含了蛋白质折叠的全部信息。1972年获诺贝尔化学奖。",
        "pitfall": "Anfinsen实验的正确性是有条件的：①体外简单体系；②小蛋白（124残基）；③不需要分子伴侣。在大而复杂的蛋白质中，体内折叠通常需要分子伴侣辅助。"
    },
    {
        "type": "true_false",
        "points": 3,
        "question": "在SDS-PAGE电泳中，蛋白质的迁移速率与其等电点成正比。",
        "answer": "错误",
        "explanation": "SDS-PAGE中蛋白质迁移速率主要取决于分子量（小蛋白迁移快）。SDS以约1.4 g/g蛋白质的比例结合，使所有蛋白质带上大量负电荷（掩盖原有电荷差异），且SDS-蛋白质复合物呈棒状，因此迁移率仅与分子量的对数呈线性关系。",
        "pitfall": "SDS-PAGE分离依据是分子量而非等电点或原有电荷。等电聚焦(IEF)才是按pI分离的方法。2D电泳=第一维IEF(pI)+第二维SDS-PAGE(分子量)。"
    },
    # ── 填空题 ──
    {
        "type": "fill_blank",
        "points": 2,
        "question": "酸性氨基酸包括______和______（写中文全称或三字母缩写）。",
        "answer": "天冬氨酸(Asp)和谷氨酸(Glu)",
        "explanation": "20种标准氨基酸中含两个羧基的酸性氨基酸只有两种：天冬氨酸(Asp/D)和谷氨酸(Glu/E)。在生理pH(~7.4)下，其侧链羧基去质子化(-COO⁻)，带负电荷。",
        "pitfall": "天冬酰胺(Asn)和谷氨酰胺(Gln)侧链为酰胺而非羧基，属于极性不带电氨基酸，不属于酸性氨基酸。二者的名称相似容易混淆。"
    },
    {
        "type": "fill_blank",
        "points": 2,
        "question": "组成蛋白质的20种标准氨基酸中，唯一在生理pH范围内具有缓冲能力的氨基酸是______（写三字母缩写），其侧链pK_R约为______。",
        "answer": "His；6.0",
        "explanation": "组氨酸(His/H)侧链咪唑基的pK_R ≈ 6.0，在生理pH(7.4)附近可发生质子化/去质子化可逆转变，赋予蛋白质缓冲能力，并使其成为许多酶的催化关键残基（如丝氨酸蛋白酶催化三联体）。",
        "pitfall": "虽然Cys的pK_R≈8.3也在生理pH附近，但Cys在蛋白质内部多以二硫键形式存在，游离—SH通常不参与酸碱缓冲。His是教科书标准的'缓冲氨基酸'。"
    },
    {
        "type": "fill_blank",
        "points": 3,
        "question": "血红蛋白的别构效应模型中，MWC模型假设所有亚基同步在______态和______态之间转换，配体选择性结合______态。（填T或R）",
        "answer": "T；R；R",
        "explanation": "MWC（齐变/协同）模型假设：①别构蛋白存在T态（紧张态，低亲和力）和R态（松弛态，高亲和力）的构象平衡；②所有亚基同步转换（全T或全R），始终保持分子对称性；③配体(O₂)选择性结合R态→拉动平衡向R态移动→正协同效应。",
        "pitfall": "MWC不假设配体'诱导'构象变化，而是认为两种构象预先存在（构象选择/population shift）。这是MWC与KNF模型的根本哲学差异。"
    },
    {
        "type": "fill_blank",
        "points": 3,
        "question": "免疫球蛋白IgG由______条重链和______条轻链组成，抗原结合位点位于______区和______区共同构成的Fab片段顶端。",
        "answer": "2；2；V_H；V_L",
        "explanation": "IgG是Y形分子：2条重链(H，~50 kDa) + 2条轻链(L，~25 kDa)。每对H-L链分为Fab（抗原结合片段，含V_H和V_L）和Fc（可结晶片段）。V_H和V_L中各有3个互补决定区(CDR)直接与抗原表位接触。",
        "pitfall": "每条链都有V区和C区。抗原结合位点由V_H + V_L共同构成（非单独的重链或轻链可变区）。"
    },
    # ── 简答题 ──
    {
        "type": "short_answer",
        "points": 10,
        "question": "简述α-螺旋的结构特征（包括每圈残基数、氢键模式、螺距、φ和ψ角），并说明为什么脯氨酸和甘氨酸不利于α-螺旋的形成。",
        "answer": "【α-螺旋结构特征】\n① 右手螺旋，每圈3.6个氨基酸残基，螺距0.54 nm（每残基升高0.15 nm）。\n② 氢键模式：第i个残基的C=O与第i+4个残基的N-H形成链内氢键，氢键方向大致平行于螺旋轴。\n③ 所有肽键的C=O和N-H均参与氢键（除两端3-4个残基），使α-螺旋非常稳定。\n④ 典型二面角：φ ≈ −57°, ψ ≈ −47°。\n⑤ 侧链R基指向螺旋外侧。\n\n【脯氨酸破坏α-螺旋的原因】\n① 脯氨酸是亚氨基酸，α-N原子参与吡咯环形成，缺少形成氢键所需的N-H基团。\n② 环状结构固定φ角（≈ −60°），在螺旋中引入\"扭结\"，破坏螺旋规整性。\n\n【甘氨酸破坏α-螺旋的原因】\n① 甘氨酸侧链仅为H原子，空间位阻极小，主链构象灵活性过高（Ramachandran图中允许区极大）。\n② 折叠成固定φ/ψ角的α-螺旋会造成较大的构象熵损失（ΔS为负且绝对值大），热力学上不利。",
        "explanation": "这道题是结构生物化学的经典简答题。需要全面掌握α-螺旋的结构参数和理解脯氨酸、甘氨酸的化学结构特点如何从不同角度破坏螺旋。",
        "pitfall": "①注意区分α-螺旋(3.6残基/圈)、3₁₀螺旋(3残基/圈、i→i+3)、π螺旋(4.4残基/圈、i→i+5)。②不要漏答氢键方向。③Pro和Gly破坏螺旋的原因不同——Pro是'结构刚性'问题，Gly是'结构柔性'问题——不能相互替代解释。"
    },
    {
        "type": "short_answer",
        "points": 10,
        "question": "试述镰刀形细胞贫血的分子机制及其在分子医学史上的重要意义。",
        "answer": "【分子机制】\n① 基因突变：Hb β链第6位密码子GAG→GTG（A→T颠换），导致谷氨酸(Glu)突变为缬氨酸(Val)。\n② 结构改变：Glu侧链−CH₂−CH₂−COO⁻为亲水带电基团，位于HbS表面；Val侧链−CH(CH₃)₂为疏水基团。突变后在脱氧HbS分子表面产生一个\"黏性疏水补丁\"。\n③ 聚合过程：一个HbS分子的疏水补丁与另一个脱氧HbS分子β链上的疏水口袋（含Phe85、Leu88）互补结合→HbS分子线性多聚化→形成14条纤维拧成的纤维束→在红细胞内沉淀。\n④ 细胞后果：纤维束使红细胞从双凹圆盘形扭曲为镰刀形→变形性下降→通过微循环时破裂→溶血性贫血。同时镰刀形细胞堵塞毛细血管→组织缺氧/疼痛危象。\n⑤ 氧合HbS不发生聚合（疏水补丁被掩埋），因此脱氧是聚合的必要条件。\n\n【历史意义】\n① Linus Pauling于1949年发现HbS与HbA的电泳差异，首次将疾病归因于\"分子\"的异常，创造了\"分子病（molecular disease）\"概念。\n② Vernon Ingram于1956年用\"指纹图谱\"技术确定突变为Glu6→Val，首次将遗传病精确定位到单个氨基酸水平。\n③ 这一发现深刻验证了\"基因→蛋白质序列→蛋白质结构→蛋白质功能→表型\"的中心关系链，是现代分子医学的奠基石之一。",
        "explanation": "镰刀形细胞贫血是连接遗传学、生物化学和医学的经典范例，高频出现在各大高校考研试题中。需要从基因突变→氨基酸改变→蛋白质结构变化→聚合机制→细胞形态→临床症状逐级阐述。",
        "pitfall": "①突变是Glu→Val，不要写反。②是β链第6位，不是α链。③氧合HbS不聚合，是脱氧HbS才聚合——这是理解疾病间歇性发作的关键。④不要忘记阐述历史意义（Pauling + Ingram的贡献），这是常见踩分点。"
    },
    {
        "type": "short_answer",
        "points": 10,
        "question": "列表比较五种常用蛋白质分离纯化方法（盐析、凝胶过滤层析、离子交换层析、SDS-PAGE、亲和层析）的分离原理和分离依据，并说明在实际纯化流程中这些方法的典型使用顺序。",
        "answer": "【方法比较】\n① 盐析：高盐竞争水合水→降低蛋白质溶解度→沉淀析出。分离依据：溶解度差异。常用硫酸铵分级沉淀。\n② 凝胶过滤层析：多孔凝胶珠筛分→大蛋白不进孔先洗脱，小蛋白进孔后洗脱。分离依据：分子大小（流体力学半径）。\n③ 离子交换层析：带电树脂与相反电荷蛋白结合→盐/pH梯度洗脱。分离依据：电荷差异（阳离子交换CM结合正电蛋白；阴离子交换DEAE结合负电蛋白）。\n④ SDS-PAGE：SDS变性并均匀结合蛋白→消除电荷差异→迁移率仅与分子量相关。分离依据：分子量。\n⑤ 亲和层析：固定化配体特异性结合目标蛋白→洗脱杂质→特异洗脱目标蛋白。分离依据：特异性生物识别（如抗原-抗体、酶-底物）。\n\n【典型纯化流程】\n① 粗提：组织匀浆→离心取上清→盐析（硫酸铵分级沉淀）→去除大量杂蛋白。\n② 脱盐：透析或凝胶过滤除盐、换缓冲液。\n③ 中度纯化：离子交换层析或疏水层析。\n④ 精细纯化：亲和层析（如果可用）或凝胶过滤层析。\n⑤ 纯度鉴定：SDS-PAGE检测纯度和分子量。\n\n总体原则：先低分辨率高容量（盐析），后高分辨率低容量（亲和层析）。每一步后检测比活性，直到比活性不再提高。",
        "explanation": "蛋白质纯化是生物化学实验的核心技能，考研常考各方法原理和流程设计。回答要点：每种方法四个字概括（原理+依据），流程体现逐步提高分辨率的逻辑。",
        "pitfall": "①盐析依据是溶解度而非分子量——虽然大分子蛋白质确实更易被盐析，但原理是竞争水合水。②凝胶过滤中大分子先出 vs SDS-PAGE中小分子先到——容易混淆。③不要遗漏亲和层析——它是唯一基于特异性识别而非物理化学性质差异的方法。④强调比活性监测——每一步后检测酶活性/总蛋白，计算比活性。"
    },
    {
        "type": "short_answer",
        "points": 10,
        "question": "解释蛋白质折叠的热力学驱动力。为什么说疏水作用是蛋白质折叠的主要驱动力？氢键在折叠中的作用是什么？",
        "answer": "【折叠热力学概述】\n蛋白质从伸展态(U)折叠为天然态(N)：ΔG_fold = ΔH_fold − TΔS_fold。在生理条件下ΔG_fold通常为−20至−65 kJ/mol（较小的净稳定化自由能）。\n\n【疏水作用为主要驱动力】\n① 在伸展态中，非极性侧链周围的水分子被迫形成有序的\"笼状\"结构（冰山结构/笼形水合物），水分子熵降低（ΔS_w为负）。\n② 折叠时非极性侧链聚集到蛋白质内部形成疏水核心→原来被\"冻结\"在非极性表面周围的有序水分子被释放到本体溶液中→水分子熵大幅增加（ΔS_w为正且数值大）。\n③ 这个巨大的熵增是蛋白质折叠的主要热力学驱动力。ΔG疏水贡献约占总折叠自由能的60-80%。\n④ 从焓的角度：疏水核心中非极性基团间的范德华接触也贡献有利的ΔH。\n\n【氢键的作用】\n① 在伸展态中，主链C=O和N-H与水分子形成氢键（能量上有利）。\n② 折叠时这些基团间的氢键被蛋白质内部氢键（α-螺旋、β-折叠中的链内/链间氢键）替代，氢键的净焓变不大（原有氢键被新氢键替代）。\n③ 但未形成氢键的C=O或N-H埋在疏水环境中是高度不利的（ΔG约+20 kJ/mol/基团），因此所有内部极性基团必须形成氢键。\n④ 氢键的作用是\"定向和选择\"折叠路径——确保形成正确的二级结构和三级结构，而非提供主要的净自由能驱动力。",
        "explanation": "这是蛋白质化学中关于折叠热力学的核心问题，需要从疏水作用的熵驱动本质和氢键的'定向而非驱动'角色两个角度回答。",
        "pitfall": "①最常见的错误：认为氢键是蛋白质折叠的主要驱动力。氢键在天然态和伸展态中都存在（折叠态是蛋白内部氢键，伸展态是蛋白-水氢键），净焓变化不大。②疏水作用本质是熵驱动（水分子释放），不是非极性基团间的'吸引力'。③注意区分折叠的驱动力（疏水作用）与结构的稳定力（氢键、范德华力、盐桥等共同贡献）。"
    },
]


def main():
    knowledge_path = "/workspace/output/生物化学_第2-5章_知识精讲.html"
    test_path = "/workspace/output/生物化学_第2-5章_自测题.html"

    save_knowledge_html(KNOWLEDGE_BODY, knowledge_path, "生物化学 第2-5章 — 知识精讲")
    print(f"[OK] 知识精讲已生成: {knowledge_path}")

    save_test(
        QUESTIONS,
        test_path,
        "生物化学 第2-5章 — 互动自测题",
        subtitle="第一篇 结构生物化学 · 氨基酸、蛋白质结构与功能",
        duration_minutes=45,
    )
    print(f"[OK] 自测题已生成: {test_path}")

    # 统计
    total = sum(q["points"] for q in QUESTIONS)
    print(f"\n统计: 共{len(QUESTIONS)}题, 满分{total}分")
    types = {}
    for q in QUESTIONS:
        t = q["type"]
        types[t] = types.get(t, 0) + 1
    for t, c in types.items():
        print(f"  {t}: {c}题")


if __name__ == "__main__":
    main()