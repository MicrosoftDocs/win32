---
title: IDWriteTextAnalyzer GetGdiCompatibleGlyphPlacements method
description: Place glyphs output from the GetGlyphs method according to the font and the writing system's rendering rules.
ms.assetid: 49312b03-9ee9-44ef-b3eb-a35631a6e693
keywords:
- GetGdiCompatibleGlyphPlacements method Direct Write
- GetGdiCompatibleGlyphPlacements method Direct Write , IDWriteTextAnalyzer interface
- IDWriteTextAnalyzer interface Direct Write , GetGdiCompatibleGlyphPlacements method
topic_type:
- apiref
api_name:
- IDWriteTextAnalyzer.GetGdiCompatibleGlyphPlacements
api_location:
- dwrite.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IDWriteTextAnalyzer::GetGdiCompatibleGlyphPlacements method

Place glyphs output from the [**GetGlyphs**](/windows/win32/api/dwrite/nf-dwrite-idwritetextanalyzer-getglyphs) method according to the font and the writing system's rendering rules.

## Syntax


```C++
virtual HRESULT GetGdiCompatibleGlyphPlacements(
  [in]           const WCHAR                           *textString,
  [in]           const UINT16                          *clusterMap,
  [in]                 DWRITE_SHAPING_TEXT_PROPERTIES  *textProps,
                       UINT32                          textLength,
  [in]           const UINT16                          *glyphIndices,
  [in]           const DWRITE_SHAPING_GLYPH_PROPERTIES *glyphProps,
                       UINT32                          glyphCount,
  [in]                 IDWriteFontFace                 *fontFace,
                       FLOAT                           fontEmSize,
                       FLOAT                           pixelsPerDip,
  [in, optional] const DWRITE_MATRIX                   *transform,
                       BOOL                            useGdiNatural,
                       BOOL                             isSideways,
                       BOOL                             isRightToLeft,
  [in]           const DWRITE_SCRIPT_ANALYSIS          * scriptAnalysis,
  [in, optional] const WCHAR                           * localeName,
  [in, optional] const DWRITE_TYPOGRAPHIC_FEATURES     ** features,
  [in, optional] const UINT32                          * featureRangeLengths,
                       UINT32                           featureRanges,
  [out]                FLOAT                           * glyphAdvances,
  [out]                DWRITE_GLYPH_OFFSET             * glyphOffsets
) = 0;
```



## Parameters

<dl> <dt>

*textString* \[in\]
</dt> <dd>

Type: **const WCHAR\***

An array of characters containing the original string from which the glyphs came.

</dd> <dt>

*clusterMap* \[in\]
</dt> <dd>

Type: **const UINT16\***

A pointer to the mapping from character ranges to glyph ranges. This is returned by [**GetGlyphs**](/windows/win32/api/dwrite/nf-dwrite-idwritetextanalyzer-getglyphs).

</dd> <dt>

*textProps* \[in\]
</dt> <dd>

Type: **[**DWRITE\_SHAPING\_TEXT\_PROPERTIES**](/windows/win32/api/dwrite/ns-dwrite-dwrite_shaping_text_properties)\***

A pointer to an array of structures that contains shaping properties for each character. This structure is returned by [**GetGlyphs**](/windows/win32/api/dwrite/nf-dwrite-idwritetextanalyzer-getglyphs).

</dd> <dt>

*textLength* 
</dt> <dd>

Type: **UINT32**

The text length of *textString*.

</dd> <dt>

*glyphIndices* \[in\]
</dt> <dd>

Type: **const UINT16\***

An array of glyph indices returned by [**GetGlyphs**](/windows/win32/api/dwrite/nf-dwrite-idwritetextanalyzer-getglyphs).

</dd> <dt>

*glyphProps* \[in\]
</dt> <dd>

Type: **const [**DWRITE\_SHAPING\_GLYPH\_PROPERTIES**](/windows/win32/api/dwrite/ns-dwrite-dwrite_shaping_glyph_properties)\***

A pointer to an array of structures that contain shaping properties for each glyph returned by [**GetGlyphs**](/windows/win32/api/dwrite/nf-dwrite-idwritetextanalyzer-getglyphs).

</dd> <dt>

*glyphCount* 
</dt> <dd>

Type: **UINT32**

The number of glyphs returned from [**GetGlyphs**](/windows/win32/api/dwrite/nf-dwrite-idwritetextanalyzer-getglyphs).

</dd> <dt>

*fontFace* \[in\]
</dt> <dd>

Type: **[**IDWriteFontFace**](/windows/win32/api/dwrite/nn-dwrite-idwritefontface)\***

A pointer to the font face that is the source for the output glyphs.

</dd> <dt>

*fontEmSize* 
</dt> <dd>

Type: **FLOAT**

The logical font size in DIPs.

</dd> <dt>

*pixelsPerDip* 
</dt> <dd>

Type: **FLOAT**

The number of physical pixels per DIP.

</dd> <dt>

*transform* \[in, optional\]
</dt> <dd>

Type: **const [**DWRITE\_MATRIX**](/windows/win32/api/dwrite/ns-dwrite-dwrite_matrix)\***

An optional transform applied to the glyphs and their positions. This transform is applied after the scaling specified by the font size and *pixelsPerDip*.

</dd> <dt>

*useGdiNatural* 
</dt> <dd>

Type: **BOOL**

When set to **FALSE**, the metrics are the same as the metrics of GDI aliased text. When set to **TRUE**, the metrics are the same as the metrics of text measured by GDI using a font created with **CLEARTYPE\_NATURAL\_QUALITY**.

</dd> <dt>

 *isSideways* 
</dt> <dd>

Type: **BOOL**

A Boolean flag set to **TRUE** if the text is intended to be drawn vertically.

</dd> <dt>

 *isRightToLeft* 
</dt> <dd>

Type: **BOOL**

A Boolean flag set to **TRUE** for right-to-left text.

</dd> <dt>

 *scriptAnalysis* \[in\]
</dt> <dd>

Type: **const [**DWRITE\_SCRIPT\_ANALYSIS**](/windows/win32/api/dwrite/ns-dwrite-dwrite_script_analysis)\***

A pointer to a Script analysis result from an[**AnalyzeScript**](/windows/win32/api/dwrite/nf-dwrite-idwritetextanalyzer-analyzescript) call.

</dd> <dt>

 *localeName* \[in, optional\]
</dt> <dd>

Type: **const WCHAR\***

An array of characters containing the locale to use when selecting glyphs. For example, the same character may map to different glyphs for ja-jp versus zh-chs. If this is **NULL**, then the default mapping based on the script is used.

</dd> <dt>

 *features* \[in, optional\]
</dt> <dd>

Type: **const [**DWRITE\_TYPOGRAPHIC\_FEATURES**](/windows/win32/api/dwrite/ns-dwrite-dwrite_typographic_features)\*\***

An array of pointers to the sets of typographic features to use in each feature range.

</dd> <dt>

 *featureRangeLengths* \[in, optional\]
</dt> <dd>

Type: **const UINT32\***

The length of each feature range, in characters. The sum of all lengths should be equal to *textLength*.

</dd> <dt>

 *featureRanges* 
</dt> <dd>

Type: **UINT32**

The number of feature ranges.

</dd> <dt>

 *glyphAdvances* \[out\]
</dt> <dd>

Type: **FLOAT\***

When this method returns, contains the advance width of each glyph.

</dd> <dt>

 *glyphOffsets* \[out\]
</dt> <dd>

Type: **[**DWRITE\_GLYPH\_OFFSET**](/windows/win32/api/dwrite/ns-dwrite-dwrite_glyph_offset)\***

When this method returns, contains the offset of the origin of each glyph.

</dd> </dl>

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------|
| Library<br/> | <dl> <dt>Dwrite.lib</dt> </dl> |
| DLL<br/>     | <dl> <dt>Dwrite.dll</dt> </dl> |



## See also

<dl> <dt>

[**IDWriteTextAnalyzer**](/windows/win32/api/dwrite/nn-dwrite-idwritetextanalyzer)
</dt> </dl>

 

