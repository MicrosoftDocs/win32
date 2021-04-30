---
title: IDWriteTextLayout3 GetLineMetrics method
description: Retrieves properties of each line.
ms.assetid: 352ca3e3-7b08-823c-0881-0b051d4ce574
keywords:
- GetLineMetrics method Direct Write
- GetLineMetrics method Direct Write , IDWriteTextLayout3 interface
- IDWriteTextLayout3 interface Direct Write , GetLineMetrics method
topic_type:
- apiref
api_name:
- IDWriteTextLayout3.GetLineMetrics
api_location:
- dwrite.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IDWriteTextLayout3::GetLineMetrics method

Retrieves properties of each line.

## Syntax


```C++
HRESULT GetLineMetrics(
  [out] DWRITE_LINE_METRICS1 *lineMetrics,
        UINT32               maxLineCount,
  [out] UINT32               *actualLineCount
);
```



## Parameters

<dl> <dt>

*lineMetrics* \[out\]
</dt> <dd>

The array to fill with line information.

</dd> <dt>

*maxLineCount* 
</dt> <dd>

The maximum size of the lineMetrics array.

</dd> <dt>

*actualLineCount* \[out\]
</dt> <dd>

The actual size of the lineMetrics array that is needed.

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

If maxLineCount is not large enough E\_NOT\_SUFFICIENT\_BUFFER, which is equivalent to HRESULT\_FROM\_WIN32(ERROR\_INSUFFICIENT\_BUFFER), is returned and actualLineCount is set to the number of lines needed.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1 \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2012 R2 \[desktop apps only\]<br/>                                 |
| Minimum supported phone<br/>  | Windows Phone 8.1 \[Windows Phone Silverlight 8.1 and Windows Runtime apps\]<br/> |
| Library<br/>                  | <dl> <dt>Dwrite.lib</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Dwrite.dll</dt> </dl>   |



## See also

<dl> <dt>

[**IDWriteTextLayout3**](idwritetextlayout3.md)
</dt> </dl>

 

 





