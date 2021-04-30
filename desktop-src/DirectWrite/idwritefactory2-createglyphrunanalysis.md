---
title: IDWriteFactory2 CreateGlyphRunAnalysis method
description: Creates a glyph run analysis object, which encapsulates information used to render a glyph run.
ms.assetid: 13cecfbf-8bb6-88a2-c8b2-3243f6cb92fd
keywords:
- CreateGlyphRunAnalysis method Direct Write
- CreateGlyphRunAnalysis method Direct Write , IDWriteFactory2 interface
- IDWriteFactory2 interface Direct Write , CreateGlyphRunAnalysis method
topic_type:
- apiref
api_name:
- IDWriteFactory2.CreateGlyphRunAnalysis
api_location:
- dwrite.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IDWriteFactory2::CreateGlyphRunAnalysis method

Creates a glyph run analysis object, which encapsulates information used to render a glyph run.

## Syntax


```C++
virtual HRESULT CreateGlyphRunAnalysis(
  [in]           const DWRITE_GLYPH_RUN           *glyphRun,
  [in, optional] const DWRITE_MATRIX              *transform,
                       DWRITE_RENDERING_MODE      renderingMode,
                       DWRITE_MEASURING_MODE      measuringMode,
                       DWRITE_GRID_FIT_MODE       gridFitMode,
                       DWRITE_TEXT_ANTIALIAS_MODE antialiasMode,
                       FLOAT                      baselineOriginX,
                       FLOAT                      baselineOriginY,
  [out]                IDWriteGlyphRunAnalysis    **glyphRunAnalysis
) = 0;
```



## Parameters

<dl> <dt>

*glyphRun* \[in\]
</dt> <dd>

Type: **const [**DWRITE\_GLYPH\_RUN**](/windows/win32/api/dwrite/ns-dwrite-dwrite_glyph_run)\***

Structure specifying the properties of the glyph run.

</dd> <dt>

*transform* \[in, optional\]
</dt> <dd>

Type: **const [**DWRITE\_MATRIX**](/windows/win32/api/dwrite/ns-dwrite-dwrite_matrix)\***

Optional transform applied to the glyphs and their positions. This transform is applied after the scaling specified by the emSize and pixelsPerDip.

</dd> <dt>

*renderingMode* 
</dt> <dd>

Type: **DWRITE\_RENDERING\_MODE**

Specifies the rendering mode, which must be one of the raster rendering modes (i.e., not default and not outline).

</dd> <dt>

*measuringMode* 
</dt> <dd>

Type: **[**DWRITE\_MEASURING\_MODE**](/windows/win32/api/dcommon/ne-dcommon-dwrite_measuring_mode)**

Specifies the method to measure glyphs.

</dd> <dt>

*gridFitMode* 
</dt> <dd>

Type: **[**DWRITE\_GRID\_FIT\_MODE**](/windows/win32/api/dwrite_2/ne-dwrite_2-dwrite_grid_fit_mode)**

How to grid-fit glyph outlines. This must be non-default.

</dd> <dt>

*antialiasMode* 
</dt> <dd>

Type: **[**DWRITE\_TEXT\_ANTIALIAS\_MODE**](/windows/win32/api/Dwrite_1/ne-dwrite_1-dwrite_text_antialias_mode)**

Specifies the antialias mode.

</dd> <dt>

*baselineOriginX* 
</dt> <dd>

Type: **FLOAT**

Horizontal position of the baseline origin, in DIPs.

</dd> <dt>

*baselineOriginY* 
</dt> <dd>

Type: **FLOAT**

Vertical position of the baseline origin, in DIPs.

</dd> <dt>

*glyphRunAnalysis* \[out\]
</dt> <dd>

Type: **[**IDWriteGlyphRunAnalysis**](/windows/win32/api/dwrite/nn-dwrite-idwriteglyphrunanalysis)\*\***

Receives a pointer to the newly created object.

</dd> </dl>

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1 \[desktop apps \| UWP apps\]<br/>                                     |
| Minimum supported server<br/> | Windows Server 2012 R2 \[desktop apps \| UWP apps\]<br/>                          |
| Minimum supported phone<br/>  | Windows Phone 8.1 \[Windows Phone Silverlight 8.1 and Windows Runtime apps\]<br/> |
| Library<br/>                  | <dl> <dt>Dwrite.lib</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Dwrite.dll</dt> </dl>   |



## See also

<dl> <dt>

[**IDWriteFactory2**](idwritefactory2.md)
</dt> </dl>

 

