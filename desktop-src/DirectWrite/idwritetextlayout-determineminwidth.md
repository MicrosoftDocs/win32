---
title: IDWriteTextLayout DetermineMinWidth method
description: Determines the minimum possible width the layout can be set to without emergency breaking between the characters of whole words occurring.
ms.assetid: 8efa1471-1b74-46d4-ac6d-fb1839ce2e74
keywords:
- DetermineMinWidth method Direct Write
- DetermineMinWidth method Direct Write , IDWriteTextLayout interface
- IDWriteTextLayout interface Direct Write , DetermineMinWidth method
topic_type:
- apiref
api_name:
- IDWriteTextLayout.DetermineMinWidth
api_location:
- dwrite.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IDWriteTextLayout::DetermineMinWidth method

Determines the minimum possible width the layout can be set to without emergency breaking between the characters of whole words occurring.

## Syntax


```C++
virtual HRESULT DetermineMinWidth(
  [out] FLOAT *minWidth
) = 0;
```



## Parameters

<dl> <dt>

*minWidth* \[out\]
</dt> <dd>

Type: **FLOAT\***

Minimum width.

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

[**IDWriteTextLayout**](/windows/win32/api/dwrite/nn-dwrite-idwritetextlayout)
</dt> <dt>

[**IDWriteTextLayout**](/windows/win32/api/dwrite/nn-dwrite-idwritetextlayout)
</dt> </dl>

 

