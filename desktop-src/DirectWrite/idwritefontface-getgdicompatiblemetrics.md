---
title: IDWriteFontFace GetGdiCompatibleMetrics method
description: Obtains design units and common metrics for the font face. These metrics are applicable to all the glyphs within a fontface and are used by applications for layout calculations.
ms.assetid: '9e132ec0-64cb-4681-b079-02a0047badd5'
keywords: ["GetGdiCompatibleMetrics method Direct Write", "GetGdiCompatibleMetrics method Direct Write , IDWriteFontFace interface", "IDWriteFontFace interface Direct Write , GetGdiCompatibleMetrics method"]
topic_type:
- apiref
api_name:
- IDWriteFontFace.GetGdiCompatibleMetrics
api_location:
- dwrite.dll
api_type:
- COM
---

# IDWriteFontFace::GetGdiCompatibleMetrics method

Obtains design units and common metrics for the font face. These metrics are applicable to all the glyphs within a fontface and are used by applications for layout calculations.

## Syntax


```C++
virtual HRESULT GetGdiCompatibleMetrics(
                       FLOAT               emSize,
                       FLOAT               pixelsPerDip,
  [in, optional] const DWRITE_MATRIX       *transform,
  [out]                DWRITE_FONT_METRICS *fontFaceMetrics
) = 0;
```



## Parameters

<dl> <dt>

*emSize* 
</dt> <dd>

Type: **FLOAT**

The logical size of the font in DIP units.

</dd> <dt>

*pixelsPerDip* 
</dt> <dd>

Type: **FLOAT**

The number of physical pixels per DIP.

</dd> <dt>

*transform* \[in, optional\]
</dt> <dd>

Type: **const [**DWRITE\_MATRIX**](dwrite-matrix.md)\***

An optional transform applied to the glyphs and their positions. This transform is applied after the scaling specified by the font size and *pixelsPerDip*.

</dd> <dt>

*fontFaceMetrics* \[out\]
</dt> <dd>

Type: **[**DWRITE\_FONT\_METRICS**](dwrite-font-metrics.md)\***

A pointer to a [**DWRITE\_FONT\_METRIC**](dwrite-font-metrics.md)S structure to fill in. The metrics returned by this function are in font design units.

</dd> </dl>

## Return value

Type: **HRESULT**

Standard HRESULT error code.

## Requirements



|                    |                                                                                       |
|--------------------|---------------------------------------------------------------------------------------|
| Library<br/> | <dl> <dt>Dwrite.lib</dt> </dl> |
| DLL<br/>     | <dl> <dt>Dwrite.dll</dt> </dl> |



## See also

<dl> <dt>

[**IDWriteFontFace**](idwritefontface.md)
</dt> <dt>

[**IDWriteFontFace**](https://msdn.microsoft.com/library/windows/desktop/dd370983)
</dt> </dl>

 

 





