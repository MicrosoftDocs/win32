---
title: WM\_DRAWCLIPBOARD message
description: Sent to the first window in the clipboard viewer chain when the content of the clipboard changes. This enables a clipboard viewer window to display the new content of the clipboard. A window receives this message through its WindowProc function.
ms.assetid: ffaadf6f-588b-4a29-b26c-629087e7ce73
keywords:
- WM_DRAWCLIPBOARD message Data Exchange
topic_type:
- apiref
api_name:
- WM_DRAWCLIPBOARD
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# WM\_DRAWCLIPBOARD message

Sent to the first window in the clipboard viewer chain when the content of the clipboard changes. This enables a clipboard viewer window to display the new content of the clipboard.

A window receives this message through its [**WindowProc**](https://msdn.microsoft.com/library/windows/desktop/ms633573) function.


```C++
#define WM_DRAWCLIPBOARD                0x0308
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

## Remarks

Only clipboard viewer windows receive this message. These are windows that have been added to the clipboard viewer chain by using the [**SetClipboardViewer**](/windows/desktop/api/Winuser/nf-winuser-setclipboardviewer) function.

Each window that receives the **WM\_DRAWCLIPBOARD** message must call the [**SendMessage**](https://msdn.microsoft.com/library/windows/desktop/ms644950) function to pass the message on to the next window in the clipboard viewer chain. The handle to the next window in the chain is returned by [**SetClipboardViewer**](/windows/desktop/api/Winuser/nf-winuser-setclipboardviewer), and may change in response to a [**WM\_CHANGECBCHAIN**](wm-changecbchain.md) message.

## Requirements



|                                     |                                                                                                          |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**SendMessage**](https://msdn.microsoft.com/library/windows/desktop/ms644950)
</dt> <dt>

[**SetClipboardViewer**](/windows/desktop/api/Winuser/nf-winuser-setclipboardviewer)
</dt> <dt>

[**WM\_CHANGECBCHAIN**](wm-changecbchain.md)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Clipboard](clipboard.md)
</dt> </dl>

 

 





