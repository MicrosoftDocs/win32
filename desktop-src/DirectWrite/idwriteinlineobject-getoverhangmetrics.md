---
title: IDWriteInlineObject GetOverhangMetrics method
description: IDWriteTextLayout calls this callback function to get the visible extents (in DIPs) of the inline object. In the case of a simple bitmap, with no padding and no overhang, all the overhangs will simply be zeroes.
ms.assetid: 'b3b3e9f0-ee35-4117-9a62-a975c03b5ca9'
keywords: ["GetOverhangMetrics method Direct Write", "GetOverhangMetrics method Direct Write , IDWriteInlineObject interface", "IDWriteInlineObject interface Direct Write , GetOverhangMetrics method"]
topic_type:
- apiref
api_name:
- IDWriteInlineObject.GetOverhangMetrics
api_location:
- dwrite.dll
api_type:
- COM
---

# IDWriteInlineObject::GetOverhangMetrics method

[**IDWriteTextLayout**](idwritetextlayout.md) calls this callback function to get the visible extents (in DIPs) of the inline object. In the case of a simple bitmap, with no padding and no overhang, all the overhangs will simply be zeroes.

The overhangs should be returned relative to the reported size of the object (see [**DWRITE\_INLINE\_OBJECT\_METRICS**](dwrite-inline-object-metrics.md)), and should not be baseline adjusted.

## Syntax


```C++
virtual HRESULT GetOverhangMetrics(
  [out] DWRITE_OVERHANG_METRICS *overhangs
) = 0;
```



## Parameters

<dl> <dt>

*overhangs* \[out\]
</dt> <dd>

Type: **[**DWRITE\_OVERHANG\_METRICS**](dwrite-overhang-metrics.md)\***

Overshoot of visible extents (in DIPs) outside the object.

</dd> </dl>

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements



|                    |                                                                                       |
|--------------------|---------------------------------------------------------------------------------------|
| Library<br/> | <dl> <dt>Dwrite.lib</dt> </dl> |
| DLL<br/>     | <dl> <dt>Dwrite.dll</dt> </dl> |



## See also

<dl> <dt>

[**IDWriteInlineObject**](idwriteinlineobject.md)
</dt> <dt>

[**IDWriteInlineObject**](https://msdn.microsoft.com/library/windows/desktop/dd371221)
</dt> </dl>

 

 





