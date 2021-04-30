---
title: IDWriteTextLayout3 SetLineSpacing method
description: Set line spacing. | IDWriteTextLayout3 SetLineSpacing method
ms.assetid: 1bfca257-189c-4d18-628c-aff8217d2775
keywords:
- SetLineSpacing method Direct Write
- SetLineSpacing method Direct Write , IDWriteTextLayout3 interface
- IDWriteTextLayout3 interface Direct Write , SetLineSpacing method
topic_type:
- apiref
api_name:
- IDWriteTextLayout3.SetLineSpacing
api_location:
- dwrite.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IDWriteTextLayout3::SetLineSpacing method

Set line spacing.

## Syntax


```C++
HRESULT SetLineSpacing(
  [in] const DWRITE_LINE_SPACING *lineSpacingOptions
);
```



## Parameters

<dl> <dt>

*lineSpacingOptions* \[in\]
</dt> <dd>

How to manage space between lines.

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

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

 

 





