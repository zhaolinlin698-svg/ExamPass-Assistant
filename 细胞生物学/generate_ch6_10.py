#!/usr/bin/env python3
"""Generate knowledge HTML and test HTML for chapters 6-10."""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'ExamPass-Assistant', 'scripts'))
from template_engine import save_knowledge_html, save_test

BASE = '/workspace/细胞生物学'

# ============================================================
# Chapter 6: 线粒体与叶绿体
# ============================================================

CH06_KNOWLEDGE = r"""
<h2>六、线粒体与叶绿体</h2>

<h3>6.1 线粒体的形态结构 <span class="tag-must">必考</span></h3>
<p><span class="kp">线粒体（Mitochondria）</span><span class="exp">——真核细胞中进行氧化磷酸化、产生ATP的细胞器，被称为"细胞的动力工厂"。</span></p>
<p><strong>结构</strong>（由外到内）：</p>
<ul>
  <li><span class="kp">外膜</span><span class="exp">——通透性较高，含孔蛋白通道</span></li>
  <li><span class="kp">膜间隙</span><span class="exp">——内外膜之间的空间</span></li>
  <li><span class="kp">内膜</span><span class="exp">——向内折叠形成嵴，通透性低，含呼吸链酶复合体</span></li>
  <li><span class="kp">基质</span><span class="exp">——含三羧酸循环酶系、mtDNA、核糖体</span></li>
</ul>

<h3>6.2 氧化磷酸化 <span class="tag-must">必考</span></h3>
<p><span class="kp">氧化磷酸化</span><span class="exp">——电子沿呼吸链传递过程中释放的能量，驱动H⁺从基质泵到膜间隙，形成质子电化学梯度，H⁺回流驱动ATP合酶合成ATP。</span></p>
<p><strong>化学渗透假说</strong>（Mitchell, 1961）：</p>
<ol>
  <li>呼吸链传递电子，将H⁺从基质泵到膜间隙</li>
  <li>形成跨内膜的质子电化学梯度（质子动力）</li>
  <li>H⁺通过ATP合酶回流到基质</li>
  <li>ATP合酶利用H⁺回流的能量合成ATP</li>
</ol>
<blockquote>易错：氧化磷酸化和光合磷酸化都基于化学渗透假说，都利用质子梯度驱动ATP合成。</blockquote>

<h3>6.3 线粒体的半自主性 <span class="tag-key">重点</span></h3>
<ul>
  <li><span class="kp">有自己的DNA（mtDNA）</span><span class="exp">——环状DNA，编码部分线粒体蛋白和tRNA、rRNA</span></li>
  <li><span class="kp">有自己的核糖体</span><span class="exp">——类似原核生物的70S核糖体</span></li>
  <li><span class="kp">大部分蛋白质由核基因编码</span><span class="exp">——在胞质中合成后转运到线粒体</span></li>
  <li><span class="kp">分裂方式类似细菌</span><span class="exp">——通过分裂增殖</span></li>
</ul>

<h3>6.4 线粒体的起源——内共生学说 <span class="tag-must">必考</span></h3>
<p><span class="kp">内共生学说</span><span class="exp">——由Margulis提出，认为线粒体起源于被原始真核细胞吞噬的需氧细菌。</span></p>
<p><strong>证据</strong>：</p>
<ul>
  <li>线粒体有双层膜（外膜来自宿主，内膜来自细菌）</li>
  <li>有独立的环状DNA</li>
  <li>核糖体为70S（与原核生物相同）</li>
  <li>以分裂方式增殖</li>
  <li>对抗生素敏感（如氯霉素抑制线粒体蛋白合成）</li>
</ul>

<h3>6.5 叶绿体 <span class="tag-key">重点</span></h3>
<p><span class="kp">叶绿体（Chloroplast）</span><span class="exp">——植物细胞中进行光合作用的细胞器。</span></p>
<p><strong>结构</strong>：</p>
<ul>
  <li><span class="kp">外膜和内膜</span><span class="exp">——双层膜包围</span></li>
  <li><span class="kp">类囊体</span><span class="exp">——扁平囊状结构，堆叠成基粒，含光合色素和电子传递链</span></li>
  <li><span class="kp">基质</span><span class="exp">——含碳固定酶系（Calvin循环）、cpDNA、核糖体</span></li>
</ul>

<h3>6.6 光合作用 <span class="tag-key">重点</span></h3>
<p><strong>光反应</strong>（类囊体膜上）：</p>
<ul>
  <li>光能 --&gt; 化学能（ATP和NADPH）</li>
  <li>水的光解：$2H_2O \rightarrow O_2 + 4H^+ + 4e^-$</li>
  <li>光合磷酸化：利用质子梯度合成ATP</li>
</ul>
<p><strong>暗反应</strong>（基质中）：</p>
<ul>
  <li>Calvin循环：利用ATP和NADPH固定CO₂</li>
  <li>$CO_2 + RuBP \rightarrow 2\times 3-PGA$（RuBisCO催化）</li>
</ul>

<h3>6.7 叶绿体的半自主性与起源 <span class="tag-freq">高频</span></h3>
<p>类似线粒体，叶绿体也有自己的DNA、核糖体（70S），大部分蛋白质由核基因编码，通过分裂增殖。内共生学说认为叶绿体起源于被吞噬的蓝藻（蓝细菌）。</p>
<blockquote>易错：线粒体和叶绿体都是半自主性细胞器，但它们的起源不同——线粒体来自需氧细菌，叶绿体来自蓝藻。</blockquote>
"""

CH06_TEST = [
    {"type": "choice", "points": 3,
     "question": "化学渗透假说中，ATP合酶利用的能量来源是：",
     "options": ["电子传递", "NADH氧化", "质子电化学梯度", "CO₂固定"],
     "answer": 2, "explanation": "化学渗透假说的核心是：呼吸链泵出H⁺形成跨膜质子梯度，H⁺通过ATP合酶回流时驱动ATP合成。"},
    {"type": "choice", "points": 3,
     "question": "下列哪项不是内共生学说的证据？",
     "options": ["线粒体有双层膜", "线粒体有环状DNA", "线粒体核糖体为80S", "线粒体以分裂方式增殖"],
     "answer": 2, "explanation": "线粒体核糖体为70S（与原核生物相同），不是80S（真核生物核糖体）。这是支持内共生学说的重要证据。"},
    {"type": "tf", "points": 2,
     "question": "线粒体和叶绿体都是完全自主的细胞器，不依赖核基因。",
     "options": [], "answer": 1,
     "explanation": "错误。它们是半自主性细胞器，大部分蛋白质由核基因编码，在胞质中合成后转运到线粒体/叶绿体中。"},
    {"type": "short", "points": 8,
     "question": "简述线粒体和叶绿体的结构和功能，并说明它们在细胞生命活动中的作用。",
     "answer": -1,
     "explanation": "<strong>线粒体</strong>：双层膜结构，内膜折叠成嵴，含呼吸链。功能：氧化磷酸化产生ATP，是细胞能量代谢中心。<br><strong>叶绿体</strong>：双层膜+类囊体，含光合色素。功能：光合作用将光能转化为化学能。<br><strong>作用</strong>：线粒体提供细胞活动所需能量；叶绿体是自养生物的能量来源，产生O₂维持大气氧含量。"},
    {"type": "short", "points": 8,
     "question": "简述光合磷酸化和氧化磷酸化的异同。",
     "answer": -1,
     "explanation": "<strong>相同</strong>：都基于化学渗透假说，利用电子传递链建立质子梯度，通过ATP合酶合成ATP。<br><strong>不同</strong>：(1)场所：光合磷酸化在类囊体膜，氧化磷酸化在线粒体内膜；(2)能量来源：光合磷酸化来自光能，氧化磷酸化来自有机物氧化；(3)电子来源：光合磷酸化来自水的光解，氧化磷酸化来自NADH/FADH₂。"},
    {"type": "essay", "points": 12,
     "question": "论述内共生学说的主要内容和证据，并说明线粒体和叶绿体的半自主性。",
     "answer": -1,
     "explanation": "<strong>内共生学说</strong>：线粒体起源于被吞噬的需氧细菌，叶绿体起源于被吞噬的蓝藻。<br><strong>证据</strong>：(1)双层膜；(2)环状DNA；(3)70S核糖体；(4)分裂方式增殖；(5)对抗生素敏感。<br><strong>半自主性</strong>：有自己的DNA和核糖体，能合成部分蛋白质；但大部分蛋白质由核基因编码，需从胞质转运进来，且分裂受核基因调控。"}
]

# ============================================================
# Chapter 7: 细胞骨架
# ============================================================

CH07_KNOWLEDGE = r"""
<h2>七、细胞骨架</h2>

<h3>7.1 细胞骨架概述 <span class="tag-key">重点</span></h3>
<p><span class="kp">细胞骨架（Cytoskeleton）</span><span class="exp">——真核细胞中的蛋白质纤维网络体系，包括微丝、微管和中间纤维三大类，在维持细胞形态、细胞运动、胞内运输和细胞分裂中发挥重要作用。</span></p>

<h3>7.2 微丝（Microfilament）<span class="tag-must">必考</span></h3>
<table>
  <tr><th>特征</th><th>描述</th></tr>
  <tr><td>直径</td><td>~7nm（最细）</td></tr>
  <tr><td>组成</td><td>肌动蛋白（Actin）</td></tr>
  <tr><td>结构</td><td>双股螺旋</td></tr>
  <tr><td>敏感药物</td><td>细胞松弛素（抑制聚合）、鬼笔环肽（稳定微丝）</td></tr>
</table>
<p><strong>功能</strong>：</p>
<ul>
  <li><span class="kp">维持细胞形态</span><span class="exp">——形成细胞皮层</span></li>
  <li><span class="kp">细胞运动</span><span class="exp">——伪足形成、变形运动</span></li>
  <li><span class="kp">肌肉收缩</span><span class="exp">——与肌球蛋白相互作用产生收缩力</span></li>
  <li><span class="kp">细胞分裂</span><span class="exp">——收缩环的形成（胞质分裂）</span></li>
  <li><span class="kp">胞内运输</span><span class="exp">——与肌球蛋白协作进行短距离运输</span></li>
</ul>

<h3>7.3 微管（Microtubule）<span class="tag-must">必考</span></h3>
<table>
  <tr><th>特征</th><th>描述</th></tr>
  <tr><td>直径</td><td>~25nm（最粗）</td></tr>
  <tr><td>组成</td><td>$\alpha$-微管蛋白和$\beta$-微管蛋白异二聚体</td></tr>
  <tr><td>结构</td><td>13根原纤维围成的中空管状</td></tr>
  <tr><td>敏感药物</td><td>秋水仙素/秋水仙碱（抑制聚合）、紫杉醇（稳定微管）</td></tr>
</table>
<p><strong>功能</strong>：</p>
<ul>
  <li><span class="kp">维持细胞形态</span></li>
  <li><span class="kp">细胞分裂</span><span class="exp">——纺锤体的形成</span></li>
  <li><span class="kp">胞内运输</span><span class="exp">——与驱动蛋白、动力蛋白协作进行长距离运输</span></li>
  <li><span class="kp">纤毛和鞭毛的运动</span></li>
</ul>
<p><span class="kp">微管组织中心（MTOC）</span><span class="exp">——微管装配的起始位点，中心体是动物细胞主要的MTOC。</span></p>

<h3>7.4 中间纤维（Intermediate Filament）<span class="tag-key">重点</span></h3>
<table>
  <tr><th>特征</th><th>描述</th></tr>
  <tr><td>直径</td><td>~10nm（介于微丝和微管之间）</td></tr>
  <tr><td>组成</td><td>多种纤维蛋白（角蛋白、波形蛋白、核纤层蛋白等）</td></tr>
  <tr><td>结构</td><td>四聚体组成的绳索状纤维</td></tr>
  <tr><td>敏感药物</td><td>无特异性药物</td></tr>
</table>
<p><strong>功能</strong>：</p>
<ul>
  <li><span class="kp">机械支撑</span><span class="exp">——抵抗机械应力</span></li>
  <li><span class="kp">细胞连接</span><span class="exp">——通过桥粒连接相邻细胞</span></li>
  <li><span class="kp">核纤层</span><span class="exp">——核纤层蛋白构成核纤层，维持核形态</span></li>
</ul>

<h3>7.5 分子马达 <span class="tag-key">重点</span></h3>
<table>
  <tr><th>马达蛋白</th><th>轨道</th><th>方向</th><th>功能</th></tr>
  <tr><td>肌球蛋白（Myosin）</td><td>微丝</td><td>指向+端</td><td>肌肉收缩、胞内运输</td></tr>
  <tr><td>驱动蛋白（Kinesin）</td><td>微管</td><td>指向+端（顺向）</td><td>胞内运输</td></tr>
  <tr><td>动力蛋白（Dynein）</td><td>微管</td><td>指向-端（逆向）</td><td>胞内运输、纤毛运动</td></tr>
</table>
<blockquote>易错：驱动蛋白和动力蛋白都在微管上运动，但方向相反。驱动蛋白向+端（细胞外周），动力蛋白向-端（细胞中心/MTOC）。</blockquote>

<h3>7.6 肌肉收缩机制 <span class="tag-freq">高频</span></h3>
<p><span class="kp">肌丝滑动模型</span><span class="exp">——肌肉收缩是由肌动蛋白（细丝）和肌球蛋白（粗丝）相对滑动所致。</span></p>
<p><strong>过程</strong>：</p>
<ol>
  <li>Ca²⁺浓度升高，与肌钙蛋白结合</li>
  <li>原肌球蛋白构象改变，暴露肌动蛋白上的肌球蛋白结合位点</li>
  <li>肌球蛋白头部与肌动蛋白结合，ATP水解驱动构象变化</li>
  <li>肌球蛋白头部摆动，拉动细丝向肌节中央滑动</li>
  <li>ATP结合使肌球蛋白头部与肌动蛋白解离</li>
</ol>
"""

CH07_TEST = [
    {"type": "choice", "points": 3,
     "question": "下列哪种药物可抑制微管的聚合？",
     "options": ["细胞松弛素", "秋水仙素", "鬼笔环肽", "紫杉醇"],
     "answer": 1, "explanation": "秋水仙素/秋水仙碱抑制微管聚合。细胞松弛素抑制微丝聚合，紫杉醇稳定微管（抑制解聚），鬼笔环肽稳定微丝。"},
    {"type": "choice", "points": 3,
     "question": "微管组织中心（MTOC）在动物细胞中主要是指：",
     "options": ["核仁", "中心体", "内质网", "高尔基体"],
     "answer": 1, "explanation": "中心体是动物细胞主要的微管组织中心，是微管装配的起始位点。"},
    {"type": "multi", "points": 4,
     "question": "下列哪些属于分子马达蛋白？",
     "options": ["肌球蛋白", "肌动蛋白", "驱动蛋白", "动力蛋白", "角蛋白"],
     "answer": [0, 2, 3], "explanation": "肌球蛋白在微丝上运动，驱动蛋白和动力蛋白在微管上运动。肌动蛋白是微丝的组成蛋白，角蛋白是中间纤维的组成蛋白。"},
    {"type": "tf", "points": 2,
     "question": "驱动蛋白和动力蛋白都在微丝上运动，方向相反。",
     "options": [], "answer": 1,
     "explanation": "错误。驱动蛋白和动力蛋白的轨道是微管，不是微丝。在微丝上运动的是肌球蛋白。"},
    {"type": "short", "points": 8,
     "question": "简述骨骼肌收缩的基本过程。",
     "answer": -1,
     "explanation": "(1)神经冲动导致Ca²⁺从肌质网释放；(2)Ca²⁺与肌钙蛋白结合，原肌球蛋白移位，暴露肌动蛋白上的结合位点；(3)肌球蛋白头部与肌动蛋白结合；(4)ATP水解驱动肌球蛋白头部摆动，细丝滑动；(5)ATP结合使肌球蛋白解离，循环往复。"},
    {"type": "short", "points": 8,
     "question": "真核细胞内物质运输的马达蛋白有哪些？描述其功能。",
     "answer": -1,
     "explanation": "<strong>肌球蛋白</strong>：在微丝上运动，向+端，参与肌肉收缩和短距离胞内运输。<br><strong>驱动蛋白</strong>：在微管上运动，向+端（顺向运输），负责从细胞中心向外周运输。<br><strong>动力蛋白</strong>：在微管上运动，向-端（逆向运输），负责从细胞外周向中心运输。"}
]

# ============================================================
# Chapter 8: 细胞核与染色体
# ============================================================

CH08_KNOWLEDGE = r"""
<h2>八、细胞核与染色体</h2>

<h3>8.1 核被膜与核孔复合体 <span class="tag-must">必考</span></h3>
<p><span class="kp">核被膜</span><span class="exp">——由内外两层核膜组成，外层与粗面内质网相连，是细胞核的边界。</span></p>
<ul>
  <li><span class="kp">外核膜</span><span class="exp">——与rER相连，表面有核糖体</span></li>
  <li><span class="kp">内核膜</span><span class="exp">——与核纤层相连</span></li>
  <li><span class="kp">核周隙</span><span class="exp">——内外核膜之间的空间</span></li>
</ul>
<p><span class="kp">核孔复合体（NPC）</span><span class="exp">——跨越核被膜的通道结构，是核质之间物质运输的通道。</span></p>
<ul>
  <li>小分子（&lt;40kD）可自由扩散</li>
  <li>大分子（蛋白质、RNA）需要<strong>主动运输</strong>，依赖核定位信号（NLS）或核输出信号（NES）</li>
</ul>
<p><span class="kp">核定位信号（NLS）</span><span class="exp">——蛋白质中引导其进入细胞核的氨基酸序列，富含碱性氨基酸（如赖氨酸、精氨酸）。</span></p>

<h3>8.2 核纤层 <span class="tag-key">重点</span></h3>
<p><span class="kp">核纤层（Nuclear Lamina）</span><span class="exp">——位于内核膜内侧的纤维网络，由核纤层蛋白（Lamin）组成。</span></p>
<p><strong>功能</strong>：</p>
<ul>
  <li>维持核的形态和结构完整性</li>
  <li>为染色质提供锚定位点</li>
  <li>参与核被膜的解体和重建（有丝分裂时）</li>
</ul>

<h3>8.3 染色质与染色体 <span class="tag-must">必考</span></h3>
<p><span class="kp">染色质</span><span class="exp">——间期细胞核中DNA与组蛋白等蛋白质的复合物。</span></p>
<p><strong>分类</strong>：</p>
<ul>
  <li><span class="kp">常染色质</span><span class="exp">——松散、染色浅、有转录活性</span></li>
  <li><span class="kp">异染色质</span><span class="exp">——紧密、染色深、转录不活跃</span></li>
</ul>

<h4>染色质包装的结构模型</h4>
<p>DNA包装过程（多级螺旋模型）：</p>
<ol>
  <li><span class="kp">核小体</span><span class="exp">——DNA(146bp)缠绕在组蛋白八聚体上，直径11nm</span></li>
  <li><span class="kp">30nm纤维</span><span class="exp">——核小体螺旋化形成螺线管</span></li>
  <li><span class="kp">超螺线管</span><span class="exp">——进一步螺旋化</span></li>
  <li><span class="kp">染色单体</span><span class="exp">——最高级别的包装</span></li>
</ol>
<p><span class="kp">核小体</span><span class="exp">——染色质的基本结构单位，由核心组蛋白八聚体（H2A、H2B、H3、H4各两份）和缠绕其上的DNA组成，H1锁住DNA进出口。</span></p>

<h3>8.4 染色体 <span class="tag-key">重点</span></h3>
<p><strong>染色体结构</strong>：</p>
<ul>
  <li><span class="kp">着丝粒</span><span class="exp">——初级缢痕，纺锤体微管附着位点</span></li>
  <li><span class="kp">端粒</span><span class="exp">——染色体末端特化结构，保护染色体完整性</span></li>
  <li><span class="kp">复制起始点</span><span class="exp">——DNA复制的起始位点</span></li>
</ul>
<p><span class="kp">端粒</span><span class="exp">——染色体末端的特殊结构，由端粒DNA（TTAGGG重复序列）和端粒蛋白组成。端粒的主要功能：保护染色体末端不被降解、防止染色体末端融合、参与染色体在核内的定位。</span></p>

<h3>8.5 核仁 <span class="tag-freq">高频</span></h3>
<p><span class="kp">核仁</span><span class="exp">——细胞核内合成核糖体RNA（rRNA）和装配核糖体亚基的场所。</span></p>
<p><strong>结构</strong>：</p>
<ul>
  <li><span class="kp">纤维中心</span><span class="exp">——rDNA所在区域</span></li>
  <li><span class="kp">致密纤维成分</span><span class="exp">——rRNA转录和加工</span></li>
  <li><span class="kp">颗粒成分</span><span class="exp">——核糖体亚基装配</span></li>
</ul>
<p><span class="kp">核仁组织区（NOR）</span><span class="exp">——染色体上含rRNA基因的区域，是核仁形成的位点。</span></p>
"""

CH08_TEST = [
    {"type": "choice", "points": 3,
     "question": "核定位信号（NLS）的典型特征是富含：",
     "options": ["酸性氨基酸", "碱性氨基酸", "疏水氨基酸", "芳香族氨基酸"],
     "answer": 1, "explanation": "NLS富含碱性氨基酸（如赖氨酸、精氨酸），这是引导蛋白质进入细胞核的关键信号。"},
    {"type": "choice", "points": 3,
     "question": "染色质的基本结构单位是：",
     "options": ["30nm纤维", "核小体", "超螺线管", "螺线管"],
     "answer": 1, "explanation": "核小体是染色质的基本结构单位，由DNA缠绕在组蛋白八聚体上构成。"},
    {"type": "tf", "points": 2,
     "question": "常染色质染色深、转录不活跃；异染色质染色浅、转录活跃。",
     "options": [], "answer": 1,
     "explanation": "错误。恰恰相反：常染色质松散、染色浅、转录活跃；异染色质紧密、染色深、转录不活跃。"},
    {"type": "short", "points": 8,
     "question": "简述核纤层的结构及其生物学功能。",
     "answer": -1,
     "explanation": "<strong>结构</strong>：位于内核膜内侧的纤维网络，由核纤层蛋白（Lamin）组成，属于中间纤维家族。<br><strong>功能</strong>：(1)维持细胞核形态和结构完整性；(2)为染色质提供锚定位点；(3)参与有丝分裂时核被膜的解体和重建。"},
    {"type": "short", "points": 8,
     "question": "端粒的主要生物学功能是什么？",
     "answer": -1,
     "explanation": "(1)保护染色体末端不被核酸酶降解；(2)防止染色体末端融合（端粒的存在使染色体末端不被识别为DNA断裂）；(3)参与染色体在细胞核内的空间定位；(4)与细胞衰老相关——端粒随细胞分裂逐渐缩短。"},
    {"type": "essay", "points": 12,
     "question": "描述DNA从双螺旋到染色体的包装过程。",
     "answer": -1,
     "explanation": "<strong>多级螺旋模型</strong>：(1)DNA双螺旋缠绕在组蛋白八聚体上形成核小体（11nm纤维），H1锁住DNA进出口；(2)核小体螺旋化形成30nm螺线管；(3)螺线管进一步螺旋化形成超螺线管；(4)超螺线管再螺旋化形成染色单体。整个过程将约2m的DNA包装成约10μm的染色体，压缩率约10000倍。"}
]

# ============================================================
# Chapter 9: 核糖体与蛋白质合成
# ============================================================

CH09_KNOWLEDGE = r"""
<h2>九、核糖体与蛋白质合成</h2>

<h3>9.1 核糖体的结构 <span class="tag-key">重点</span></h3>
<p><span class="kp">核糖体（Ribosome）</span><span class="exp">——蛋白质合成的场所，由rRNA和核糖体蛋白组成。</span></p>
<table>
  <tr><th></th><th>原核（70S）</th><th>真核（80S）</th></tr>
  <tr><td>大亚基</td><td>50S（23S+5S rRNA + 34蛋白）</td><td>60S（28S+5.8S+5S rRNA + ~49蛋白）</td></tr>
  <tr><td>小亚基</td><td>30S（16S rRNA + 21蛋白）</td><td>40S（18S rRNA + ~33蛋白）</td></tr>
</table>

<h3>9.2 核糖体的组装 <span class="tag-freq">高频</span></h3>
<p>rRNA在核仁中转录，与核糖体蛋白在核仁中组装成大小亚基，然后分别通过核孔进入细胞质。</p>

<h3>9.3 蛋白质合成过程 <span class="tag-must">必考</span></h3>

<h4>氨基酸的活化</h4>
<p>氨基酸 + tRNA + ATP --&gt; 氨酰-tRNA + AMP + PPi（氨酰-tRNA合成酶催化）</p>

<h4>翻译过程</h4>
<p><strong>起始</strong>：</p>
<ul>
  <li>小亚基与mRNA结合，识别起始密码子AUG</li>
  <li>起始tRNA（携带甲硫氨酸）与起始密码子配对</li>
  <li>大亚基结合，形成起始复合物</li>
</ul>
<p><strong>延伸</strong>（循环重复）：</p>
<ol>
  <li>氨酰-tRNA进入A位（进位）</li>
  <li>肽键形成（转肽）——P位肽链转移到A位氨基酸</li>
  <li>核糖体移位——向mRNA 3'端移动一个密码子</li>
</ol>
<p><strong>终止</strong>：</p>
<ul>
  <li>终止密码子（UAA、UAG、UGA）被释放因子识别</li>
  <li>肽链释放，核糖体大小亚基解离</li>
</ul>

<h3>9.4 多聚核糖体 <span class="tag-freq">高频</span></h3>
<p><span class="kp">多聚核糖体（Polyribosome/Polysome）</span><span class="exp">——一条mRNA上同时结合多个核糖体进行翻译，提高翻译效率。</span></p>

<h3>9.5 rRNA和核糖体蛋白的功能 <span class="tag-key">重点</span></h3>
<ul>
  <li><span class="kp">rRNA</span><span class="exp">——不仅是结构成分，还具有催化功能（核酶），催化肽键形成（肽基转移酶活性由23S/28S rRNA承担）</span></li>
  <li><span class="kp">核糖体蛋白</span><span class="exp">——维持核糖体结构，协助rRNA正确折叠，参与翻译调控</span></li>
</ul>
<blockquote>易错：核糖体的肽基转移酶活性来自rRNA（核酶），不是蛋白质。这是核酶概念的重要例证。</blockquote>
"""

CH09_TEST = [
    {"type": "choice", "points": 3,
     "question": "真核细胞核糖体的大亚基为：",
     "options": ["30S", "40S", "50S", "60S"],
     "answer": 3, "explanation": "真核核糖体为80S，由60S大亚基和40S小亚基组成。原核核糖体为70S，由50S大亚基和30S小亚基组成。"},
    {"type": "choice", "points": 3,
     "question": "核糖体中催化肽键形成的活性来自：",
     "options": ["核糖体蛋白", "rRNA", "mRNA", "tRNA"],
     "answer": 1, "explanation": "肽基转移酶活性由大亚基rRNA（原核23S/真核28S）承担，是核酶（ribozyme）。"},
    {"type": "tf", "points": 2,
     "question": "多聚核糖体是指多个核糖体串联在一条mRNA上同时进行翻译。",
     "options": [], "answer": 0,
     "explanation": "正确。多聚核糖体（polysome）是指一条mRNA上同时结合多个核糖体，同时进行多条肽链的合成，提高翻译效率。"},
    {"type": "short", "points": 8,
     "question": "简述蛋白质合成的延伸过程。",
     "answer": -1,
     "explanation": "(1)<strong>进位</strong>：氨酰-tRNA进入A位，由EF-Tu（原核）/eEF1（真核）协助；(2)<strong>转肽</strong>：P位肽链（或起始氨基酸）转移到A位氨基酸的氨基上，形成肽键，由rRNA催化；(3)<strong>移位</strong>：核糖体向mRNA 3'端移动一个密码子，A位空出，tRNA从P位移到E位后退出。循环重复。"},
    {"type": "short", "points": 8,
     "question": "简述rRNA在核糖体中的功能。",
     "answer": -1,
     "explanation": "(1)结构功能：构成核糖体的骨架，维持核糖体三维结构；(2)催化功能：大亚基rRNA具有肽基转移酶活性，催化肽键形成（核酶）；(3)识别功能：小亚基16S/18S rRNA与mRNA的SD序列/5'帽子相互作用，参与翻译起始；(4)保证翻译精确性。"}
]

# ============================================================
# Chapter 10: 细胞信号转导
# ============================================================

CH10_KNOWLEDGE = r"""
<h2>十、细胞信号转导</h2>

<h3>10.1 细胞通讯方式 <span class="tag-key">重点</span></h3>
<table>
  <tr><th>方式</th><th>特点</th><th>举例</th></tr>
  <tr><td><span class="kp">内分泌</span></td><td>激素经血液远距离运输</td><td>胰岛素</td></tr>
  <tr><td><span class="kp">旁分泌</span></td><td>信号分子作用于邻近细胞</td><td>神经递质、生长因子</td></tr>
  <tr><td><span class="kp">自分泌</span></td><td>信号分子作用于自身</td><td>某些生长因子</td></tr>
  <tr><td><span class="kp">突触传递</span></td><td>神经元之间通过突触</td><td>神经递质</td></tr>
  <tr><td><span class="kp">接触依赖</span></td><td>膜结合信号分子</td><td>Delta-Notch</td></tr>
</table>

<h3>10.2 信号分子与受体 <span class="tag-key">重点</span></h3>
<p><span class="kp">信号分子（配体）</span><span class="exp">——传递信息的化学物质，可以是蛋白质、肽、氨基酸、核苷酸、脂质、气体（NO）等。</span></p>
<p><strong>受体类型</strong>：</p>
<ul>
  <li><span class="kp">胞内受体</span><span class="exp">——位于胞质或核内，配体为脂溶性小分子（如类固醇激素）</span></li>
  <li><span class="kp">细胞表面受体</span><span class="exp">——位于质膜上，配体为水溶性信号分子</span></li>
</ul>

<h3>10.3 细胞表面受体的主要类型 <span class="tag-must">必考</span></h3>
<table>
  <tr><th>类型</th><th>特点</th><th>举例</th></tr>
  <tr><td><span class="kp">离子通道偶联受体</span></td><td>配体门控离子通道</td><td>乙酰胆碱受体</td></tr>
  <tr><td><span class="kp">G蛋白偶联受体（GPCR）</span></td><td>7次跨膜，激活G蛋白</td><td>肾上腺素受体</td></tr>
  <tr><td><span class="kp">酶联受体</span></td><td>自身有酶活性或结合酶</td><td>受体酪氨酸激酶（RTK）</td></tr>
</table>

<h3>10.4 G蛋白偶联受体信号通路 <span class="tag-must">必考</span></h3>
<p><strong>基本过程</strong>：</p>
<ol>
  <li>配体与GPCR结合</li>
  <li>GPCR激活G蛋白（G蛋白$\alpha$亚基上的GDP被GTP替换）</li>
  <li>G蛋白$\alpha$亚基（和$\beta\gamma$二聚体）激活下游效应器</li>
  <li>效应器产生第二信使</li>
  <li>$\alpha$亚基GTP酶活性水解GTP，信号终止</li>
</ol>

<h4>cAMP-PKA通路</h4>
<p>激素 --&gt; GPCR --&gt; Gs蛋白 --&gt; 腺苷酸环化酶（AC）--&gt; cAMP升高 --&gt; PKA活化 --&gt; 磷酸化靶蛋白</p>

<h4>磷脂酰肌醇通路</h4>
<p>信号 --&gt; GPCR --&gt; Gq蛋白 --&gt; 磷脂酶C（PLC）--&gt; PIP₂分解为IP₃和DAG --&gt; IP₃促进Ca²⁺释放，DAG激活PKC</p>

<h3>10.5 第二信使 <span class="tag-must">必考</span></h3>
<table>
  <tr><th>第二信使</th><th>来源</th><th>作用</th></tr>
  <tr><td>cAMP</td><td>ATP经AC催化</td><td>激活PKA</td></tr>
  <tr><td>IP₃</td><td>PIP₂水解</td><td>促进内质网释放Ca²⁺</td></tr>
  <tr><td>DAG</td><td>PIP₂水解</td><td>激活PKC</td></tr>
  <tr><td>Ca²⁺</td><td>ER释放或胞外流入</td><td>激活多种钙结合蛋白</td></tr>
  <tr><td>cGMP</td><td>GTP经GC催化</td><td>激活PKG等</td></tr>
</table>

<h3>10.6 酶联受体信号通路 <span class="tag-key">重点</span></h3>
<p><span class="kp">受体酪氨酸激酶（RTK）-Ras-MAPK通路</span>：</p>
<ol>
  <li>配体结合 --&gt; RTK二聚化 --&gt; 自身磷酸化</li>
  <li>Grb2-SOS复合物结合磷酸化RTK</li>
  <li>SOS激活Ras（GDP --&gt; GTP）</li>
  <li>Ras-GTP激活MAPK级联反应（Raf --&gt; MEK --&gt; ERK）</li>
  <li>ERK进入细胞核，磷酸化转录因子，调控基因表达</li>
</ol>
<blockquote>易错：Ras蛋白是分子开关蛋白，Ras-GTP为活性状态，Ras-GDP为非活性状态。Ras突变（持续激活）是多种癌症的重要原因。</blockquote>
"""

CH10_TEST = [
    {"type": "choice", "points": 3,
     "question": "下列哪种不属于第二信使？",
     "options": ["cAMP", "IP₃", "胰岛素", "Ca²⁺"],
     "answer": 2, "explanation": "胰岛素是第一信使（激素），不是第二信使。cAMP、IP₃、Ca²⁺都是第二信使。"},
    {"type": "choice", "points": 3,
     "question": "GPCR信号通路中，G蛋白的活性形式是：",
     "options": ["G蛋白-GDP", "G蛋白-GTP", "G蛋白-ATP", "G蛋白-ADP"],
     "answer": 1, "explanation": "G蛋白α亚基结合GTP时为活性状态，结合GDP时为非活性状态。G蛋白本身具有GTP酶活性，可水解GTP为GDP而失活。"},
    {"type": "multi", "points": 4,
     "question": "下列哪些属于细胞表面受体类型？",
     "options": ["离子通道偶联受体", "G蛋白偶联受体", "胞内受体", "酶联受体"],
     "answer": [0, 1, 3], "explanation": "胞内受体位于细胞质或细胞核内，不属于细胞表面受体。其他三种都位于质膜上。"},
    {"type": "tf", "points": 2,
     "question": "Ras蛋白是分子开关蛋白，Ras-GTP为活性状态，可激活下游MAPK级联反应。",
     "options": [], "answer": 0,
     "explanation": "正确。Ras-GTP是活性形式，激活Raf-MEK-ERK级联反应。Ras-GDP为非活性状态。"},
    {"type": "short", "points": 8,
     "question": "简述第二信使分子在信号传递过程中的重要作用，并举例两个。",
     "answer": -1,
     "explanation": "<strong>作用</strong>：(1)放大信号——一个信号分子可产生大量第二信使；(2)扩散——在胞质中快速扩散传播信号；(3)多样性——不同第二信使激活不同效应器。<br><strong>举例</strong>：(1)<strong>cAMP</strong>——由AC催化ATP产生，激活PKA，磷酸化多种靶蛋白，调节代谢和基因表达；(2)<strong>IP₃</strong>——促进内质网释放Ca²⁺，Ca²⁺激活钙调蛋白等，参与多种细胞反应。"},
    {"type": "essay", "points": 12,
     "question": "比较G蛋白偶联受体和受体酪氨酸激酶介导的信号转导通路。",
     "answer": -1,
     "explanation": "<strong>GPCR通路</strong>：(1)受体为7次跨膜蛋白；(2)激活三聚体G蛋白；(3)产生第二信使（cAMP、IP₃、DAG等）；(4)信号放大效应强。<br><strong>RTK通路</strong>：(1)配体结合导致二聚化和自身磷酸化；(2)通过接头蛋白激活Ras；(3)启动MAPK级联反应；(4)最终调控基因表达。<br><strong>共同点</strong>：都通过蛋白磷酸化级联传递信号，都有信号放大效应。"}
]

# ============================================================
# Generate all files
# ============================================================

chapters = [
    ("06-线粒体与叶绿体", "第六章 线粒体与叶绿体", CH06_KNOWLEDGE, CH06_TEST),
    ("07-细胞骨架", "第七章 细胞骨架", CH07_KNOWLEDGE, CH07_TEST),
    ("08-细胞核与染色体", "第八章 细胞核与染色体", CH08_KNOWLEDGE, CH08_TEST),
    ("09-核糖体与蛋白质合成", "第九章 核糖体与蛋白质合成", CH09_KNOWLEDGE, CH09_TEST),
    ("10-细胞信号转导", "第十章 细胞信号转导", CH10_KNOWLEDGE, CH10_TEST),
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

print("\nDone! Chapters 6-10 generated.")