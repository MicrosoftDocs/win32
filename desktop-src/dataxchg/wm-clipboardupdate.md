---
title: WM\_CLIPBOARDUPDATE message
description: Sent when the contents of the clipboard have changed.
ms.assetid: 1508aa22-9cf0-40a2-8cb0-ce7c8671df2c
keywords:
- WM_CLIPBOARDUPDATE message Data Exchange
topic_type:
- apiref
api_name:
- WM_CLIPBOARDUPDATE
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
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

To register a window to receive this message, use the [**AddClipboardFormatListener**](/windows/win32/Winuser/nf-winuser-addclipboardformatlistener?branch=master) function.

## Requirements



|                                     |                                                                                                          |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

[**AddClipboardFormatListener**](/windows/win32/Winuser/nf-winuser-addclipboardformatlistener?branch=master)
</dt> <dt>

[**RemoveClipboardFormatListener**](/windows/win32/Winuser/nf-winuser-removeclipboardformatlistener?branch=master)
</dt> <dt>

[**GetClipboardSequenceNumber**](/windows/win32/Winuser/nf-winuser-getclipboardsequencenumber?branch=master)
</dt> </dl>

 

 





