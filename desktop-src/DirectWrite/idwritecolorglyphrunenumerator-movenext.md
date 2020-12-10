---
title: IDWriteColorGlyphRunEnumerator MoveNext method
description: Move to the next glyph run in the enumerator.
ms.assetid: E6336C0E-F880-485C-9111-A102298257C1
keywords:
- MoveNext method Direct Write
- MoveNext method Direct Write , IDWriteColorGlyphRunEnumerator interface
- IDWriteColorGlyphRunEnumerator interface Direct Write , MoveNext method
topic_type:
- apiref
api_name:
- IDWriteColorGlyphRunEnumerator.MoveNext
api_location:
- dwrite.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IDWriteColorGlyphRunEnumerator::MoveNext method

Move to the next glyph run in the enumerator.

## Syntax


```C++
HRESULT MoveNext(
  [out] BOOL *haveRun
);
```



## Parameters

<dl> <dt>

*haveRun* \[out\]
</dt> <dd>

Type: **BOOL\***

Returns **TRUE** if there is a next glyph run.

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

[**IDWriteColorGlyphRunEnumerator**](idwritecolorglyphrunenumerator.md)
</dt> </dl>

 

 





