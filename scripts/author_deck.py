"""Reproducible, content-preserving authoring of the Slidev Markdown source.

The source-text JSON is extracted from the untouched PPTX. Text embedded in
screenshots is transcribed below. This script does not draw or alter microscopy.
"""
from pathlib import Path
import json, html, re

ROOT = Path(__file__).resolve().parents[1]
SOURCE = json.loads((ROOT/'reference/source-text.json').read_text(encoding='utf-8'))
P = {s['slide']:s['paragraphs'] for s in SOURCE['slides']}
def norm(s):
    return (s.replace('Gaisb�ck','Gaisböck').replace(' � ',' ± ')
            .replace('g/dL�','g/dL ± ').replace('%�','% ± '))
def esc(s): return html.escape(norm(s))
def para(s, cls=''): return f'<p{f" class={chr(34)}{cls}{chr(34)}" if cls else ""}>{esc(s)}</p>'
def h2(s): return f'<h2>{esc(s)}</h2>'
def h3(s): return f'<h3>{esc(s)}</h3>'
def ul(items): return '<ul>'+''.join(f'<li>{esc(s)}</li>' for s in items)+'</ul>'
def rows(items,cls=''):return f'<dl class="rows {cls}">'+''.join('<div><dt>'+esc(a)+'</dt><dd>'+esc(b)+'</dd></div>' for a,b in items)+'</dl>'
def cols(a,b,cls=''): return f'<div class="columns {cls}"><div>{a}</div><div>{b}</div></div>'
SLIDES=[]
def add(title,body,section='',cls='',meta='',notes=''):
    i=len(SLIDES)+1
    fm=f'class: clinical {cls}\n' + (meta+'\n' if meta else '')
    content=f'# {title}\n\n{body}\n\n<SlideFooter number="{i}" section="{section}"'+(' light' if 'title-slide' in cls else '')+' />\n'
    if notes:content+='\n<!--\n'+notes+'\n-->\n'
    SLIDES.append((fm,content))

add('Polycythemias:',para(P[1][0],'subtitle')+'<p class="presenter"><span>Presented by:</span>Zeinab Eftekhar</p>',cls='title-slide')

add('Erythrocytosis',para(P[2][1])+'<VolumeComparison />'+para(P[2][2],'small'),'Erythrocytosis')

add('Classification','<div class="classification-summary">'+''.join([
'<section><span class="num">1</span>'+h2(P[3][2])+ '<div>'+para(P[3][6])+para(P[3][7])+'</div></section>',
'<section><span class="num">2</span>'+h2(P[3][4])+ '<div>'+para(P[3][0])+para(P[3][1])+'</div></section>',
'<section><span class="num">3</span>'+h2(P[3][3])+ '<div>'+para(P[3][8])+para(P[3][9])+'</div></section>',
])+'</div>','Erythrocytosis',cls='dense')

add('Clinical classification of erythrocytosis / polycythemia',para('First separate relative from absolute erythrocytosis; then classify the mechanism.','fine')+'<ClassificationTree />','Erythrocytosis',cls='dense classification-slide')

add('Reference ranges',para(P[5][1])+f'<table><thead><tr><th>For reference</th><th>Hemoglobin</th><th>Hematocrit</th></tr></thead><tbody><tr><th>Healthy adult man</th><td>16 g/dL ± 2 g/dL</td><td>47% ± 6%</td></tr><tr><th>Menstruating adult woman<br><span class="fine">Usually</span></th><td>13 g/dL ± 2 gm/dL</td><td>40% ± 6%</td></tr></tbody></table><div style="height:36px"></div>'+para(P[5][3],'emphasis'),'Erythrocytosis',notes='The original adult reference-value paragraph is faithfully represented as a table, including all means, ± values, units, population labels, and the qualifier “usually.”')

add('Relative erythrocytosis: Gaisböck', '<span class="section">PART 1</span>'+para('(stress or relative polycythemia)','subtitle')+para(P[6][3],'lead')+'<VolumeComparison />'+cols(para(P[6][4]),para(P[6][5]),'small'),'Relative erythrocytosis',cls='dense relative-slide')

add('Relative erythrocytosis', '<span class="section">PART 1</span>'+para(P[7][2],'lead')+'<VolumeComparison />'+para(P[7][3],'emphasis lead'),'Relative erythrocytosis')

add('Absolute (True) Polycythemia','<span class="section">PART 2</span>'+para(P[8][2],'lead')+'<div style="margin-top:52px"><span class="section">PART 2-1</span>'+h2(P[8][4])+ul(P[8][5:])+'</div>','Absolute erythrocytosis')

add('Absolute SECONDARY erythrocytosis','<span class="section">PART 2</span>'+ '<div class="mechanism"><div class="step">'+h2('Low oxygen delivery or excess EPO')+'</div><span class="arrow" aria-hidden="true">→</span><div class="step">'+h2('Kidney / tissue signal')+'</div><span class="arrow" aria-hidden="true">→</span><div class="step">'+h2('Marrow erythropoiesis')+'</div></div>'+para(P[9][3],'emphasis')+'<div class="three-col">'+''.join('<div>'+h3(P[9][i])+para(P[9][i+1],'small')+'</div>' for i in [4,6,8])+'</div>','Secondary erythrocytosis')

causes=[]
for t in P[10][2:]:
 if ':' in t:causes.append(t.split(':',1))
 else:causes.append([t,''])
add('Absolute SECONDARY erythrocytosis','<span class="section">PART 2-2 · High serum EPO levels</span>'+rows(causes,'compact secondary-causes'),'Secondary erythrocytosis',cls='dense causes-slide')

add('Absolute secondary erythrocytosis',para('Hypoxia-driven','subtitle')+rows([
('Sleep-disordered breathing','Ask about snoring, witnessed apnoea and daytime sleepiness; consider a sleep study.'),
('Lung disease','COPD and interstitial lung disease can cause chronic hypoxemia.'),
('Smoking / CO','Carboxyhemoglobin impairs oxygen delivery and may make pulse oximetry misleading.'),
('Cardiac disease / altitude','Cyanotic heart disease and high altitude reduce inspired or delivered oxygen.'),
],'wide-label'),'Secondary erythrocytosis')

add('Absolute secondary erythrocytosis',para('EPO or drug-driven','subtitle')+rows([
('EPO-producing lesions','Renal cell carcinoma, hepatocellular carcinoma and rare tumors → EPO level, renal/hepatic assessment and targeted imaging'),
('Hormones and drugs','Testosterone, anabolic agents and exogenous EPO → medication, supplement and doping review'),
('SGLT2 inhibitors','Erythropoietic effect and hemoconcentration may coexist → review timing, volume status and competing causes'),
('Relative mimic','Dehydration and diuretics can create the same CBC signal → repeat after volume correction'),
],'wide-label'),'Secondary erythrocytosis',cls='dense')

add('Absolute secondary erythrocytosis: laboratory work-up',para(P[13][1],'emphasis small')+rows([
('CBC trend','Confirm persistence; inspect WBC, platelets, MCV and smear.'),
('Oxygen assessment','Pulse oximetry, sleep study, smoking/CO history, pulmonary and cardiac evaluation when indicated.'),
('Serum EPO','Usually normal or high in secondary disease; interpret “normal” relative to the degree of erythrocytosis.'),
('JAK2 testing','Usually absent; if low EPO or the phenotype is strongly suggestive, test JAK2 before closing the case.'),
('Targeted tests','Medication review, renal/hepatic evaluation, imaging or hereditary work-up according to the history.'),
],'compact'),'Secondary erythrocytosis',cls='dense workup-slide')

add('Absolute SECONDARY erythrocytosis','<span class="section">PART 2-3</span>'+h2('Neonatal Polycythemia')+para(P[14][2],'lead')+'<div class="mechanism"><div class="step">'+h3('Relative intrauterine tissue hypoxia')+'</div><span class="arrow" aria-hidden="true">→</span><div class="step">'+h3('Higher neonatal hematocrit')+'</div><span class="arrow" aria-hidden="true">+</span><div class="step">'+h3('High affinity of fetal hemoglobin for oxygen')+'</div></div>','Secondary erythrocytosis')

add('Absolute hereditary / congenital erythrocytosis','<span class="section">PART 3</span>'+para(P[15][1],'emphasis small')+cols(h2('Clinical clues')+ul(['Young age at onset','Several affected relatives','Persistent elevation without hypoxia, drugs or tumor','Stable pattern over many years']),h2('Mechanistic groups')+ul(['EPOR: primary, often low EPO','VHL / EGLN1 / EPAS1: oxygen-sensing pathway','High-affinity hemoglobin: impaired oxygen unloading']))+para('The phenotype should guide the genetic panel.','small'),'Hereditary erythrocytosis',cls='dense')

add('TABLE 1. Differential Diagnosis of Polycythemia','<DifferentialTable />','Differential diagnosis',cls='dense differential-slide',meta='clicks: 3',notes='Arrow Right / Space: full table overview, magnified upper secondary section, magnified lower secondary section, congenital and relative sections. Arrow Left reverses. All columns and source text are preserved; the source table’s clinical associations have not been reinterpreted.')

add('PV: absolute primary acquired erythrocytosis','<span class="section">PART 4</span><div class="thresholds">'+para(P[17][1])+para(P[17][2])+'</div>'+h2('Myeloid proliferations and neoplasms')+rows([
('Chronic myeloid neoplasms','CML • CNL • CEL • MPNs'),
('Myeloproliferative neoplasms','PV • ET • PMF • MPN, NOS'),
('PV diagnosis','Blood counts + marrow morphology + molecular clonality + clinical exclusions'),
],'compact')+para('The key diagnostic principle is integration: no isolated CBC value or mutation replaces morphology and clinical context.','fine'),'Polycythemia vera',cls='dense')

add('PV: Pathophysiology',cols(h2(P[18][4])+para(P[18][5]),h2(P[18][2])+para(P[18][3]),'small'),'Polycythemia vera',cls='pathophysiology-slide')

add('PV: EPO-independent erythropoiesis','<div class="mechanism jak-pathway"><div class="step">'+h2('Hematopoietic stem cell')+'</div><span v-click="1" class="arrow" aria-hidden="true">→</span><div v-click="1" class="step">'+h2('JAK2 V617F or exon 12')+'</div><span v-click="2" class="arrow" aria-hidden="true">→</span><div v-click="2" class="step">'+h2('Persistent JAK–STAT signal')+'</div><span v-click="3" class="arrow" aria-hidden="true">→</span><div v-click="3" class="step">'+h2('Pan myelosis and symptoms')+'</div></div>'+para(P[19][-1],'emphasis lead'),'Polycythemia vera',meta='clicks: 3')

add('TABLE 2. International Consensus Criteria for the Diagnosis of Polycythemia Vera','<div class="criteria">'+h2('Major criteria')+'<ol><li>Hemoglobin &gt;16.5 g/dL in men or &gt;16.0 g/dL in women or hematocrit &gt;49% in men or &gt;48% in women or red blood cell mass &gt;25% above mean normal predicted value</li><li>Bone marrow biopsy showing age-adjusted hypercellularity with trilineage proliferation (panmyelosis), including prominent erythroid, granulocytic, and increase in pleomorphic, mature megakaryocytes without atypia</li><li>Presence of <i>JAK2</i> V617F or <i>JAK2</i> exon 12 mutation</li></ol>'+h2('Minor criterion')+para('1. Subnormal serum erythropoietin level')+'<div class="footnotes">'+para('a All 3 major criteria or the first 2 of the major criteria together with the minor criterion are required for formal diagnosis.')+para('b SI conversion factors: To convert hemoglobin value to g/L, multiply by 10.0.')+'</div></div>','Polycythemia vera',cls='dense criteria-slide')

add('PV: Epidemiology','<div class="epidemiology"><div><div class="stat">22</div><p class="stat-caption">'+esc(P[21][2])+'</p></div><div>'+ul(P[21][3:])+'</div></div>','Polycythemia vera',cls='dense')

add('PV laboratory diagnosis',cols('<div class="numbered">'+''.join('<article><span class="num">'+str(i+1)+'</span><div>'+h3(a)+para(b)+'</div></article>' for i,(a,b) in enumerate([
('Erythrocytosis','Hb >16.5 g/dL or Hct >49% in men; Hb >16.0 g/dL or Hct >48% in women.'),
('Serum EPO','Subnormal EPO is the minor criterion and supports EPO-independent biology.'),
('JAK2','V617F or exon 12 mutation establishes a clonal signal in the correct phenotype.'),
('Bone marrow','Age-adjusted hypercellularity with trilineage proliferation and characteristic megakaryocytes.'),
]))+'</div>','<MicroscopyFigure image="60160" title="PV, polycythemic phase: peripheral blood" />','asym'),'Polycythemia vera',cls='dense laboratory-slide',notes='Added image: Elizabeth L. Courville. Polycythemia vera (PV), polycythemic phase, peripheral blood. ASH Image Bank. 2015; 60160. https://imagebank.hematology.org/image/60160/polycythemia-vera-pv-polycythemic-phase-peripheral-blood . Unmodified, for local/classroom noncommercial use. https://imagebank.hematology.org/permissions')

add('Bone marrow morphology: The differential diagnosis of PV',cols('<MicroscopyFigure image="60162" title="PV, polycythemic phase: core biopsy" />',rows([
('PV','Panmyelosis with erythroid, granulocytic and megakaryocytic expansion.'),
('ET','Predominantly megakaryocytic proliferation with large mature hyperlobulated megakaryocytes.'),
('Pre-PMF','Atypical clustered megakaryocytes with granulocytic expansion; LDH and spleen may be higher.'),
],'compact'),'asym'),'Polycythemia vera',cls='dense morphology-slide',notes='Replacement microscopy: Elizabeth L. Courville. Polycythemia vera (PV), polycythemic phase, core biopsy 2. ASH Image Bank. 2015; 60162. https://imagebank.hematology.org/image/60162/polycythemia-vera-pv-polycythemic-phase-core-biopsy-2 . Unmodified. The micrograph illustrates PV only, not the adjacent ET or pre-PMF descriptions. Local/classroom noncommercial use: https://imagebank.hematology.org/permissions')

sentences=re.split(r'(?<=\.) ',P[24][1])
add('PV Complications','<div class="complications-prose">'+''.join(para(s) for s in sentences)+'</div>','Polycythemia vera')

add('Clinical phenotype: PV complications and risk',rows([
('Thrombosis','Arterial, venous or unusual-site events; the major preventable complication.'),
('Microvascular symptoms','Headache, visual disturbance, erythromelalgia and acral paresthesia.'),
('Bleeding','Especially with extreme thrombocytosis and acquired von Willebrand syndrome.'),
('Conventional high risk','Age ≥60 years or previous thrombosis.'),
('Progression','Post-PV myelofibrosis or blast phase: cytopenias, rising LDH, splenomegaly or blasts.'),
],'compact wide-label'),'Polycythemia vera',cls='dense')

add('PV treatment',rows([
('For every patient','Phlebotomy to Hct <45%; low-dose aspirin when safe; control blood pressure, diabetes, lipids and smoking.'),
('If high risk','Age ≥60 or prior thrombosis → add cytoreduction.'),
('If symptoms or poor control','Consider cytoreduction for repeated phlebotomy, leukocytosis, splenomegaly or persistent symptom burden.'),
('Available strategies','Hydroxyurea, interferon or ruxolitinib according to age, tolerance and treatment goal; rusfertide is a 2026 targeted option for PV erythrocytosis.'),
],'wide-label'),'Polycythemia vera',cls='dense treatment-slide')

add('PV treatment','<div class="treatment-list">'+''.join('<div><span class="num">'+str(i+1).zfill(2)+'</span>'+para(t)+'</div>' for i,t in enumerate(P[27][1:]))+'</div>','Polycythemia vera')

add('THANK YOU', '',cls='title-slide closing')

assert len(SLIDES)==len(SOURCE['slides'])
from illustrated_edition import assemble
SLIDES=assemble(SLIDES,ROOT)
head='''theme: default
title: 'Polycythemias: From erythrocytosis to WHO-defined polycythemia vera'
author: Zeinab Eftekhar
info: |
  Polycythemias. Zeinab Eftekhar.
aspectRatio: 16/9
canvasWidth: 1280
colorSchema: light
fonts:
  provider: none
  sans: Source Sans 3
  serif: Source Sans 3
transition: fade
drawings:
  enabled: false
download: false
favicon: /favicon.png
comark: false
'''
out='---\n'+head+SLIDES[0][0]+'---\n\n'+SLIDES[0][1]
for fm,body in SLIDES[1:]:out+='\n---\n'+fm+'---\n\n'+body
(ROOT/'slides.md').write_text(out,encoding='utf-8')
print(f'Authored {len(SLIDES)} slides, {len(out):,} characters.')
