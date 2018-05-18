---
title: Structures
description: DirectWrite defines the following structures.
ms.assetid: '348dd001-bad9-4f1a-a5f5-84b118a5e2d4'
keywords: ["DirectWrite,structures"]
---

# Structures

DirectWrite defines the following structures.

## In this section



| Topic                                                                                     | Description                                                                                                                                                                                                     |
|-------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**DWRITE\_CARET\_METRICS**](dwrite-caret-metrics.md)<br/>                         | The [**DWRITE\_CARET\_METRICS**](dwrite-caret-metrics.md) structure specifies the metrics for caret placement in a font.<br/>                                                                            |
| [**DWRITE\_CLUSTER\_METRICS**](dwrite-cluster-metrics.md)<br/>                     | Contains information about a glyph cluster.<br/>                                                                                                                                                          |
| [**DWRITE\_COLOR\_F**](dwrite-color-f.md)<br/>                                     | Describes the red, green, blue, and alpha components of a color.<br/>                                                                                                                                     |
| [**DWRITE\_COLOR\_GLYPH\_RUN**](dwrite-color-glyph-run.md)<br/>                    | Contains the information needed by renderers to draw glyph runs with glyph color information.<br/>                                                                                                        |
| [**DWRITE\_COLOR\_GLYPH\_RUN1**](dwrite-color-glyph-run1.md)<br/>                  | Represents a color glyph run. The IDWriteFactory4::TranslateColorGlyphRun method returns an ordered collection of color glyph runs of varying types depending on what the font supports.<br/>             |
| [**DWRITE\_FILE\_FRAGMENT**](dwrite-file-fragment.md)<br/>                         | Represents a range of bytes in a font file.<br/>                                                                                                                                                          |
| [**DWRITE\_FONT\_FEATURE**](dwrite-font-feature.md)<br/>                           | Specifies properties used to identify and execute typographic features in the current font face.<br/>                                                                                                     |
| [**DWRITE\_FONT\_METRICS**](dwrite-font-metrics.md)<br/>                           | The [**DWRITE\_FONT\_METRICS**](dwrite-font-metrics.md) structure specifies the metrics that are applicable to all glyphs within the font face.<br/>                                                     |
| [**DWRITE\_FONT\_METRICS1**](dwrite-font-metrics1.md)<br/>                         | The [**DWRITE\_FONT\_METRICS1**](dwrite-font-metrics1.md) structure specifies the metrics that are applicable to all glyphs within the font face.<br/>                                                   |
| [**DWRITE\_FONT\_PROPERTY**](dwrite-font-property.md)<br/>                         | Font property used for filtering font sets and building a font set with explicit properties.<br/>                                                                                                         |
| [**DWRITE\_GLYPH\_IMAGE\_DATA**](dwrite-glyph-image-data.md)<br/>                  | Data for a single glyph from GetGlyphImageData.<br/>                                                                                                                                                      |
| [**DWRITE\_GLYPH\_METRICS**](dwrite-glyph-metrics.md)<br/>                         | Specifies the metrics of an individual glyph.<br/>                                                                                                                                                        |
| [**DWRITE\_GLYPH\_OFFSET**](dwrite-glyph-offset.md)<br/>                           | The optional adjustment to a glyph's position.<br/>                                                                                                                                                       |
| [**DWRITE\_GLYPH\_RUN**](dwrite-glyph-run.md)<br/>                                 | Contains the information needed by renderers to draw glyph runs.<br/>                                                                                                                                     |
| [**DWRITE\_GLYPH\_RUN\_DESCRIPTION**](dwrite-glyph-run-description.md)<br/>        | Contains additional properties related to those in [**DWRITE\_GLYPH\_RUN**](dwrite-glyph-run.md).<br/>                                                                                                   |
| [**DWRITE\_HIT\_TEST\_METRICS**](dwrite-hit-test-metrics.md)<br/>                  | Describes the region obtained by a hit test.<br/>                                                                                                                                                         |
| [**DWRITE\_INLINE\_OBJECT\_METRICS**](dwrite-inline-object-metrics.md)<br/>        | Contains properties describing the geometric measurement of an application-defined inline object.<br/>                                                                                                    |
| [**DWRITE\_JUSTIFICATION\_OPPORTUNITY**](dwrite-justification-opportunity.md)<br/> | The [**DWRITE\_JUSTIFICATION\_OPPORTUNITY**](dwrite-justification-opportunity.md) structure specifies justification info per glyph.<br/>                                                                 |
| [**DWRITE\_LINE\_BREAKPOINT**](dwrite-line-breakpoint.md)<br/>                     | Line breakpoint characteristics of a character.<br/>                                                                                                                                                      |
| [**DWRITE\_LINE\_METRICS**](dwrite-line-metrics.md)<br/>                           | Contains information about a formatted line of text.<br/>                                                                                                                                                 |
| [**DWRITE\_LINE\_METRICS1**](dwrite-line-metrics1.md)<br/>                         | Contains information about a formatted line of text.<br/>                                                                                                                                                 |
| [**DWRITE\_LINE\_SPACING**](dwrite-line-spacing.md)<br/>                           |                                                                                                                                                                                                                 |
| [**DWRITE\_MATRIX**](dwrite-matrix.md)<br/>                                        | The [**DWRITE\_MATRIX**](dwrite-matrix.md) structure specifies the graphics transform to be applied to rendered glyphs.<br/>                                                                             |
| [**DWRITE\_OVERHANG\_METRICS**](dwrite-overhang-metrics.md)<br/>                   | Indicates how much any visible DIPs (device independent pixels) overshoot each side of the layout or inline objects.<br/>                                                                                 |
| [**DWRITE\_PANOSE**](dwrite-panose.md)<br/>                                        | The [**DWRITE\_PANOSE**](dwrite-panose.md) union describes typeface classification values that you use with [**IDWriteFont1::GetPanose**](idwritefont1-getpanose.md) to select and match the font.<br/> |
| [**DWRITE\_SCRIPT\_ANALYSIS**](dwrite-script-analysis.md)<br/>                     | Stores the association of text and its writing system script, as well as some display attributes.<br/>                                                                                                    |
| [**DWRITE\_SCRIPT\_PROPERTIES**](dwrite-script-properties.md)<br/>                 | The [**DWRITE\_SCRIPT\_PROPERTIES**](dwrite-script-properties.md) structure specifies script properties for caret navigation and justification.<br/>                                                     |
| [**DWRITE\_SHAPING\_GLYPH\_PROPERTIES**](dwrite-shaping-glyph-properties.md)<br/>  | Contains shaping output properties for an output glyph.<br/>                                                                                                                                              |
| [**DWRITE\_SHAPING\_TEXT\_PROPERTIES**](dwrite-shaping-text-properties.md)<br/>    | Shaping output properties for an output glyph.<br/>                                                                                                                                                       |
| [**DWRITE\_STRIKETHROUGH**](dwrite-strikethrough.md)<br/>                          | Contains information regarding the size and placement of strikethroughs.<br/>                                                                                                                             |
| [**DWRITE\_TEXT\_METRICS**](dwrite-text-metrics.md)<br/>                           | Contains the metrics associated with text after layout.<br/>                                                                                                                                              |
| [**DWRITE\_TEXT\_METRICS1**](dwrite-text-metrics1.md)<br/>                         | Contains the metrics associated with text after layout.<br/>                                                                                                                                              |
| [**DWRITE\_TEXT\_RANGE**](dwrite-text-range.md)<br/>                               | Specifies a range of text positions where format is applied in the text represented by an [**IDWriteTextLayout**](idwritetextlayout.md) object.<br/>                                                     |
| [**DWRITE\_TRIMMING**](dwrite-trimming.md)<br/>                                    | Specifies the trimming option for text overflowing the layout box. <br/>                                                                                                                                  |
| [**DWRITE\_TYPOGRAPHIC\_FEATURES**](dwrite-typographic-features.md)<br/>           | Contains a set of typographic features to be applied during text shaping.<br/>                                                                                                                            |
| [**DWRITE\_UNDERLINE**](dwrite-underline.md)<br/>                                  | Contains information about the width, thickness, offset, run height, reading direction, and flow direction of an underline. <br/>                                                                         |
| [**DWRITE\_UNICODE\_RANGE**](dwrite-unicode-range.md)<br/>                         | The [**DWRITE\_UNICODE\_RANGE**](dwrite-unicode-range.md) structure specifies the range of Unicode code points.<br/>                                                                                     |



 

 

 





