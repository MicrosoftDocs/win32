---
title: WM\_CLIPBOARDUPDATE message
description: Sent when the contents of the clipboard have changed.
ms.assetid: '1508aa22-9cf0-40a2-8cb0-ce7c8671df2c'
keywords: ["WM_CLIPBOARDUPDATE message Data Exchange"]
topic_type:
- apiref
api_name:
- WM_CLIPBOARDUPDATE
api_location:
- Winuser.h
api_type:
- HeaderDef
---

# WM\_CLIPBOARDUPDATE message

Sent when the contents of the clipboard have changed.


```C++
#define WM_CLIPBOARDUPDATE              0x031D
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

This parameter is not used and must be zero.

</dd> <dt>

*lParam* 
</dt> <dd>

This parameter is not used and must be zero.

</dd> </dl>

## Return value

If an application processes this message, it should return zero.

## Remarks

To register a window to receive this message, use the [**AddClipboardFormatListener**](addclipboardformatlistener.md) function.

## Requirements



|                                     |                                                                                                          |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

[**AddClipboardFormatListener**](addclipboardformatlistener.md)
</dt> <dt>

[**RemoveClipboardFormatListener**](removeclipboardformatlistener.md)
</dt> <dt>

[**GetClipboardSequenceNumber**](getclipboardsequencenumber.md)
</dt> </dl>

 

 





