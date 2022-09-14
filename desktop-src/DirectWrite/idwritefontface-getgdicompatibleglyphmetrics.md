---
title: IDWriteFontFace GetGdiCompatibleGlyphMetrics method
description: Obtains glyph metrics in font design units with the return values compatible with what GDI would produce.
ms.assetid: 7bda3916-6db3-4f56-b18c-288506c0b646
keywords:
- GetGdiCompatibleGlyphMetrics method Direct Write
- GetGdiCompatibleGlyphMetrics method Direct Write , IDWriteFontFace interface
- IDWriteFontFace interface Direct Write , GetGdiCompatibleGlyphMetrics method
topic_type:
- apiref
api_name:
- IDWriteFontFace.GetGdiCompatibleGlyphMetrics
api_location:
- dwrite.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IDWriteFontFace::GetGdiCompatibleGlyphMetrics method

Obtains glyph metrics in font design units with the return values compatible with what GDI would produce.

## Syntax


```C++
virtual HRESULT GetGdiCompatibleGlyphMetrics(
                       FLOAT                emSize,
                       FLOAT                pixelsPerDip,
  [in, optional] const DWRITE_MATRIX        *transform,
                       BOOL                 useGdiNatural,
  [in]           const UINT16               *glyphIndices,
                       UINT32               glyphCount,
  [out]                DWRITE_GLYPH_METRICS *glyphMetrics,
                       BOOL                 isSideways = FALSE
) = 0;
```



## Parameters

<dl> <dt>

*emSize* 
</dt> <dd>

Type: **FLOAT**

The ogical size of the font in DIP units.

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

*glyphIndices* \[in\]
</dt> <dd>

Type: **const UINT16\***

An array of glyph indices for which to compute the metrics.

</dd> <dt>

*glyphCount* 
</dt> <dd>

Type: **UINT32**

The number of elements in the *glyphIndices* array.

</dd> <dt>

*glyphMetrics* \[out\]
</dt> <dd>

Type: **[**DWRITE\_GLYPH\_METRICS**](/windows/win32/api/dwrite/ns-dwrite-dwrite_glyph_metrics)\***

An array of [**DWRITE\_GLYPH\_METRICS**](/windows/win32/api/dwrite/ns-dwrite-dwrite_glyph_metrics) structures filled by this function. The metrics are in font design units.

</dd> <dt>

*isSideways* 
</dt> <dd>

Type: **BOOL**

A BOOL value that indicates whether the font is being used in a sideways run. This can affect the glyph metrics if the font has oblique simulation because sideways oblique simulation differs from non-sideways oblique simulation.

</dd> </dl>

## Return value

Type: **HRESULT**

Standard **HRESULT** error code. If any of the input glyph indices are outside of the valid glyph index range for the current font face, **E\_INVALIDARG** will be returned.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------|
| Library<br/> | <dl> <dt>Dwrite.lib</dt> </dl> |
| DLL<br/>     | <dl> <dt>Dwrite.dll</dt> </dl> |



## See also

<dl> <dt>

[**IDWriteFontFace**](/windows/win32/api/dwrite/nn-dwrite-idwritefontface)
</dt> <dt>

[**IDWriteFontFace**](/windows/win32/api/dwrite/nn-dwrite-idwritefontface)
</dt> </dl>

 

