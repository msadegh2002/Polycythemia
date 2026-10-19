$ErrorActionPreference = 'Stop'
$atlasRoot = Split-Path -Parent $PSScriptRoot
$atlasOut = Join-Path $atlasRoot 'public/art/atlas'
# Original grouped illustrations, not whole slides or screenshots.
$atlasExports = @(
 @{id='erythrocyte';kit='Blood-immunology';slide=4;shape='Group 844'},
 @{id='erythrocyte-oblique';kit='Blood-immunology';slide=4;shape='Group 809'},
 @{id='erythrocyte-front';kit='Blood-immunology';slide=4;shape='Group 833'},
 @{id='stem-cell';kit='Blood-immunology';slide=15;shape='Group 17'},
 @{id='neutrophil';kit='Blood-immunology';slide=8;shape='Group 711'},
 @{id='platelet';kit='Blood-immunology';slide=12;shape='Group 1208'},
 @{id='kidney';kit='Urinary-system';slide=4;shape='Group 3'},
 @{id='specimen';kit='Medical-equipment';slide=5;shape='Group 3'}
)
$atlasApplication = New-Object -ComObject PowerPoint.Application
$atlasRecords = @()
foreach ($atlasKit in ($atlasExports.kit | Select-Object -Unique)) {
 $atlasFile = Join-Path $atlasRoot ('reference/servier-kits/SMART-' + $atlasKit + '.pptx')
 $atlasPresentation = $atlasApplication.Presentations.Open($atlasFile,-1,0,0)
 try {
  foreach ($atlasEntry in ($atlasExports | Where-Object kit -eq $atlasKit)) {
   $atlasShape = $atlasPresentation.Slides.Item($atlasEntry.slide).Shapes.Item($atlasEntry.shape)
   $atlasTarget = Join-Path $atlasOut ($atlasEntry.id + '.svg')
   $atlasShape.Export($atlasTarget,6)
   $atlasRecords += @{
    id=$atlasEntry.id;file=('/art/atlas/' + $atlasEntry.id + '.svg');creator='Servier Medical Art';
    license='CC BY 4.0';licenseUrl='https://creativecommons.org/licenses/by/4.0/';
    source=('https://smart.servier.com/wp-content/uploads/2016/10/SMART-' + $atlasKit + '.pptx');
    sourceSlide=$atlasEntry.slide;sourceShape=$atlasEntry.shape;
    sha256=(Get-FileHash -LiteralPath $atlasTarget -Algorithm SHA256).Hash.ToLower();
    modifications='Original illustration group exported as SVG using PowerPoint. Scaled, positioned, rotated, and animated in the presentation.'
   }
   Write-Output ($atlasEntry.id + ' exported')
  }
 } finally { $atlasPresentation.Close() }
}
$atlasRecords | ConvertTo-Json -Depth 5 | Set-Content -LiteralPath (Join-Path $atlasOut 'vector-sources.json') -Encoding utf8
