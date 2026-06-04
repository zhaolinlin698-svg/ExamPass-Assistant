#!/usr/bin/env python3
"""Generate Chapters 14-18 knowledge guide and self-test in deep-learning mode."""

import sys
sys.path.insert(0, '/workspace/ExamPass-Assistant')
from scripts.template_engine import save_knowledge_html, save_test

# ═══════════════════════════════════════════════════════════════════
# 知识精讲 body HTML
# ═══════════════════════════════════════════════════════════════════

body = r"""

<h2>第一篇 · 结构生物化学 —— 第14-18章 知识精讲</h2>

<p><span class="kp">本篇聚焦从「分子如何通讯」到「能量如何转化」的宏大主题。</span><span class="exp">第14章讲细胞如何感知外界信号并做出响应（信号转导），第15章讲物质如何穿越生物膜（运输），第16章建立能量转换的热力学语言（生物能学），第17章揭示线粒体中营养物氧化与ATP合成的耦合机制（生物氧化），第18章则展示叶绿体如何利用光能将CO₂固定为有机物（光合作用）。这五章合在一起，构成了从结构到功能的关键桥梁。</span></p>

<hr>

<h2>第14章 激素与信号转导 <span class="tag-must">必考</span></h2>

<blockquote><strong>核心问题</strong>：多细胞生物中，一个细胞如何告诉另一个细胞该做什么？远处的信号如何被精确接收、放大并转化为特定的细胞响应？</blockquote>

<h3>14.1 激素的定义与分类 <span class="tag-must">必考</span></h3>

<p><span class="kp">激素（Hormone）</span><span class="exp">是由内分泌腺或特定细胞分泌的、经血液循环运送到靶组织、在极低浓度（nM-pM）下即可发挥调节作用的化学信使。激素不直接参与代谢反应，而是作为「信号」调控细胞已有的代谢程序。</span></p>

<p><strong>直觉类比</strong>：激素好比城市的广播系统——市长办公室（内分泌腺）不需要亲自跑到每家每户，只需要通过广播（血液循环）发布指令，有收音机（受体）的家庭（靶细胞）才能接收并执行。</p>

<p><strong>动机推演</strong>：为什么进化出了激素系统？单细胞生物直接与环境交换物质，不需要通讯系统。多细胞生物的细胞需要分工协作，但细胞之间不能物理连接——激素解决了「远距离协调」的问题。从进化上看，激素系统比神经系统更古老（植物只有激素系统），也更能维持长时程响应。</p>

<h4>14.1.1 水溶性激素 vs 脂溶性激素 <span class="tag-freq">高频</span></h4>

<table>
<tr><th>特征</th><th>水溶性激素</th><th>脂溶性激素</th></tr>
<tr><td><span class="kp">代表</span></td><td>肽类激素（胰岛素、胰高血糖素）、儿茶酚胺（肾上腺素）、多数垂体激素</td><td>类固醇激素（皮质醇、醛固酮、性激素）、甲状腺激素(T₃/T₄)、维甲酸</td></tr>
<tr><td><span class="kp">受体位置</span></td><td>细胞膜表面受体（跨膜蛋白）</td><td>胞内受体（核受体超家族，位于胞质或核内）</td></tr>
<tr><td><span class="kp">是否需要第二信使</span></td><td>是（cAMP、IP₃、DAG、Ca²⁺等）</td><td>否（激素-受体复合物直接作为转录因子）</td></tr>
<tr><td><span class="kp">响应速度</span></td><td>快（秒-分钟），通过酶级联放大</td><td>慢（小时-天），需要转录和翻译</td></tr>
<tr><td><span class="kp">效应持续时间</span></td><td>短（信号终止机制快速关闭）</td><td>长（mRNA和蛋白质的半衰期决定）</td></tr>
<tr><td><span class="kp">能否穿越质膜</span></td><td>不能（亲水，被脂双层阻隔）</td><td>能（疏水，穿越脂双层后与胞内受体结合）</td></tr>
</table>

<blockquote><strong>易错辨析</strong>：(1) 肾上腺素是水溶性的（属于氨基酸衍生物/儿茶酚胺），但甲状腺激素T₃/T₄虽然也是氨基酸衍生物（酪氨酸衍生物），却是脂溶性的——因为其分子中碘原子的存在显著增加了疏水性；(2) 「肽类激素=水溶性」但胰岛素例外吗？不，胰岛素也是水溶性的，它在血液中以游离形式运输，作用于细胞膜上的胰岛素受体（RTK）。</blockquote>

<h3>14.2 信号转导的基本模式 <span class="tag-key">重点</span></h3>

<p><span class="kp">信号转导（Signal Transduction）</span><span class="exp">是指细胞将胞外信号分子（第一信使）携带的信息转化为胞内信号（第二信使），并逐级放大，最终引起特定细胞响应的全过程。</span></p>

<div style="background:var(--card-bg);border:1px solid var(--card-border);border-radius:var(--radius);padding:14px 18px;margin:12px 0;">
<p style="margin:0;text-align:center;font-weight:700;">信号转导三阶段：<span style="color:#2563eb;">接收（Reception）</span> → <span style="color:#2563eb;">转导（Transduction）</span> → <span style="color:#2563eb;">响应（Response）</span></p>
</div>

<ul>
<li><span class="kp">接收</span><span class="exp">：第一信使（配体）与受体的特异性结合。受体-配体结合服从可饱和性、高亲和力和特异性——类似酶-底物结合。</span></li>
<li><span class="kp">转导</span><span class="exp">：受体构象变化→激活下游效应器→产生第二信使→信号逐级放大。一级放大可达10⁴-10⁶倍——这就是为什么极低浓度的激素能引起显著的细胞响应。</span></li>
<li><span class="kp">响应</span><span class="exp">：最终效应包括酶活性改变（快速）、基因表达改变（慢速）、细胞骨架重排、细胞分裂/分化/凋亡等。</span></li>
</ul>

<p><strong>信号转导的共同特征</strong>：(1) 特异性（特定的受体识别特定的配体）；(2) 放大（酶级联，每个催化步骤放大信号）；(3) 模块化（不同通路共享组件，如cAMP、Ca²⁺被多种信号使用）；(4) 交叉对话（cross-talk，不同信号通路之间相互影响）；(5) 去敏感/适应（持续刺激下响应减弱，防止过度反应）。</p>

<h3>14.3 G蛋白偶联受体（GPCR）信号通路 <span class="tag-must">必考</span></h3>

<p><span class="kp">GPCR超家族</span><span class="exp">是人类基因组中最大的受体家族（~800个成员），具有7次跨膜α螺旋的共同结构。其命名源自与异三聚体G蛋白的偶联。约34%的FDA批准药物以GPCR为靶点——足见其在药理学中的核心地位。</span></p>

<h4>14.3.1 异三聚体G蛋白的激活/失活循环 <span class="tag-must">必考</span></h4>

<div style="background:var(--card-bg);border:1px solid var(--card-border);border-radius:var(--radius);padding:14px 18px;margin:12px 0;">
<p style="margin:0 0 8px 0;font-weight:700;">G蛋白分子开关的GTP/GDP循环（核心机制）：</p>
<p style="margin:0;"><strong>静息态</strong>：Gα·GDP + Gβγ 三聚体（Gα与GDP结合，信号关闭）</p>
<p style="margin:2px 0;">↓ 配体结合GPCR → 受体构象变化 → 促进Gα释放GDP</p>
<p style="margin:2px 0;"><strong>激活态</strong>：Gα·GTP（Gα与GTP结合后与Gβγ解离）</p>
<p style="margin:2px 0;">↓ Gα·GTP 和 Gβγ 各自激活下游效应器</p>
<p style="margin:2px 0;"><strong>终止</strong>：Gα的固有GTP酶活性 → GTP水解为GDP</p>
<p style="margin:2px 0;"><strong>复归</strong>：Gα·GDP 重新与 Gβγ 结合 → 回到静息态</p>
</div>

<p><strong>直觉类比</strong>：G蛋白像一个「定时炸弹」——静息时Gα绑着GDP（安全栓插着），GPCR激活后拔出GDP换上GTP（拔安全栓，倒计时开始），Gα·GTP和Gβγ各自扩散去激活下游（炸弹分开行动），Gα的GTP酶就是内置的「自动拆弹器」（GTP→GDP，定时归零后自动安全）。</p>

<table>
<tr><th>G蛋白类型</th><th>下游效应器</th><th>第二信使</th><th>效应</th></tr>
<tr><td><span class="kp">Gα<sub>s</sub></span></td><td>激活腺苷酸环化酶(AC)</td><td>cAMP ↑</td><td>激活PKA</td></tr>
<tr><td><span class="kp">Gα<sub>i</sub></span></td><td>抑制腺苷酸环化酶</td><td>cAMP ↓</td><td>抑制PKA</td></tr>
<tr><td><span class="kp">Gα<sub>q</sub></span></td><td>激活磷脂酶C(PLC)</td><td>IP₃↑ + DAG↑</td><td>释放Ca²⁺ + 激活PKC</td></tr>
</table>

<blockquote>易错：霍乱毒素催化Gα<sub>s</sub>的ADP-核糖基化，抑制其GTP酶活性 → Gα<sub>s</sub>·GTP持续激活 → cAMP持续升高 → 肠道上皮细胞大量分泌Cl⁻和水 → 严重腹泻。而百日咳毒素催化Gα<sub>i</sub>的ADP-核糖基化，阻止Gα<sub>i</sub>被受体激活 → Gα<sub>i</sub>无法抑制AC → cAMP升高。两者的靶点不同，但都导致cAMP异常。</blockquote>

<h4>14.3.2 cAMP信号通路 <span class="tag-must">必考</span></h4>

<div style="background:var(--card-bg);border:1px solid var(--card-border);border-radius:var(--radius);padding:14px 18px;margin:12px 0;">
<p style="margin:0;font-weight:700;">cAMP通路主线：</p>
<p style="margin:2px 0;">配体(如肾上腺素) → GPCR → Gα<sub>s</sub>·GTP → 腺苷酸环化酶(AC) → ATP→cAMP → PKA → 磷酸化靶蛋白(如糖原磷酸化酶激酶)</p>
</div>

<p><span class="kp">cAMP</span><span class="exp">（3',5'-环腺苷酸）由ATP经腺苷酸环化酶催化生成，被磷酸二酯酶(PDE)水解为5'-AMP而失活。咖啡因和茶碱通过抑制PDE而延长cAMP信号——这就是为什么喝咖啡能提神（之一）。</span></p>

<p><span class="kp">PKA（cAMP依赖的蛋白激酶A）</span><span class="exp">：静息时PKA是四聚体(R₂C₂)——两个调节亚基(R)抑制两个催化亚基(C)。cAMP与R亚基结合 → R亚基构象变化 → R₂C₂解离 → C亚基释放并磷酸化底物。这是一个别构激活的经典案例。</span></p>

<p><strong>信号放大级联</strong>：1个肾上腺素分子 → 激活1个GPCR → 激活多个Gα<sub>s</sub> → 每个激活1个AC产生多个cAMP → 激活多个PKA → 每个PKA磷酸化多个底物酶 → 每个底物酶催化多个底物分子。总放大倍数可达10⁶以上。</p>

<h4>14.3.3 IP₃/DAG双信使通路 <span class="tag-must">必考</span></h4>

<div style="background:var(--card-bg);border:1px solid var(--card-border);border-radius:var(--radius);padding:14px 18px;margin:12px 0;">
<p style="margin:0;font-weight:700;">IP₃/DAG通路主线：</p>
<p style="margin:2px 0;">配体 → GPCR → Gα<sub>q</sub>·GTP → 磷脂酶C(PLC) → PIP₂ → <strong>IP₃ + DAG</strong></p>
<p style="margin:2px 0;"><strong>IP₃分支</strong>：IP₃ → 内质网膜IP₃受体(Ca²⁺通道) → Ca²⁺释放至胞质 → Ca²⁺/钙调蛋白 → CaM激酶等</p>
<p style="margin:2px 0;"><strong>DAG分支</strong>：DAG + Ca²⁺ → 激活蛋白激酶C(PKC) → 磷酸化靶蛋白</p>
</div>

<p><strong>直觉类比</strong>：PIP₂好比一个压缩包，PLC把它解压成两个文件——IP₃是「打开钙库的钥匙」（水溶性，扩散到ER），DAG是「留在膜上的PKC激活器」（脂溶性，锚定在质膜内层）。两个信使分工协作，一条信号通路拆成两个并行分支执行。</p>

<h3>14.4 受体酪氨酸激酶（RTK）通路 <span class="tag-freq">高频</span></h3>

<p><span class="kp">RTK</span><span class="exp">是单次跨膜受体，其胞内域具有酪氨酸激酶活性。代表：胰岛素受体、EGF受体、PDGF受体等。</span></p>

<div style="background:var(--card-bg);border:1px solid var(--card-border);border-radius:var(--radius);padding:14px 18px;margin:12px 0;">
<p style="margin:0;font-weight:700;">RTK → Ras → MAPK级联（核心路径）：</p>
<p style="margin:2px 0;">1. <strong>配体诱导二聚化</strong>：配体结合 → 受体二聚化（或构象变化激活预先存在的二聚体）</p>
<p style="margin:2px 0;">2. <strong>自磷酸化</strong>：二聚体胞内域互相对方酪氨酸残基磷酸化(trans-autophosphorylation)</p>
<p style="margin:2px 0;">3. <strong>接头蛋白招募</strong>：Grb2的SH2结构域识别磷酸化酪氨酸，SH3结构域结合SOS</p>
<p style="margin:2px 0;">4. <strong>Ras激活</strong>：SOS是Ras的GEF（鸟苷酸交换因子），促进Ras释放GDP结合GTP</p>
<p style="margin:2px 0;">5. <strong>MAPK级联</strong>：Ras·GTP → <strong>Raf</strong>(MAPKKK) → <strong>MEK</strong>(MAPKK) → <strong>ERK</strong>(MAPK)</p>
<p style="margin:2px 0;">6. <strong>效应</strong>：ERK进入核内 → 磷酸化转录因子(如Elk-1) → 调控基因表达（细胞增殖/分化）</p>
</div>

<blockquote><strong>易错辨析</strong>：(1) RTK的二聚化是「配体诱导的」——不同于GPCR（GPCR本身就是单体且有7次跨膜）；(2) 自磷酸化是「trans-」（互相磷酸化），不是「cis-」（自己磷酸自己）；(3) Ras和Gα虽然都是GTP酶，但Ras是小G蛋白（单体~21kDa），Gα是异三聚体G蛋白的一部分——两者都属于GTP酶超家族，但调控机制不同。Ras需要GAP(GTP酶激活蛋白)来加速GTP水解，而Gα自身就有较高的固有GTP酶活性。</blockquote>

<h3>14.5 第二信使家族 <span class="tag-must">必考</span></h3>

<table>
<tr><th>第二信使</th><th>来源</th><th>作用方式</th><th>被什么信号激活</th></tr>
<tr><td><span class="kp">cAMP</span></td><td>ATP → AC催化</td><td>激活PKA</td><td>Gα<sub>s</sub>（如肾上腺素β受体）</td></tr>
<tr><td><span class="kp">cGMP</span></td><td>GTP → 鸟苷酸环化酶(GC)</td><td>激活PKG、调节离子通道</td><td>NO、心房钠尿肽(ANP)、光受体（视紫红质→Gt→cGMP PDE→cGMP↓）</td></tr>
<tr><td><span class="kp">IP₃</span></td><td>PIP₂ → PLC水解</td><td>开放ER膜Ca²⁺通道</td><td>Gα<sub>q</sub>（如血管紧张素II受体）</td></tr>
<tr><td><span class="kp">DAG</span></td><td>PIP₂ → PLC水解</td><td>激活PKC（需Ca²⁺协同）</td><td>Gα<sub>q</sub></td></tr>
<tr><td><span class="kp">Ca²⁺</span></td><td>ER/胞外 → 通道介导流入</td><td>激活钙调蛋白(CaM)→CaM激酶；或直接激活PKC、肌钙蛋白等</td><td>IP₃、电压门控Ca²⁺通道、NMDA受体等</td></tr>
</table>

<blockquote>易错：cGMP在视觉信号转导中是降低而不是升高——光激活视紫红质→激活转导素(Gt)→激活cGMP磷酸二酯酶→cGMP被水解→cGMP门控Na⁺/Ca²⁺通道关闭→膜超极化→神经递质释放减少。这是在暗处cGMP高、光照后cGMP降低的模式。</blockquote>

<h3>14.6 脂溶性激素的作用机制 <span class="tag-freq">高频</span></h3>

<p><span class="kp">核受体超家族</span><span class="exp">：脂溶性激素穿越质膜后，与胞内受体（大多位于核内，少数在胞质）结合。激素-受体复合物作为配体激活的转录因子，直接与DNA上的激素响应元件(HRE)结合，调控靶基因的转录。</span></p>

<p><strong>经典途径</strong>：类固醇激素(如皮质醇) → 穿越质膜 → 与胞质中的糖皮质激素受体(GR)结合 → GR构象变化，Hsp90解离 → GR-激素复合物二聚化 → 入核 → 结合DNA上的GRE(糖皮质激素响应元件) → 激活/抑制靶基因转录。</p>

<p><strong>为什么脂溶性激素不需要第二信使？</strong>因为它们能直接进入细胞、直接作用于DNA——信号就是激素本身。响应慢（>30分钟才有mRNA变化），但持久（一次激素脉冲可维持数小时到数天的效应）。</p>

<h3>14.7 信号转导的终止机制 <span class="tag-key">重点</span></h3>

<p><strong>信号必须终止，否则细胞永远处于「被刺激」状态。</strong></p>

<ul>
<li><span class="kp">配体清除</span><span class="exp">：激素被降解或重摄取（如神经递质被突触前末梢重摄取）</span></li>
<li><span class="kp">受体脱敏</span><span class="exp">：GRK(GPCR激酶)磷酸化激活的GPCR → β-arrestin结合 → 阻止G蛋白偶联 + 促进受体内吞 → 受体下调</span></li>
<li><span class="kp">GTP水解</span><span class="exp">：Gα·GTP → Gα·GDP（Gα固有GTP酶活性 + GAP辅助）——这是GPCR信号终止的最基本机制</span></li>
<li><span class="kp">第二信使降解</span><span class="exp">：cAMP→PDE水解为5'-AMP；IP₃→磷酸酶去磷酸化；DAG→脂酶水解；Ca²⁺→泵回ER/泵出胞外</span></li>
<li><span class="kp">磷酸酶</span><span class="exp">：蛋白磷酸酶(PP1, PP2A等)去磷酸化被PKA/PKC/ERK等磷酸化的靶蛋白，恢复基态</span></li>
</ul>

<hr>

<h2>第15章 生物膜与物质运输 <span class="tag-must">必考</span></h2>

<blockquote><strong>核心问题</strong>：细胞如何用一张几纳米厚的脂双层，精确地控制哪些物质能进来、哪些物质必须留在外面？</blockquote>

<h3>15.1 生物膜的组成与结构</h3>

<p><span class="kp">生物膜的基本结构</span><span class="exp">是脂双层（lipid bilayer），由两亲性磷脂分子自组装形成——亲水头部朝外接触水环境，疏水尾部埋藏在膜内部形成疏水屏障。膜蛋白镶嵌其中（流动镶嵌模型，Singer-Nicolson, 1972）。</span></p>

<table>
<tr><th>组分</th><th>比例</th><th>功能</th></tr>
<tr><td><span class="kp">磷脂</span></td><td>~40%</td><td>构成膜的基本屏障——磷脂酰胆碱(PC)、磷脂酰乙醇胺(PE)、磷脂酰丝氨酸(PS)、鞘磷脂(SM)等</td></tr>
<tr><td><span class="kp">胆固醇</span></td><td>~20%（动物细胞）</td><td>调节膜流动性（高温时限制运动、低温时阻止结晶）——「膜流动性的缓冲剂」</td></tr>
<tr><td><span class="kp">膜蛋白</span></td><td>~40-50%</td><td>运输(通道/载体/泵)、信号转导(受体)、催化(酶)、附着(锚定蛋白)</td></tr>
<tr><td><span class="kp">糖类</span></td><td>~2-10%</td><td>糖萼(glycocalyx)——细胞识别、保护、润滑</td></tr>
</table>

<blockquote>易错：膜的不对称性——磷脂酰丝氨酸(PS)几乎全部分布在内层（细胞质侧）。当细胞凋亡时PS外翻到外层，成为巨噬细胞识别和吞噬的「吃我」信号。PC和鞘磷脂则主要在外层。</blockquote>

<h3>15.2 物质跨膜运输方式分类 <span class="tag-must">必考</span></h3>

<table>
<tr><th>类型</th><th>是否需要载体/通道</th><th>是否耗能</th><th>方向</th><th>举例</th></tr>
<tr><td><span class="kp">简单扩散</span></td><td>否</td><td>否</td><td>顺浓度梯度</td><td>O₂、CO₂、疏水小分子（类固醇激素）</td></tr>
<tr><td><span class="kp">协助扩散—载体</span></td><td>是（载体蛋白）</td><td>否</td><td>顺浓度梯度</td><td>GLUT转运葡萄糖</td></tr>
<tr><td><span class="kp">协助扩散—通道</span></td><td>是（通道蛋白）</td><td>否</td><td>顺电化学梯度</td><td>Na⁺通道、K⁺通道、水通道蛋白</td></tr>
<tr><td><span class="kp">初级主动运输</span></td><td>是（泵）</td><td>是（直接消耗ATP）</td><td>逆浓度梯度</td><td>Na⁺-K⁺ ATP酶、Ca²⁺ ATP酶</td></tr>
<tr><td><span class="kp">次级主动运输</span></td><td>是（共转运体）</td><td>是（间接——利用离子梯度）</td><td>逆浓度梯度</td><td>Na⁺/葡萄糖同向转运(SGLT)</td></tr>
</table>

<p><strong>直觉理解各类运输的差异</strong>：</p>
<ul>
<li><span class="kp">简单扩散</span><span class="exp">= 滑雪下坡（不需缆车、不需能量，自然下滑）</span></li>
<li><span class="kp">协助扩散</span><span class="exp">= 有闸门的滑道（需要专门的通道/载体，但仍是下坡，不需要能量）</span></li>
<li><span class="kp">初级主动运输</span><span class="exp">= 缆车直接用电（ATP）把乘客拉上坡</span></li>
<li><span class="kp">次级主动运输</span><span class="exp">= 一辆下坡的卡车带动另一辆上坡车（利用Na⁺顺梯度的能量来驱动葡萄糖逆梯度运输）</span></li>
</ul>

<h3>15.3 离子通道的特征 <span class="tag-key">重点</span></h3>

<p><span class="kp">离子通道</span><span class="exp">是跨膜蛋白形成的亲水孔道，允许特定离子快速通过（10⁶-10⁸ ions/s，比载体蛋白快~1000倍）。</span></p>

<p><strong>三大特征</strong>：</p>
<ul>
<li><span class="kp">选择性（Selectivity）</span><span class="exp">：通道的「选择过滤器」(selectivity filter)仅允许特定离子通过。例如K⁺通道的选择过滤器由保守序列TVGYG的羰基氧原子排列而成，刚好匹配脱水的K⁺（离子半径1.33Å），而Na⁺（半径0.95Å）太小，羰基氧不能有效配位，脱水的能量代价太高。这就是K⁺通道对K⁺的选择性比Na⁺高~10000倍的原因。</span></li>
<li><span class="kp">门控性（Gating）</span><span class="exp">：通道在开(open)和关(closed)状态之间切换——电压门控（膜电位变化，如Na⁺/K⁺/Ca²⁺通道）、配体门控（配体结合，如乙酰胆碱受体/离子通道）、机械门控（膜张力变化，如听觉毛细胞的机械敏感通道）。</span></li>
<li><span class="kp">快速性</span><span class="exp">：通道不经过构象变化的催化循环，仅「开/关」切换，转运速率极高。</span></li>
</ul>

<h3>15.4 Na⁺-K⁺ ATP酶（P型ATP酶）<span class="tag-must">必考</span></h3>

<p><span class="kp">Na⁺-K⁺ ATP酶</span><span class="exp">存在于几乎所有动物细胞质膜上，是维持细胞内外Na⁺/K⁺浓度梯度的核心泵。</span></p>

<div style="background:var(--card-bg);border:1px solid var(--card-border);border-radius:var(--radius);padding:14px 18px;margin:12px 0;">
<p style="margin:0;font-weight:700;">化学计量比（必须牢记！）：</p>
<p style="margin:4px 0;"><strong>每水解1分子ATP → 泵出3个Na⁺ + 泵入2个K⁺</strong></p>
<p style="margin:6px 0 0 0;color:var(--ink-light);">→ 每个循环净移出1个正电荷（生电性泵）</p>
<p style="margin:2px 0;color:var(--ink-light);">→ 消耗神经元可用ATP的~70%（大脑是高能耗器官）</p>
</div>

<p><strong>工作机制（E1-E2模型）</strong>：</p>
<table>
<tr><th>步骤</th><th>状态</th><th>事件</th></tr>
<tr><td>1</td><td>E1·ATP</td><td>3个胞内Na⁺结合（高亲和力Na⁺位点）→ ATP水解 → 天冬氨酸残基被磷酸化（形成E1~P）</td></tr>
<tr><td>2</td><td>E2~P</td><td>构象从E1变为E2 → Na⁺结合位点亲和力降低，3Na⁺释放到胞外</td></tr>
<tr><td>3</td><td>E2~P</td><td>2个胞外K⁺结合（高亲和力K⁺位点）</td></tr>
<tr><td>4</td><td>E1</td><td>天冬氨酰磷酸去磷酸化 → 构象从E2变回E1 → K⁺亲和力降低，2K⁺释放到胞内 → 回到步骤1</td></tr>
</table>

<p><strong>哇巴因（ouabain）</strong>是Na⁺-K⁺ ATP酶的特异性抑制剂，结合在E2~P状态，阻断去磷酸化步骤。洋地黄类药物（地高辛）也是通过抑制心肌细胞Na⁺-K⁺ ATP酶 → 胞内Na⁺↑ → Na⁺/Ca²⁺交换减少 → 胞内Ca²⁺↑ → 心肌收缩力增强（正性肌力作用）。</p>

<h3>15.5 葡萄糖转运蛋白GLUT家族 <span class="tag-key">重点</span></h3>

<table>
<tr><th>亚型</th><th>组织分布</th><th>Km(葡萄糖)</th><th>功能</th></tr>
<tr><td><span class="kp">GLUT1</span></td><td>红细胞、血脑屏障、全身</td><td>~1 mM（低）</td><td>基础葡萄糖摄取（高亲和力）</td></tr>
<tr><td><span class="kp">GLUT2</span></td><td>肝、胰岛β细胞、小肠基底膜</td><td>~15-20 mM（高）</td><td>葡萄糖传感器——血糖高时快速摄取入肝/β细胞</td></tr>
<tr><td><span class="kp">GLUT4</span></td><td>肌肉、脂肪组织</td><td>~5 mM（中）</td><td>胰岛素调节的葡萄糖摄取——胰岛素→GLUT4囊泡从胞内转移到质膜</td></tr>
</table>

<blockquote><strong>易错辨析</strong>：GLUT1-4都是协助扩散（不耗能、顺浓度梯度）。小肠上皮细胞的葡萄糖吸收（从肠腔→上皮细胞）是次级主动运输（SGLT1利用Na⁺梯度），但从上皮细胞→血液才是GLUT2协助扩散。</blockquote>

<h3>15.6 胞吞与胞吐作用 <span class="tag-info">了解</span></h3>

<p><span class="kp">胞吐（Exocytosis）</span><span class="exp">：胞内囊泡膜与质膜融合→内容物释放到胞外。SNARE蛋白(v-SNARE + t-SNARE)介导融合。Ca²⁺触发神经递质释放是典型例子。</span></p>

<p><span class="kp">胞吞（Endocytosis）</span><span class="exp">：质膜内陷→形成囊泡内吞入胞。(1) 吞噬作用——吞入大颗粒（如巨噬细胞吞噬细菌）；(2) 胞饮作用——吞入液体和溶质；(3) 受体介导的胞吞——LDL受体→有被小窝(clathrin-coated pit)→内吞→LDL释放。</span></p>

<hr>

<h2>第16章 生物能学 <span class="tag-must">必考</span></h2>

<blockquote><strong>核心问题</strong>：生物化学反应哪些能自发进行？哪些不能？细胞如何利用ATP的能量来「支付」不利反应的热力学代价？</blockquote>

<h3>16.1 热力学基本概念复习 <span class="tag-must">必考</span></h3>

<p><span class="kp">Gibbs自由能(ΔG)</span><span class="exp">是判断反应能否在恒温恒压下自发进行的标准：ΔG = ΔH - TΔS。ΔG &lt; 0 自发（放能），ΔG &gt; 0 非自发（吸能），ΔG = 0 平衡。</span></p>

<div style="background:var(--card-bg);border:1px solid var(--card-border);border-radius:var(--radius);padding:14px 18px;margin:12px 0;">
<p style="margin:0;font-weight:700;">ΔG°' 与 ΔG 的区别（高频考点）：</p>
<table>
<tr><th></th><th>ΔG°'（标准生化自由能变化）</th><th>ΔG（实际自由能变化）</th></tr>
<tr><td>条件</td><td>pH 7, 25°C, 各物质浓度1M（水55.5M, [H⁺]=10⁻⁷M）</td><td>细胞内实际浓度（远非1M）</td></tr>
<tr><td>公式</td><td>ΔG°' = -RT ln K'<sub>eq</sub></td><td>ΔG = ΔG°' + RT ln Q（Q为实际反应商）</td></tr>
<tr><td>决定因素</td><td>仅取决于反应物和产物的化学本质</td><td>取决于ΔG°' + 实际浓度比</td></tr>
</table>
</div>

<p><strong>关键公式</strong>：$$\Delta G = \Delta G^{\circ\prime} + RT \ln\frac{[\text{产物}]}{[\text{反应物}]}$$</p>

<p>在平衡时，ΔG = 0，Q = K'<sub>eq</sub>，所以：$$\Delta G^{\circ\prime} = -RT \ln K'_{eq}$$</p>

<p><strong>直觉理解</strong>：ΔG°'告诉你的是「在标准条件下反应往哪边走」（反应的固有倾向），ΔG告诉你的是「在当前细胞条件下反应往哪边走」。由于细胞中实际浓度比率可以极低（如产物立即被消耗），一个ΔG°'为+的反应在细胞内仍可能ΔG &lt; 0 从而自发进行。</p>

<h3>16.2 ATP——细胞的能量货币 <span class="tag-must">必考</span></h3>

<h4>16.2.1 ATP的结构与高能磷酸键的本质</h4>

<p><span class="kp">ATP = 腺苷-三磷酸</span><span class="exp">：腺嘌呤碱基 + 核糖（β-N-糖苷键）+ 三个串联的磷酸基团（α-β-γ）。γ和β之间的磷酸酐键即「高能磷酸键」（符号~P）。</span></p>

<p><span class="kp">「高能磷酸键」为什么「高能」？</span><span class="exp">——这不是因为键能特别高（磷酸酐键的键能本身并不大），而是因为ATP的水解产物（ADP + Pi）比ATP本身稳定得多：</span></p>
<ul>
<li><span class="kp">静电排斥减轻</span><span class="exp">：ATP带有4个负电荷（在pH 7时三个磷酸基团负电荷集中），强的静电排斥力使ATP不稳定。水解掉一个磷酸基团，ADP只剩3个负电荷，Pi单独游离，排斥力大幅减小。</span></li>
<li><span class="kp">共振稳定化</span><span class="exp">：游离Pi比ATP中被连接的磷酸基团有更多的共振形式——Pi可以写出多种等价共振结构，而在ATP中磷酸基团的电子被锁定在P-O键中，共振自由度受限。</span></li>
<li><span class="kp">电离和溶剂化</span><span class="exp">：ATP水解产生的ADP和Pi能更好地被水分子水合，释放水合能。</span></li>
</ul>

<h4>16.2.2 ATP水解的ΔG°'与能量货币地位</h4>

<div style="background:var(--card-bg);border:1px solid var(--card-border);border-radius:var(--radius);padding:14px 18px;margin:12px 0;">
<p style="margin:0;font-weight:700;">ATP + H₂O → ADP + Pi &nbsp;&nbsp; ΔG°' = -30.5 kJ/mol</p>
<p style="margin:2px 0;font-weight:700;">ATP + H₂O → AMP + PPi &nbsp;&nbsp; ΔG°' = -45.6 kJ/mol（PPi进一步水解为2Pi，ΔG°'约-19.2 kJ/mol）</p>
</div>

<p><strong>为什么ATP恰好是「中间位置」的能量货币？</strong></p>

<table>
<tr><th>分类</th><th>化合物</th><th>ΔG°'(kJ/mol)</th><th>地位</th></tr>
<tr><td><span class="kp">超高能</span></td><td>磷酸烯醇式丙酮酸(PEP)</td><td>-61.9</td><td>糖酵解的终极高能中间体</td></tr>
<tr><td><span class="kp">高能</span></td><td>1,3-二磷酸甘油酸(1,3-BPG)</td><td>-49.4</td><td>糖酵解</td></tr>
<tr><td><span class="kp">高能</span></td><td>磷酸肌酸</td><td>-43.1</td><td>肌肉中的ATP「备用电池」（脊椎动物）</td></tr>
<tr><td><span class="kp" style="background:#fef3c7;padding:1px 6px;border-radius:3px;">能量货币</span></td><td><strong>ATP → ADP + Pi</strong></td><td><strong>-30.5</strong></td><td>通用能量货币</td></tr>
<tr><td><span class="kp">低能</span></td><td>葡萄糖-6-磷酸</td><td>-13.8</td><td>普通磷酸酯</td></tr>
<tr><td><span class="kp">低能</span></td><td>甘油-3-磷酸</td><td>-9.2</td><td>普通磷酸酯</td></tr>
</table>

<p><strong>动机推演——为什么ATP在中间？</strong>如果ATP的ΔG°'太高（如PEP），则ADP磷酸化为ATP会过于困难（因为没有足够能量的供体来驱动此反应）；如果ATP的ΔG°'太低，则ATP水解无法为大多数反应提供足够的驱动力。ATP恰好处于中间位置——它既能被分解代谢（如糖酵解）轻松合成，又能为合成代谢（如蛋白质合成）提供足够的能量。这是进化优化出的完美折中。</p>

<h3>16.3 偶联反应原理 <span class="tag-must">必考</span></h3>

<p><span class="kp">偶联反应</span><span class="exp">：将一个热力学不利的反应（ΔG₁ &gt; 0）与一个热力学有利的反应（ΔG₂ &lt;&lt; 0，通常是ATP水解）通过共同的中间体偶联，使总反应的ΔG = ΔG₁ + ΔG₂ &lt; 0。</span></p>

<p><strong>经典实例</strong>：葡萄糖 + Pi → 葡萄糖-6-磷酸 + H₂O（ΔG°' = +13.8 kJ/mol，不利）不能直接发生。但将ATP水解偶联：</p>
<p style="text-align:center;">ATP + H₂O → ADP + Pi（ΔG°' = -30.5 kJ/mol）</p>
<p style="text-align:center;">葡萄糖 + ATP → 葡萄糖-6-磷酸 + ADP（ΔG°' = 13.8 + (-30.5) = -16.7 kJ/mol）</p>
<p>总反应由己糖激酶催化，磷酸基团直接由ATP转移到葡萄糖——不是先水解ATP再磷酸化葡萄糖，而是通过「磷酸基团转移」机制实现偶联。</p>

<blockquote><strong>易错辨析</strong>：偶联不是「ATP先水解产生能量，再用这个能量推动另一反应」——这在化学上说不通，因为热是弥散的，不能定向使用。真正的偶联机制是「形成共同的化学中间体」——ATP的γ-磷酸基团直接转移到葡萄糖上，使得两个反应变成同一个反应序列。</blockquote>

<h3>16.4 能荷（Energy Charge）<span class="tag-must">必考</span></h3>

<div style="background:var(--card-bg);border:1px solid var(--card-border);border-radius:var(--radius);padding:14px 18px;margin:12px 0;">
<p style="margin:0;font-weight:700;text-align:center;font-size:1.05em;">$$\text{能荷(EC)} = \frac{[\text{ATP}] + 0.5[\text{ADP}]}{[\text{ATP}] + [\text{ADP}] + [\text{AMP}]}$$</p>
</div>

<p><span class="kp">能荷</span><span class="exp">是细胞内高能磷酸键可用性的度量，反映了腺苷酸池中磷酸酐键的比例。EC的范围是0～1：EC=0表示全是AMP（能量完全耗尽），EC=1表示全是ATP（能量完全充满）。正常细胞EC维持在0.85-0.90的窄范围内。</span></p>

<p><strong>动机推演</strong>：EC同时调控分解代谢和合成代谢——EC低时激活分解代谢（产生ATP）并抑制合成代谢；EC高时激活合成代谢（消耗ATP）并抑制分解代谢。这是一个精细的反馈控制系统，保证细胞能量供应的稳态。关键调控酶（如磷酸果糖激酶、丙酮酸激酶、柠檬酸合酶等）的活性都受EC的别构调节。</p>

<hr>

<h2>第17章 生物氧化 <span class="tag-must">必考</span></h2>

<blockquote><strong>核心问题</strong>：我们吃的食物中的化学能如何被提取出来，并以ATP的形式存储？为什么直接燃烧葡萄糖效率很低，而细胞氧化效率高达~40%？</blockquote>

<h3>17.1 生物氧化的特点 <span class="tag-key">重点</span></h3>

<table>
<tr><th>特征</th><th>体外燃烧</th><th>生物氧化</th></tr>
<tr><td><span class="kp">温度</span></td><td>高温（>300°C）</td><td>体温（37°C）</td></tr>
<tr><td><span class="kp">方式</span></td><td>一步直接氧化，能量以热释放</td><td>多步酶催化，能量逐步释放</td></tr>
<tr><td><span class="kp">能量捕获</span></td><td>几乎全部为热（效率~0%）</td><td>~40%被捕获为ATP（其余为热，维持体温）</td></tr>
<tr><td><span class="kp">氢的去除</span></td><td>H直接与O₂结合生成H₂O</td><td>H通过NAD⁺/FAD依次传递给电子传递链，最终才与O₂结合</td></tr>
</table>

<p><strong>直觉类比</strong>：体外燃烧 = 把水库的水一泻而下（水能全浪费成热能），生物氧化 = 建了一系列水电站（多步骤，每步捕获一小部分能量）——最终水还是流到了底部，但过程中已经发了很多电。</p>

<h3>17.2 呼吸链（电子传递链）的组成 <span class="tag-must">必考</span></h3>

<p><span class="kp">呼吸链</span><span class="exp">位于线粒体内膜，由4个多亚基蛋白复合体(I-IV)和2个流动电子载体（辅酶Q和细胞色素c）组成。NADH和FADH₂将电子送入呼吸链，电子经过一系列氧化还原反应最终传给O₂生成H₂O。</span></p>

<table>
<tr><th>组分</th><th>名称</th><th>辅基/氧化还原中心</th><th>质子泵?</th></tr>
<tr><td><span class="kp">复合体I</span></td><td>NADH脱氢酶</td><td>FMN, Fe-S簇(>8个)</td><td>✓（泵出4H⁺）</td></tr>
<tr><td><span class="kp">复合体II</span></td><td>琥珀酸脱氢酶</td><td>FAD, Fe-S簇</td><td>✗</td></tr>
<tr><td><span class="kp">CoQ（泛醌）</span></td><td>辅酶Q/泛醌</td><td>醌环（可接受1或2个电子）</td><td>—（流动载体）</td></tr>
<tr><td><span class="kp">复合体III</span></td><td>细胞色素bc1</td><td>血红素b, 血红素c1, Fe-S簇(Rieske)</td><td>✓（泵出4H⁺，Q循环）</td></tr>
<tr><td><span class="kp">Cyt c</span></td><td>细胞色素c</td><td>血红素c（共价连接）</td><td>—（流动载体，膜间隙）</td></tr>
<tr><td><span class="kp">复合体IV</span></td><td>细胞色素c氧化酶</td><td>血红素a, 血红素a₃, Cu<sub>A</sub>, Cu<sub>B</sub></td><td>✓（泵出2H⁺）</td></tr>
</table>

<p><strong>直觉理解呼吸链布局</strong>：复合体I、III、IV像三个「质子泵站」，辅酶Q和细胞色素c是两个「穿梭巴士」把电子从上一个泵站送到下一个泵站。复合体II是一个「侧门」——FADH₂从这里进入，不经过复合体I，因此产生的ATP更少（FADH₂~1.5 ATP vs NADH~2.5 ATP）。</p>

<blockquote><strong>易错辨析</strong>：(1) 复合体II就是三羧酸循环中的琥珀酸脱氢酶——同一个酶身兼二职（代谢酶 + 呼吸链成员）；(2) 辅酶Q是疏水性小分子，在线粒体内膜的脂双层中自由扩散（流动电子载体），而细胞色素c是水溶性蛋白，位于膜间隙侧（膜外周蛋白），也是流动的；(3) 复合体I→III→IV传递的是来自NADH的电子，复合体II→III→IV传递的是来自FADH₂（即琥珀酸）的电子。</blockquote>

<h3>17.3 电子传递顺序的确定 <span class="tag-freq">高频</span></h3>

<p>电子传递顺序的确定依据：</p>
<ul>
<li><span class="kp">各组分氧化还原电位的测定</span><span class="exp">：E°'值从低到高排列——电子自发从低电位流向高电位。NADH/NAD⁺(-0.32V) → FMN(-0.30V) → Fe-S → CoQ(+0.06V) → Cyt b(+0.07V) → Cyt c1(+0.22V) → Cyt c(+0.25V) → Cyt a(+0.29V) → Cyt a₃(+0.55V) → O₂/H₂O(+0.82V)</span></li>
<li><span class="kp">特异抑制剂实验 + 光谱分析</span><span class="exp">：加入特异抑制剂阻断某处→被阻断点之前的组分全部处于还原态，之后的组分处于氧化态→光谱差异确定顺序。</span></li>
</ul>

<h3>17.4 呼吸链抑制剂 <span class="tag-must">必考</span></h3>

<table>
<tr><th>抑制剂</th><th>靶点</th><th>效应</th><th>ΔP?</th></tr>
<tr><td><span class="kp">鱼藤酮</span></td><td>复合体I（阻断Fe-S→CoQ）</td><td>来自NADH的电子传递阻断；FADH₂→III→IV仍正常</td><td>↓</td></tr>
<tr><td><span class="kp">抗霉素A</span></td><td>复合体III（阻断Cyt b→Cyt c1）</td><td>全部电子传递阻断</td><td>↓</td></tr>
<tr><td><span class="kp">CN⁻/CO/N₃⁻</span></td><td>复合体IV（与Cyt a₃结合，阻断→O₂）</td><td>全部电子传递阻断——致死！</td><td>↓</td></tr>
<tr><td><span class="kp">寡霉素</span></td><td>ATP合酶（F₀质子通道）</td><td>阻断H⁺回流→质子梯度累积→反向抑制电子传递</td><td>↑</td></tr>
</table>

<blockquote>易错：氰化物(CN⁻)比鱼藤酮毒性大得多，因为鱼藤酮只阻断NADH来源的电子传递（FADH₂的电子还能通过复合体II→III→IV），而CN⁻阻断复合体IV使所有电子传递停止——而且O₂是终端电子受体，被阻断后整个呼吸链无法运转。</blockquote>

<h3>17.5 氧化磷酸化——化学渗透假说 <span class="tag-must">必考</span></h3>

<p><span class="kp">Peter Mitchell的化学渗透假说</span><span class="exp">（1961年提出，1978年诺贝尔化学奖）：电子传递释放的能量用于将H⁺从线粒体基质泵到膜间隙，在线粒体内膜两侧建立质子电化学梯度（质子动力Δμ<sub>H⁺</sub>），H⁺经ATP合酶回流时驱动ATP合成。其核心思想是「电子传递与ATP合成通过跨膜H⁺梯度间接耦合」，而非通过「高能化学中间体」。</span></p>

<div style="background:var(--card-bg);border:1px solid var(--card-border);border-radius:var(--radius);padding:14px 18px;margin:12px 0;">
<p style="margin:0;font-weight:700;text-align:center;">化学渗透假说的三要素：</p>
<p style="margin:2px 0;">1. 线粒体内膜对H⁺不通透（前提——否则H⁺会漏回去）</p>
<p style="margin:2px 0;">2. 电子传递→H⁺泵出内膜→质子梯度（ΔpH + Δψ = Δμ<sub>H⁺</sub>）</p>
<p style="margin:2px 0;">3. H⁺只能通过ATP合酶回流→驱动ATP合成</p>
</div>

<p><strong>关键实验证据</strong>：(1) 解偶联剂(DNP)消除质子梯度，电子传递继续但ATP不合成——证明电子传递和ATP合成是可分离的过程；(2) 人工构建的H⁺梯度可以在没有电子传递的情况下驱动ATP合成；(3) ATP合酶F₀F₁的结构直接证实了质子通道的存在。</p>

<h3>17.6 ATP合酶的结构 <span class="tag-freq">高频</span></h3>

<p><span class="kp">ATP合酶（F₀F₁-ATPase）</span><span class="exp">是一种精妙的分子马达：</span></p>

<ul>
<li><span class="kp">F₁（催化头部，基质侧）</span><span class="exp">：由α₃β₃γδε亚基组成。三对αβ交替排列形成六聚体环，β亚基是催化亚基。γ亚基是不对称的中心轴，旋转时依次接触三个β亚基，诱导其构象循环：开放(O)→松散(L)→紧密(T)→开放(O)。T态合成ATP，O态释放ATP。</span></li>
<li><span class="kp">F₀（质子通道，跨膜部分）</span><span class="exp">：由a亚基和c亚基环(c₈₋₁₅)组成。每个c亚基含一个关键Asp/Glu残基。H⁺通过F₀流入→c环旋转→带动γ轴旋转→F₁构象变化→ATP合成。</span></li>
</ul>

<p><strong>直觉类比</strong>：F₀F₁好比一个水力发电机组——水流（H⁺回流）推动水轮机旋转（c环），旋转的水轮机带动发电机转子（γ轴），转子在定子（α₃β₃）中旋转产生电力（ATP）。这是一个物理旋转与化学合成的精妙耦合——结合改变机制（binding change mechanism）。</p>

<h3>17.7 P/O比与解偶联 <span class="tag-key">重点</span></h3>

<p><span class="kp">P/O比</span><span class="exp">：每消耗1个氧原子(½ O₂)所酯化的无机磷酸(Pi)的摩尔数，即产生的ATP分子数。现代测量：</span></p>
<ul>
<li>NADH → 约2.5 ATP（10个H⁺泵出 ÷ 4个H⁺/ATP ≈ 2.5）</li>
<li>FADH₂ → 约1.5 ATP（6个H⁺泵出 ÷ 4个H⁺/ATP ≈ 1.5）</li>
</ul>

<p><span class="kp">解偶联剂</span><span class="exp">：消除质子梯度而不抑制电子传递的物质。2,4-二硝基苯酚(DNP)是质子载体——在膜间隙侧结合H⁺，扩散到基质侧释放H⁺，短路了ATP合酶。结果是电子传递照常进行，但能量全部以热的形式释放（ATP不合成）。</span></p>

<p><span class="kp">生理性解偶联</span><span class="exp">：褐色脂肪组织中的解偶联蛋白UCP1（thermogenin）——在线粒体内膜上形成H⁺通道，将质子梯度直接以热的形式释放，用于维持新生儿和冬眠动物的体温。</span></p>

<hr>

<h2>第18章 光合作用 <span class="tag-must">必考</span></h2>

<blockquote><strong>核心问题</strong>：植物如何利用最廉价、最丰富的能源——阳光——将最氧化的碳(CO₂)还原为有机碳(葡萄糖)？这个地球上最重要的化学反应是如何进行的？</blockquote>

<h3>18.1 光合作用的两个阶段 <span class="tag-must">必考</span></h3>

<div style="background:var(--card-bg);border:1px solid var(--card-border);border-radius:var(--radius);padding:14px 18px;margin:12px 0;">
<p style="margin:0;font-weight:700;text-align:center;">光合作用总反应：</p>
<p style="margin:4px 0;text-align:center;font-size:1.05em;">$$6\text{CO}_2 + 6\text{H}_2\text{O} \xrightarrow{h\nu} \text{C}_6\text{H}_{12}\text{O}_6 + 6\text{O}_2$$</p>
<p style="margin:6px 0 0 0;text-align:center;color:var(--ink-light);">注意：O₂来自H₂O的光解（不是CO₂）——用¹⁸O同位素标记实验证明！</p>
</div>

<table>
<tr><th>阶段</th><th>场所</th><th>输入</th><th>输出</th><th>核心事件</th></tr>
<tr><td><span class="kp">光反应</span></td><td>类囊体膜</td><td>H₂O, NADP⁺, ADP, Pi</td><td>O₂, NADPH, ATP</td><td>光能→化学能（ATP+NADPH）</td></tr>
<tr><td><span class="kp">暗反应(Calvin循环)</span></td><td>叶绿体基质</td><td>CO₂, ATP, NADPH</td><td>G3P→葡萄糖等</td><td>CO₂固定和还原</td></tr>
</table>

<blockquote>易错：「暗反应」不是只能在暗中进行——它不需要光，但需要光反应提供的ATP和NADPH，因此在光照下同时进行。「暗反应」的名称仅指该阶段本身不直接依赖光。</blockquote>

<h3>18.2 光合色素 <span class="tag-key">重点</span></h3>

<table>
<tr><th>色素</th><th>吸收峰</th><th>功能</th></tr>
<tr><td><span class="kp">叶绿素a (Chl a)</span></td><td>~430nm(蓝紫), ~662nm(红)</td><td>反应中心色素——直接参与光化学反应</td></tr>
<tr><td><span class="kp">叶绿素b (Chl b)</span></td><td>~453nm, ~642nm</td><td>天线色素——捕获光能传递给Chl a</td></tr>
<tr><td><span class="kp">类胡萝卜素</span></td><td>~400-500nm</td><td>辅助天线色素 + <strong>光保护</strong>（淬灭三线态叶绿素和单线态氧）</td></tr>
</table>

<p><strong>直觉理解</strong>：天线色素像太阳能电池板的阵列（增加光吸收面积），反应中心色素是真正「发电」的核心单元。每个光系统有~200-300个天线叶绿素分子，它们吸收的光能通过共振能量转移汇集到1个反应中心——这好比用无数面镜子把阳光聚焦到一点。</p>

<h3>18.3 光系统I和光系统II <span class="tag-must">必考</span></h3>

<table>
<tr><th>特征</th><th>光系统II (PSII)</th><th>光系统I (PSI)</th></tr>
<tr><td><span class="kp">反应中心</span></td><td>P680（最大吸收680nm）</td><td>P700（最大吸收700nm）</td></tr>
<tr><td><span class="kp">功能</span></td><td>水的光解放氧（提供电子）</td><td>NADP⁺的还原（产生NADPH）</td></tr>
<tr><td><span class="kp">电子来源</span></td><td>H₂O → O₂ + 4e⁻ + 4H⁺</td><td>经PC传来的电子（来自PSII）</td></tr>
<tr><td><span class="kp">电子去向</span></td><td>PQ → Cyt b₆f → PC → PSI</td><td>Fd → NADP⁺还原酶 → NADPH</td></tr>
</table>

<h3>18.4 光反应电子传递——Z方案 <span class="tag-must">必考</span></h3>

<div style="background:var(--card-bg);border:1px solid var(--card-border);border-radius:var(--radius);padding:14px 18px;margin:12px 0;">
<p style="margin:0;font-weight:700;text-align:center;">Z方案电子传递链：</p>
<p style="margin:2px 0;text-align:center;">H₂O → <strong>P680*</strong> → Pheo → Q<sub>A</sub> → Q<sub>B</sub> → <strong>PQ</strong> → </p>
<p style="margin:2px 0;text-align:center;"><strong>Cyt b₆f</strong> → <strong>PC</strong> → <strong>P700*</strong> → A₀ → A₁ → Fe-S → </p>
<p style="margin:2px 0;text-align:center;"><strong>Fd</strong> → FNR → <strong>NADPH</strong></p>
</div>

<p><strong>「Z」字的含义</strong>：当各氧化还原对的E°'值按电子传递顺序作图时，曲线呈Z字形——因为PSII和PSI各吸收一个光子，将电子两次提升到更高的还原电位。电子从H₂O(+0.82V)出发，被P680*激发→低电位(约-0.8V)→再经PSI被P700*再次激发→极低电位(约-1.3V)→最终还原NADP⁺为NADPH(-0.32V)。</p>

<h3>18.5 水的光解（放氧复合体OEC）<span class="tag-freq">高频</span></h3>

<p><span class="kp">OEC（Oxygen-Evolving Complex）</span><span class="exp">位于PSII的类囊体腔侧，核心是一个Mn₄CaO₅簇。通过积累4个正电荷的S态循环(S₀→S₁→S₂→S₃→S₄→S₀)，分5步将2个H₂O分子氧化为1个O₂：</span></p>

<p style="text-align:center;">$$2\text{H}_2\text{O} \rightarrow \text{O}_2 + 4\text{H}^+ + 4e^-$$</p>

<p>每次吸收一个光子放出一个电子，累积4个光子后才能一次释放O₂——这是自然界唯一能催化水氧化的生物催化剂。PSII每次被激发，P680⁺从OEC中抽取1个电子（经Tyr<sub>Z</sub>桥接）。</p>

<h3>18.6 光合磷酸化 <span class="tag-key">重点</span></h3>

<p><span class="kp">非循环式光合磷酸化</span><span class="exp">：电子从H₂O→PSII→PQ→Cyt b₆f→PC→PSI→Fd→NADP⁺（终点），同时产生ATP和NADPH。H⁺在PSII水光解（腔内）和PQH₂氧化（经Q循环，相似于呼吸链复合体III）时泵入类囊体腔→质子梯度经CF₀CF₁-ATP合酶驱动ATP合成。</span></p>

<p><span class="kp">循环式光合磷酸化</span><span class="exp">：电子绕PSI循环——Fd→Cyt b₆f→PC→PSI→Fd，仅产生ATP（不产生NADPH，不放O₂）。当细胞需要更多ATP（Calvin循环ATP:NADPH=1.5:1，非循环式产生比例约1.28:1，需要循环式补充ATP）。</span></p>

<h3>18.7 Calvin循环三阶段 <span class="tag-must">必考</span></h3>

<div style="background:var(--card-bg);border:1px solid var(--card-border);border-radius:var(--radius);padding:14px 18px;margin:12px 0;">
<p style="margin:0;font-weight:700;">Calvin循环（3次循环净合成1分子G3P）：</p>
<p style="margin:4px 0;">$$3\text{CO}_2 + 9\text{ATP} + 6\text{NADPH} \rightarrow \text{G3P} + 9\text{ADP} + 8\text{Pi} + 6\text{NADP}^+$$</p>
</div>

<table>
<tr><th>阶段</th><th>反应</th><th>关键酶</th></tr>
<tr><td><span class="kp">1. 羧化</span></td><td>CO₂ + RuBP(5C) → 2×3-PGA(3C)</td><td><strong>RuBisCO</strong>（地球上最丰富的酶）</td></tr>
<tr><td><span class="kp">2. 还原</span></td><td>3-PGA → 1,3-BPG(ATP) → G3P(NADPH)</td><td>磷酸甘油酸激酶 + G3P脱氢酶</td></tr>
<tr><td><span class="kp">3. 再生</span></td><td>5×G3P → 3×RuBP(5C)（复杂碳骨架重排）</td><td>转酮酶 + 转醛酶 + 磷酸核酮糖激酶等</td></tr>
</table>

<p><strong>Calvin循环的关键数字</strong>：3轮循环固定3CO₂ → 产生6分子3-PGA → 还原为6分子G3P → 1分子G3P输出（净合成）→ 5分子G3P再生为3分子RuBP。每净合成1分子G3P消耗9ATP+6NADPH。</p>

<blockquote><strong>易错辨析</strong>：Calvin循环的还原阶段与糖酵解的逆过程不同！G3P脱氢酶催化的反应在Calvin循环中使用NADPH（而非NADH），且是从1,3-BPG还原为G3P（合成方向），而糖酵解中是从G3P氧化为1,3-BPG。</blockquote>

<h3>18.8 C3与C4植物的比较 <span class="tag-freq">高频</span></h3>

<p><span class="kp">光呼吸</span><span class="exp">：RuBisCO不仅能羧化RuBP（正常Calvin循环），还能加氧RuBP（光呼吸——消耗O₂释放CO₂，浪费能量）。C3植物在高温干旱条件下（气孔关闭→O₂/CO₂比例↑）光呼吸严重，显著降低光合效率。</span></p>

<p><span class="kp">C4植物的适应性</span><span class="exp">：</span></p>
<table>
<tr><th>特征</th><th>C3植物</th><th>C4植物</th></tr>
<tr><td><span class="kp">解剖结构</span></td><td>仅叶肉细胞含叶绿体</td><td><strong>Kranz结构</strong>——叶肉细胞+维管束鞘细胞双层排列</td></tr>
<tr><td><span class="kp">CO₂固定机制</span></td><td>直接Calvin循环（RuBisCO）</td><td>先由PEP羧化酶固定CO₂为C4酸（叶肉细胞）→转运到维管束鞘细胞→释放CO₂→Calvin循环</td></tr>
<tr><td><span class="kp">光呼吸</span></td><td>高（尤其高温干旱时）</td><td>极低（CO₂被浓缩在维管束鞘细胞中）</td></tr>
<tr><td><span class="kp">代表</span></td><td>水稻、小麦、大豆</td><td>玉米、甘蔗、高粱</td></tr>
<tr><td><span class="kp">RubisCO定位</span></td><td>叶肉细胞</td><td>仅维管束鞘细胞</td></tr>
</table>

<p><strong>直觉类比</strong>：C4途径好比一个「CO₂泵」——PEP羧化酶对CO₂的亲和力远高于RuBisCO（且不加氧），先在叶肉细胞捕获CO₂并浓缩，然后运到维管束鞘细胞「卸货」。这样维管束鞘细胞中的RuBisCO面对高浓度CO₂，加氧活性被抑制，光呼吸大幅降低。</p>

<h3>18.9 光合作用与呼吸作用的对比 <span class="tag-freq">高频</span></h3>

<table>
<tr><th>特征</th><th>光合作用</th><th>呼吸作用（氧化磷酸化）</th></tr>
<tr><td><span class="kp">场所</span></td><td>叶绿体（类囊体膜）</td><td>线粒体（内膜）</td></tr>
<tr><td><span class="kp">能量来源</span></td><td>光能</td><td>化学能（NADH/FADH₂）</td></tr>
<tr><td><span class="kp">电子来源</span></td><td>H₂O（光解）</td><td>NADH/FADH₂</td></tr>
<tr><td><span class="kp">终端受体</span></td><td>NADP⁺ → NADPH</td><td>O₂ → H₂O</td></tr>
<tr><td><span class="kp">产物</span></td><td>O₂ + ATP + NADPH</td><td>H₂O + ATP</td></tr>
<tr><td><span class="kp">质子泵方向</span></td><td>基质 → 类囊体腔（向内泵）</td><td>基质 → 膜间隙（向外泵）</td></tr>
<tr><td><span class="kp">H⁺回流方向</span></td><td>类囊体腔 → 基质</td><td>膜间隙 → 基质</td></tr>
<tr><td><span class="kp">ATP合酶</span></td><td>CF₀CF₁（同源结构）</td><td>F₀F₁</td></tr>
</table>

<blockquote><strong>进化视角</strong>：叶绿体和线粒体都是内共生的产物（内共生假说）——分别来自被原始真核细胞吞噬的光合细菌和需氧细菌。这解释了为什么两者都有双层膜、自身的DNA和核糖体、以及相似的ATP合酶结构。</blockquote>

"""

# ═══════════════════════════════════════════════════════════════════
# 保存知识精讲
# ═══════════════════════════════════════════════════════════════════

knowledge_path = '/workspace/output/生物化学_第14-18章_知识精讲.html'
save_knowledge_html(body, knowledge_path, '第14-18章 激素·信号转导·生物膜·生物能学·生物氧化·光合作用')
print(f'Generated: {knowledge_path}')

# ═══════════════════════════════════════════════════════════════════
# 自测题（28题，满分100分）
# ═══════════════════════════════════════════════════════════════════

questions = [
    # ── 第14章 激素与信号转导 (7题) ──
    {
        "type": "choice", "points": 3,
        "question": "关于水溶性与脂溶性激素，以下描述正确的是？",
        "options": [
            "水溶性激素的受体位于胞内，脂溶性激素的受体位于膜上",
            "水溶性激素需要第二信使，脂溶性激素直接调控基因转录",
            "甲状腺激素是水溶性激素",
            "脂溶性激素的响应速度比水溶性激素快"
        ],
        "answer": 1,
        "explanation": "水溶性激素不能穿越质膜，受体在膜上，需要第二信使传递信号，响应快（秒-分钟）。脂溶性激素穿越质膜与胞内受体（核受体）结合，直接调控基因转录，响应慢（小时-天）。甲状腺激素虽然来自氨基酸（酪氨酸衍生物），但碘原子的引入使其具有脂溶性。",
        "pitfall": "甲状腺激素T₃/T₄虽然和肾上腺素一样是酪氨酸衍生物，但它是脂溶性的——因为碘原子的引入显著增加了疏水性。这是一个经典混淆点。"
    },
    {
        "type": "choice", "points": 3,
        "question": "异三聚体G蛋白激活后，Gα亚基上结合的是哪一分子的核苷酸？",
        "options": ["GDP", "GTP", "ATP", "cAMP"],
        "answer": 1,
        "explanation": "激活态Gα结合GTP（Gα·GTP）。静息态结合GDP（Gα·GDP）。激活过程是GDP被GTP置换。Gα的固有GTP酶活性将GTP水解为GDP，使G蛋白回到静息态——这是GPCR信号终止的基本机制。",
        "pitfall": "注意区分：Gα·GTP=激活态，Gα·GDP=静息态。不要与G蛋白的类型(Gαs/Gαi/Gαq)混淆。激活/静息取决于结合的核苷酸是GTP还是GDP。"
    },
    {
        "type": "multi", "points": 3,
        "question": "以下哪些属于第二信使？（多选）",
        "options": ["cAMP", "肾上腺素", "IP₃", "DAG"],
        "answer": [0, 2, 3],
        "explanation": "cAMP、IP₃和DAG都是第二信使（胞内信号分子）。肾上腺素是第一信使（胞外信号分子/激素），作用于细胞膜表面的GPCR。",
        "pitfall": "第一信使=胞外的信号分子（激素、神经递质等）；第二信使=胞内信号分子（cAMP、cGMP、IP₃、DAG、Ca²⁺）。区分的关键是看它们在胞外还是胞内发挥作用。"
    },
    {
        "type": "choice", "points": 3,
        "question": "cAMP信号通路中，PKA的激活机制是？",
        "options": [
            "cAMP直接磷酸化PKA",
            "cAMP结合调节亚基(R)→R₂C₂解离→催化亚基(C)释放",
            "cAMP使PKA从胞质转移到细胞核",
            "cAMP被PKA水解产生激活效应"
        ],
        "answer": 1,
        "explanation": "静息态PKA是四聚体R₂C₂，两个调节亚基(R)抑制两个催化亚基(C)。cAMP与R亚基结合→R亚基构象变化→R₂C₂解离→C亚基游离并磷酸化下游靶蛋白。这是一个别构激活的经典机制，不是共价修饰。",
        "pitfall": "PKA的激活是「别构激活」（cAMP结合R→R-C解离），不是「磷酸化激活」。PKA本身以去磷酸化状态就有活性，只是被R亚基挡住了活性位点。"
    },
    {
        "type": "choice", "points": 3,
        "question": "IP₃/DAG双信使通路中，IP₃和DAG的来源是？",
        "options": [
            "ATP的水解产物",
            "磷脂酶C(PLC)水解PIP₂",
            "腺苷酸环化酶催化ATP",
            "磷脂酶A₂水解磷脂"
        ],
        "answer": 1,
        "explanation": "Gαq激活磷脂酶C(PLC)，PLC水解质膜内层的磷脂酰肌醇-4,5-二磷酸(PIP₂)，产生IP₃（水溶性，释放Ca²⁺）和DAG（脂溶性，激活PKC）。",
        "pitfall": "PIP₂→IP₃+DAG（PLC催化），ATP→cAMP（AC催化），GTP→cGMP（GC催化）。三对信使、三种来源、三种合成酶，容易混淆，需要分开记忆。"
    },
    {
        "type": "choice", "points": 3,
        "question": "RTK→Ras→MAPK级联的正确顺序是？",
        "options": [
            "RTK二聚化→Ras→Raf→MEK→ERK",
            "RTK二聚化→自磷酸化→Grb2/SOS→Ras→Raf→MEK→ERK",
            "RTK→PLC→Ras→Raf→ERK",
            "RTK→Gα→AC→Ras→MAPK"
        ],
        "answer": 1,
        "explanation": "完整顺序：配体诱导RTK二聚化→自磷酸化→Grb2(SH2)识别磷酸酪氨酸，Grb2(SH3)招募SOS→SOS(GEF)促进Ras释放GDP结合GTP→Ras·GTP激活Raf→Raf激活MEK→MEK激活ERK→ERK入核磷酸化转录因子。",
        "pitfall": "RTK不经过G蛋白（那是GPCR的通路）！RTK通过接头蛋白(Grb2/SOS)直接激活Ras（小G蛋白）。Ras→Raf→MEK→ERK是MAPK级联，各级命名规则：MAPKKK→MAPKK→MAPK。"
    },
    {
        "type": "short", "points": 5,
        "question": "简述G蛋白偶联受体(GPCR)信号转导中G蛋白的GTP/GDP循环过程。",
        "answer": -1,
        "explanation": "<strong>参考答案：</strong><br><br>(1) <strong>静息态</strong>：Gα·GDP与Gβγ形成异三聚体（Gαβγ），信号关闭。(2分)<br><br>(2) <strong>激活</strong>：配体结合GPCR→GPCR构象变化→GPCR作为GEF促进Gα释放GDP→GTP结合到Gα→Gα·GTP与Gβγ解离→Gα·GTP和Gβγ各自激活下游效应器。(2分)<br><br>(3) <strong>终止</strong>：Gα的固有GTP酶活性将GTP水解为GDP→Gα·GDP重新与Gβγ结合→恢复静息三聚体状态。(2分)<br><br>霍乱毒素抑制Gαs的GTP酶活性→Gαs·GTP持续激活→cAMP持续升高。百日咳毒素阻止Gαi被受体激活→Gαi无法抑制AC→cAMP升高。",
        "pitfall": "常见丢分点：(1) 混淆GDP和GTP谁在静息态谁在激活态；(2) 遗漏Gβγ在信号转导中也发挥作用（不仅Gα）；(3) 遗漏G蛋白循环的终止环节——GTP水解是信号终止的关键。"
    },

    # ── 第15章 生物膜与物质运输 (5题) ──
    {
        "type": "choice", "points": 3,
        "question": "Na⁺-K⁺ ATP酶每水解1分子ATP，跨膜转运的离子数量是？",
        "options": ["泵出2Na⁺，泵入3K⁺", "泵出3Na⁺，泵入2K⁺", "泵出3Na⁺，泵入3K⁺", "泵出1Na⁺，泵入1K⁺"],
        "answer": 1,
        "explanation": "Na⁺-K⁺ ATP酶的化学计量比是：3Na⁺出 / 2K⁺进 / 1ATP。每个循环净移出1个正电荷（生电性泵），维持细胞膜电位（约-70mV）和渗透平衡。",
        "pitfall": "3出/2进=净出1正电荷。这是最核心的数字，考试常考。哇巴因(ouabain)是该酶的经典抑制剂。"
    },
    {
        "type": "choice", "points": 3,
        "question": "以下哪种运输方式属于次级主动运输？",
        "options": [
            "GLUT1转运葡萄糖进入红细胞",
            "Na⁺/葡萄糖同向转运(SGLT1)将葡萄糖吸收进小肠上皮细胞",
            "Na⁺-K⁺ ATP酶维持细胞Na⁺/K⁺梯度",
            "K⁺通道介导K⁺外流"
        ],
        "answer": 1,
        "explanation": "SGLT1利用Na⁺-K⁺ ATP酶建立的Na⁺电化学梯度（Na⁺顺梯度流入），将葡萄糖逆梯度运入细胞。这不直接消耗ATP，但间接依赖ATP——属于次级主动运输。GLUT1是协助扩散，Na⁺-K⁺ ATP酶是初级主动运输，K⁺通道是协助扩散。",
        "pitfall": "区分初级和次级主动运输：初级=直接水解ATP（Na⁺-K⁺ ATP酶），次级=利用离子梯度（SGLT），两者都逆浓度梯度运输，但从ATP到离子梯度到葡萄糖是「两步走」。"
    },
    {
        "type": "tf", "points": 2,
        "question": "离子通道的转运速率比载体蛋白慢，因为通道需要经历构象变化。",
        "answer": 1,
        "explanation": "错误。离子通道的转运速率(~10⁶-10⁸ ions/s)远快于载体蛋白(~10²-10⁴ molecules/s)，快了约1000倍。通道仅需「开/关」切换而不经历底物结合-构象变化-释放的催化循环。",
        "pitfall": "恰恰相反——通道快、载体慢。通道是一次开一个孔让离子自由通过，载体需要结合→构象变化→释放的完整催化循环，速率受限于构象变化频率。"
    },
    {
        "type": "tf", "points": 2,
        "question": "GLUT4转运葡萄糖是主动运输过程，需要消耗ATP。",
        "answer": 1,
        "explanation": "错误。GLUT4是葡萄糖协助扩散转运体，不消耗ATP，顺浓度梯度转运。但GLUT4的「上膜」（囊泡从胞内转移到质膜）是受胰岛素信号调控的——这个调控过程消耗能量，但GLUT4本身转运葡萄糖时不耗能。",
        "pitfall": "GLUT1-4都是协助扩散（不耗能）！小肠的SGLT1才是Na⁺依赖的次级主动运输。GLUT的「胰岛素调控」指的是GLUT4的上膜/回收的动态调控过程需要信号转导（消耗能量），而非转运本身需能。"
    },
    {
        "type": "fill", "points": 3,
        "question": "离子的跨膜运输方式中，____运输直接消耗____以逆浓度梯度泵出离子；____运输利用另一种溶质的____能量间接驱动逆浓度运输；____扩散通过通道或载体顺浓度梯度运输，不消耗能量。（依次填入）",
        "answer": [["初级主动"], ["ATP"], ["次级主动"], ["电化学梯度"], ["协助"]],
        "explanation": "三种基本运输方式：初级主动运输直接消耗ATP（如Na⁺-K⁺ ATP酶），次级主动运输利用离子梯度（如SGLT），协助扩散顺梯度不耗能（如GLUT）。",
        "pitfall": "注意区分次级主动运输和协助扩散——两者都涉及载体/通道蛋白，但次级主动运输逆梯度（间接耗能），协助扩散顺梯度（不耗能）。"
    },

    # ── 第16章 生物能学 (5题) ──
    {
        "type": "choice", "points": 3,
        "question": "ΔG°'(标准生化自由能变化)与平衡常数K'eq的关系是？",
        "options": [
            "ΔG°' = K'eq × RT",
            "ΔG°' = -RT ln K'eq",
            "ΔG°' = -RT / K'eq",
            "ΔG°' = RT × ln K'eq"
        ],
        "answer": 1,
        "explanation": "在平衡时ΔG=0，Q=K'eq，代入ΔG=ΔG°'+RT ln Q得：ΔG°'=-RT ln K'eq。R=8.314 J/(mol·K)，T=298K。ΔG°'的负值越大→K'eq越大→反应越趋于完全。",
        "pitfall": "记住负号！ΔG°'=-RT ln K'eq。如果K'eq>1（平衡偏向产物），ln K'eq为正，ΔG°'为负（自发）。"
    },
    {
        "type": "choice", "points": 3,
        "question": "ATP水解的ΔG°'约为-30.5 kJ/mol，为什么ATP被称为「能量货币」？最准确的解释是？",
        "options": [
            "ATP含有最高能的化学键",
            "ATP的磷酸基团转移势能居中——既能被分解代谢合成，又能为合成代谢提供能量",
            "ATP是非可再生的唯一能量形式",
            "ATP的浓度在细胞内最高"
        ],
        "answer": 1,
        "explanation": "ATP不是磷酸化合物的最高能量形式（PEP的ΔG°'=-61.9 kJ/mol），也不是最低的。ATP恰好居中——比低能磷酸酯（如葡萄糖-6-磷酸，-13.8 kJ/mol）高，比超高能化合物（PEP）低。这个中间位置使它既能被代谢途径轻松合成（从ADP+Pi），又能为大多数需能反应提供足够的驱动力。",
        "pitfall": "「高能磷酸键」不是说键能特别高，而是说水解反应的ΔG°'很大（绝对值大）——因为产物的共振稳定化和静电排斥的解除，产物比反应物稳定得多。"
    },
    {
        "type": "choice", "points": 3,
        "question": "ATP水解具有较大负ΔG°'的主要原因是什么？",
        "options": [
            "ATP中的磷酸酐键键能特别高",
            "ATP水解产物的共振稳定化、静电排斥解除和更好的溶剂化",
            "ATP在水溶液中不稳定",
            "ATP的浓度极低"
        ],
        "answer": 1,
        "explanation": "ATP水解ΔG°'大的三个原因：(1) 静电排斥减轻（ATP有4个负电荷集中，水解后ADP和Pi各带负电分开）；(2) 共振稳定化（游离Pi有更多共振形式）；(3) 更好的溶剂化（ADP和Pi比ATP更容易被水分子水合）。",
        "pitfall": "不是因为磷酸酐键的「键能特别高」——键能本身适中。ΔG°'大是因为产物比反应物稳定得多。同样道理，PEP的ΔG°'最大(-61.9)是因为烯醇式→酮式的互变异构释放大量能量，不是磷酸键本身多强。"
    },
    {
        "type": "choice", "points": 3,
        "question": "能荷(Energy Charge)的计算公式是？",
        "options": [
            "[ATP] / ([ATP]+[ADP]+[AMP])",
            "([ATP]+[ADP]) / ([ATP]+[ADP]+[AMP])",
            "([ATP]+0.5[ADP]) / ([ATP]+[ADP]+[AMP])",
            "[ATP] / [ADP]"
        ],
        "answer": 2,
        "explanation": "能荷 EC = ([ATP] + 0.5[ADP]) / ([ATP]+[ADP]+[AMP])。ADP的权重是0.5因为它只有一个高能磷酸酐键。EC范围0～1，正常细胞0.85-0.90。EC调控分解代谢和合成代谢的平衡。",
        "pitfall": "ADP的系数是0.5（不是1），因为ADP只有一个高能磷酸酐键（γ-β），而ATP有两个（γ-β和β-α）。试题可能把0.5换成1来迷惑你。"
    },
    {
        "type": "short", "points": 6,
        "question": "解释偶联反应的原理：为什么己糖激酶能催化葡萄糖+G6P这个ΔG°'>0的反应？",
        "answer": -1,
        "explanation": "<strong>参考答案：</strong><br><br>葡萄糖 + Pi → G6P + H₂O 的ΔG°' = +13.8 kJ/mol（不利反应，不能自发进行）(1分)。<br><br>体内实际反应是：葡萄糖 + ATP → G6P + ADP（ΔG°' = -16.7 kJ/mol）(1分)。<br><br>这是偶联反应的典型——不是「先水解ATP再磷酸化葡萄糖」，而是ATP的γ-磷酸基团直接转移到葡萄糖上（通过己糖激酶的催化），形成一个反应序列。总ΔG°' = ΔG°'(G6P水解) + ΔG°'(ATP水解) = +13.8 + (-30.5) = -16.7 kJ/mol，热力学上变得有利(2分)。<br><br>关键理解：偶联通过「共同化学中间体」（磷酸基团转移）实现，而不是ATP水解「释放能量」再被「利用」——热是弥散的，不能定向驱动反应(1分)。",
        "pitfall": "不能写成「ATP水解放出能量，推动葡萄糖磷酸化」——这在热力学上不准确。偶联的实质是形成共同中间体，两个反应合并为一条反应路径。"
    },

    # ── 第17章 生物氧化 (6题) ──
    {
        "type": "choice", "points": 3,
        "question": "以下哪一组呼吸链组分的电子传递顺序是正确的？",
        "options": [
            "NADH→CoQ→Cyt c→复合体I→O₂",
            "NADH→复合体I→CoQ→复合体III→Cyt c→复合体IV→O₂",
            "NADH→复合体II→CoQ→复合体III→Cyt c→复合体I→O₂",
            "FADH₂→复合体I→CoQ→复合体IV→O₂"
        ],
        "answer": 1,
        "explanation": "正确顺序：NADH→复合体I→CoQ→复合体III→Cyt c→复合体IV→O₂。FADH₂进入点在复合体II（即琥珀酸脱氢酶），然后→CoQ→复合体III→Cyt c→复合体IV→O₂。",
        "pitfall": "(1) 复合体II不是NADH的入口——它是FADH₂（来自琥珀酸氧化）的入口；(2) Cyt c位于复合体III和IV之间；(3) 复合体IV是最后一个复合体，最终将电子传给O₂。"
    },
    {
        "type": "choice", "points": 3,
        "question": "以下哪一对抑制剂与靶点的匹配是错误的？",
        "options": [
            "鱼藤酮 — 复合体I",
            "抗霉素A — 复合体III",
            "CN⁻ — 复合体II",
            "寡霉素 — ATP合酶(F₀)"
        ],
        "answer": 2,
        "explanation": "CN⁻（氰化物）、CO和N₃⁻抑制复合体IV（细胞色素c氧化酶），不是复合体II。鱼藤酮→复合体I，抗霉素A→复合体III，寡霉素→ATP合酶(F₀)。",
        "pitfall": "CN⁻/CO的靶点是复合体IV（与Cyt a₃结合），这是最致命的抑制剂——因为O₂是终端受体，被阻断后整个呼吸链无法运转。"
    },
    {
        "type": "choice", "points": 3,
        "question": "化学渗透假说的核心内容是什么？",
        "options": [
            "电子传递和ATP合成通过高能化学中间体(X~P)耦合",
            "电子传递将H⁺泵出线粒体内膜→形成质子电化学梯度→H⁺经ATP合酶回流驱动ATP合成",
            "ATP合酶直接消耗O₂产生ATP",
            "NADH直接磷酸化ADP产生ATP"
        ],
        "answer": 1,
        "explanation": "Mitchell的化学渗透假说（1978年诺贝尔化学奖）核心：电子传递和ATP合成通过跨膜的质子电化学梯度（ΔμH⁺）间接耦合——不通过「高能化学中间体」。三个必要条件：内膜对H⁺不通透、电子传递泵H⁺、H⁺经ATP合酶回流。",
        "pitfall": "这个假说的关键是「间接耦合」——电子传递链和ATP合酶是物理分离的，通过H⁺梯度连接。解偶联剂(DNP)消除H⁺梯度后，电子传递继续但ATP不合成，这直接证明了两个过程是可分离的。"
    },
    {
        "type": "choice", "points": 3,
        "question": "ATP合酶的F₁部分中，负责催化ATP合成的亚基是？",
        "options": ["α亚基", "β亚基", "γ亚基", "c亚基"],
        "answer": 1,
        "explanation": "F₁的β亚基是催化亚基（3个β亚基在γ轴旋转时依次经历O→L→T→O构象循环，T态合成ATP）。γ亚基是不对称中心轴（旋转驱动），α亚基是结构亚基（提供支撑），c亚基属于F₀（质子通道的旋转环）。",
        "pitfall": "注意区分：F₁催化头部=α₃β₃γδε（β是催化亚基），F₀质子通道=a+c环。γ轴的旋转被β亚基感知并转化为构象变化，ATP在β亚基的T态合成。"
    },
    {
        "type": "tf", "points": 2,
        "question": "鱼藤酮同时阻断来自NADH和FADH₂的电子传递。",
        "answer": 1,
        "explanation": "错误。鱼藤酮仅阻断复合体I（NADH→CoQ的电子传递）。FADH₂通过复合体II进入呼吸链（在复合体I下游的CoQ处汇入），鱼藤酮不阻断FADH₂→复合体II→CoQ→III→IV→O₂的电子传递。",
        "pitfall": "区分不同抑制剂的阻断范围：鱼藤酮=阻断NADH来源的电子；抗霉素A和CN⁻=阻断全部电子传递（因为它们在复合体I和II交汇后的下游）。"
    },
    {
        "type": "short", "points": 4,
        "question": "解释为什么NADH氧化产生约2.5个ATP，而FADH₂氧化仅产生约1.5个ATP。",
        "answer": -1,
        "explanation": "<strong>参考答案：</strong><br><br>关键原因是「进入点的差异」导致「泵出的H⁺数量不同」。(1分)<br><br>NADH的电子从复合体I进入呼吸链→经过复合体I、III、IV三个质子泵，共泵出约10个H⁺→ATP合酶每合成1个ATP需要约4个H⁺回流→10÷4≈2.5 ATP。(2分)<br><br>FADH₂的电子从复合体II（琥珀酸脱氢酶）进入→不经过复合体I，只经过复合体III和IV两个质子泵，共泵出约6个H⁺→6÷4≈1.5 ATP。(2分)",
        "pitfall": "(1) 复合体II本身不是质子泵！(2) 不是所有电子传递组分都能泵H⁺——只有复合体I、III、IV是质子泵；(3) 这解释了为什么1分子葡萄糖完全氧化产生约30-32 ATP（而非旧教科书的36-38）。"
    },

    # ── 第18章 光合作用 (5题) ──
    {
        "type": "choice", "points": 3,
        "question": "光合作用Z方案中，光系统I(PSI)反应中心的色素是？",
        "options": ["P680", "P700", "叶绿素b", "类胡萝卜素"],
        "answer": 1,
        "explanation": "PSI反应中心是P700（最大吸收700nm），PSII反应中心是P680（最大吸收680nm）。两者都是特殊的叶绿素a二聚体。",
        "pitfall": "PSII=P680（短波长=更高能量），PSI=P700（长波长=较低能量）。「II在先，I在后」的命名是按发现顺序，不是按电子传递顺序——实际上电子先经过PSII再经过PSI。"
    },
    {
        "type": "choice", "points": 3,
        "question": "Calvin循环的三个阶段依次是？",
        "options": [
            "还原→羧化→再生",
            "羧化→还原→再生",
            "羧化→再生→还原",
            "再生→羧化→还原"
        ],
        "answer": 1,
        "explanation": "Calvin循环三阶段：(1) 羧化——CO₂与RuBP反应（RuBisCO催化），生成2分子3-PGA；(2) 还原——3-PGA经磷酸化和还原生成G3P（消耗ATP和NADPH）；(3) 再生——G3P经碳骨架重排再生RuBP。每3轮循环净合成1分子G3P。",
        "pitfall": "「羧化→还原→再生」的顺序不可颠倒。每净合成1分子G3P消耗9ATP+6NADPH——这些数字是高频考点。"
    },
    {
        "type": "choice", "points": 3,
        "question": "关于C4植物与C3植物的比较，以下描述正确的是？",
        "options": [
            "C4植物在高温干旱条件下光合效率低于C3植物",
            "C4植物的RuBisCO存在于叶肉细胞中",
            "C4植物的Kranz结构包括叶肉细胞和维管束鞘细胞两层",
            "C4植物的光呼吸比C3植物更强烈"
        ],
        "answer": 2,
        "explanation": "C4植物有Kranz结构——叶肉细胞+维管束鞘细胞呈双层同心排列。PEP羧化酶在叶肉细胞固定CO₂→生成C4酸→转运到维管束鞘细胞释放CO₂→被维管束鞘细胞中的RuBisCO用于Calvin循环。C4植物在高温干旱条件下光呼吸极低，光合效率更高。",
        "pitfall": "C4植物的RuBisCO不在叶肉细胞，而在维管束鞘细胞——这是Kranz结构的关键特征。PEP羧化酶在叶肉细胞中「初固定」CO₂以浓缩。"
    },
    {
        "type": "tf", "points": 2,
        "question": "光合作用释放的O₂来自CO₂的光解。",
        "answer": 1,
        "explanation": "错误。光合作用释放的O₂来自H₂O的光解（水的氧化），不是CO₂。这一结论由¹⁸O同位素标记实验证明——用H₂¹⁸O培养植物时释放的是¹⁸O₂，用C¹⁸O₂时释放的是普通O₂。",
        "pitfall": "总反应式中O₂看起来可以来自CO₂或H₂O的O原子——但同位素实验证实是H₂O的O。水光解发生在PSII的放氧复合体(OEC)，Mn₄CaO₅簇催化。"
    },
    {
        "type": "short", "points": 5,
        "question": "简述光合磷酸化与氧化磷酸化的异同。",
        "answer": -1,
        "explanation": "<strong>参考答案：</strong><br><br><strong>相同点（3分）：</strong><br>(1) 都基于化学渗透原理——电子传递泵H⁺→质子梯度→H⁺经ATP合酶回流→驱动ATP合成。<br>(2) 都有相似的ATP合酶结构（叶绿体CF₀CF₁与线粒体F₀F₁同源）。<br>(3) 都使用醌类(CoQ/PQ)和细胞色素类作为电子载体。<br><br><strong>不同点（3分）：</strong><br>(1) 能量来源：光合磷酸化用光能（光子），氧化磷酸化用化学能（NADH/FADH₂）。<br>(2) 电子来源：光合磷酸化来自H₂O的光解，氧化磷酸化来自NADH/FADH₂。<br>(3) 电子最终去向：光合磷酸化去向NADP⁺→NADPH，氧化磷酸化去向O₂→H₂O。<br>(4) 场所：类囊体膜 vs 线粒体内膜。<br>(5) 质子泵方向：基质→类囊体腔(向内) vs 基质→膜间隙(向外)。",
        "pitfall": "两者的相似性源于进化上的同源（内共生假说），但电子流向正好相反——光合作用中H₂O→电子传递链→NADP⁺（还原方向），呼吸作用中NADH→电子传递链→O₂（氧化方向）。光合作用的光反应本质是「将低能电子(H₂O)提升为高能电子(NADPH)的逆热力学过程」。"
    },

    # ── 综合题 (2题) ──
    {
        "type": "fill", "points": 4,
        "question": "能荷(Energy Charge) = (________ + 0.5×________) / (________ + ________ + ________)。正常的哺乳动物细胞能荷约为________。",
        "answer": [["[ATP]"], ["[ADP]"], ["[ATP]"], ["[ADP]"], ["[AMP]"], ["0.85-0.90"]],
        "explanation": "EC = ([ATP]+0.5[ADP])/([ATP]+[ADP]+[AMP])。正常细胞EC维持在0.85-0.90。EC<0.5时细胞趋向死亡。EC调控分解代谢(EC低时激活)和合成代谢(EC高时激活)的平衡。",
        "pitfall": "ADP的系数是0.5——因为它只有一个高能磷酸酐键。三种腺苷酸的总和构成腺苷酸池。"
    },
    {
        "type": "essay", "points": 8,
        "question": "综合阐述化学渗透假说的核心内容，并结合氧化磷酸化和光合磷酸化说明其普遍性。",
        "answer": -1,
        "explanation": "<strong>参考答案要点：</strong><br><br><strong>1. 化学渗透假说核心（Mitchell, 1961, Nobel 1978）（4分）：</strong><br>- 线粒体内膜对H⁺不通透<br>- 电子传递释放的能量用于将H⁺从基质泵到膜间隙→形成质子电化学梯度(ΔμH⁺)=ΔpH+Δψ<br>- H⁺经ATP合酶(F₀F₁)回流→构象变化→驱动ATP合成<br>- 电子传递和ATP合成是间接耦合（通过H⁺梯度），而非高能化学中间体<br>- 关键证据：解偶联剂(DNP)消除梯度后电子传递继续但ATP不合成<br><br><strong>2. 在氧化磷酸化中（2分）：</strong><br>- 复合体I、III、IV泵H⁺→膜间隙→F₀F₁→ATP<br><br><strong>3. 在光合磷酸化中（2分）：</strong><br>- PSII水光解(腔内产H⁺)+PQH₂氧化(Cyt b₆f将H⁺泵入腔内)→类囊体腔质子梯度→CF₀CF₁→ATP<br>- 基本逻辑完全相同，仅场所（线粒体内膜vs类囊体膜）和方向（泵出vs泵入）不同<br><br>化学渗透假说是生物化学中最具统一性的概念之一——线粒体和叶绿体虽为不同细胞器，但使用相同的底层物理原理：H⁺梯度耦合电子传递和ATP合成。",
        "pitfall": "这道大题最忌「偏科」——只写氧化磷酸化而忽略光合磷酸化，或反之。题干明确要求「结合两者说明普遍性」。还需注意注明Mitchell获诺贝尔奖和关键实验证据（解偶联剂实验）。"
    }
]

# ═══════════════════════════════════════════════════════════════════
# 保存自测题
# ═══════════════════════════════════════════════════════════════════

test_path = '/workspace/output/生物化学_第14-18章_自测题.html'
save_test(
    questions,
    test_path,
    '第14-18章 激素·信号转导·生物膜·生物能学·生物氧化·光合作用',
    subtitle='生物化学原理第四版 · 深度学习模式 · 满分100分',
    duration_minutes=60
)
print(f'Generated: {test_path}')
print('Done!')