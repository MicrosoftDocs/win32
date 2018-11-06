---
title: Enumerations
description: DirectWrite defines the following enumerations.
ms.assetid: '809ccacd-ff23-4d7b-a177-e7a9937c0c5a'
keywords:
- DirectWrite,enumerations
ms.topic: article
ms.date: 05/31/2018
---

# Enumerations

DirectWrite defines the following enumerations.

## In this section



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Topic</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><a href="/windows/desktop/api/Dwrite_1/ne-dwrite_1-dwrite_baseline"><strong>DWRITE_BASELINE</strong></a><br/></td>
<td>The <a href="/windows/desktop/api/Dwrite_1/ne-dwrite_1-dwrite_baseline"><strong>DWRITE_BASELINE</strong></a> enumeration contains values that specify the baseline for text alignment.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/dwrite/ne-dwrite-dwrite_break_condition"><strong>DWRITE_BREAK_CONDITION</strong></a><br/></td>
<td>Indicates the condition at the edges of inline object or text used to determine line-breaking behavior.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/dwrite_3/ne-dwrite_3-dwrite_container_type"><strong>DWRITE_CONTAINER_TYPE</strong></a><br/></td>
<td>Specifies the container format of a font resource. A container format is distinct from a font file format (DWRITE_FONT_FILE_TYPE) because the container describes the container in which the underlying font file is packaged. <br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/dwrite/ne-dwrite-dwrite_factory_type"><strong>DWRITE_FACTORY_TYPE</strong></a><br/></td>
<td>Specifies the type of DirectWrite factory object.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/dwrite/ne-dwrite-dwrite_flow_direction"><strong>DWRITE_FLOW_DIRECTION</strong></a><br/></td>
<td>Indicates the direction of how lines of text are placed relative to one another. <br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/dwrite/ne-dwrite-dwrite_font_face_type"><strong>DWRITE_FONT_FACE_TYPE</strong></a><br/></td>
<td>Indicates the file format of a complete font face.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/dwrite/ne-dwrite-dwrite_font_feature_tag"><strong>DWRITE_FONT_FEATURE_TAG</strong></a><br/></td>
<td>A value that indicates the typographic feature of text supplied by the font.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/dwrite/ne-dwrite-dwrite_font_file_type"><strong>DWRITE_FONT_FILE_TYPE</strong></a><br/></td>
<td>The type of a font represented by a single font file. Font formats that consist of multiple files, for example Type 1 .PFM and .PFB, have separate enum values for each of the file types.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/dwrite_3/ne-dwrite_3-dwrite_font_line_gap_usage"><strong>DWRITE_FONT_LINE_GAP_USAGE</strong></a><br/></td>
<td>Specify whether <a href="/windows/desktop/api/dwrite/ns-dwrite-dwrite_font_metrics"><strong>DWRITE_FONT_METRICS</strong></a>::lineGap value should be part of the line metrics<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/dwrite_3/ne-dwrite_3-dwrite_font_property_id"><strong>DWRITE_FONT_PROPERTY_ID</strong></a><br/></td>
<td>Identifies a string in a font.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/dwrite/ne-dwrite-dwrite_font_simulations"><strong>DWRITE_FONT_SIMULATIONS</strong></a><br/></td>
<td>Specifies algorithmic style simulations to be applied to the font face. Bold and oblique simulations can be combined via bitwise OR operation.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/dwrite/ne-dwrite-dwrite_font_stretch"><strong>DWRITE_FONT_STRETCH</strong></a><br/></td>
<td>Represents the degree to which a font has been stretched compared to a font's normal aspect ratio.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/dwrite/ne-dwrite-dwrite_font_style"><strong>DWRITE_FONT_STYLE</strong></a><br/></td>
<td>Represents the style of a font face as normal, italic, or oblique.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/dwrite/ne-dwrite-dwrite_font_weight"><strong>DWRITE_FONT_WEIGHT</strong></a><br/></td>
<td>Represents the density of a typeface, in terms of the lightness or heaviness of the strokes.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/dcommon/ne-dcommon-dwrite_glyph_image_formats"><strong>DWRITE_GLYPH_IMAGE_FORMATS</strong></a><br/></td>
<td>Specifies which formats are supported in the font, either at a font-wide level or per glyph.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/Dwrite_1/ne-dwrite_1-dwrite_glyph_orientation_angle"><strong>DWRITE_GLYPH_ORIENTATION_ANGLE</strong></a><br/></td>
<td>The <a href="/windows/desktop/api/Dwrite_1/ne-dwrite_1-dwrite_glyph_orientation_angle"><strong>DWRITE_GLYPH_ORIENTATION_ANGLE</strong></a> enumeration contains values that specify how the glyph is oriented to the x-axis.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/dwrite_2/ne-dwrite_2-dwrite_grid_fit_mode"><strong>DWRITE_GRID_FIT_MODE</strong></a><br/></td>
<td>Specifies whether to enable grid-fitting of glyph outlines (also known as hinting).<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/dwrite/ne-dwrite-dwrite_informational_string_id"><strong>DWRITE_INFORMATIONAL_STRING_ID</strong></a><br/></td>
<td>The informational string enumeration which identifies a string embedded in a font file.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/dwrite/ne-dwrite-dwrite_line_spacing_method"><strong>DWRITE_LINE_SPACING_METHOD</strong></a><br/></td>
<td>The method used for line spacing in a text layout.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/dwrite_3/ne-dwrite_3-dwrite_locality"><strong>DWRITE_LOCALITY</strong></a><br/></td>
<td>Specifies the location of a resource.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/dcommon/ne-dcommon-dwrite_measuring_mode"><strong>DWRITE_MEASURING_MODE</strong></a><br/></td>
<td>Indicates the measuring method used for text layout.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/dwrite/ne-dwrite-dwrite_number_substitution_method"><strong>DWRITE_NUMBER_SUBSTITUTION_METHOD</strong></a><br/></td>
<td>Specifies how to apply number substitution on digits and related punctuation.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/dwrite_2/ne-dwrite_2-dwrite_optical_alignment"><strong>DWRITE_OPTICAL_ALIGNMENT</strong></a><br/></td>
<td>The optical margin alignment mode.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/Dwrite_1/ne-dwrite_1-dwrite_outline_threshold"><strong>DWRITE_OUTLINE_THRESHOLD</strong></a><br/></td>
<td>The <a href="/windows/desktop/api/Dwrite_1/ne-dwrite_1-dwrite_outline_threshold"><strong>DWRITE_OUTLINE_THRESHOLD</strong></a> enumeration contains values that specify the policy used by the <a href="https://msdn.microsoft.com/library/windows/desktop/dd371015"><strong>IDWriteFontFace1::GetRecommendedRenderingMode</strong></a> method to determine whether to render glyphs in outline mode.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/Dwrite_1/ne-dwrite_1-dwrite_panose_arm_style"><strong>DWRITE_PANOSE_ARM_STYLE</strong></a><br/></td>
<td>The <a href="/windows/desktop/api/Dwrite_1/ne-dwrite_1-dwrite_panose_arm_style"><strong>DWRITE_PANOSE_ARM_STYLE</strong></a> enumeration contains values that specify the style of termination of stems and rounded letterforms for text.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/Dwrite_1/ne-dwrite_1-dwrite_panose_aspect"><strong>DWRITE_PANOSE_ASPECT</strong></a><br/></td>
<td>The <a href="/windows/desktop/api/Dwrite_1/ne-dwrite_1-dwrite_panose_aspect"><strong>DWRITE_PANOSE_ASPECT</strong></a> enumeration contains values that specify the ratio between the width and height of the character face.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/Dwrite_1/ne-dwrite_1-dwrite_panose_aspect_ratio"><strong>DWRITE_PANOSE_ASPECT_RATIO</strong></a><br/></td>
<td>The <a href="/windows/desktop/api/Dwrite_1/ne-dwrite_1-dwrite_panose_aspect_ratio"><strong>DWRITE_PANOSE_ASPECT_RATIO</strong></a> enumeration contains values that specify info about the ratio between width and height of the character face.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/Dwrite_1/ne-dwrite_1-dwrite_panose_character_ranges"><strong>DWRITE_PANOSE_CHARACTER_RANGES</strong></a><br/></td>
<td>The <a href="/windows/desktop/api/Dwrite_1/ne-dwrite_1-dwrite_panose_character_ranges"><strong>DWRITE_PANOSE_CHARACTER_RANGES</strong></a> enumeration contains values that specify the type of characters available in the font.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/Dwrite_1/ne-dwrite_1-dwrite_panose_contrast"><strong>DWRITE_PANOSE_CONTRAST</strong></a><br/></td>
<td>The <a href="/windows/desktop/api/Dwrite_1/ne-dwrite_1-dwrite_panose_contrast"><strong>DWRITE_PANOSE_CONTRAST</strong></a> enumeration contains values that specify the ratio between thickest and thinnest point of the stroke for a letter such as uppercase 'O'.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/Dwrite_1/ne-dwrite_1-dwrite_panose_decorative_class"><strong>DWRITE_PANOSE_DECORATIVE_CLASS</strong></a><br/></td>
<td>The <a href="/windows/desktop/api/Dwrite_1/ne-dwrite_1-dwrite_panose_decorative_class"><strong>DWRITE_PANOSE_DECORATIVE_CLASS</strong></a> enumeration contains values that specify the general look of the character face.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/Dwrite_1/ne-dwrite_1-dwrite_panose_decorative_topology"><strong>DWRITE_PANOSE_DECORATIVE_TOPOLOGY</strong></a><br/></td>
<td>The <a href="/windows/desktop/api/Dwrite_1/ne-dwrite_1-dwrite_panose_decorative_topology"><strong>DWRITE_PANOSE_DECORATIVE_TOPOLOGY</strong></a> enumeration contains values that specify the overall shape characteristics of the font.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/Dwrite_1/ne-dwrite_1-dwrite_panose_family"><strong>DWRITE_PANOSE_FAMILY</strong></a><br/></td>
<td>The <a href="/windows/desktop/api/Dwrite_1/ne-dwrite_1-dwrite_panose_family"><strong>DWRITE_PANOSE_FAMILY</strong></a> enumeration contains values that specify the kind of typeface classification.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/Dwrite_1/ne-dwrite_1-dwrite_panose_fill"><strong>DWRITE_PANOSE_FILL</strong></a><br/></td>
<td>The <a href="/windows/desktop/api/Dwrite_1/ne-dwrite_1-dwrite_panose_fill"><strong>DWRITE_PANOSE_FILL</strong></a> enumeration contains values that specify the type of fill and line treatment.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/Dwrite_1/ne-dwrite_1-dwrite_panose_finials"><strong>DWRITE_PANOSE_FINIALS</strong></a><br/></td>
<td>The <a href="/windows/desktop/api/Dwrite_1/ne-dwrite_1-dwrite_panose_finials"><strong>DWRITE_PANOSE_FINIALS</strong></a> enumeration contains values that specify how character ends and miniscule ascenders are treated.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/Dwrite_1/ne-dwrite_1-dwrite_panose_letterform"><strong>DWRITE_PANOSE_LETTERFORM</strong></a><br/></td>
<td>The <a href="/windows/desktop/api/Dwrite_1/ne-dwrite_1-dwrite_panose_letterform"><strong>DWRITE_PANOSE_LETTERFORM</strong></a> enumeration contains values that specify the roundness of letterform for text.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/Dwrite_1/ne-dwrite_1-dwrite_panose_lining"><strong>DWRITE_PANOSE_LINING</strong></a><br/></td>
<td>The <a href="/windows/desktop/api/Dwrite_1/ne-dwrite_1-dwrite_panose_lining"><strong>DWRITE_PANOSE_LINING</strong></a> enumeration contains values that specify the handling of the outline for the decorative typeface.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/Dwrite_1/ne-dwrite_1-dwrite_panose_midline"><strong>DWRITE_PANOSE_MIDLINE</strong></a><br/></td>
<td>The <a href="/windows/desktop/api/Dwrite_1/ne-dwrite_1-dwrite_panose_midline"><strong>DWRITE_PANOSE_MIDLINE</strong></a> enumeration contains values that specify info about the placement of midline across uppercase characters and the treatment of diagonal stem apexes.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/Dwrite_1/ne-dwrite_1-dwrite_panose_proportion"><strong>DWRITE_PANOSE_PROPORTION</strong></a><br/></td>
<td>The <a href="/windows/desktop/api/Dwrite_1/ne-dwrite_1-dwrite_panose_proportion"><strong>DWRITE_PANOSE_PROPORTION</strong></a> enumeration contains values that specify the proportion of the glyph shape by considering additional detail to standard characters.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/Dwrite_1/ne-dwrite_1-dwrite_panose_script_form"><strong>DWRITE_PANOSE_SCRIPT_FORM</strong></a><br/></td>
<td>The <a href="/windows/desktop/api/Dwrite_1/ne-dwrite_1-dwrite_panose_script_form"><strong>DWRITE_PANOSE_SCRIPT_FORM</strong></a> enumeration contains values that specify the general look of the character face, with consideration of its slope and tails.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/Dwrite_1/ne-dwrite_1-dwrite_panose_script_topology"><strong>DWRITE_PANOSE_SCRIPT_TOPOLOGY</strong></a><br/></td>
<td>The <a href="/windows/desktop/api/Dwrite_1/ne-dwrite_1-dwrite_panose_script_topology"><strong>DWRITE_PANOSE_SCRIPT_TOPOLOGY</strong></a> enumeration contains values that specify the topology of letterforms.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/Dwrite_1/ne-dwrite_1-dwrite_panose_serif_style"><strong>DWRITE_PANOSE_SERIF_STYLE</strong></a><br/></td>
<td>The <a href="/windows/desktop/api/Dwrite_1/ne-dwrite_1-dwrite_panose_serif_style"><strong>DWRITE_PANOSE_SERIF_STYLE</strong></a> enumeration contains values that specify the appearance of the serif text.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/Dwrite_1/ne-dwrite_1-dwrite_panose_spacing"><strong>DWRITE_PANOSE_SPACING</strong></a><br/></td>
<td>The <a href="/windows/desktop/api/Dwrite_1/ne-dwrite_1-dwrite_panose_spacing"><strong>DWRITE_PANOSE_SPACING</strong></a> enumeration contains values that specify character spacing (monospace versus proportional).<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/Dwrite_1/ne-dwrite_1-dwrite_panose_stroke_variation"><strong>DWRITE_PANOSE_STROKE_VARIATION</strong></a><br/></td>
<td>The <a href="/windows/desktop/api/Dwrite_1/ne-dwrite_1-dwrite_panose_stroke_variation"><strong>DWRITE_PANOSE_STROKE_VARIATION</strong></a> enumeration contains values that specify the relationship between thin and thick stems of text characters.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/Dwrite_1/ne-dwrite_1-dwrite_panose_symbol_aspect_ratio"><strong>DWRITE_PANOSE_SYMBOL_ASPECT_RATIO</strong></a><br/></td>
<td>The <a href="/windows/desktop/api/Dwrite_1/ne-dwrite_1-dwrite_panose_symbol_aspect_ratio"><strong>DWRITE_PANOSE_SYMBOL_ASPECT_RATIO</strong></a> enumeration contains values that specify the aspect ratio of symbolic characters.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/Dwrite_1/ne-dwrite_1-dwrite_panose_symbol_kind"><strong>DWRITE_PANOSE_SYMBOL_KIND</strong></a><br/></td>
<td>The <a href="/windows/desktop/api/Dwrite_1/ne-dwrite_1-dwrite_panose_symbol_kind"><strong>DWRITE_PANOSE_SYMBOL_KIND</strong></a> enumeration contains values that specify the kind of symbol set.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/Dwrite_1/ne-dwrite_1-dwrite_panose_tool_kind"><strong>DWRITE_PANOSE_TOOL_KIND</strong></a><br/></td>
<td>The <a href="/windows/desktop/api/Dwrite_1/ne-dwrite_1-dwrite_panose_tool_kind"><strong>DWRITE_PANOSE_TOOL_KIND</strong></a> enumeration contains values that specify the kind of tool that is used to create character forms.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/Dwrite_1/ne-dwrite_1-dwrite_panose_weight"><strong>DWRITE_PANOSE_WEIGHT</strong></a><br/></td>
<td>The <a href="/windows/desktop/api/Dwrite_1/ne-dwrite_1-dwrite_panose_weight"><strong>DWRITE_PANOSE_WEIGHT</strong></a> enumeration contains values that specify the weight of characters.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/Dwrite_1/ne-dwrite_1-dwrite_panose_xascent"><strong>DWRITE_PANOSE_XASCENT</strong></a><br/></td>
<td>The <a href="/windows/desktop/api/Dwrite_1/ne-dwrite_1-dwrite_panose_xascent"><strong>DWRITE_PANOSE_XASCENT</strong></a> enumeration contains values that specify the relative size of the lowercase letters.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/Dwrite_1/ne-dwrite_1-dwrite_panose_xheight"><strong>DWRITE_PANOSE_XHEIGHT</strong></a><br/></td>
<td>The <a href="/windows/desktop/api/Dwrite_1/ne-dwrite_1-dwrite_panose_xheight"><strong>DWRITE_PANOSE_XHEIGHT</strong></a> enumeration contains values that specify info about the relative size of lowercase letters and the treatment of diacritic marks (xheight).<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/dwrite/ne-dwrite-dwrite_paragraph_alignment"><strong>DWRITE_PARAGRAPH_ALIGNMENT</strong></a><br/></td>
<td>Specifies the alignment of paragraph text along the flow direction axis, relative to the top and bottom of the flow's layout box. <br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/dwrite/ne-dwrite-dwrite_pixel_geometry"><strong>DWRITE_PIXEL_GEOMETRY</strong></a><br/></td>
<td>Represents the internal structure of a device pixel (that is, the physical arrangement of red, green, and blue color components) that is assumed for purposes of rendering text. <br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/dwrite/ne-dwrite-dwrite_reading_direction"><strong>DWRITE_READING_DIRECTION</strong></a><br/></td>
<td>Specifies the direction in which reading progresses. <br/>
<blockquote>
[!Note]<br />
<strong>DWRITE_READING_DIRECTION_TOP_TO_BOTTOM</strong> and <strong>DWRITE_READING_DIRECTION_BOTTOM_TO_TOP</strong> are available in Windows 8.1 and later, only.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td><a href="dwrite-rendering-mode-enumerations">DWRITE_RENDERING_MODE enumerations</a><br/></td>
<td>Starting in Windows 8, the <strong>DWRITE_RENDERING_MODE</strong> enumeration added new enumeration values and deprecated others.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/dwrite_3/ne-dwrite_3-dwrite_rendering_mode1"><strong>DWRITE_RENDERING_MODE1</strong></a><br/></td>
<td>Specifies how glyphs are rendered.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/dwrite/ne-dwrite-dwrite_script_shapes"><strong>DWRITE_SCRIPT_SHAPES</strong></a><br/></td>
<td>Indicates additional shaping requirements for text.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/dwrite/ne-dwrite-dwrite_text_alignment"><strong>DWRITE_TEXT_ALIGNMENT</strong></a><br/></td>
<td>Specifies the alignment of paragraph text along the reading direction axis, relative to the leading and trailing edge of the layout box.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/Dwrite_1/ne-dwrite_1-dwrite_text_antialias_mode"><strong>DWRITE_TEXT_ANTIALIAS_MODE</strong></a><br/></td>
<td>The <a href="/windows/desktop/api/Dwrite_1/ne-dwrite_1-dwrite_text_antialias_mode"><strong>DWRITE_TEXT_ANTIALIAS_MODE</strong></a> enumeration contains values that specify the type of antialiasing to use for text when the rendering mode calls for antialiasing.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/dwrite/ne-dwrite-dwrite_texture_type"><strong>DWRITE_TEXTURE_TYPE</strong></a><br/></td>
<td>Identifies a type of alpha texture.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/dwrite/ne-dwrite-dwrite_trimming_granularity"><strong>DWRITE_TRIMMING_GRANULARITY</strong></a><br/></td>
<td>Specifies the text granularity used to trim text overflowing the layout box.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/Dwrite_1/ne-dwrite_1-dwrite_vertical_glyph_orientation"><strong>DWRITE_VERTICAL_GLYPH_ORIENTATION</strong></a><br/></td>
<td>The <a href="/windows/desktop/api/Dwrite_1/ne-dwrite_1-dwrite_vertical_glyph_orientation"><strong>DWRITE_VERTICAL_GLYPH_ORIENTATION</strong></a> enumeration contains values that specify the desired kind of glyph orientation for the text.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/dwrite/ne-dwrite-dwrite_word_wrapping"><strong>DWRITE_WORD_WRAPPING</strong></a><br/></td>
<td>Specifies the word wrapping to be used in a particular multiline paragraph. <br/>
<blockquote>
[!Note]<br />
<strong>DWRITE_WORD_WRAPPING_EMERGENCY_BREAK</strong>, <strong>DWRITE_WORD_WRAPPING_WHOLE _WORD</strong>, and <strong>DWRITE_WORD_WRAPPING_CHARACTER</strong> are available in Windows 8.1 and later, only.
</blockquote>
<br/></td>
</tr>
</tbody>
</table>



 

 

 





