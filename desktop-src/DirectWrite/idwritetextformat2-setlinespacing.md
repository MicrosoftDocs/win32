---
title: IDWriteTextFormat2 SetLineSpacing method
description: Set line spacing. | IDWriteTextFormat2 SetLineSpacing method
ms.assetid: 71d8c6c4-920f-a1b5-5a13-9985a7aca41e
keywords:
- SetLineSpacing method Direct Write
- SetLineSpacing method Direct Write , IDWriteTextFormat2 interface
- IDWriteTextFormat2 interface Direct Write , SetLineSpacing method
topic_type:
- apiref
api_name:
- IDWriteTextFormat2.SetLineSpacing
api_location:
- dwrite.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IDWriteTextFormat2::SetLineSpacing method

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

Type: **const [**DWRITE\_LINE\_SPACING**](/windows/win32/api/Dwrite_3/ns-dwrite_3-dwrite_line_spacing)\***

How to manage space between lines.

</dd> </dl>

## Return value

Type: **HRESULT**

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

[**IDWriteTextFormat2**](idwritetextformat2.md)
</dt> </dl>

 

 





