---
title: IDWriteTextLayout2 GetMetrics method
description: Retrieves overall metrics for the formatted string.
ms.assetid: EADCD83A-9FF5-44AB-8AB5-35FCB3A84889
keywords:
- GetMetrics method Direct Write
- GetMetrics method Direct Write , IDWriteTextLayout2 interface
- IDWriteTextLayout2 interface Direct Write , GetMetrics method
topic_type:
- apiref
api_name:
- IDWriteTextLayout2.GetMetrics
api_location:
- dwrite.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IDWriteTextLayout2::GetMetrics method

Retrieves overall metrics for the formatted string.

## Syntax


```C++
virtual HRESULT GetMetrics(
  [out] DWRITE_TEXT_METRICS1 * textMetrics
) = 0;
```



## Parameters

<dl> <dt>

 *textMetrics* \[out\]
</dt> <dd>

Type: **[**DWRITE\_TEXT\_METRICS1**](/windows/win32/api/dwrite_2/ns-dwrite_2-dwrite_text_metrics1)\***

When this method returns, contains the measured distances of text and associated content after being formatted.

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

[**IDWriteTextLayout2**](idwritetextlayout2.md)
</dt> </dl>

 

 





