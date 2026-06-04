#!/usr/bin/env python3
"""Merge the two knowledge HTML files and generate interactive test."""

import sys, re
sys.path.insert(0, '/workspace/ExamPass-Assistant')
from scripts.template_engine import save_knowledge_html, save_test

# Read both generated HTML files and extract body content
def extract_body(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    # Extract body between <body> and first <script> or </body>
    m = re.search(r'<body[^>]*>(.*?)<script', html, re.DOTALL)
    if not m:
        m = re.search(r'<body[^>]*>(.*?)</body>', html, re.DOTALL)
    if m:
        body = m.group(1)
        # Remove the H1 and TOC (already auto-generated, will be regenerated)
        # Remove existing H1
        body = re.sub(r'<h1[^>]*>.*?</h1>', '', body, flags=re.DOTALL)
        # Remove existing TOC div
        body = re.sub(r'<div class="toc">.*?</div>', '', body, flags=re.DOTALL)
        return body.strip()
    return ''

body1 = extract_body('/workspace/output/生物化学_第一篇_结构生物化学_知识精讲.html')
body2 = extract_body('/workspace/output/生物化学_第一篇_结构生物化学_Ch10-18.html')

combined = body1 + '\n\n' + body2

# Save combined knowledge page
save_knowledge_html(combined, '/workspace/output/生物化学_第一篇_知识精讲_完整版.html', '第一篇 结构生物化学（第1-18章）知识精讲')
print('Merged knowledge guide saved.')

# ─── Generate interactive test for Part 1 ───

questions = [
    # Chapter 2 - Amino Acids
    {
        "type": "choice", "points": 2,
        "question": "下列哪种氨基酸没有手性碳？",
        "options": ["丙氨酸", "甘氨酸", "脯氨酸", "丝氨酸"],
        "answer": 1,
        "explanation": "甘氨酸(Gly)的R基为H，Cα上连接了两个相同的H原子，因此没有手性碳。其他19种标准氨基酸的Cα均为手性碳（L构型）。",
        "pitfall": "不要把脯氨酸误认为没有手性——脯氨酸有手性碳，只是它是亚氨基酸而非α-氨基酸。"
    },
    {
        "type": "choice", "points": 2,
        "question": "下列哪种氨基酸在生理pH下侧链带正电荷？",
        "options": ["天冬氨酸(Asp)", "谷氨酸(Glu)", "赖氨酸(Lys)", "天冬酰胺(Asn)"],
        "answer": 2,
        "explanation": "赖氨酸(Lys)侧链ε-氨基的pKa≈10.5，在pH 7时质子化(-NH₃⁺)带正电。Asp和Glu为酸性氨基酸带负电，Asn为极性不带电。",
        "pitfall": "注意区分Asn/Asp和Gln/Glu——酰胺形式(Asn/Gln)属于极性不带电类，酸性形式(Asp/Glu)带负电。"
    },
    {
        "type": "choice", "points": 2,
        "question": "组氨酸(His)在酶催化中特别重要，主要原因是其侧链咪唑基的pKa约为？",
        "options": ["3.5", "6.0", "8.0", "10.5"],
        "answer": 1,
        "explanation": "His咪唑基pKa≈6.0，在生理pH附近既能提供质子又能接受质子，使其成为酶催化中最重要的一般酸碱催化剂。",
        "pitfall": "不要混淆His的pKa(~6.0)与Lys(~10.5)或Asp(~3.9)。"
    },
    {
        "type": "multi", "points": 3,
        "question": "下列哪些氨基酸属于疏水（非极性）氨基酸？（多选）",
        "options": ["缬氨酸(Val)", "丝氨酸(Ser)", "苯丙氨酸(Phe)", "谷氨酰胺(Gln)"],
        "answer": [0, 2],
        "explanation": "Val的侧链为异丙基（纯烷基链），Phe的侧链为苄基（芳环），都高度疏水。Ser有-OH，Gln有酰胺基，均属于极性不带电类。",
        "pitfall": "注意区分Phe(Phenylalanine, 疏水)和Tyr(Tyrosine, 极性不带电但偏疏水)——Tyr的-OH使其有一定极性但常常出现在蛋白质疏水-亲水界面。"
    },
    {
        "type": "tf", "points": 1,
        "question": "脯氨酸是α-氨基酸。",
        "answer": 1,
        "explanation": "错误。脯氨酸是亚氨基酸(imino acid)，其α-氨基是亚氨基(-NH-)，而非自由氨基(-NH₂)。",
        "pitfall": "脯氨酸是唯一一个氨基为亚氨基的标准氨基酸，这一特性使其成为α螺旋的「破坏者」。"
    },
    {
        "type": "fill", "points": 2,
        "question": "氨基酸等电点(pI)的定义是：氨基酸____为零时的pH值。在等电点时，氨基酸的溶解度最____。",
        "answer": [["净电荷"], ["低", "小"]],
        "explanation": "pI时氨基酸净电荷为零，分子间静电排斥力消失，容易聚集沉淀，溶解度最低。中性氨基酸pI = (pK₁ + pK₂)/2。",
        "pitfall": "等电点时不代表氨基酸不带电，而是正负电荷恰好抵消，净电荷为零。"
    },

    # Chapter 3 - Protein Structure
    {
        "type": "choice", "points": 2,
        "question": "α螺旋中，氢键的配对模式是？",
        "options": ["第i个残基C=O与第i+2个残基N-H", "第i个残基C=O与第i+3个残基N-H", "第i个残基C=O与第i+4个残基N-H", "第i个残基C=O与第i+5个残基N-H"],
        "answer": 2,
        "explanation": "α螺旋中，第i个残基的C=O与第i+4个残基的N-H形成氢键（i→i+4），方向几乎平行于螺旋轴。每圈3.6个残基，螺距0.54nm。",
        "pitfall": "不要混淆：α螺旋是i→i+4，β转角是i→i+3，β折叠是链间氢键。"
    },
    {
        "type": "choice", "points": 2,
        "question": "肽键具有部分双键性质的原因是什么？",
        "options": ["C=O双键的吸电子效应", "酰胺N的孤对电子与C=O共轭（共振）", "Cα的构象限制", "氢键的稳定作用"],
        "answer": 1,
        "explanation": "酰胺N上的孤对电子与羰基C=O的π键共轭，产生共振结构(O⁻-C=N⁺)，使C-N键具有约40%的双键特征，不能自由旋转，六个原子处于同一平面（肽平面）。",
        "pitfall": "肽键的部分双键性质使C-N键不能旋转，但Cα-N(φ)和Cα-C(ψ)是单键，可以旋转——Ramachandran图就是绘制这两个角度的。"
    },
    {
        "type": "choice", "points": 2,
        "question": "Anfinsen实验使用RNase A证明了什么？",
        "options": ["蛋白质折叠需要分子伴侣", "蛋白质折叠完全由二级结构决定", "一级结构包含决定三维结构所需的全部信息", "二硫键是蛋白质折叠的唯一驱动力"],
        "answer": 2,
        "explanation": "Anfinsen将RNase A完全变性展开后，去除变性剂，RNase A自发恢复全部酶活性。这证明了一级结构（氨基酸序列）包含了决定三维结构所需的全部信息。",
        "pitfall": "这个实验并不意味着所有蛋白质在体内都能自发折叠——许多蛋白质需要分子伴侣辅助。Anfinsen实验证明的是热力学可行性（信息存在于序列中），而非动力学可行性。"
    },
    {
        "type": "tf", "points": 1,
        "question": "二硫键是稳定蛋白质二级结构（α螺旋、β折叠）的主要作用力。",
        "answer": 1,
        "explanation": "错误。二级结构（α螺旋、β折叠）的稳定力是主链间的氢键。二硫键是稳定三级结构的共价键，参与维持蛋白质的整体三维折叠。",
        "pitfall": "二硫键在两个Cys残基的侧链-SH之间形成，属于三级结构稳定力，不是二级结构稳定力。"
    },
    {
        "type": "fill", "points": 2,
        "question": "蛋白质折叠中，____效应是主要的热力学驱动力。Levinthal悖论指出蛋白质不可能通过____搜索所有可能构象来折叠。",
        "answer": [["疏水"], ["随机"]],
        "explanation": "疏水效应释放有序水分子，增加系统的熵，是折叠的主要驱动力。Levinthal悖论：100残基蛋白有~10⁴⁷种构象，即使飞秒级搜索也要远超宇宙年龄，因此折叠必然是沿特定路径进行的。",
        "pitfall": "Levinthal悖论不是否定蛋白质能折叠，而是证明折叠不是随机搜索过程——折叠沿能量漏斗(funnel)进行。"
    },

    # Chapter 4 - Protein Function
    {
        "type": "choice", "points": 2,
        "question": "血红蛋白(Hb)的氧合曲线呈S形，而肌红蛋白(Mb)的曲线呈双曲线。S形反映了什么？",
        "options": ["Hb对O₂的亲和力比Mb高", "Hb的亚基间存在正协同效应", "Hb含有更多血红素", "Hb受2,3-BPG激活"],
        "answer": 1,
        "explanation": "Hb是四聚体(α₂β₂)，亚基间存在正协同效应——结合第一个O₂最困难，结合第四个O₂最容易。这种协同效应使Hb的氧合曲线呈S形(sigmoidal)，有利于在肺部高效结合O₂和在组织中高效释放O₂。",
        "pitfall": "Mb是单亚基，无协同效应，曲线为双曲线。S形曲线是协同效应的标志，但不是动力学上的优势——Mb在每个pO₂下的亲和力实际上都高于Hb的T态。"
    },
    {
        "type": "choice", "points": 2,
        "question": "2,3-BPG对血红蛋白的作用是？",
        "options": ["提高Hb对O₂的亲和力", "降低Hb对O₂的亲和力，促进O₂释放", "激活Hb的催化活性", "与血红素的Fe²⁺直接结合"],
        "answer": 1,
        "explanation": "2,3-BPG结合在Hb四聚体中央空腔（带正电的Lys、His残基之间），稳定T态构象，降低Hb对O₂的亲和力，促进O₂在组织中释放。高原适应时红细胞内2,3-BPG升高。",
        "pitfall": "2,3-BPG只影响Hb不影响Mb（Mb是单亚基，无中央空腔）。胎儿Hb(α₂γ₂)对2,3-BPG亲和力低（γ链His143→Ser），因此对O₂亲和力更高，有利于从母体血中摄取O₂。"
    },
    {
        "type": "choice", "points": 2,
        "question": "Bohr效应描述的是？",
        "options": ["O₂浓度升高促进Hb释放H⁺", "H⁺和CO₂降低Hb对O₂的亲和力", "温度升高提高Hb对O₂的亲和力", "2,3-BPG浓度升高提高Hb对O₂的亲和力"],
        "answer": 1,
        "explanation": "Bohr效应：H⁺和CO₂降低Hb对O₂的亲和力。在活跃代谢的组织中，CO₂↑→H₂CO₃→H⁺+HCO₃⁻，pH↓，H⁺与Hb结合稳定T态，促进O₂释放——恰好是组织需要O₂之时。",
        "pitfall": "Bohr效应是「低pH降低O₂亲和力」，不要记反。这是生理精妙设计：代谢活跃组织产酸→pH↓→O₂释放增加→组织获得更多O₂。"
    },
    {
        "type": "tf", "points": 1,
        "question": "肌球蛋白头部具有ATP酶活性，ATP水解驱动肌肉收缩的力产生(power stroke)。",
        "answer": 0,
        "explanation": "正确。肌球蛋白头部是ATP酶，ATP+H₂O→ADP+Pi，释放的能量通过构象变化转化为机械功（power stroke），使肌动蛋白丝滑动约10nm。",
        "pitfall": "注意：ATP结合使肌球蛋白脱离肌动蛋白，ATP水解使头部「扳起」(cocking)，Pi释放触发了力产生步骤，ADP释放完成循环。"
    },

    # Chapter 7 - Nucleic Acid Structure
    {
        "type": "choice", "points": 2,
        "question": "B-DNA双螺旋中，每圈含有多少个碱基对？",
        "options": ["8", "10", "12", "14"],
        "answer": 1,
        "explanation": "B-DNA（生理条件下的标准构象）每圈含10个碱基对，螺距3.4nm，碱基对间距0.34nm。右手双螺旋，直径约2nm。",
        "pitfall": "A-DNA每圈11bp，Z-DNA每圈12bp。B-DNA是生理条件下最常见的构象，但DNA在溶液中实际为10.5bp/圈（非恰好10）。"
    },
    {
        "type": "choice", "points": 2,
        "question": "DNA双螺旋中，G-C碱基对之间形成几个氢键？",
        "options": ["1个", "2个", "3个", "4个"],
        "answer": 2,
        "explanation": "G-C碱基对之间形成3个氢键（G的O⁶与C的N⁴、G的N¹与C的N³、G的N²与C的O²），A-T碱基对之间只有2个氢键。因此G-C含量越高，DNA越稳定，Tm越高。",
        "pitfall": "G-C除了3个氢键外，还有更好的碱基堆积相互作用，两者共同贡献了G-C含量高的DNA的更高稳定性。"
    },
    {
        "type": "tf", "points": 1,
        "question": "DNA变性时，磷酸二酯键断裂，导致两条链分开。",
        "answer": 1,
        "explanation": "错误。DNA变性只断裂碱基对之间的氢键和碱基堆积力，磷酸二酯键（共价键）保持完整。变性是物理变化（去折叠），不是化学变化（键断裂）。",
        "pitfall": "DNA变性是氢键的断裂（可逆的复性），而非共价键的断裂。如果磷酸二酯键断裂，那叫DNA降解，不是变性。"
    },
    {
        "type": "fill", "points": 2,
        "question": "DNA变性时，A₂₆₀吸光度增加的现象称为____效应。DNA熔解温度Tm是指____%的DNA双链解离为单链时的温度。",
        "answer": [["增色"], ["50"]],
        "explanation": "增色效应(hyperchromic effect)是因为双链中碱基紧密堆积限制紫外吸收，解链后碱基暴露，A₂₆₀增加约30-40%。Tm是50%变性时的温度，不是完全熔解的温度。",
        "pitfall": "Tm受GC含量和盐浓度影响——GC含量越高Tm越高，盐浓度越高Tm越高（阳离子屏蔽磷酸骨架负电荷排斥）。"
    },

    # Chapter 9-10 - Enzymes
    {
        "type": "choice", "points": 2,
        "question": "关于酶催化，以下哪项描述是正确的？",
        "options": ["酶改变反应的平衡常数", "酶降低反应的活化能", "酶改变反应的ΔG", "酶提高产物的能量"],
        "answer": 1,
        "explanation": "酶降低反应的活化能(ΔG‡)，使更多分子能越过能垒，从而加速反应。但酶不改变反应的ΔG（平衡常数）——它只影响速率，不影响热力学。",
        "pitfall": "酶降低ΔG‡，不改变ΔG。催化剂只能改变反应速率，不能使热力学上不利的反应(ΔG>0)变为有利。"
    },
    {
        "type": "choice", "points": 2,
        "question": "竞争性抑制剂对酶动力学参数的影响是？",
        "options": ["Km不变，Vmax减小", "Km增大，Vmax不变", "Km减小，Vmax不变", "Km和Vmax都减小"],
        "answer": 1,
        "explanation": "竞争性抑制剂与底物竞争活性中心，提高表观Km（需要更高[S]达到半饱和），但Vmax不变（因为[S]→∞时底物可以「竞争赢」抑制剂）。双倒数图中交于Y轴同一点。",
        "pitfall": "非竞争性抑制剂Vmax减小、Km不变（交于X轴同一点）。反竞争性抑制剂Vmax和Km等比例减小（平行线）。"
    },
    {
        "type": "choice", "points": 2,
        "question": "丝氨酸蛋白酶催化三联体由哪三个残基组成？",
        "options": ["Ser-Cys-His", "Ser-His-Asp", "Ser-Glu-His", "Cys-His-Asp"],
        "answer": 1,
        "explanation": "催化三联体为Ser¹⁹⁵-His⁵⁷-Asp¹⁰²（以胰凝乳蛋白酶编号）。Asp的-COO⁻定向His的咪唑环，His从Ser的-OH接受质子，使Ser变为更强的亲核试剂(Ser-O⁻)。",
        "pitfall": "催化三联体中Asp不直接参与催化，而是通过电荷中继网络(charge relay network)定向His提高其碱催化能力。"
    },
    {
        "type": "tf", "points": 1,
        "question": "核酶(ribozyme)的发现证明所有酶都是蛋白质。",
        "answer": 1,
        "explanation": "错误。核酶的发现恰恰推翻了「酶==蛋白质」的教条。Cech(1982)发现四膜虫rRNA前体可以自我剪接，证明RNA也具有催化功能。核糖体肽酰转移酶活性也由rRNA催化。",
        "pitfall": "核酶(ribozyme)发现于1982年，Cech和Altman获1989年诺贝尔化学奖。这一发现为「RNA世界」假说提供了关键支持。"
    },
    {
        "type": "fill", "points": 2,
        "question": "Michaelis-Menten方程中，Km的定义是反应速率达到____的一半时的底物浓度。kcat/Km被称为____常数，其上限受扩散控制（~10⁸-10⁹ M⁻¹s⁻¹）。",
        "answer": [["Vmax", "最大速率"], ["催化效率", "专一性"]],
        "explanation": "Km = (k₋₁ + kcat)/k₁，当kcat << k₋₁时Km≈Kd。kcat/Km综合衡量催化效率，最高效的酶（如碳酸酐酶）kcat/Km≈10⁸ M⁻¹s⁻¹，接近扩散控制极限。",
        "pitfall": "Km不是ES的解离常数Kd，除非kcat远小于k₋₁。一般来说Km≥Kd。"
    },

    # Chapter 14 - Vitamins
    {
        "type": "choice", "points": 2,
        "question": "NAD⁺的活性部分来自哪种维生素？",
        "options": ["维生素B₁ (硫胺素)", "维生素B₂ (核黄素)", "维生素B₃ (烟酸)", "维生素B₆ (吡哆醇)"],
        "answer": 2,
        "explanation": "NAD⁺（烟酰胺腺嘌呤二核苷酸）的活性部分是烟酰胺，来自维生素B₃（烟酸/niacin）。NAD⁺接受一个H⁻（两个电子+一个质子）→NADH。",
        "pitfall": "NAD⁺来自B₃，FAD来自B₂，TPP来自B₁，PLP来自B₆，CoA来自B₅。不要混淆！"
    },
    {
        "type": "choice", "points": 2,
        "question": "PLP（磷酸吡哆醛）在转氨反应中，与氨基酸的什么基团形成Schiff碱？",
        "options": ["侧链羧基", "α-氨基", "α-羧基", "侧链羟基"],
        "answer": 1,
        "explanation": "PLP的醛基与氨基酸的α-氨基形成Schiff碱（亚胺，-N=CH-），随后吡啶环作为「电子下沉」稳定各种转化中间体的负电荷。",
        "pitfall": "PLP与α-NH₂成键，不是与α-COOH或侧链基团。所有PLP催化的反应都从此Schiff碱开始，不同反应路径由酶控制断裂Cα的哪个键来决定。"
    },

    # Chapter 16 - Carbohydrates
    {
        "type": "choice", "points": 2,
        "question": "蔗糖为什么是非还原糖？",
        "options": ["不含醛基", "两个单糖的异头碳都参与了糖苷键的形成", "分子量太大", "不含游离羟基"],
        "answer": 1,
        "explanation": "蔗糖由葡萄糖(α1↔2β)果糖组成，两个单糖的异头碳（Glc的C₁和Fru的C₂）都参与了糖苷键的形成，没有游离的异头碳-OH，因此不能开环形成醛基，是非还原糖。",
        "pitfall": "乳糖(Gal β1→4 Glc)是还原糖，因为Glc的异头碳(C₁)是游离的，可以开环暴露醛基。麦芽糖也是还原糖。"
    },
    {
        "type": "choice", "points": 2,
        "question": "淀粉和纤维素都是由葡萄糖组成的聚合物，但人类只能消化淀粉，原因是什么？",
        "options": ["纤维素分子量太大", "淀粉含α-1,4糖苷键，纤维素含β-1,4糖苷键", "纤维素含有支链", "淀粉溶解度更高"],
        "answer": 1,
        "explanation": "淀粉的葡萄糖单元以α-1,4糖苷键连接，人类消化酶（α-淀粉酶）只能识别α糖苷键。纤维素的葡萄糖单元以β-1,4糖苷键连接，人类缺乏β-糖苷酶，无法消化。",
        "pitfall": "α和β仅差异头碳一个构型，但导致链的几何形状完全不同——α使链弯曲成螺旋（可溶），β使链伸直形成纤维（不溶）。这就是「小差异，大后果」的经典案例。"
    },

    # Chapter 17-18 - Lipids & Hormones  
    {
        "type": "choice", "points": 2,
        "question": "下列哪种脂肪酸是必需脂肪酸（人体不能合成）？",
        "options": ["棕榈酸(16:0)", "硬脂酸(18:0)", "亚油酸(18:2 ω-6)", "油酸(18:1 ω-9)"],
        "answer": 2,
        "explanation": "亚油酸(18:2 ω-6)和α-亚麻酸(18:3 ω-3)是必需脂肪酸，人体不能合成，因为缺乏在ω-3和ω-6位置引入双键的酶。油酸(18:1 ω-9)可以自身合成。",
        "pitfall": "人体可以在脂肪酸链的ω-9位置引入双键（如油酸），但不能在ω-3和ω-6位置引入。ω-3和ω-6脂肪酸只能从食物获取。"
    },
    {
        "type": "choice", "points": 2,
        "question": "cAMP信号通路中，腺苷酸环化酶被什么激活？",
        "options": ["Gi蛋白的α亚基", "Gs蛋白的α亚基-GTP复合物", "G蛋白的βγ亚基", "PKA"],
        "answer": 1,
        "explanation": "激素与GPCR结合→Gsα-GDP→Gsα-GTP（激活）→Gsα-GTP激活腺苷酸环化酶→ATP→cAMP→cAMP激活PKA→下游磷酸化级联。",
        "pitfall": "Gi蛋白抑制腺苷酸环化酶（降低cAMP）。Gs是激活，Gi是抑制——区分：s=stimulatory, i=inhibitory。"
    },
    {
        "type": "tf", "points": 1,
        "question": "霍乱毒素通过ADP-核糖基化修饰Gsα，使其GTPase活性增强，cAMP持续升高导致腹泻。",
        "answer": 1,
        "explanation": "错误。霍乱毒素ADP-核糖基化修饰Gsα后，Gsα的GTPase活性丧失（而非增强），导致Gsα-GTP持续存在→腺苷酸环化酶持续激活→cAMP持续升高→肠上皮过度分泌Cl⁻和水→严重腹泻。",
        "pitfall": "霍乱毒素使Gsα「锁死」在激活态——GTPase活性丧失，不能水解GTP为GDP来关闭信号。"
    },
    {
        "type": "essay", "points": 10,
        "question": "请从结构和功能两个角度，阐述血红蛋白(Hb)的氧合协同效应和别构调控机制，包括MWC模型、Bohr效应和2,3-BPG的作用。",
        "answer": -1,
        "explanation": "<strong>参考答案要点：</strong><br><br><strong>1. 结构基础</strong>：Hb为α₂β₂四聚体，每个亚基含一个血红素。存在T态（低亲和力）和R态（高亲和力）两种构象。<br><br><strong>2. MWC模型</strong>：所有亚基同时处于T或R态（对称性）。无O₂时平衡偏向T态；O₂结合后逐渐移向R态。S形曲线源自低[O₂]时主要结合T态（低亲和力），高[O₂]时转为R态（高亲和力）。<br><br><strong>3. Bohr效应</strong>：H⁺和CO₂降低Hb对O₂亲和力。代谢活跃组织CO₂↑→pH↓→H⁺结合Hb稳定T态→促进O₂释放。肺部CO₂排出→pH↑→O₂亲和力升高→促进O₂结合。<br><br><strong>4. 2,3-BPG</strong>：结合在Hb四聚体中央空腔，静电稳定T态，降低O₂亲和力。高原适应时2,3-BPG升高。胎儿Hb(α₂γ₂)对2,3-BPG亲和力低→O₂亲和力高→从母体摄O₂。<br><br><strong>评分要点</strong>：T/R态概念(3分)，MWC模型解释S形曲线(2分)，Bohr效应生理意义(3分)，2,3-BPG机制(2分)。",
        "pitfall": "常见错误：(1) 混淆MWC和KNF模型的区别；(2) 认为Bohr效应是O₂浓度变化引起的；(3) 忘记2,3-BPG只影响Hb不影响Mb。"
    },
    {
        "type": "short", "points": 5,
        "question": "酶通过哪些机制降低反应的活化能？请列举至少三种并简要说明。",
        "answer": -1,
        "explanation": "<strong>参考答案：</strong><br>1. <strong>酸碱催化</strong>：活性中心氨基酸侧链作为质子供体或受体，稳定过渡态电荷。<br>2. <strong>共价催化</strong>：酶与底物形成共价中间体（如Ser-O⁻亲核攻击形成酰基-酶中间体），提供低能反应路径。<br>3. <strong>邻近与定向效应</strong>：将两个底物在活性中心以正确空间取向放置，使有效浓度极大提高。<br>4. <strong>过渡态稳定化</strong>：活性中心形状完美匹配过渡态（而非底物），降低过渡态自由能。<br>5. <strong>金属离子催化</strong>：Zn²⁺/Mg²⁺等提供Lewis酸催化或稳定负电荷。",
        "pitfall": "常漏掉「邻近与定向效应」——这是熵效应（减少平移熵和转动熵），与焓效应（酸碱催化等）互补。"
    }
]

save_test(questions, '/workspace/output/生物化学_第一篇_自测题.html', '第一篇 结构生物化学', '生物化学原理第四版 · 深度学习模式 · 100分', duration_minutes=60)
print('Test saved.')
print('Done!')