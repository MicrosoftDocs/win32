---
title: IDWriteTextLayout GetOverhangMetrics method
description: Returns the overhangs (in DIPs) of the layout and all objects contained in it, including text glyphs and inline objects.
ms.assetid: 4b23f6c5-cacc-41e2-8934-6f95208b999a
keywords:
- GetOverhangMetrics method Direct Write
- GetOverhangMetrics method Direct Write , IDWriteTextLayout interface
- IDWriteTextLayout interface Direct Write , GetOverhangMetrics method
topic_type:
- apiref
api_name:
- IDWriteTextLayout.GetOverhangMetrics
api_location:
- dwrite.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IDWriteTextLayout::GetOverhangMetrics method

Returns the overhangs (in DIPs) of the layout and all objects contained in it, including text glyphs and inline objects.

## Syntax


```C++
virtual HRESULT GetOverhangMetrics(
  [out] DWRITE_OVERHANG_METRICS *overhangs
) = 0;
```



## Parameters

<dl> <dt>

*overhangs* \[out\]
</dt> <dd>

Type: **[**DWRITE\_OVERHANG\_METRICS**](/windows/win32/api/dwrite/ns-dwrite-dwrite_overhang_metrics)\***

Overshoots of visible extents (in DIPs) outside the layout.

</dd> </dl>

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

Underlines and strikethroughs do not contribute to the black box determination, since these are actually drawn by the renderer, which is allowed to draw them in any variety of styles.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------|
| Library<br/> | <dl> <dt>Dwrite.lib</dt> </dl> |
| DLL<br/>     | <dl> <dt>Dwrite.dll</dt> </dl> |



## See also

<dl> <dt>

[**IDWriteTextLayout**](/windows/win32/api/dwrite/nn-dwrite-idwritetextlayout)
</dt> <dt>

[**IDWriteTextLayout**](/windows/win32/api/dwrite/nn-dwrite-idwritetextlayout)
</dt> </dl>

 

