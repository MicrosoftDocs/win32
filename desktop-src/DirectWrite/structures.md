---
title: Structures
description: DirectWrite defines the following structures.
ms.assetid: 348dd001-bad9-4f1a-a5f5-84b118a5e2d4
keywords:
- DirectWrite,structures
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Structures

DirectWrite defines the following structures.

## In this section



| Topic                                                                                     | Description                                                                                                                                                                                                     |
|-------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**DWRITE\_CARET\_METRICS**](/windows/win32/Dwrite_1/ns-dwrite_1-dwrite_caret_metrics?branch=master)<br/>                         | The [**DWRITE\_CARET\_METRICS**](/windows/win32/Dwrite_1/ns-dwrite_1-dwrite_caret_metrics?branch=master) structure specifies the metrics for caret placement in a font.<br/>                                                                            |
| [**DWRITE\_CLUSTER\_METRICS**](/windows/win32/dwrite/ns-dwrite-dwrite_cluster_metrics?branch=master)<br/>                     | Contains information about a glyph cluster.<br/>                                                                                                                                                          |
| [**DWRITE\_COLOR\_F**](dwrite-color-f.md)<br/>                                     | Describes the red, green, blue, and alpha components of a color.<br/>                                                                                                                                     |
| [**DWRITE\_COLOR\_GLYPH\_RUN**](/windows/win32/DWrite_2/ns-dwrite_2-dwrite_color_glyph_run?branch=master)<br/>                    | Contains the information needed by renderers to draw glyph runs with glyph color information.<br/>                                                                                                        |
| [**DWRITE\_COLOR\_GLYPH\_RUN1**](/windows/win32/dwrite_3/ns-dwrite_3-dwrite_color_glyph_run1?branch=master)<br/>                  | Represents a color glyph run. The IDWriteFactory4::TranslateColorGlyphRun method returns an ordered collection of color glyph runs of varying types depending on what the font supports.<br/>             |
| [**DWRITE\_FILE\_FRAGMENT**](/windows/win32/dwrite_3/ns-dwrite_3-dwrite_file_fragment?branch=master)<br/>                         | Represents a range of bytes in a font file.<br/>                                                                                                                                                          |
| [**DWRITE\_FONT\_FEATURE**](/windows/win32/dwrite/ns-dwrite-dwrite_font_feature?branch=master)<br/>                           | Specifies properties used to identify and execute typographic features in the current font face.<br/>                                                                                                     |
| [**DWRITE\_FONT\_METRICS**](/windows/win32/dwrite/ns-dwrite-dwrite_font_metrics?branch=master)<br/>                           | The [**DWRITE\_FONT\_METRICS**](/windows/win32/dwrite/ns-dwrite-dwrite_font_metrics?branch=master) structure specifies the metrics that are applicable to all glyphs within the font face.<br/>                                                     |
| [**DWRITE\_FONT\_METRICS1**](/windows/win32/Dwrite_1/ns-dwrite_1-dwrite_font_metrics1?branch=master)<br/>                         | The [**DWRITE\_FONT\_METRICS1**](/windows/win32/Dwrite_1/ns-dwrite_1-dwrite_font_metrics1?branch=master) structure specifies the metrics that are applicable to all glyphs within the font face.<br/>                                                   |
| [**DWRITE\_FONT\_PROPERTY**](/windows/win32/dwrite_3/ns-dwrite_3-dwrite_font_property?branch=master)<br/>                         | Font property used for filtering font sets and building a font set with explicit properties.<br/>                                                                                                         |
| [**DWRITE\_GLYPH\_IMAGE\_DATA**](/windows/win32/dwrite_3/ns-dwrite_3-dwrite_glyph_image_data?branch=master)<br/>                  | Data for a single glyph from GetGlyphImageData.<br/>                                                                                                                                                      |
| [**DWRITE\_GLYPH\_METRICS**](/windows/win32/dwrite/ns-dwrite-dwrite_glyph_metrics?branch=master)<br/>                         | Specifies the metrics of an individual glyph.<br/>                                                                                                                                                        |
| [**DWRITE\_GLYPH\_OFFSET**](/windows/win32/dwrite/ns-dwrite-dwrite_glyph_offset?branch=master)<br/>                           | The optional adjustment to a glyph's position.<br/>                                                                                                                                                       |
| [**DWRITE\_GLYPH\_RUN**](/windows/win32/dwrite/ns-dwrite-dwrite_glyph_run?branch=master)<br/>                                 | Contains the information needed by renderers to draw glyph runs.<br/>                                                                                                                                     |
| [**DWRITE\_GLYPH\_RUN\_DESCRIPTION**](/windows/win32/dwrite/ns-dwrite-dwrite_glyph_run_description?branch=master)<br/>        | Contains additional properties related to those in [**DWRITE\_GLYPH\_RUN**](/windows/win32/dwrite/ns-dwrite-dwrite_glyph_run?branch=master).<br/>                                                                                                   |
| [**DWRITE\_HIT\_TEST\_METRICS**](/windows/win32/dwrite/ns-dwrite-dwrite_hit_test_metrics?branch=master)<br/>                  | Describes the region obtained by a hit test.<br/>                                                                                                                                                         |
| [**DWRITE\_INLINE\_OBJECT\_METRICS**](/windows/win32/dwrite/ns-dwrite-dwrite_inline_object_metrics?branch=master)<br/>        | Contains properties describing the geometric measurement of an application-defined inline object.<br/>                                                                                                    |
| [**DWRITE\_JUSTIFICATION\_OPPORTUNITY**](/windows/win32/Dwrite_1/ns-dwrite_1-dwrite_justification_opportunity?branch=master)<br/> | The [**DWRITE\_JUSTIFICATION\_OPPORTUNITY**](/windows/win32/Dwrite_1/ns-dwrite_1-dwrite_justification_opportunity?branch=master) structure specifies justification info per glyph.<br/>                                                                 |
| [**DWRITE\_LINE\_BREAKPOINT**](/windows/win32/dwrite/ns-dwrite-dwrite_line_breakpoint?branch=master)<br/>                     | Line breakpoint characteristics of a character.<br/>                                                                                                                                                      |
| [**DWRITE\_LINE\_METRICS**](/windows/win32/dwrite/ns-dwrite-dwrite_line_metrics?branch=master)<br/>                           | Contains information about a formatted line of text.<br/>                                                                                                                                                 |
| [**DWRITE\_LINE\_METRICS1**](/windows/win32/dwrite_3/ns-dwrite_3-dwrite_line_metrics1?branch=master)<br/>                         | Contains information about a formatted line of text.<br/>                                                                                                                                                 |
| [**DWRITE\_LINE\_SPACING**](/windows/win32/Dwrite_3/ns-dwrite_3-dwrite_line_spacing?branch=master)<br/>                           |                                                                                                                                                                                                                 |
| [**DWRITE\_MATRIX**](/windows/win32/dwrite/ns-dwrite-dwrite_matrix?branch=master)<br/>                                        | The [**DWRITE\_MATRIX**](/windows/win32/dwrite/ns-dwrite-dwrite_matrix?branch=master) structure specifies the graphics transform to be applied to rendered glyphs.<br/>                                                                             |
| [**DWRITE\_OVERHANG\_METRICS**](/windows/win32/dwrite/ns-dwrite-dwrite_overhang_metrics?branch=master)<br/>                   | Indicates how much any visible DIPs (device independent pixels) overshoot each side of the layout or inline objects.<br/>                                                                                 |
| [**DWRITE\_PANOSE**](/windows/win32/Dwrite_1/ns-dwrite_1-dwrite_panose?branch=master)<br/>                                        | The [**DWRITE\_PANOSE**](/windows/win32/Dwrite_1/ns-dwrite_1-dwrite_panose?branch=master) union describes typeface classification values that you use with [**IDWriteFont1::GetPanose**](/windows/win32/dwrite_1/?branch=master) to select and match the font.<br/> |
| [**DWRITE\_SCRIPT\_ANALYSIS**](/windows/win32/dwrite/ns-dwrite-dwrite_script_analysis?branch=master)<br/>                     | Stores the association of text and its writing system script, as well as some display attributes.<br/>                                                                                                    |
| [**DWRITE\_SCRIPT\_PROPERTIES**](/windows/win32/Dwrite_1/ns-dwrite_1-dwrite_script_properties?branch=master)<br/>                 | The [**DWRITE\_SCRIPT\_PROPERTIES**](/windows/win32/Dwrite_1/ns-dwrite_1-dwrite_script_properties?branch=master) structure specifies script properties for caret navigation and justification.<br/>                                                     |
| [**DWRITE\_SHAPING\_GLYPH\_PROPERTIES**](/windows/win32/dwrite/ns-dwrite-dwrite_shaping_glyph_properties?branch=master)<br/>  | Contains shaping output properties for an output glyph.<br/>                                                                                                                                              |
| [**DWRITE\_SHAPING\_TEXT\_PROPERTIES**](/windows/win32/dwrite/ns-dwrite-dwrite_shaping_text_properties?branch=master)<br/>    | Shaping output properties for an output glyph.<br/>                                                                                                                                                       |
| [**DWRITE\_STRIKETHROUGH**](/windows/win32/dwrite/ns-dwrite-dwrite_strikethrough?branch=master)<br/>                          | Contains information regarding the size and placement of strikethroughs.<br/>                                                                                                                             |
| [**DWRITE\_TEXT\_METRICS**](/windows/win32/dwrite/ns-dwrite-dwrite_text_metrics?branch=master)<br/>                           | Contains the metrics associated with text after layout.<br/>                                                                                                                                              |
| [**DWRITE\_TEXT\_METRICS1**](/windows/win32/dwrite_2/ns-dwrite_2-dwrite_text_metrics1?branch=master)<br/>                         | Contains the metrics associated with text after layout.<br/>                                                                                                                                              |
| [**DWRITE\_TEXT\_RANGE**](/windows/win32/dwrite/ns-dwrite-dwrite_text_range?branch=master)<br/>                               | Specifies a range of text positions where format is applied in the text represented by an [**IDWriteTextLayout**](/windows/win32/dwrite/?branch=master) object.<br/>                                                     |
| [**DWRITE\_TRIMMING**](/windows/win32/dwrite/ns-dwrite-dwrite_trimming?branch=master)<br/>                                    | Specifies the trimming option for text overflowing the layout box. <br/>                                                                                                                                  |
| [**DWRITE\_TYPOGRAPHIC\_FEATURES**](/windows/win32/dwrite/ns-dwrite-dwrite_typographic_features?branch=master)<br/>           | Contains a set of typographic features to be applied during text shaping.<br/>                                                                                                                            |
| [**DWRITE\_UNDERLINE**](/windows/win32/dwrite/ns-dwrite-dwrite_underline?branch=master)<br/>                                  | Contains information about the width, thickness, offset, run height, reading direction, and flow direction of an underline. <br/>                                                                         |
| [**DWRITE\_UNICODE\_RANGE**](/windows/win32/Dwrite_1/ns-dwrite_1-dwrite_unicode_range?branch=master)<br/>                         | The [**DWRITE\_UNICODE\_RANGE**](/windows/win32/Dwrite_1/ns-dwrite_1-dwrite_unicode_range?branch=master) structure specifies the range of Unicode code points.<br/>                                                                                     |



 

 

 





