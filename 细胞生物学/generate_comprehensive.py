#!/usr/bin/env python3
"""Generate comprehensive mock exam for 细胞生物学."""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'ExamPass-Assistant', 'scripts'))
from template_engine import save_knowledge_html, save_test

BASE = '/workspace/细胞生物学/16-综合模拟'
os.makedirs(BASE, exist_ok=True)

# ============================================================
# Comprehensive Mock Exam (仿新疆大学真题格式)
# ============================================================

# Part 1: 名词解释 (10题, 每题4分, 共40分)
# Part 2: 简答题 (8题, 每题到10分, 共60分)
# Part 3: 论述题 (2题, 每题15分, 共30分) -- converted to short/essay for automatic grading

COMPREHENSIVE_TEST = [
    # ===== 名词解释 (40分) =====
    {"type": "short", "points": 4,
     "question": "名词解释：细胞学说",
     "answer": -1,
     "explanation": "细胞学说由施莱登和施旺提出，核心内容：(1)一切生物体都由细胞构成；(2)细胞是生命活动的基本单位；(3)细胞来自细胞（Virchow补充）。"},
    {"type": "short", "points": 4,
     "question": "名词解释：信号识别颗粒（SRP）",
     "answer": -1,
     "explanation": "SRP是识别分泌蛋白N端信号肽的核糖核蛋白复合体，引导核糖体-mRNA-新生肽链复合体结合到ER膜上的SRP受体，实现共翻译转运。"},
    {"type": "short", "points": 4,
     "question": "名词解释：化学渗透假说",
     "answer": -1,
     "explanation": "由Mitchell于1961年提出：电子传递链将H⁺从线粒体基质泵到膜间隙，形成跨内膜的质子电化学梯度，H⁺通过ATP合酶回流时驱动ATP合成。"},
    {"type": "short", "points": 4,
     "question": "名词解释：微管组织中心（MTOC）",
     "answer": -1,
     "explanation": "微管装配的起始位点。动物细胞中中心体是主要的MTOC，含一对中心粒和周围物质（γ-微管蛋白环），微管负端锚定于此，正端向外延伸。"},
    {"type": "short", "points": 4,
     "question": "名词解释：核定位信号（NLS）",
     "answer": -1,
     "explanation": "蛋白质中引导其进入细胞核的氨基酸序列，富含碱性氨基酸（赖氨酸、精氨酸）。被核输入受体（importin）识别，通过核孔复合体主动运输进入细胞核。"},
    {"type": "short", "points": 4,
     "question": "名词解释：G₀期细胞",
     "answer": -1,
     "explanation": "退出细胞周期、暂时不增殖的细胞。G₀期细胞仍保持分裂潜能，在适当刺激下可重新进入G₁期继续细胞周期。与终末分化细胞不同。"},
    {"type": "short", "points": 4,
     "question": "名词解释：细胞凋亡（Apoptosis）",
     "answer": -1,
     "explanation": "由基因调控的程序性细胞死亡，是主动有序的自我消亡过程。特征：细胞皱缩、染色质凝集、DNA有规律断裂、形成凋亡小体、不引起炎症。由Caspase家族介导。"},
    {"type": "short", "points": 4,
     "question": "名词解释：管家基因（Housekeeping Gene）",
     "answer": -1,
     "explanation": "在所有细胞类型中都表达的基因，维持细胞基本生命活动。如组蛋白基因、核糖体蛋白基因、微管蛋白基因等。与组织特异性基因（奢侈基因）相对。"},
    {"type": "short", "points": 4,
     "question": "名词解释：Hayflick界限",
     "answer": -1,
     "explanation": "正常人体细胞在体外培养时分裂次数有限（约50-60代），之后细胞停止分裂进入衰老状态。由Hayflick于1961年发现，是细胞衰老的经典实验证据，与端粒缩短有关。"},
    {"type": "short", "points": 4,
     "question": "名词解释：整联蛋白（Integrin）",
     "answer": -1,
     "explanation": "细胞表面跨膜受体蛋白，由α和β亚基组成异二聚体。主要介导细胞与细胞外基质的黏着（如黏着斑、半桥粒），也参与细胞信号转导。与钙黏蛋白不同，整联蛋白介导异嗜性黏着。"},

    # ===== 简答题 (60分) =====
    {"type": "short", "points": 8,
     "question": "简答：比较组成型胞吐和调节型胞吐的特点及生物学意义。",
     "answer": -1,
     "explanation": "<strong>组成型胞吐</strong>：持续进行，不需要信号刺激，所有真核细胞都有。运输细胞外基质成分和质膜蛋白，维持细胞基本功能。<br><strong>调节型胞吐</strong>：需要特定信号触发（如Ca²⁺内流），存在于分泌细胞（如神经细胞、内分泌细胞）。分泌激素、神经递质等，实现快速响应。<br><strong>意义</strong>：组成型维持基本功能，调节型实现精确调控和快速响应。"},
    {"type": "short", "points": 8,
     "question": "简答：简述溶酶体的发生过程和基本功能。",
     "answer": -1,
     "explanation": "<strong>发生过程</strong>：溶酶体酶在rER合成--&gt;高尔基体加工（M6P标记）--&gt;从trans面出芽形成初级溶酶体--&gt;与内体/底物融合形成次级溶酶体--&gt;消化完成后形成残余体。<br><strong>基本功能</strong>：(1)异噬作用——消化外来物质（细菌、异物）；(2)自噬作用——消化自身衰老细胞器；(3)自溶作用——细胞死亡时溶酶体膜破裂，细胞自溶。"},
    {"type": "short", "points": 8,
     "question": "简答：线粒体和叶绿体的结构和功能，并说明它们在细胞生命活动中的作用。",
     "answer": -1,
     "explanation": "<strong>线粒体</strong>：双层膜，内膜折叠成嵴，含呼吸链酶复合体和ATP合酶。功能：氧化磷酸化产生ATP，是细胞能量代谢中心。三羧酸循环在基质中进行。<br><strong>叶绿体</strong>：双层膜+类囊体系统，含光合色素。功能：光反应（类囊体膜）产生ATP和NADPH，暗反应（基质）固定CO₂。<br><strong>作用</strong>：线粒体提供细胞活动所需能量；叶绿体将光能转化为化学能，是地球上几乎所有生命活动的能量来源。"},
    {"type": "short", "points": 8,
     "question": "简答：真核细胞内物质运输的马达蛋白有哪些？描述其功能。",
     "answer": -1,
     "explanation": "(1)<strong>肌球蛋白（Myosin）</strong>：在微丝上运动，向+端。参与肌肉收缩（与肌动蛋白相互作用）、短距离胞内运输和细胞运动。<br>(2)<strong>驱动蛋白（Kinesin）</strong>：在微管上运动，向+端（顺向运输）。负责从细胞中心向外周运输囊泡和细胞器。<br>(3)<strong>动力蛋白（Dynein）</strong>：在微管上运动，向-端（逆向运输）。负责从细胞外周向中心运输，也参与纤毛和鞭毛的运动。"},
    {"type": "short", "points": 8,
     "question": "简答：简述端粒的主要生物学功能。",
     "answer": -1,
     "explanation": "(1)保护染色体末端不被核酸酶降解；(2)防止染色体末端融合——端粒使染色体末端不被识别为DNA双链断裂；(3)参与染色体在细胞核内的空间定位；(4)与细胞衰老密切相关——端粒随每次细胞分裂逐渐缩短，缩短到临界长度时触发细胞衰老；(5)端粒酶在生殖细胞和癌细胞中维持端粒长度。"},
    {"type": "short", "points": 8,
     "question": "简答：细胞周期存在哪些检验点？说明细胞周期的调控机制。",
     "answer": -1,
     "explanation": "<strong>检验点</strong>：(1)G₁/S检验点（限制点）——检查DNA损伤、营养条件、生长因子；(2)G₂/M检验点——检查DNA复制是否完成、是否有损伤；(3)M期纺锤体检验点——检查染色体是否正常连接到纺锤体。<br><strong>调控机制</strong>：(1)Cyclin周期性合成与降解，结合并激活CDK；(2)CDK磷酸化多种底物驱动周期进程；(3)CDK抑制剂（如p21）在DNA损伤时抑制CDK活性；(4)p53感应DNA损伤，诱导p21表达，阻滞细胞周期；(5)Rb蛋白调控G₁/S转换。"},
    {"type": "short", "points": 8,
     "question": "简答：癌症的发生与原癌基因和抑癌基因的关系。",
     "answer": -1,
     "explanation": "<strong>原癌基因</strong>：正常功能是促进细胞增殖。突变后（点突变、扩增、染色体易位）成为癌基因，功能获得（gain-of-function），一个等位基因突变即可。如Ras突变导致持续激活的信号通路。<br><strong>抑癌基因</strong>：正常功能是抑制增殖或促进凋亡。突变导致功能丧失（loss-of-function），需两个等位基因都失活（Knudson二次打击假说）。如p53缺失使DNA损伤细胞继续增殖。<br><strong>关系</strong>：癌症是多步骤过程，需要多个癌基因激活和抑癌基因失活的共同作用。"},
    {"type": "short", "points": 8,
     "question": "简答：细胞凋亡的概念、形态特征及其与细胞坏死的区别。",
     "answer": -1,
     "explanation": "<strong>概念</strong>：细胞凋亡是由基因调控的程序性细胞死亡，是主动有序的自我消亡过程。<br><strong>形态特征</strong>：细胞皱缩、染色质凝集、细胞膜保持完整、形成凋亡小体、DNA有规律断裂（梯状条带）。<br><strong>与坏死区别</strong>：(1)凋亡是主动的生理性过程，坏死是被动的病理性过程；(2)凋亡细胞膜保持完整，坏死细胞膜破裂；(3)凋亡DNA有规律断裂，坏死DNA随机降解；(4)凋亡不引起炎症反应，坏死引起炎症反应；(5)凋亡涉及Caspase级联反应，坏死无特异性酶参与。"},

    # ===== 论述题 (30分) =====
    {"type": "essay", "points": 15,
     "question": "论述：生物大分子物质的跨膜运输有哪些方式？有什么特点？在细胞生命活动中有何作用？",
     "answer": -1,
     "explanation": "<strong>胞吞作用</strong>：(1)吞噬作用——吞噬大颗粒物质（如细菌），形成吞噬体，与溶酶体融合降解；(2)胞饮作用——吞噬液体和溶质，形成胞饮泡；(3)受体介导的胞吞——配体与受体结合后内化，高效特异（如LDL的内吞）。<br><strong>胞吐作用</strong>：(1)组成型胞吐——持续进行，分泌ECM成分和质膜蛋白；(2)调节型胞吐——信号触发，分泌激素、神经递质。<br><strong>特点</strong>：都需要能量（ATP），涉及膜的融合和分离，可运输大分子甚至颗粒，具有方向性。<br><strong>作用</strong>：(1)营养摄取；(2)免疫防御；(3)细胞信号转导；(4)膜更新和修复；(5)神经递质释放。"},
    {"type": "essay", "points": 15,
     "question": "论述：第二信使分子在信号传递过程中有哪些重要作用？举例两个并解释说明。",
     "answer": -1,
     "explanation": "<strong>第二信使的作用</strong>：(1)信号放大——一个信号分子可激活多个效应器，产生大量第二信使；(2)信号扩散——第二信使在胞质中快速扩散，将信号传播到整个细胞；(3)多样性——不同第二信使激活不同下游效应器，实现信号的特异性和多样性；(4)信号整合——多种信号通路通过第二信使交汇整合。<br><strong>cAMP</strong>：由腺苷酸环化酶（AC）催化ATP产生。肾上腺素与GPCR结合--&gt;激活Gs蛋白--&gt;激活AC--&gt;cAMP升高--&gt;激活PKA--&gt;PKA磷酸化多种靶蛋白，调节糖原分解、脂肪分解等代谢反应。<br><strong>IP₃/DAG</strong>：由PLC催化PIP₂水解产生。IP₃扩散到内质网，促进Ca²⁺释放；DAG留在质膜上，激活PKC。Ca²⁺和PKC共同调控多种细胞反应，如分泌、收缩、基因表达。"}
]

# ============================================================
# Generate comprehensive exam
# ============================================================

test_path = os.path.join(BASE, "综合模拟考试.html")
save_test(COMPREHENSIVE_TEST, test_path, "细胞生物学综合模拟考试", "仿新疆大学真题格式 | 满分130分", duration_minutes=180)
print(f"Generated: {test_path}")

# Also create a knowledge summary for the comprehensive review
COMPREHENSIVE_KNOWLEDGE = r"""
<h2>细胞生物学 综合复习总纲</h2>

<h3>考试信息 <span class="tag-must">必考</span></h3>
<p><strong>新疆大学 817细胞生物学 考试题型</strong>：</p>
<ul>
  <li><span class="kp">名词解释</span><span class="exp">——10题，每题3-4分，共30-40分</span></li>
  <li><span class="kp">简答题</span><span class="exp">——6-8题，每题6-10分，共40-60分</span></li>
  <li><span class="kp">论述题</span><span class="exp">——2-3题，每题12-15分，共30-40分</span></li>
</ul>

<h3>高频考点总览</h3>
<table>
  <tr><th>章节</th><th>核心考点</th><th>考频</th></tr>
  <tr><td>绪论</td><td>细胞学说、研究层次</td><td>★★★</td></tr>
  <tr><td>细胞统一性与多样性</td><td>原核vs真核、病毒特征、模式生物</td><td>★★★</td></tr>
  <tr><td>研究方法</td><td>电镜对比、差速离心vs密度梯度离心</td><td>★★★</td></tr>
  <tr><td>细胞质膜</td><td>流动镶嵌模型、物质运输方式、血影</td><td>★★★★★</td></tr>
  <tr><td>内膜系统</td><td>信号假说、溶酶体发生、蛋白质分选</td><td>★★★★★</td></tr>
  <tr><td>线粒体与叶绿体</td><td>氧化磷酸化、内共生学说、半自主性</td><td>★★★★★</td></tr>
  <tr><td>细胞骨架</td><td>三类骨架对比、分子马达、肌肉收缩</td><td>★★★★</td></tr>
  <tr><td>细胞核与染色体</td><td>核小体、核纤层、NLS、端粒</td><td>★★★★★</td></tr>
  <tr><td>核糖体</td><td>核酶、多聚核糖体、翻译过程</td><td>★★★</td></tr>
  <tr><td>细胞信号转导</td><td>GPCR通路、第二信使、RTK-Ras-MAPK</td><td>★★★★★</td></tr>
  <tr><td>细胞周期与分裂</td><td>有丝分裂vs减数分裂、时相事件</td><td>★★★★★</td></tr>
  <tr><td>周期调控与癌症</td><td>MPF、检验点、癌基因vs抑癌基因</td><td>★★★★★</td></tr>
  <tr><td>细胞分化与干细胞</td><td>全能性、管家基因、干细胞分类</td><td>★★★★</td></tr>
  <tr><td>细胞衰老与凋亡</td><td>Hayflick界限、凋亡vs坏死、Caspase</td><td>★★★★★</td></tr>
  <tr><td>细胞连接</td><td>三类连接、整联蛋白、胶原</td><td>★★★</td></tr>
</table>

<h3>复习策略</h3>
<ol>
  <li><strong>名词解释</strong>：每天背诵10个高频名词，确保能写出定义+核心特征+举例</li>
  <li><strong>简答题</strong>：重点掌握「对比类」题目（如原核vs真核、凋亡vs坏死、有丝vs减数）</li>
  <li><strong>论述题</strong>：重点掌握跨章节综合题（如物质运输、信号转导、周期调控）</li>
  <li><strong>真题导向</strong>：2009-2025年真题反复出现的考点就是重中之重</li>
</ol>
<blockquote>新疆大学真题特点：名词解释占分高（30-40分），且经常重复出题。建议把历年真题中所有名词解释都背熟。</blockquote>
"""

knowledge_path = os.path.join(BASE, "综合复习总纲.html")
save_knowledge_html(COMPREHENSIVE_KNOWLEDGE, knowledge_path, "细胞生物学 综合复习总纲")
print(f"Generated: {knowledge_path}")

print("\nDone! Comprehensive exam generated.")