---
title: Structures
description: DirectWrite defines the following structures.
ms.assetid: 348dd001-bad9-4f1a-a5f5-84b118a5e2d4
keywords:
- DirectWrite,structures
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Structures

DirectWrite defines the following structures.

## In this section



| Topic                                                                                     | Description                                                                                                                                                                                                     |
|-------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**DWRITE\_CARET\_METRICS**](/windows/desktop/api/Dwrite_1/ns-dwrite_1-dwrite_caret_metrics)<br/>                         | The [**DWRITE\_CARET\_METRICS**](/windows/desktop/api/Dwrite_1/ns-dwrite_1-dwrite_caret_metrics) structure specifies the metrics for caret placement in a font.<br/>                                                                            |
| [**DWRITE\_CLUSTER\_METRICS**](/windows/desktop/api/dwrite/ns-dwrite-dwrite_cluster_metrics)<br/>                     | Contains information about a glyph cluster.<br/>                                                                                                                                                          |
| [**DWRITE\_COLOR\_F**](dwrite-color-f.md)<br/>                                     | Describes the red, green, blue, and alpha components of a color.<br/>                                                                                                                                     |
| [**DWRITE\_COLOR\_GLYPH\_RUN**](/windows/desktop/api/DWrite_2/ns-dwrite_2-dwrite_color_glyph_run)<br/>                    | Contains the information needed by renderers to draw glyph runs with glyph color information.<br/>                                                                                                        |
| [**DWRITE\_COLOR\_GLYPH\_RUN1**](/windows/desktop/api/dwrite_3/ns-dwrite_3-dwrite_color_glyph_run1)<br/>                  | Represents a color glyph run. The IDWriteFactory4::TranslateColorGlyphRun method returns an ordered collection of color glyph runs of varying types depending on what the font supports.<br/>             |
| [**DWRITE\_FILE\_FRAGMENT**](/windows/desktop/api/dwrite_3/ns-dwrite_3-dwrite_file_fragment)<br/>                         | Represents a range of bytes in a font file.<br/>                                                                                                                                                          |
| [**DWRITE\_FONT\_FEATURE**](/windows/desktop/api/dwrite/ns-dwrite-dwrite_font_feature)<br/>                           | Specifies properties used to identify and execute typographic features in the current font face.<br/>                                                                                                     |
| [**DWRITE\_FONT\_METRICS**](/windows/desktop/api/dwrite/ns-dwrite-dwrite_font_metrics)<br/>                           | The [**DWRITE\_FONT\_METRICS**](/windows/desktop/api/dwrite/ns-dwrite-dwrite_font_metrics) structure specifies the metrics that are applicable to all glyphs within the font face.<br/>                                                     |
| [**DWRITE\_FONT\_METRICS1**](/windows/desktop/api/Dwrite_1/ns-dwrite_1-dwrite_font_metrics1)<br/>                         | The [**DWRITE\_FONT\_METRICS1**](/windows/desktop/api/Dwrite_1/ns-dwrite_1-dwrite_font_metrics1) structure specifies the metrics that are applicable to all glyphs within the font face.<br/>                                                   |
| [**DWRITE\_FONT\_PROPERTY**](/windows/desktop/api/dwrite_3/ns-dwrite_3-dwrite_font_property)<br/>                         | Font property used for filtering font sets and building a font set with explicit properties.<br/>                                                                                                         |
| [**DWRITE\_GLYPH\_IMAGE\_DATA**](/windows/desktop/api/dwrite_3/ns-dwrite_3-dwrite_glyph_image_data)<br/>                  | Data for a single glyph from GetGlyphImageData.<br/>                                                                                                                                                      |
| [**DWRITE\_GLYPH\_METRICS**](/windows/desktop/api/dwrite/ns-dwrite-dwrite_glyph_metrics)<br/>                         | Specifies the metrics of an individual glyph.<br/>                                                                                                                                                        |
| [**DWRITE\_GLYPH\_OFFSET**](/windows/desktop/api/dwrite/ns-dwrite-dwrite_glyph_offset)<br/>                           | The optional adjustment to a glyph's position.<br/>                                                                                                                                                       |
| [**DWRITE\_GLYPH\_RUN**](/windows/desktop/api/dwrite/ns-dwrite-dwrite_glyph_run)<br/>                                 | Contains the information needed by renderers to draw glyph runs.<br/>                                                                                                                                     |
| [**DWRITE\_GLYPH\_RUN\_DESCRIPTION**](/windows/desktop/api/dwrite/ns-dwrite-dwrite_glyph_run_description)<br/>        | Contains additional properties related to those in [**DWRITE\_GLYPH\_RUN**](/windows/desktop/api/dwrite/ns-dwrite-dwrite_glyph_run).<br/>                                                                                                   |
| [**DWRITE\_HIT\_TEST\_METRICS**](/windows/desktop/api/dwrite/ns-dwrite-dwrite_hit_test_metrics)<br/>                  | Describes the region obtained by a hit test.<br/>                                                                                                                                                         |
| [**DWRITE\_INLINE\_OBJECT\_METRICS**](/windows/desktop/api/dwrite/ns-dwrite-dwrite_inline_object_metrics)<br/>        | Contains properties describing the geometric measurement of an application-defined inline object.<br/>                                                                                                    |
| [**DWRITE\_JUSTIFICATION\_OPPORTUNITY**](/windows/desktop/api/Dwrite_1/ns-dwrite_1-dwrite_justification_opportunity)<br/> | The [**DWRITE\_JUSTIFICATION\_OPPORTUNITY**](/windows/desktop/api/Dwrite_1/ns-dwrite_1-dwrite_justification_opportunity) structure specifies justification info per glyph.<br/>                                                                 |
| [**DWRITE\_LINE\_BREAKPOINT**](/windows/desktop/api/dwrite/ns-dwrite-dwrite_line_breakpoint)<br/>                     | Line breakpoint characteristics of a character.<br/>                                                                                                                                                      |
| [**DWRITE\_LINE\_METRICS**](/windows/desktop/api/dwrite/ns-dwrite-dwrite_line_metrics)<br/>                           | Contains information about a formatted line of text.<br/>                                                                                                                                                 |
| [**DWRITE\_LINE\_METRICS1**](/windows/desktop/api/dwrite_3/ns-dwrite_3-dwrite_line_metrics1)<br/>                         | Contains information about a formatted line of text.<br/>                                                                                                                                                 |
| [**DWRITE\_LINE\_SPACING**](/windows/desktop/api/Dwrite_3/ns-dwrite_3-dwrite_line_spacing)<br/>                           |                                                                                                                                                                                                                 |
| [**DWRITE\_MATRIX**](/windows/desktop/api/dwrite/ns-dwrite-dwrite_matrix)<br/>                                        | The [**DWRITE\_MATRIX**](/windows/desktop/api/dwrite/ns-dwrite-dwrite_matrix) structure specifies the graphics transform to be applied to rendered glyphs.<br/>                                                                             |
| [**DWRITE\_OVERHANG\_METRICS**](/windows/desktop/api/dwrite/ns-dwrite-dwrite_overhang_metrics)<br/>                   | Indicates how much any visible DIPs (device independent pixels) overshoot each side of the layout or inline objects.<br/>                                                                                 |
| [**DWRITE\_PANOSE**](/windows/desktop/api/Dwrite_1/ns-dwrite_1-dwrite_panose)<br/>                                        | The [**DWRITE\_PANOSE**](/windows/desktop/api/Dwrite_1/ns-dwrite_1-dwrite_panose) union describes typeface classification values that you use with [**IDWriteFont1::GetPanose**](https://msdn.microsoft.com/en-us/library/Hh780406(v=VS.85).aspx) to select and match the font.<br/> |
| [**DWRITE\_SCRIPT\_ANALYSIS**](/windows/desktop/api/dwrite/ns-dwrite-dwrite_script_analysis)<br/>                     | Stores the association of text and its writing system script, as well as some display attributes.<br/>                                                                                                    |
| [**DWRITE\_SCRIPT\_PROPERTIES**](/windows/desktop/api/Dwrite_1/ns-dwrite_1-dwrite_script_properties)<br/>                 | The [**DWRITE\_SCRIPT\_PROPERTIES**](/windows/desktop/api/Dwrite_1/ns-dwrite_1-dwrite_script_properties) structure specifies script properties for caret navigation and justification.<br/>                                                     |
| [**DWRITE\_SHAPING\_GLYPH\_PROPERTIES**](/windows/desktop/api/dwrite/ns-dwrite-dwrite_shaping_glyph_properties)<br/>  | Contains shaping output properties for an output glyph.<br/>                                                                                                                                              |
| [**DWRITE\_SHAPING\_TEXT\_PROPERTIES**](/windows/desktop/api/dwrite/ns-dwrite-dwrite_shaping_text_properties)<br/>    | Shaping output properties for an output glyph.<br/>                                                                                                                                                       |
| [**DWRITE\_STRIKETHROUGH**](/windows/desktop/api/dwrite/ns-dwrite-dwrite_strikethrough)<br/>                          | Contains information regarding the size and placement of strikethroughs.<br/>                                                                                                                             |
| [**DWRITE\_TEXT\_METRICS**](/windows/desktop/api/dwrite/ns-dwrite-dwrite_text_metrics)<br/>                           | Contains the metrics associated with text after layout.<br/>                                                                                                                                              |
| [**DWRITE\_TEXT\_METRICS1**](/windows/desktop/api/dwrite_2/ns-dwrite_2-dwrite_text_metrics1)<br/>                         | Contains the metrics associated with text after layout.<br/>                                                                                                                                              |
| [**DWRITE\_TEXT\_RANGE**](/windows/desktop/api/dwrite/ns-dwrite-dwrite_text_range)<br/>                               | Specifies a range of text positions where format is applied in the text represented by an [**IDWriteTextLayout**](https://msdn.microsoft.com/en-us/library/Dd316718(v=VS.85).aspx) object.<br/>                                                     |
| [**DWRITE\_TRIMMING**](/windows/desktop/api/dwrite/ns-dwrite-dwrite_trimming)<br/>                                    | Specifies the trimming option for text overflowing the layout box. <br/>                                                                                                                                  |
| [**DWRITE\_TYPOGRAPHIC\_FEATURES**](/windows/desktop/api/dwrite/ns-dwrite-dwrite_typographic_features)<br/>           | Contains a set of typographic features to be applied during text shaping.<br/>                                                                                                                            |
| [**DWRITE\_UNDERLINE**](/windows/desktop/api/dwrite/ns-dwrite-dwrite_underline)<br/>                                  | Contains information about the width, thickness, offset, run height, reading direction, and flow direction of an underline. <br/>                                                                         |
| [**DWRITE\_UNICODE\_RANGE**](/windows/desktop/api/Dwrite_1/ns-dwrite_1-dwrite_unicode_range)<br/>                         | The [**DWRITE\_UNICODE\_RANGE**](/windows/desktop/api/Dwrite_1/ns-dwrite_1-dwrite_unicode_range) structure specifies the range of Unicode code points.<br/>                                                                                     |



 

 

 





