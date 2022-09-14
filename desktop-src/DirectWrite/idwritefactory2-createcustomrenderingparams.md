---
title: IDWriteFactory2 CreateCustomRenderingParams method
description: Creates a rendering parameters object with the specified properties.
ms.assetid: 947d50fd-888c-2f0b-25c2-b19b0e6fad58
keywords:
- CreateCustomRenderingParams method Direct Write
- CreateCustomRenderingParams method Direct Write , IDWriteFactory2 interface
- IDWriteFactory2 interface Direct Write , CreateCustomRenderingParams method
topic_type:
- apiref
api_name:
- IDWriteFactory2.CreateCustomRenderingParams
api_location:
- dwrite.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IDWriteFactory2::CreateCustomRenderingParams method

Creates a rendering parameters object with the specified properties.

## Syntax


```C++
virtual HRESULT CreateCustomRenderingParams(
        FLOAT                   gamma,
        FLOAT                   enhancedContrast,
        FLOAT                   grayscaleEnhancedContrast,
        FLOAT                   clearTypeLevel,
        DWRITE_PIXEL_GEOMETRY   pixelGeometry,
        DWRITE_RENDERING_MODE   renderingMode,
        DWRITE_GRID_FIT_MODE    gridFitMode,
  [out] IDWriteRenderingParams2 **renderingParams
) = 0;
```



## Parameters

<dl> <dt>

*gamma* 
</dt> <dd>

Type: **FLOAT**

The gamma value used for gamma correction, which must be greater than zero and cannot exceed 256.

</dd> <dt>

*enhancedContrast* 
</dt> <dd>

Type: **FLOAT**

The amount of contrast enhancement, zero or greater.

</dd> <dt>

*grayscaleEnhancedContrast* 
</dt> <dd>

Type: **FLOAT**

The amount of contrast enhancement, zero or greater.

</dd> <dt>

*clearTypeLevel* 
</dt> <dd>

Type: **FLOAT**

The degree of ClearType level, from 0.0f (no ClearType) to 1.0f (full ClearType).

</dd> <dt>

*pixelGeometry* 
</dt> <dd>

Type: **[**DWRITE\_PIXEL\_GEOMETRY**](/windows/win32/api/dwrite/ne-dwrite-dwrite_pixel_geometry)**

The geometry of a device pixel.

</dd> <dt>

*renderingMode* 
</dt> <dd>

Type: **[**DWRITE\_RENDERING\_MODE**](/windows/win32/api/dwrite/ne-dwrite-dwrite_rendering_mode)**

Method of rendering glyphs. In most cases, this should be DWRITE\_RENDERING\_MODE\_DEFAULT to automatically use an appropriate mode.

</dd> <dt>

*gridFitMode* 
</dt> <dd>

Type: **[**DWRITE\_GRID\_FIT\_MODE**](/windows/win32/api/dwrite_2/ne-dwrite_2-dwrite_grid_fit_mode)**

How to grid fit glyph outlines. In most cases, this should be DWRITE\_GRID\_FIT\_DEFAULT to automatically choose an appropriate mode.

</dd> <dt>

*renderingParams* \[out\]
</dt> <dd>

Type: **[**IDWriteRenderingParams2**](/windows/win32/api/dwrite_2/nn-dwrite_2-idwriterenderingparams2)\*\***

Holds the newly created rendering parameters object, or NULL in case of failure.

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

 

