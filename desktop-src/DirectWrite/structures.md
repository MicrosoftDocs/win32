---
title: DirectWrite structures
description: DirectWrite defines the following structures.
ms.assetid: 348dd001-bad9-4f1a-a5f5-84b118a5e2d4
keywords:
- DirectWrite,structures
ms.topic: article
ms.date: 05/31/2018
---

# DirectWrite structures

DirectWrite defines the following structures.

## In this section

| Topic | Description |
|-|-|
| [**DWRITE_BITMAP_DATA_BGRA32**](./dwrite_3/ns-dwrite_3-dwrite_bitmap_data_bgra32.md) | Represents bitmap data in BGRA32 format. |
| [**DWRITE\_CARET\_METRICS**](/windows/win32/api/dwrite_1/ns-dwrite_1-dwrite_caret_metrics) | The [**DWRITE\_CARET\_METRICS**](/windows/win32/api/dwrite_1/ns-dwrite_1-dwrite_caret_metrics) structure specifies the metrics for caret placement in a font. |
| [**DWRITE\_CLUSTER\_METRICS**](/windows/win32/api/dwrite/ns-dwrite-dwrite_cluster_metrics) | Contains information about a glyph cluster. |
| [**DWRITE\_COLOR\_F**](dwrite-color-f.md) | Describes the red, green, blue, and alpha components of a color. |
| [**DWRITE\_COLOR\_GLYPH\_RUN**](/windows/win32/api/DWrite_2/ns-dwrite_2-dwrite_color_glyph_run) | Contains the information needed by renderers to draw glyph runs with glyph color information. |
| [**DWRITE\_COLOR\_GLYPH\_RUN1**](/windows/win32/api/dwrite_3/ns-dwrite_3-dwrite_color_glyph_run1) | Represents a color glyph run. The IDWriteFactory4::TranslateColorGlyphRun method returns an ordered collection of color glyph runs of varying types depending on what the font supports. |
| [**DWRITE\_FILE\_FRAGMENT**](/windows/win32/api/dwrite_3/ns-dwrite_3-dwrite_file_fragment) | Represents a range of bytes in a font file. |
| [**DWRITE_FONT_AXIS_RANGE**](/windows/win32/api/dwrite_3/ns-dwrite_3-dwrite_font_axis_range) | Represents the minimum and maximum range of the possible values for a font axis. |
| [**DWRITE_FONT_AXIS_VALUE**](/windows/win32/api/dwrite_3/ns-dwrite_3-dwrite_font_axis_value) | Represents a value for a font axis. Used when querying and creating font instances. |
| [**DWRITE\_FONT\_FEATURE**](/windows/win32/api/dwrite/ns-dwrite-dwrite_font_feature) | Specifies properties used to identify and execute typographic features in the current font face. |
| [**DWRITE\_FONT\_METRICS**](/windows/win32/api/dwrite/ns-dwrite-dwrite_font_metrics) | The [**DWRITE\_FONT\_METRICS**](/windows/win32/api/dwrite/ns-dwrite-dwrite_font_metrics) structure specifies the metrics that are applicable to all glyphs within the font face. |
| [**DWRITE\_FONT\_METRICS1**](/windows/win32/api/dwrite_1/ns-dwrite_1-dwrite_font_metrics1) | The [**DWRITE\_FONT\_METRICS1**](/windows/win32/api/dwrite_1/ns-dwrite_1-dwrite_font_metrics1) structure specifies the metrics that are applicable to all glyphs within the font face. |
| [**DWRITE\_FONT\_PROPERTY**](/windows/win32/api/dwrite_3/ns-dwrite_3-dwrite_font_property) | Font property used for filtering font sets and building a font set with explicit properties. |
| [**DWRITE\_GLYPH\_IMAGE\_DATA**](/windows/win32/api/dwrite_3/ns-dwrite_3-dwrite_glyph_image_data) | Data for a single glyph from GetGlyphImageData. |
| [**DWRITE\_GLYPH\_METRICS**](/windows/win32/api/dwrite/ns-dwrite-dwrite_glyph_metrics) | Specifies the metrics of an individual glyph. |
| [**DWRITE\_GLYPH\_OFFSET**](/windows/win32/api/dwrite/ns-dwrite-dwrite_glyph_offset) | The optional adjustment to a glyph's position. |
| [**DWRITE\_GLYPH\_RUN**](/windows/win32/api/dwrite/ns-dwrite-dwrite_glyph_run) | Contains the information needed by renderers to draw glyph runs. |
| [**DWRITE\_GLYPH\_RUN\_DESCRIPTION**](/windows/win32/api/dwrite/ns-dwrite-dwrite_glyph_run_description) | Contains additional properties related to those in [**DWRITE\_GLYPH\_RUN**](/windows/win32/api/dwrite/ns-dwrite-dwrite_glyph_run). |
| [**DWRITE\_HIT\_TEST\_METRICS**](/windows/win32/api/dwrite/ns-dwrite-dwrite_hit_test_metrics) | Describes the region obtained by a hit test. |
| [**DWRITE\_INLINE\_OBJECT\_METRICS**](/windows/win32/api/dwrite/ns-dwrite-dwrite_inline_object_metrics) | Contains properties describing the geometric measurement of an application-defined inline object. |
| [**DWRITE\_JUSTIFICATION\_OPPORTUNITY**](/windows/win32/api/dwrite_1/ns-dwrite_1-dwrite_justification_opportunity) | The [**DWRITE\_JUSTIFICATION\_OPPORTUNITY**](/windows/win32/api/dwrite_1/ns-dwrite_1-dwrite_justification_opportunity) structure specifies justification info per glyph. |
| [**DWRITE\_LINE\_BREAKPOINT**](/windows/win32/api/dwrite/ns-dwrite-dwrite_line_breakpoint) | Line breakpoint characteristics of a character. |
| [**DWRITE\_LINE\_METRICS**](/windows/win32/api/dwrite/ns-dwrite-dwrite_line_metrics) | Contains information about a formatted line of text. |
| [**DWRITE\_LINE\_METRICS1**](/windows/win32/api/dwrite_3/ns-dwrite_3-dwrite_line_metrics1) | Contains information about a formatted line of text. |
| [**DWRITE\_LINE\_SPACING**](/windows/win32/api/dwrite_3/ns-dwrite_3-dwrite_line_spacing) | |
| [**DWRITE\_MATRIX**](/windows/win32/api/dwrite/ns-dwrite-dwrite_matrix) | The [**DWRITE\_MATRIX**](/windows/win32/api/dwrite/ns-dwrite-dwrite_matrix) structure specifies the graphics transform to be applied to rendered glyphs. |
| [**DWRITE\_OVERHANG\_METRICS**](/windows/win32/api/dwrite/ns-dwrite-dwrite_overhang_metrics) | Indicates how much any visible DIPs (device independent pixels) overshoot each side of the layout or inline objects. |
| [**DWRITE\_PANOSE**](/windows/win32/api/dwrite_1/ns-dwrite_1-dwrite_panose) | The [**DWRITE\_PANOSE**](/windows/win32/api/dwrite_1/ns-dwrite_1-dwrite_panose) union describes typeface classification values that you use with [**IDWriteFont1::GetPanose**](/windows/win32/api/dwrite_1/nf-dwrite_1-idwritefont1-getpanose) to select and match the font. |
| [**DWRITE\_SCRIPT\_ANALYSIS**](/windows/win32/api/dwrite/ns-dwrite-dwrite_script_analysis) | Stores the association of text and its writing system script, as well as some display attributes. |
| [**DWRITE\_SCRIPT\_PROPERTIES**](/windows/win32/api/dwrite_1/ns-dwrite_1-dwrite_script_properties) | The [**DWRITE\_SCRIPT\_PROPERTIES**](/windows/win32/api/dwrite_1/ns-dwrite_1-dwrite_script_properties) structure specifies script properties for caret navigation and justification. |
| [**DWRITE\_SHAPING\_GLYPH\_PROPERTIES**](/windows/win32/api/dwrite/ns-dwrite-dwrite_shaping_glyph_properties) | Contains shaping output properties for an output glyph. |
| [**DWRITE\_SHAPING\_TEXT\_PROPERTIES**](/windows/win32/api/dwrite/ns-dwrite-dwrite_shaping_text_properties) | Shaping output properties for an output glyph. |
| [**DWRITE\_STRIKETHROUGH**](/windows/win32/api/dwrite/ns-dwrite-dwrite_strikethrough) | Contains information regarding the size and placement of strikethroughs. |
| [**DWRITE\_TEXT\_METRICS**](/windows/win32/api/dwrite/ns-dwrite-dwrite_text_metrics) | Contains the metrics associated with text after layout. |
| [**DWRITE\_TEXT\_METRICS1**](/windows/win32/api/dwrite_2/ns-dwrite_2-dwrite_text_metrics1) | Contains the metrics associated with text after layout. |
| [**DWRITE\_TEXT\_RANGE**](/windows/win32/api/dwrite/ns-dwrite-dwrite_text_range) | Specifies a range of text positions where format is applied in the text represented by an [**IDWriteTextLayout**](/windows/win32/api/dwrite/nn-dwrite-idwritetextlayout) object. |
| [**DWRITE\_TRIMMING**](/windows/win32/api/dwrite/ns-dwrite-dwrite_trimming) | Specifies the trimming option for text overflowing the layout box.  |
| [**DWRITE\_TYPOGRAPHIC\_FEATURES**](/windows/win32/api/dwrite/ns-dwrite-dwrite_typographic_features) | Contains a set of typographic features to be applied during text shaping. |
| [**DWRITE\_UNDERLINE**](/windows/win32/api/dwrite/ns-dwrite-dwrite_underline) | Contains information about the width, thickness, offset, run height, reading direction, and flow direction of an underline.  |
| [**DWRITE\_UNICODE\_RANGE**](/windows/win32/api/dwrite_1/ns-dwrite_1-dwrite_unicode_range) | The [**DWRITE\_UNICODE\_RANGE**](/windows/win32/api/dwrite_1/ns-dwrite_1-dwrite_unicode_range) structure specifies the range of Unicode code points. |



 

