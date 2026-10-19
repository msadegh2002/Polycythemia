"""Apply the medical-atlas art direction and retain the eight visual additions."""
import json,re

def visual(title,body,section,ident,refs,clicks=0,kind='diagram',image=None):
    cls='clinical illustrated atlas '+('microscopy-page' if kind=='microscopy' else 'diagram-page')
    fm=f'class: {cls}\n'+(f'clicks: {clicks}\n' if clicks else '')
    return dict(id=ident,sourceSlide=None,sourceRefs=refs,kind=kind,clicks=clicks,title=title,section=section,fm=fm,body=body,image=image)

def assemble(original,root):
    inserts={
      2:[visual('Red-cell mass and plasma volume','<p class="diagram-intro">Absolute erythrocytosis and relative erythrocytosis</p><BloodVolumeScene />','Erythrocytosis','diagram-volume',[2,6,7],2)],
      4:[visual('Classification: follow the mechanism','<ClassificationWalkthrough />','Erythrocytosis','diagram-classification',[3,4,8,15],3)],
      9:[visual('Hypoxia, EPO and the marrow','<EpoJourney />','Secondary erythrocytosis','diagram-epo',[9,18],2)],
      13:[visual('Erythrocytosis: the work-up map','<p class="diagram-intro">The laboratory goal is to prove an external driver and avoid mislabeling the patient as PV</p><WorkupMap />','Secondary erythrocytosis','diagram-workup',[13],4)],
      19:[visual('EPO-driven and autonomous signaling','<JAK2Comparison />','Polycythemia vera','diagram-jak2',[18,19],3)],
      22:[
        visual('PV: peripheral blood','<MicroscopyStage image="60160" specimen="Peripheral blood" label="PV, polycythemic phase: peripheral blood" />','Microscopy','microscopy-blood',[22],kind='microscopy',image='60160'),
        visual('PV: marrow core biopsy','<MicroscopyStage image="60161" specimen="Core biopsy" label="PV, polycythemic phase: core biopsy 1" />','Microscopy','microscopy-core',[20,22,23],kind='microscopy',image='60161'),
      ],
      23:[visual('PV: aspirate smear','<MicroscopyStage image="60164" specimen="Aspirate smear" label="PV, polycythemic phase: aspirate smear" />','Microscopy','microscopy-aspirate',[23],kind='microscopy',image='60164')],
    }
    entries=[]
    for source,(fm,content) in enumerate(original,1):
        title,rest=content.split('\n\n',1)
        title=title.removeprefix('# ')
        body,footer=re.split(r'\n\n<SlideFooter[^>]+/>',rest,maxsplit=1)
        notes=footer.strip()
        section_match=re.search(r'section="([^"]*)"',rest)
        section=section_match.group(1) if section_match else ''
        if source==2:body=body.replace('<VolumeComparison />','')
        if source in (6,7):body=body.replace('<VolumeComparison />','<BloodVolumeScene compact fixed="relative" />')
        if source==19:
            body=re.sub(r'<div class="mechanism jak-pathway">.*?</div></div>','<JAK2Pathway />',body,count=1,flags=re.S)
        if source==20:body='<DiagnosticCriteria />'
        if source==26:body='<TreatmentFocus />'
        if source==22:
            body=re.sub(r'<MicroscopyFigure image="60160"[^>]+/>','<HematologyArt variant="specimen" inline />',body)
            body=body.replace('in men; Hb','in men;<br />Hb')
            notes=''
        fm=fm.replace('class: clinical ',f'class: clinical illustrated atlas source-{source:02d} ')
        clicks={16:6,19:3,20:3,26:2}.get(source,0)
        fm=re.sub(r'(?m)^clicks:.*\n?','',fm).rstrip()+'\n'
        if clicks:fm+=f'clicks: {clicks}\n'
        entries.append(dict(id=f'source-{source:02d}',sourceSlide=source,sourceRefs=[source],kind='source',clicks=clicks,title=title,section=section,fm=fm,body=body,notes=notes,image='60162' if source==23 else None))
        entries.extend(inserts.get(source,[]))
    assert len(entries)==36
    manifest=[];result=[]
    artwork={1:'cover',2:'erythrocyte',5:'specimen',8:'stem',15:'stem',17:'marrow',22:'none',24:'marrow',28:'cover'}
    for position,e in enumerate(entries,1):
        source=e.get('sourceSlide')
        variant=artwork.get(source,'none')
        ref=source or min(e['sourceRefs'])
        chapter='laboratory' if e['kind']=='microscopy' else 'foundations' if ref<=8 else 'secondary' if ref<=14 else 'hereditary' if ref<=16 else 'pv' if ref<=21 else 'laboratory' if ref<=23 else 'management'
        illustrated=variant!='none' or source in (6,7,19,22,26) or e['id'] in ('diagram-volume','diagram-epo','diagram-workup','diagram-jak2')
        e['chapter']=chapter;e['artwork']='treatment-inline' if source==26 else 'specimen-inline' if source==22 else variant if variant!='none' else e['id'] if illustrated else 'none'
        e['illustrationCredit']=illustrated
        light=source in (1,28) or e['kind']=='microscopy'
        art='' if variant=='none' else f'<HematologyArt variant="{variant}" />\n\n'
        content=f'# {e["title"]}\n\n{art}<div class="deck-content">\n\n{e["body"]}\n\n</div>\n\n<SlideFooter number="{position}" section="{e["section"]}"'+(' light' if light else '')+' />\n'
        if e['kind']=='microscopy':
            image=e['image'];content+=f'\n<!--\nElizabeth L. Courville. ASH Image Bank. 2015; image {image}. https://imagebank.hematology.org/image/{image}\nComplete, unmodified image; local/classroom use. https://imagebank.hematology.org/permissions\n-->\n'
        elif e.get('notes'):content+='\n'+e['notes']+'\n'
        result.append((e['fm'],content))
        manifest.append({key:e.get(key) for key in ['id','sourceSlide','sourceRefs','kind','clicks','title','image','chapter','artwork','illustrationCredit']}|{'position':position})
    (root/'slide-manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
    lines=['# Medical-atlas edition: source-to-slide map','','36 slides: 28 original content slides, five diagram additions, and three microscopy additions. Original source order and medical content are preserved.','','| Slide | Stable ID | Original source reference | Type | Reveals | Chapter | Artwork |','|---|---|---|---|---|---|---|']
    for m in manifest:lines.append(f'| {m["position"]} | {m["id"]} | '+', '.join(map(str,m['sourceRefs']))+f' | {m["kind"]} | {m["clicks"]} | {m["chapter"]} | {m["artwork"]} |')
    lines+=['','Original paragraph text and the original PowerPoint SHA-256 remain in `source-text.json`. The 28-slide transcription checklist is retained in `SOURCE-CONTENT-CHECKLIST.md`. All additional content is a diagram illustrating source statements or an ASH microscopy slide.','', 'ASH images: 60160 (peripheral blood), 60161 (core biopsy 1), 60162 (existing morphology comparison), 60164 (aspirate smear). Each is displayed once, complete and unmodified, with attribution.']
    (root/'reference/CONTENT-MAP.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
    return result
